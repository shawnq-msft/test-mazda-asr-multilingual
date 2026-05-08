# Mazda ASR Benchmark — mazda_es-ES_20260508_120527.csv

Total rows: **450**  
Tester public IP: **167.220.233.51**  
Tester location: **Tokyo, Tokyo, Japan** (Microsoft Corporation)  
Azure region: **eastus**  
Azure endpoint host: **eastus.api.cognitive.microsoft.com**  
TCP ping to `eastus.api.cognitive.microsoft.com:443` (avg of 5): **221.8 ms**  
VAD set to **500 ms** (realtime `Speech_SegmentationSilenceTimeoutMs`; fast_* audio truncated at `speech_end + 500 ms`)

## Endpoints under test

### `fast_default` — Azure Fast Transcription (default)
- URL: `https://eastus.api.cognitive.microsoft.com/speechtotext/transcriptions:transcribe?api-version=2024-11-15`
- Transport: HTTPS POST (multipart/form-data, chunked)
- Config: `definition = {"locales": ["es-ES"]}`
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
- Config: `definition = {"locales": ["es"], "enhancedMode": {"enabled": true, "model": "mai-transcribe-1"}}`
- Partial results: no
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe>
- Note: Requires Speech resource with mai-transcribe-1 preview enabled.

### `realtime` — Azure Speech SDK — continuous recognition
- URL: `https://eastus.api.cognitive.microsoft.com`
- Transport: WebSocket via azure-cognitiveservices-speech SDK
- Config: `PushAudioInputStream, language="es-ES", continuous`
- Partial results: yes (recognizing/recognized events)
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech>

### `realtime_refine` — Azure Speech SDK — continuous + Post-Stream Refinement (MRS preview)
- URL: `https://eastus.api.cognitive.microsoft.com`
- Transport: WebSocket via azure-cognitiveservices-speech SDK (>=1.49.0)
- Config: `PushAudioInputStream, language="es-ES", continuous, PostProcessingOption="PostRefinement"`
- Partial results: yes (recognizing/recognized events; final replaced after refinement)
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech>
- Note: Requires Speech SDK >= 1.49.0 and a Speech resource in a region where Multi-Recognizer / Post-Stream Refinement public preview is enabled (East US / North Europe rollout). Falls back to non-MRS behavior if PostProcessingOption is not set.

## Datasets under test

- **es-ES_DT1** — Mazda es-ES DT1 voice commands (male + female pooled, 30 random samples)
- **es-ES_DT2** — Mazda es-ES DT2 voice commands (male + female pooled, 30 random samples)
- **es-ES_JT1** — Mazda es-ES JT1 voice commands (male + female pooled, 30 random samples)

## Results

WER breakdown columns are *rates per 100 reference words*. Per-row WER ≈ (INS + DEL + SUB) / ref_len (capped at 1.0 per sample in aggregation).

| Dataset | Service | N | Errors | WER | SER | INS/100 | DEL/100 | SUB/100 | First Latency ms (mean / p90) | LBL ms (mean / p90) | UPL ms (mean / p90) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| es-ES_DT1 | fast_default | 30 | 0 | 0.147 | 0.433 | 0.0 | 6.4 | 8.1 | - | 573 / 641 | 1177 / 1443 |
| es-ES_DT1 | fast_llm | 30 | 0 | 0.202 | 0.467 | 1.2 | 8.1 | 10.5 | - | 487 / 530 | 1097 / 1414 |
| es-ES_DT1 | fast_mai | 30 | 0 | 0.172 | 0.400 | 0.0 | 8.7 | 7.0 | - | 509 / 665 | 974 / 1154 |
| es-ES_DT1 | realtime | 30 | 0 | 0.283 | 0.600 | 1.7 | 19.8 | 5.2 | 1349 / 1778 | -88 / 2 | 676 / 843 |
| es-ES_DT1 | realtime_refine | 30 | 0 | 0.162 | 0.467 | 0.0 | 11.0 | 4.7 | 1365 / 1605 | 312 / 403 | 1036 / 1255 |
| es-ES_DT2 | fast_default | 30 | 0 | 0.169 | 0.567 | 0.0 | 5.2 | 9.9 | - | 569 / 619 | 1141 / 1179 |
| es-ES_DT2 | fast_llm | 30 | 0 | 0.164 | 0.467 | 1.2 | 7.0 | 7.0 | - | 488 / 537 | 1073 / 1230 |
| es-ES_DT2 | fast_mai | 30 | 0 | 0.161 | 0.367 | 2.9 | 0.6 | 12.2 | - | 496 / 607 | 989 / 1198 |
| es-ES_DT2 | realtime | 30 | 0 | 0.208 | 0.567 | 1.2 | 11.6 | 6.4 | 1256 / 1501 | -111 / 91 | 702 / 912 |
| es-ES_DT2 | realtime_refine | 30 | 0 | 0.188 | 0.567 | 2.9 | 4.1 | 9.9 | 1468 / 2479 | 337 / 752 | 1146 / 1542 |
| es-ES_JT1 | fast_default | 30 | 0 | 0.117 | 0.300 | 0.0 | 6.4 | 4.1 | - | 686 / 780 | 1251 / 1335 |
| es-ES_JT1 | fast_llm | 30 | 0 | 0.143 | 0.400 | 1.2 | 6.4 | 5.8 | - | 513 / 537 | 1089 / 1275 |
| es-ES_JT1 | fast_mai | 30 | 0 | 0.083 | 0.300 | 0.0 | 3.5 | 4.1 | - | 532 / 659 | 1010 / 1200 |
| es-ES_JT1 | realtime | 30 | 0 | 0.159 | 0.500 | 0.0 | 9.3 | 5.2 | 1314 / 1576 | -47 / 78 | 716 / 880 |
| es-ES_JT1 | realtime_refine | 30 | 0 | 0.115 | 0.333 | 0.6 | 7.0 | 2.9 | 1421 / 1891 | 562 / 746 | 1201 / 1306 |

## Speech boundaries

`speech_start_s` / `speech_end_s` (CSV columns) come from the realtime SDK's word-level timestamps and anchor UPL for all services. The full per-word log lives in the sidecar `mazda_es-ES_20260508_120527_words.jsonl` (one JSON object per realtime sample).

Boundary-fix decisions across 90 realtime samples:

- `skip`: 12
- `trim_both`: 1
- `trim_first`: 2
- `trim_last`: 4

Trimmed/skipped samples (first 20):

| Dataset | Sample ID | Action | speech_start_s | speech_end_s |
|---|---|---|---:|---:|
| es-ES_DT1 | 1l_es-ES_male-DT1/130.¿Cuántos minutos faltan para llegar.wav | skip | - | - |
| es-ES_DT1 | 1l_es-ES_male-DT1/109.Ve a la página siguiente.wav | skip | - | - |
| es-ES_DT1 | 1l_es-ES_female-DT1/014.Activa la circulación externa.wav | trim_first | 1.88 | 3.08 |
| es-ES_DT1 | 1l_es-ES_male-DT1/065.Abre la pantalla de iterinario.wav | skip | - | - |
| es-ES_DT1 | 1l_es-ES_male-DT1/080.Activa los datos móviles.wav | trim_last | 1.55 | 2.11 |
| es-ES_DT1 | 1l_es-ES_female-DT1/080.Activa los datos móviles.wav | trim_last | 1.71 | 2.23 |
| es-ES_DT1 | 1l_es-ES_female-DT1/111.Ve a la última página.wav | trim_last | 1.41 | 2.01 |
| es-ES_DT1 | 1l_es-ES_male-DT1/023.Sube un poco el asiento.wav | skip | - | - |
| es-ES_DT1 | 1l_es-ES_male-DT1/045.Activa el modo de mantenimiento de limpiaparabrisas.wav | skip | - | - |
| es-ES_DT2 | 1l_es-ES_female-DT2/014.Activa la circulación externa.wav | trim_first | 1.83 | 3.07 |
| es-ES_DT2 | 1l_es-ES_male-DT2/065.Abre la pantalla de iterinario.wav | skip | - | - |
| es-ES_DT2 | 1l_es-ES_male-DT2/080.Activa los datos móviles.wav | skip | - | - |
| es-ES_DT2 | 1l_es-ES_female-DT2/080.Activa los datos móviles.wav | trim_last | 1.72 | 2.24 |
| es-ES_DT2 | 1l_es-ES_male-DT2/023.Sube un poco el asiento.wav | skip | - | - |
| es-ES_JT1 | 1l_es-ES_male-JT1/109.Ve a la página siguiente.wav | skip | - | - |
| es-ES_JT1 | 1l_es-ES_female-JT1/014.Activa la circulación externa.wav | skip | - | - |
| es-ES_JT1 | 1l_es-ES_male-JT1/065.Abre la pantalla de iterinario.wav | skip | - | - |
| es-ES_JT1 | 1l_es-ES_female-JT1/080.Activa los datos móviles.wav | trim_both | 1.72 | 2.24 |
| es-ES_JT1 | 1l_es-ES_male-JT1/023.Sube un poco el asiento.wav | skip | - | - |

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