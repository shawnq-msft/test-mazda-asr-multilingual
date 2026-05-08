from __future__ import annotations

import random
from pathlib import Path

from .audio_utils import load_audio_as_pcm16_mono_16k, write_pcm16_wav
from .config import LOCALES, SCENARIOS, Sample

DATA_ROOT = Path(__file__).resolve().parent.parent / "TestAudio3.0"


def _scenario_dirs(locale: str, scenario: str) -> list[Path]:
    locale_dir = DATA_ROOT / locale
    dirs = []
    for d in sorted(locale_dir.iterdir()):
        if d.is_dir() and d.name.endswith(f"-{scenario}"):
            dirs.append(d)
    return dirs


def _load_trans(trans_path: Path) -> list[tuple[str, str]]:
    entries = []
    text = trans_path.read_text(encoding="utf-8-sig")
    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split("\t", 1)
        if len(parts) != 2:
            continue
        filename, reference = parts
        entries.append((filename, reference))
    return entries


def iter_samples(dataset: str, limit: int | None = 30,
                 seed: int = 42) -> list[Sample]:
    parts = dataset.rsplit("_", 1)
    if len(parts) != 2:
        raise ValueError(f"Invalid dataset name: {dataset}. Expected format: locale_scenario (e.g. de-DE_DT1)")
    locale, scenario = parts

    dirs = _scenario_dirs(locale, scenario)
    if not dirs:
        raise FileNotFoundError(f"No directories found for {locale}/{scenario}")

    all_entries: list[tuple[Path, str, str]] = []
    for d in dirs:
        trans_path = d / "trans.txt"
        if not trans_path.exists():
            continue
        for filename, reference in _load_trans(trans_path):
            wav_path = d / filename
            if wav_path.exists():
                all_entries.append((wav_path, reference, f"{d.name}/{filename}"))

    if limit and len(all_entries) > limit:
        rng = random.Random(seed)
        all_entries = rng.sample(all_entries, limit)

    samples = []
    for wav_path, reference, sample_id in all_entries:
        try:
            pcm, duration = load_audio_as_pcm16_mono_16k(str(wav_path))
        except Exception as e:
            print(f"[skip] {wav_path}: {e}")
            continue
        if duration < 0.2:
            continue
        samples.append(Sample(
            sample_id=sample_id,
            dataset=dataset,
            locale=locale,
            pcm16_mono_16k=pcm,
            reference=reference,
            duration_s=duration,
        ))
    return samples


def list_datasets(locale: str | None = None) -> list[str]:
    locales = [locale] if locale else list(LOCALES)
    datasets = []
    for loc in locales:
        for scn in SCENARIOS:
            dirs = _scenario_dirs(loc, scn)
            if dirs:
                datasets.append(f"{loc}_{scn}")
    return datasets
