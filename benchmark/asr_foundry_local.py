from __future__ import annotations

import os
import tempfile
import threading
import time
import wave
from pathlib import Path
from typing import Any

from .config import AsrResult, Sample, TARGET_CHANNELS, TARGET_SAMPWIDTH, TARGET_SR


_MANAGER: Any | None = None
_MANAGER_LOCK = threading.Lock()
_MODELS: dict[str, Any] = {}
_MODEL_LOCK = threading.Lock()
_INFER_LOCKS: dict[str, threading.Lock] = {}


def _foundry_language(locale: str) -> str:
    override = os.getenv("FOUNDRY_LANGUAGE")
    if override:
        return override
    return locale.split("-", 1)[0].lower()


def _foundry_device() -> str:
    return os.getenv("FOUNDRY_DEVICE", "cpu").strip().lower()


def _get_manager() -> Any:
    global _MANAGER
    if _MANAGER is None:
        with _MANAGER_LOCK:
            if _MANAGER is None:
                try:
                    from foundry_local_sdk import Configuration, FoundryLocalManager
                except ImportError as exc:
                    raise RuntimeError(
                        "Install Foundry Local support with `pip install -r requirements-foundry.txt`"
                    ) from exc
                config = Configuration(app_name="mazda_asr_benchmark")
                FoundryLocalManager.initialize(config)
                _MANAGER = FoundryLocalManager.instance
                _MANAGER.download_and_register_eps()
    return _MANAGER


def _select_variant(model: Any, device: str) -> None:
    if device in ("", "auto"):
        return
    variants = list(getattr(model, "variants", []) or [])
    if not variants:
        return
    candidates = []
    for variant in variants:
        runtime = getattr(getattr(variant, "info", None), "runtime", None)
        device_type = str(getattr(runtime, "device_type", "")).lower()
        execution_provider = str(getattr(runtime, "execution_provider", "")).lower()
        variant_id = str(getattr(variant, "id", "")).lower()
        haystack = " ".join((device_type, execution_provider, variant_id))
        if device in haystack:
            candidates.append(variant)
        elif device == "gpu" and ("cuda" in haystack or "gpu" in haystack):
            candidates.append(variant)
    if not candidates:
        available = ", ".join(str(getattr(v, "id", "")) for v in variants)
        raise RuntimeError(f"Foundry Local model has no {device!r} variant. Available variants: {available}")
    model.select_variant(candidates[0])


def _get_model(alias: str) -> Any:
    device = _foundry_device()
    cache_key = f"{alias}|{device}"
    if cache_key not in _MODELS:
        with _MODEL_LOCK:
            if cache_key not in _MODELS:
                manager = _get_manager()
                model = manager.catalog.get_model(alias)
                if model is None:
                    raise RuntimeError(f'Foundry Local model "{alias}" was not found in the catalog')
                _select_variant(model, device)
                model.download()
                model.load()
                _MODELS[cache_key] = model
                _INFER_LOCKS[cache_key] = threading.Lock()
    return _MODELS[cache_key]


def _infer_lock(alias: str) -> threading.Lock:
    return _INFER_LOCKS[f"{alias}|{_foundry_device()}"]


def _write_sample_wav(path: Path, sample: Sample) -> None:
    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(TARGET_CHANNELS)
        wav.setsampwidth(TARGET_SAMPWIDTH)
        wav.setframerate(TARGET_SR)
        wav.writeframes(sample.pcm16_mono_16k)


def _transcribe_file(sample: Sample, service: str, alias: str) -> AsrResult:
    try:
        model = _get_model(alias)
        with tempfile.NamedTemporaryFile(prefix=f"{service}_", suffix=".wav", delete=False) as tmp:
            wav_path = Path(tmp.name)
        try:
            _write_sample_wav(wav_path, sample)
            audio_client = model.get_audio_client()
            language = _foundry_language(sample.locale)
            settings = getattr(audio_client, "settings", None)
            if settings is not None and hasattr(settings, "language"):
                settings.language = language
            start = time.perf_counter()
            with _infer_lock(alias):
                result = audio_client.transcribe(str(wav_path))
            elapsed_ms = (time.perf_counter() - start) * 1000.0
        finally:
            try:
                wav_path.unlink()
            except OSError:
                pass

        return AsrResult(
            service=service,
            hypothesis=str(getattr(result, "text", result) or "").strip(),
            first_latency_ms=None,
            lbl_ms=elapsed_ms,
            upl_ms=None,
            upl_self_ms=None,
            upl_anchor="foundry_local",
        )
    except Exception as exc:
        return AsrResult(service, "", None, None, f"exception: {exc!r}")


def _result_text(result: Any) -> str:
    content = getattr(result, "content", None) or []
    if not content:
        return ""
    return str(getattr(content[0], "text", "") or "")


def _transcribe_live_pcm(sample: Sample, service: str, alias: str, pace: bool) -> AsrResult:
    try:
        model = _get_model(alias)
        audio_client = model.get_audio_client()
        session = audio_client.create_live_transcription_session()
        session.settings.sample_rate = TARGET_SR
        session.settings.channels = TARGET_CHANNELS
        session.settings.language = _foundry_language(sample.locale)

        final_parts: list[str] = []
        partial_parts: list[str] = []
        read_error: list[BaseException] = []

        def read_results() -> None:
            try:
                for result in session.get_stream():
                    text = _result_text(result)
                    if not text:
                        continue
                    if getattr(result, "is_final", False):
                        final_parts.append(text)
                    else:
                        partial_parts.append(text)
            except BaseException as exc:
                read_error.append(exc)

        chunk_bytes = TARGET_SR // 10 * TARGET_CHANNELS * TARGET_SAMPWIDTH
        start = time.perf_counter()
        with _infer_lock(alias):
            session.start()
            read_thread = threading.Thread(target=read_results, daemon=True)
            read_thread.start()
            try:
                for offset in range(0, len(sample.pcm16_mono_16k), chunk_bytes):
                    chunk = sample.pcm16_mono_16k[offset:offset + chunk_bytes]
                    if chunk:
                        session.append(chunk)
                    if pace:
                        time.sleep(0.1)
            finally:
                session.stop()
                read_thread.join(timeout=10)
        elapsed_ms = (time.perf_counter() - start) * 1000.0

        if read_error:
            raise RuntimeError(f"Foundry Local read stream failed: {read_error[0]!r}")
        hypothesis = " ".join(final_parts).strip() or (partial_parts[-1].strip() if partial_parts else "")
        return AsrResult(
            service=service,
            hypothesis=hypothesis,
            first_latency_ms=None,
            lbl_ms=elapsed_ms,
            upl_ms=None,
            upl_self_ms=None,
            upl_anchor="foundry_local",
        )
    except Exception as exc:
        return AsrResult(service, "", None, None, f"exception: {exc!r}")


def transcribe_foundry_whisper_v3(sample: Sample, pace: bool = True) -> AsrResult:
    del pace
    alias = os.getenv("FOUNDRY_WHISPER_MODEL_ALIAS", "whisper-large-v3-turbo")
    return _transcribe_file(sample, "foundry_whisper_v3", alias)


def transcribe_foundry_nemotron_asr(sample: Sample, pace: bool = True) -> AsrResult:
    alias = os.getenv(
        "FOUNDRY_NEMOTRON_MODEL_ALIAS",
        "nemotron-3.5-asr-streaming-0.6b",
    )
    return _transcribe_live_pcm(sample, "foundry_nemotron_asr", alias, pace)