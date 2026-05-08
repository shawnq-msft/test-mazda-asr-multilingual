# Mazda ASR Benchmark — mazda_de-DE_20260508_193734.csv

Total rows: **450**  
Tester public IP: **167.220.233.51**  
Tester location: **Tokyo, Tokyo, Japan** (Microsoft Corporation)  
Azure region: **eastus**  
Azure endpoint host: **eastus.api.cognitive.microsoft.com**  
TCP ping to `eastus.api.cognitive.microsoft.com:443` (avg of 5): **254.2 ms**  
VAD set to **500 ms** (realtime `Speech_SegmentationSilenceTimeoutMs`; fast_* audio truncated at `speech_end + 500 ms`)

## Endpoints under test

### `fast_default` — Azure Fast Transcription (default)
- URL: `https://eastus.api.cognitive.microsoft.com/speechtotext/transcriptions:transcribe?api-version=2024-11-15`
- Transport: HTTPS POST (multipart/form-data, chunked)
- Config: `definition = {"locales": ["de-DE"]}`
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
- Config: `definition = {"locales": ["de"], "enhancedMode": {"enabled": true, "model": "mai-transcribe-1"}}`
- Partial results: no
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe>
- Note: Requires Speech resource with mai-transcribe-1 preview enabled.

### `realtime` — Azure Speech SDK — continuous recognition
- URL: `https://eastus.api.cognitive.microsoft.com`
- Transport: WebSocket via azure-cognitiveservices-speech SDK
- Config: `PushAudioInputStream, language="de-DE", continuous`
- Partial results: yes (recognizing/recognized events)
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech>

### `realtime_refine` — Azure Speech SDK — continuous + Post-Stream Refinement (MRS preview)
- URL: `https://eastus.api.cognitive.microsoft.com`
- Transport: WebSocket via azure-cognitiveservices-speech SDK (>=1.49.0)
- Config: `PushAudioInputStream, language="de-DE", continuous, PostProcessingOption="PostRefinement"`
- Partial results: yes (recognizing/recognized events; final replaced after refinement)
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech>
- Note: Requires Speech SDK >= 1.49.0 and a Speech resource in a region where Multi-Recognizer / Post-Stream Refinement public preview is enabled (East US / North Europe rollout). Falls back to non-MRS behavior if PostProcessingOption is not set.

## Datasets under test

- **de-DE_DT1** — Mazda de-DE DT1 voice commands (male + female pooled, 30 random samples)
- **de-DE_DT2** — Mazda de-DE DT2 voice commands (male + female pooled, 30 random samples)
- **de-DE_JT1** — Mazda de-DE JT1 voice commands (male + female pooled, 30 random samples)

## Results

WER breakdown columns are *rates per 100 reference words*. Per-row WER ≈ (INS + DEL + SUB) / ref_len (capped at 1.0 per sample in aggregation).

| Dataset | Service | N | Errors | WER | SER | INS/100 | DEL/100 | SUB/100 | First Latency ms (mean / p90) | LBL ms (mean / p90) | UPL ms (mean / p90) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| de-DE_DT1 | fast_default | 30 | 0 | 0.575 | 0.733 | 9.3 | 26.3 | 33.9 | - | 717 / 1146 | 1659 / 2986 |
| de-DE_DT1 | fast_llm | 30 | 0 | 0.549 | 0.700 | 15.3 | 10.2 | 45.8 | - | 563 / 595 | 1586 / 2784 |
| de-DE_DT1 | fast_mai | 30 | 0 | 0.475 | 0.700 | 16.9 | 10.2 | 33.9 | - | 502 / 590 | 865 / 1147 |
| de-DE_DT1 | realtime | 30 | 0 | 0.571 | 0.800 | 2.5 | 37.3 | 18.6 | 1565 / 1896 | -1133 / -580 | 771 / 958 |
| de-DE_DT1 | realtime_refine | 30 | 0 | 0.492 | 0.733 | 12.7 | 11.9 | 35.6 | 1569 / 1870 | -492 / 58 | 1368 / 1745 |
| de-DE_DT2 | fast_default | 30 | 0 | 0.684 | 0.800 | 13.6 | 33.1 | 37.3 | - | 671 / 821 | 1894 / 3062 |
| de-DE_DT2 | fast_llm | 30 | 0 | 0.663 | 0.800 | 21.2 | 20.3 | 45.8 | - | 492 / 564 | 2162 / 4145 |
| de-DE_DT2 | fast_mai | 30 | 0 | 0.602 | 0.800 | 22.9 | 16.9 | 41.5 | - | 543 / 643 | 769 / 1181 |
| de-DE_DT2 | realtime | 30 | 0 | 0.685 | 0.833 | 0.8 | 61.0 | 8.5 | 1501 / 1708 | -779 / -371 | 835 / 970 |
| de-DE_DT2 | realtime_refine | 30 | 0 | 0.646 | 0.800 | 11.0 | 32.2 | 32.2 | 1452 / 1707 | -414 / 474 | 1342 / 2035 |
| de-DE_JT1 | fast_default | 30 | 0 | 0.351 | 0.600 | 0.8 | 12.7 | 24.6 | - | 636 / 800 | 1263 / 1461 |
| de-DE_JT1 | fast_llm | 30 | 0 | 0.320 | 0.533 | 1.7 | 13.6 | 18.6 | - | 484 / 539 | 1114 / 1106 |
| de-DE_JT1 | fast_mai | 30 | 0 | 0.252 | 0.500 | 1.7 | 11.0 | 13.6 | - | 497 / 575 | 991 / 1141 |
| de-DE_JT1 | realtime | 30 | 0 | 0.294 | 0.633 | 3.4 | 11.9 | 15.3 | 1344 / 1639 | -1022 / -419 | 671 / 877 |
| de-DE_JT1 | realtime_refine | 30 | 0 | 0.295 | 0.500 | 0.8 | 12.7 | 16.9 | 1483 / 1662 | -560 / 65 | 1151 / 1228 |

## Speech boundaries

`speech_start_s` / `speech_end_s` (CSV columns) come from the realtime SDK's word-level timestamps and anchor UPL for all services. The full per-word log lives in the sidecar `mazda_de-DE_20260508_193734_words.jsonl` (one JSON object per realtime sample).

Boundary-fix decisions across 90 realtime samples:

- `skip`: 33
- `trim_first`: 6
- `trim_last`: 4

Trimmed/skipped samples (first 20):

| Dataset | Sample ID | Action | speech_start_s | speech_end_s |
|---|---|---|---:|---:|
| de-DE_DT1 | 1l_de-DE_female-DT1/Fahren Sie nach Birmingham.wav | skip | - | - |
| de-DE_DT1 | 1l_de-DE_female-DT1/Navigation stummschalten.wav | skip | - | - |
| de-DE_DT1 | 1l_de-DE_female-DT1/Fahrtenanzeige öffnen.wav | trim_first | 1.95 | 3.07 |
| de-DE_DT1 | 1l_de-DE_female-DT1/Linke Rücksitzbelüftung leicht erhöhen.wav | skip | - | - |
| de-DE_DT1 | 1l_de-DE_male-DT1/Vorderen Bereich etwas erwärmen.wav | skip | - | - |
| de-DE_DT1 | 1l_de-DE_male-DT1/Kartenansicht auf 2D einstellen.wav | trim_last | 1.19 | 3.63 |
| de-DE_DT1 | 1l_de-DE_female-DT1/Eco-Fahrmodus aktivieren.wav | skip | - | - |
| de-DE_DT1 | 1l_de-DE_male-DT1/Luftstrom nach vorn ausrichten.wav | trim_last | 1.56 | 3.68 |
| de-DE_DT1 | 1l_de-DE_male-DT1/Automatische Belüftung beim Entriegeln deaktivieren.wav | skip | - | - |
| de-DE_DT1 | 1l_de-DE_female-DT1/Automatische Belüftung beim Entriegeln deaktivieren.wav | skip | - | - |
| de-DE_DT1 | 1l_de-DE_female-DT1/Automatische Belüftung beim Entriegeln aktivieren.wav | skip | - | - |
| de-DE_DT1 | 1l_de-DE_female-DT1/Diesen Sender aus den Favoriten löschen.wav | trim_first | 3.6 | 4.32 |
| de-DE_DT1 | 1l_de-DE_female-DT1/Linke Rücksitzbelüftung auf Maximum.wav | skip | - | - |
| de-DE_DT1 | 1l_de-DE_male-DT1/Klingelton stummschalten.wav | skip | - | - |
| de-DE_DT1 | 1l_de-DE_female-DT1/Kannst du die Lautstärke auf das Minimum einstellen.wav | skip | - | - |
| de-DE_DT2 | 1l_de-DE_male-DT2/Scheinwerfer auf dritte Stufe einstellen.wav | skip | - | - |
| de-DE_DT1 | 1l_de-DE_female-DT1/Linke Rücksitzbelüftung auf Minimum.wav | trim_first | 4.4 | 5.12 |
| de-DE_DT2 | 1l_de-DE_female-DT2/Fahren Sie nach Birmingham.wav | skip | - | - |
| de-DE_DT2 | 1l_de-DE_female-DT2/Autofenster halb öffnen.wav | skip | - | - |
| de-DE_DT2 | 1l_de-DE_female-DT2/Navigation stummschalten.wav | skip | - | - |

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