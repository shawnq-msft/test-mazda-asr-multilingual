# Mazda ASR Benchmark — mazda_it-IT_20260508_133009.csv

Total rows: **450**  
Tester public IP: **167.220.233.51**  
Tester location: **Tokyo, Tokyo, Japan** (Microsoft Corporation)  
Azure region: **eastus**  
Azure endpoint host: **eastus.api.cognitive.microsoft.com**  
TCP ping to `eastus.api.cognitive.microsoft.com:443` (avg of 5): **228.2 ms**  
VAD set to **500 ms** (realtime `Speech_SegmentationSilenceTimeoutMs`; fast_* audio truncated at `speech_end + 500 ms`)

## Endpoints under test

### `fast_default` — Azure Fast Transcription (default)
- URL: `https://eastus.api.cognitive.microsoft.com/speechtotext/transcriptions:transcribe?api-version=2024-11-15`
- Transport: HTTPS POST (multipart/form-data, chunked)
- Config: `definition = {"locales": ["it-IT"]}`
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
- Config: `definition = {"locales": ["it"], "enhancedMode": {"enabled": true, "model": "mai-transcribe-1"}}`
- Partial results: no
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe>
- Note: Requires Speech resource with mai-transcribe-1 preview enabled.

### `realtime` — Azure Speech SDK — continuous recognition
- URL: `https://eastus.api.cognitive.microsoft.com`
- Transport: WebSocket via azure-cognitiveservices-speech SDK
- Config: `PushAudioInputStream, language="it-IT", continuous`
- Partial results: yes (recognizing/recognized events)
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech>

### `realtime_refine` — Azure Speech SDK — continuous + Post-Stream Refinement (MRS preview)
- URL: `https://eastus.api.cognitive.microsoft.com`
- Transport: WebSocket via azure-cognitiveservices-speech SDK (>=1.49.0)
- Config: `PushAudioInputStream, language="it-IT", continuous, PostProcessingOption="PostRefinement"`
- Partial results: yes (recognizing/recognized events; final replaced after refinement)
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech>
- Note: Requires Speech SDK >= 1.49.0 and a Speech resource in a region where Multi-Recognizer / Post-Stream Refinement public preview is enabled (East US / North Europe rollout). Falls back to non-MRS behavior if PostProcessingOption is not set.

## Datasets under test

- **it-IT_DT1** — Mazda it-IT DT1 voice commands (male + female pooled, 30 random samples)
- **it-IT_DT2** — Mazda it-IT DT2 voice commands (male + female pooled, 30 random samples)
- **it-IT_JT1** — Mazda it-IT JT1 voice commands (male + female pooled, 30 random samples)

## Results

WER breakdown columns are *rates per 100 reference words*. Per-row WER ≈ (INS + DEL + SUB) / ref_len (capped at 1.0 per sample in aggregation).

| Dataset | Service | N | Errors | WER | SER | INS/100 | DEL/100 | SUB/100 | First Latency ms (mean / p90) | LBL ms (mean / p90) | UPL ms (mean / p90) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| it-IT_DT1 | fast_default | 30 | 0 | 0.089 | 0.300 | 2.4 | 0.6 | 5.9 | - | 617 / 723 | 1021 / 1251 |
| it-IT_DT1 | fast_llm | 30 | 0 | 0.072 | 0.267 | 1.8 | 1.2 | 4.7 | - | 513 / 627 | 917 / 1167 |
| it-IT_DT1 | fast_mai | 30 | 0 | 0.096 | 0.300 | 2.4 | 0.0 | 5.3 | - | 491 / 608 | 895 / 1138 |
| it-IT_DT1 | realtime | 30 | 0 | 0.097 | 0.367 | 3.6 | 1.2 | 5.3 | 1213 / 1691 | -118 / 301 | 603 / 869 |
| it-IT_DT1 | realtime_refine | 30 | 0 | 0.082 | 0.267 | 1.8 | 1.2 | 4.7 | 1157 / 1526 | 336 / 748 | 1081 / 1317 |
| it-IT_DT2 | fast_default | 30 | 0 | 0.185 | 0.433 | 1.2 | 7.1 | 10.7 | - | 653 / 731 | 1163 / 1309 |
| it-IT_DT2 | fast_llm | 30 | 0 | 0.205 | 0.433 | 3.0 | 4.1 | 14.2 | - | 524 / 622 | 992 / 1190 |
| it-IT_DT2 | fast_mai | 30 | 0 | 0.183 | 0.467 | 2.4 | 2.4 | 13.6 | - | 500 / 570 | 886 / 1059 |
| it-IT_DT2 | realtime | 30 | 0 | 0.246 | 0.500 | 2.4 | 11.8 | 11.2 | 1207 / 1544 | -97 / 321 | 624 / 864 |
| it-IT_DT2 | realtime_refine | 30 | 0 | 0.180 | 0.433 | 1.8 | 5.9 | 10.7 | 1249 / 1580 | 386 / 782 | 1260 / 2006 |
| it-IT_JT1 | fast_default | 30 | 0 | 0.055 | 0.233 | 1.2 | 0.6 | 3.6 | - | 625 / 728 | 1012 / 1239 |
| it-IT_JT1 | fast_llm | 30 | 0 | 0.053 | 0.200 | 1.8 | 0.6 | 3.0 | - | 507 / 584 | 894 / 1114 |
| it-IT_JT1 | fast_mai | 30 | 0 | 0.042 | 0.200 | 1.2 | 0.0 | 3.0 | - | 551 / 724 | 938 / 1153 |
| it-IT_JT1 | realtime | 30 | 0 | 0.042 | 0.200 | 0.6 | 0.6 | 3.0 | 1114 / 1378 | -144 / 295 | 556 / 787 |
| it-IT_JT1 | realtime_refine | 30 | 0 | 0.055 | 0.233 | 1.2 | 0.6 | 3.6 | 1098 / 1414 | 333 / 712 | 1043 / 1280 |

## Speech boundaries

`speech_start_s` / `speech_end_s` (CSV columns) come from the realtime SDK's word-level timestamps and anchor UPL for all services. The full per-word log lives in the sidecar `mazda_it-IT_20260508_133009_words.jsonl` (one JSON object per realtime sample).

Boundary-fix decisions across 90 realtime samples:

- `skip`: 2
- `trim_both`: 2
- `trim_first`: 3
- `trim_last`: 3

Trimmed/skipped samples (first 20):

| Dataset | Sample ID | Action | speech_start_s | speech_end_s |
|---|---|---|---:|---:|
| it-IT_DT1 | 1l_it-IT_male-DT1/Minimizza la luminosità del display centrale.wav | trim_last | 1.27 | 3.51 |
| it-IT_DT1 | 1l_it-IT_female-DT1/Abilità luminosità schermo automatica.wav | trim_first | 2.47 | 4.87 |
| it-IT_DT1 | 1l_it-IT_female-DT1/Guida verso Birmingham.wav | trim_last | 1.57 | 2.45 |
| it-IT_DT2 | 1l_it-IT_female-DT2/Imposta i fari più alti.wav | trim_both | 2.63 | 2.67 |
| it-IT_DT2 | 1l_it-IT_female-DT2/Apri la visuale panoramica.wav | skip | - | - |
| it-IT_DT2 | 1l_it-IT_female-DT2/Abilità luminosità schermo automatica.wav | trim_first | 2.46 | 4.94 |
| it-IT_DT2 | 1l_it-IT_female-DT2/Apri il finestrino posteriore destro  a metà.wav | skip | - | - |
| it-IT_DT2 | 1l_it-IT_male-DT2/Chiudi Lettore multimediale per il passeggero.wav | trim_last | 1.51 | 2.99 |
| it-IT_DT2 | 1l_it-IT_male-DT2/Disattiva Apple Carplay per il passeggero.wav | trim_both | 2.01 | 3.25 |
| it-IT_JT1 | 1l_it-IT_female-JT1/Abilità luminosità schermo automatica.wav | trim_first | 2.46 | 4.8 |

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