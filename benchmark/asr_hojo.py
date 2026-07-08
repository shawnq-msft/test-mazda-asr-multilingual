from __future__ import annotations

import os
import tempfile
import threading
import time
import wave
from pathlib import Path
from typing import Any

from .config import AsrResult, Sample, TARGET_CHANNELS, TARGET_SAMPWIDTH, TARGET_SR


_MODEL: Any | None = None
_MODEL_LOCK = threading.Lock()
_INFER_LOCK = threading.Lock()


def _model_path() -> str:
    path = os.getenv("HOJO_MODEL_PATH")
    if not path:
        raise RuntimeError("HOJO_MODEL_PATH must point to a local Hojo-ASR-V1 model folder")
    return path


def _device() -> str:
    return os.getenv("HOJO_DEVICE", "cuda:0")


def _get_model() -> Any:
    global _MODEL
    if _MODEL is None:
        with _MODEL_LOCK:
            if _MODEL is None:
                model_path = _model_path()
                try:
                    from hojo_asr import HOJO_ASR
                except ImportError as exc:
                    raise RuntimeError("Install Hojo support with `pip install -U hojo-asr`") from exc
                _MODEL = HOJO_ASR.load_model(model_path, device=_device())
    return _MODEL


def _write_sample_wav(path: Path, sample: Sample) -> None:
    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(TARGET_CHANNELS)
        wav.setsampwidth(TARGET_SAMPWIDTH)
        wav.setframerate(TARGET_SR)
        wav.writeframes(sample.pcm16_mono_16k)


def transcribe_hojo_asr(sample: Sample, pace: bool = True) -> AsrResult:
    del pace
    try:
        model = _get_model()
        batch_size = int(os.getenv("HOJO_BATCH_SIZE", "1"))
        with tempfile.NamedTemporaryFile(prefix="hojo_asr_", suffix=".wav", delete=False) as tmp:
            wav_path = Path(tmp.name)
        try:
            _write_sample_wav(wav_path, sample)
            start = time.perf_counter()
            with _INFER_LOCK:
                results = model.run_infer([str(wav_path)], batch_size=batch_size)
            elapsed_ms = (time.perf_counter() - start) * 1000.0
        finally:
            try:
                wav_path.unlink()
            except OSError:
                pass

        hypothesis = ""
        if results:
            first = results[0]
            if isinstance(first, dict):
                hypothesis = str(first.get("text") or "")
            else:
                hypothesis = str(first)
        return AsrResult(
            service="hojo_asr",
            hypothesis=hypothesis.strip(),
            first_latency_ms=None,
            lbl_ms=elapsed_ms,
            upl_ms=None,
            upl_self_ms=None,
            upl_anchor="offline",
        )
    except Exception as exc:
        return AsrResult("hojo_asr", "", None, None, f"exception: {exc!r}")