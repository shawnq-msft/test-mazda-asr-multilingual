from __future__ import annotations

from .asr_fast import _streaming_upload
from .config import (AZURE_SPEECH_KEY, FAST_API_VERSION, SEGMENTATION_SILENCE_MS,
                     AsrResult, Sample, rest_base_url)


def _endpoint() -> str:
    return f"{rest_base_url()}?api-version={FAST_API_VERSION}"


def transcribe_whisper_v3(sample: Sample, pace: bool = True) -> AsrResult:
    definition = {
        "locales": [sample.locale],
        "model": "whisper-large-v3",
    }
    vad_end_s = None
    if sample.last_word_end_s is not None:
        vad_end_s = sample.last_word_end_s + SEGMENTATION_SILENCE_MS / 1000.0
    return _streaming_upload(sample.pcm16_mono_16k, definition,
                             _endpoint(), pace, "whisper_v3", sample,
                             vad_end_s=vad_end_s)
