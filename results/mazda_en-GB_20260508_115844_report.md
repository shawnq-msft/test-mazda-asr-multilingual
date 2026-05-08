# Mazda ASR Benchmark — mazda_en-GB_20260508_115844.csv

Total rows: **450**  
Tester public IP: **167.220.233.51**  
Tester location: **Tokyo, Tokyo, Japan** (Microsoft Corporation)  
Azure region: **eastus**  
Azure endpoint host: **eastus.api.cognitive.microsoft.com**  
TCP ping to `eastus.api.cognitive.microsoft.com:443` (avg of 5): **241.5 ms**  
VAD set to **500 ms** (realtime `Speech_SegmentationSilenceTimeoutMs`; fast_* audio truncated at `speech_end + 500 ms`)

## Endpoints under test

### `fast_default` — Azure Fast Transcription (default)
- URL: `https://eastus.api.cognitive.microsoft.com/speechtotext/transcriptions:transcribe?api-version=2024-11-15`
- Transport: HTTPS POST (multipart/form-data, chunked)
- Config: `definition = {"locales": ["en-GB"]}`
- Partial results: no
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/fast-transcription-create>

### `fast_llm` — Azure Fast Transcription — LLM enhanced (preview)
- URL: `https://eastus.api.cognitive.microsoft.com/speechtotext/transcriptions:transcribe?api-version=2025-10-15`
- Transport: HTTPS POST (multipart/form-data, chunked)
- Config: `definition = {"enhancedMode": {"enabled": true, "task": "transcribe"}}`
- Partial results: no
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/llm-speech>
- Note: Requires Speech resource with LLM-Speech preview enabled.

### `fast_mai` — Azure Fast Transcription — MAI model (preview)
- URL: `https://eastus.api.cognitive.microsoft.com/speechtotext/transcriptions:transcribe?api-version=2025-10-15`
- Transport: HTTPS POST (multipart/form-data, chunked)
- Config: `definition = {"locales": ["en"], "enhancedMode": {"enabled": true, "model": "mai-transcribe-1"}}`
- Partial results: no
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe>
- Note: Requires Speech resource with mai-transcribe-1 preview enabled.

### `realtime` — Azure Speech SDK — continuous recognition
- URL: `https://eastus.api.cognitive.microsoft.com`
- Transport: WebSocket via azure-cognitiveservices-speech SDK
- Config: `PushAudioInputStream, language="en-GB", continuous`
- Partial results: yes (recognizing/recognized events)
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech>

### `realtime_refine` — Azure Speech SDK — continuous + Post-Stream Refinement (MRS preview)
- URL: `https://eastus.api.cognitive.microsoft.com`
- Transport: WebSocket via azure-cognitiveservices-speech SDK (>=1.49.0)
- Config: `PushAudioInputStream, language="en-GB", continuous, PostProcessingOption="PostRefinement"`
- Partial results: yes (recognizing/recognized events; final replaced after refinement)
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech>
- Note: Requires Speech SDK >= 1.49.0 and a Speech resource in a region where Multi-Recognizer / Post-Stream Refinement public preview is enabled (East US / North Europe rollout). Falls back to non-MRS behavior if PostProcessingOption is not set.

## Datasets under test

- **en-GB_DT1** — Mazda en-GB DT1 voice commands (male + female pooled, 30 random samples)
- **en-GB_DT2** — Mazda en-GB DT2 voice commands (male + female pooled, 30 random samples)
- **en-GB_JT1** — Mazda en-GB JT1 voice commands (male + female pooled, 30 random samples)

## Results

WER breakdown columns are *rates per 100 reference words*. Per-row WER ≈ (INS + DEL + SUB) / ref_len (capped at 1.0 per sample in aggregation).

| Dataset | Service | N | Errors | WER | SER | INS/100 | DEL/100 | SUB/100 | First Latency ms (mean / p90) | LBL ms (mean / p90) | UPL ms (mean / p90) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| en-GB_DT1 | fast_default | 30 | 0 | 0.260 | 0.433 | 3.8 | 5.6 | 12.5 | - | 583 / 642 | 1025 / 1193 |
| en-GB_DT1 | fast_llm | 30 | 0 | 0.220 | 0.367 | 4.4 | 5.0 | 8.8 | - | 497 / 549 | 939 / 1076 |
| en-GB_DT1 | fast_mai | 30 | 0 | 0.200 | 0.367 | 4.4 | 2.5 | 10.6 | - | 474 / 537 | 915 / 1060 |
| en-GB_DT1 | realtime | 30 | 0 | 0.241 | 0.500 | 2.5 | 3.8 | 13.8 | 1542 / 2153 | -279 / 429 | 643 / 942 |
| en-GB_DT1 | realtime_refine | 30 | 0 | 0.246 | 0.467 | 4.4 | 3.1 | 13.8 | 1592 / 2419 | 76 / 801 | 1137 / 1307 |
| en-GB_DT2 | fast_default | 30 | 0 | 0.356 | 0.567 | 3.1 | 12.5 | 20.0 | - | 603 / 663 | 1099 / 1176 |
| en-GB_DT2 | fast_llm | 30 | 0 | 0.273 | 0.500 | 1.9 | 8.1 | 16.9 | - | 495 / 577 | 992 / 1170 |
| en-GB_DT2 | fast_mai | 30 | 0 | 0.261 | 0.400 | 4.4 | 2.5 | 17.5 | - | 489 / 591 | 915 / 1090 |
| en-GB_DT2 | realtime | 30 | 0 | 0.351 | 0.600 | 5.0 | 11.9 | 16.9 | 1452 / 1870 | -292 / 331 | 624 / 872 |
| en-GB_DT2 | realtime_refine | 30 | 0 | 0.382 | 0.600 | 5.0 | 6.2 | 25.6 | 1481 / 1880 | 133 / 712 | 1253 / 1687 |
| en-GB_JT1 | fast_default | 30 | 0 | 0.086 | 0.200 | 2.5 | 3.1 | 1.9 | - | 608 / 709 | 1016 / 1209 |
| en-GB_JT1 | fast_llm | 30 | 0 | 0.080 | 0.200 | 1.9 | 3.8 | 1.2 | - | 491 / 548 | 899 / 1059 |
| en-GB_JT1 | fast_mai | 30 | 0 | 0.104 | 0.233 | 2.5 | 3.8 | 3.1 | - | 465 / 623 | 873 / 1056 |
| en-GB_JT1 | realtime | 30 | 0 | 0.135 | 0.300 | 2.5 | 3.1 | 5.0 | 1375 / 1832 | -250 / 339 | 612 / 901 |
| en-GB_JT1 | realtime_refine | 30 | 0 | 0.138 | 0.267 | 4.4 | 2.5 | 3.8 | 1429 / 1848 | 105 / 756 | 1115 / 1281 |

## Speech boundaries

`speech_start_s` / `speech_end_s` (CSV columns) come from the realtime SDK's word-level timestamps and anchor UPL for all services. The full per-word log lives in the sidecar `mazda_en-GB_20260508_115844_words.jsonl` (one JSON object per realtime sample).

Boundary-fix decisions across 90 realtime samples:

- `skip`: 2
- `trim_both`: 4
- `trim_first`: 5
- `trim_last`: 4

Trimmed/skipped samples (first 20):

| Dataset | Sample ID | Action | speech_start_s | speech_end_s |
|---|---|---|---:|---:|
| en-GB_DT1 | 1l_en-GB_female-DT1/Play 100.wav | trim_both | 1.63 | 3.75 |
| en-GB_DT1 | 1l_en-GB_female-DT1/Decrease the driver's window.wav | trim_both | 2.81 | 3.53 |
| en-GB_DT1 | 1l_en-GB_male-DT1/Call Jane.wav | trim_first | 1.48 | 1.96 |
| en-GB_DT1 | 1l_en-GB_female-DT1/Close HUD.wav | trim_first | 1.95 | 2.67 |
| en-GB_DT2 | 1l_en-GB_female-DT2/Play 100.wav | trim_last | 0.99 | 3.67 |
| en-GB_DT2 | 1l_en-GB_female-DT2/Set the  POI  as my home.wav | skip | - | - |
| en-GB_DT2 | 1l_en-GB_male-DT2/Turn off wireless charging Turn off wireless charging.wav | skip | - | - |
| en-GB_DT2 | 1l_en-GB_male-DT2/Increase the driverΓÇÖs seat temperature a little.wav | trim_both | 1.67 | 2.95 |
| en-GB_DT2 | 1l_en-GB_female-DT2/Close HUD.wav | trim_first | 1.99 | 2.63 |
| en-GB_DT2 | 1l_en-GB_male-DT2/Mute the voice.wav | trim_first | 1.34 | 2.3 |
| en-GB_DT2 | 1l_en-GB_female-DT2/Open right rear window to 60%.wav | trim_last | 1.23 | 3.47 |
| en-GB_DT2 | 1l_en-GB_male-DT2/Adjust ringtone volume to 5 levels.wav | trim_last | 1.13 | 2.97 |
| en-GB_DT2 | 1l_en-GB_male-DT2/Close front row window to half.wav | trim_both | 1.45 | 2.41 |
| en-GB_JT1 | 1l_en-GB_female-JT1/Play 100.wav | trim_last | 1.09 | 3.73 |
| en-GB_JT1 | 1l_en-GB_female-JT1/Close HUD.wav | trim_first | 2.03 | 2.63 |

## Latency definitions (all values in ms)

Wall-clock timeline for one realtime sample. The clip has leading and
trailing silence; the user only speaks during the middle. Word offsets
come from the SDK's word-level timestamps.

```
  audio_start         speech_start                  speech_end       end_of_audio
       │                   │                              │                │
       ├───────────────────┼──────────────────────────────┼────────────────┤
       │  leading silence  │        user speaking         │trailing silence│
       │                   │                              │                │
       │                   │   first_recognizing event    │                │   last_recognized event
       │                   │             ▼                │                │           ▼
       │                   ├────────────→│ First Latency  │                │           │
       │                   │                              │                │           │
       │                   │                              ├────────────────┼──────────→│ UPL
       │                   │                              │                │           │
       │                   │                              │                ├──────────→│ LBL  (can be negative)
```

Reference points on the timeline:
- `audio_start` — wall time of the first PCM chunk we push.
- `speech_start` = `audio_start + first_word_start_in_audio` — first word's `Offset` from the first `recognized` event.
- `speech_end` = `audio_start + last_word_end_in_audio` — last word's `Offset + Duration` from the last `recognized` event.
- `end_of_audio` — wall time when the last PCM chunk has been pushed.

**realtime** (Speech SDK, partials available):
- **First Latency** = `first_recognizing_event_wall − speech_start`. Subtracts leading silence so the metric reflects how fast the first partial appears *after the user starts speaking*, not after we start streaming bytes.
- **LBL** (last-final beyond last-chunk) = `last_recognized_event_wall − end_of_audio`. Pure server flush time relative to the last byte we pushed. **May be negative** when the SDK emits the final result before the last chunk goes out — that's the streaming pipeline running ahead of audio I/O.
- **UPL** (user-perceived latency) = `last_recognized_event_wall − speech_end`. How late the final result arrives after the user actually stopped speaking. `speech_end` comes from the last word's `Offset + Duration` in the recognized event JSON.

**fast_default / fast_llm / fast_mai** (REST, no partials):
- **LBL** = `response_fully_read_wall − end_of_audio_wall`. Time from last uploaded byte to fully-received response.
- **UPL** = `response_fully_read_wall − speech_end_wall`. `speech_end_wall` is taken from the realtime SDK's last-word offset for that sample (when realtime ran successfully on it), so all services compare against the same reference. The CSV column `upl_self_ms` keeps each service's own phrase-derived value, and `upl_anchor` is `realtime` when anchored or `self` when the realtime anchor was unavailable.
- Note: `fast_mai`'s own phrase boundaries often span the entire audio; using the realtime anchor here makes its UPL directly comparable to the others.
- **First Latency** is omitted because the REST response is delivered in one shot — there is no first-token signal to measure against.
- **VAD truncation**: when realtime ran first and produced word timestamps, fast_* audio is truncated at `speech_end + 500 ms` to simulate a VAD cutting the stream after end-of-speech. This reduces upload time and makes LBL/UPL realistic for a VAD-equipped pipeline. The CSV column `vad_truncated_s` records the truncated duration (blank when no truncation was applied).

**Other:**
- WER/SER use NFKC + lowercase + punctuation stripping normalization.
- Per-sample WER is capped at 1.0 in aggregation (a hypothesis far longer than the reference is still 100% wrong, not more).