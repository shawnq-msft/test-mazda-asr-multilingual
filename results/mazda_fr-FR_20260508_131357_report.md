# Mazda ASR Benchmark — mazda_fr-FR_20260508_131357.csv

Total rows: **450**  
Tester public IP: **167.220.233.51**  
Tester location: **Tokyo, Tokyo, Japan** (Microsoft Corporation)  
Azure region: **eastus**  
Azure endpoint host: **eastus.api.cognitive.microsoft.com**  
TCP ping to `eastus.api.cognitive.microsoft.com:443` (avg of 5): **226.5 ms**  
VAD set to **500 ms** (realtime `Speech_SegmentationSilenceTimeoutMs`; fast_* audio truncated at `speech_end + 500 ms`)

## Endpoints under test

### `fast_default` — Azure Fast Transcription (default)
- URL: `https://eastus.api.cognitive.microsoft.com/speechtotext/transcriptions:transcribe?api-version=2024-11-15`
- Transport: HTTPS POST (multipart/form-data, chunked)
- Config: `definition = {"locales": ["fr-FR"]}`
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
- Config: `definition = {"locales": ["fr"], "enhancedMode": {"enabled": true, "model": "mai-transcribe-1"}}`
- Partial results: no
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe>
- Note: Requires Speech resource with mai-transcribe-1 preview enabled.

### `realtime` — Azure Speech SDK — continuous recognition
- URL: `https://eastus.api.cognitive.microsoft.com`
- Transport: WebSocket via azure-cognitiveservices-speech SDK
- Config: `PushAudioInputStream, language="fr-FR", continuous`
- Partial results: yes (recognizing/recognized events)
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech>

### `realtime_refine` — Azure Speech SDK — continuous + Post-Stream Refinement (MRS preview)
- URL: `https://eastus.api.cognitive.microsoft.com`
- Transport: WebSocket via azure-cognitiveservices-speech SDK (>=1.49.0)
- Config: `PushAudioInputStream, language="fr-FR", continuous, PostProcessingOption="PostRefinement"`
- Partial results: yes (recognizing/recognized events; final replaced after refinement)
- Docs: <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech>
- Note: Requires Speech SDK >= 1.49.0 and a Speech resource in a region where Multi-Recognizer / Post-Stream Refinement public preview is enabled (East US / North Europe rollout). Falls back to non-MRS behavior if PostProcessingOption is not set.

## Datasets under test

- **fr-FR_DT1** — Mazda fr-FR DT1 voice commands (male + female pooled, 30 random samples)
- **fr-FR_DT2** — Mazda fr-FR DT2 voice commands (male + female pooled, 30 random samples)
- **fr-FR_JT1** — Mazda fr-FR JT1 voice commands (male + female pooled, 30 random samples)

## Results

WER breakdown columns are *rates per 100 reference words*. Per-row WER ≈ (INS + DEL + SUB) / ref_len (capped at 1.0 per sample in aggregation).

| Dataset | Service | N | Errors | WER | SER | INS/100 | DEL/100 | SUB/100 | First Latency ms (mean / p90) | LBL ms (mean / p90) | UPL ms (mean / p90) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| fr-FR_DT1 | fast_default | 30 | 0 | 0.132 | 0.400 | 0.0 | 5.1 | 7.3 | - | 642 / 710 | 1300 / 1618 |
| fr-FR_DT1 | fast_llm | 30 | 0 | 0.180 | 0.367 | 1.1 | 3.4 | 11.9 | - | 505 / 556 | 1171 / 1169 |
| fr-FR_DT1 | fast_mai | 30 | 0 | 0.113 | 0.400 | 1.7 | 0.6 | 9.6 | - | 494 / 557 | 1004 / 1124 |
| fr-FR_DT1 | realtime | 30 | 0 | 0.177 | 0.467 | 1.1 | 3.4 | 13.0 | 1348 / 1624 | -1602 / -1098 | 769 / 921 |
| fr-FR_DT1 | realtime_refine | 30 | 0 | 0.098 | 0.333 | 1.1 | 1.1 | 8.5 | 1462 / 1933 | -1178 / -635 | 1194 / 1330 |
| fr-FR_DT2 | fast_default | 30 | 0 | 0.130 | 0.400 | 0.0 | 6.2 | 7.3 | - | 620 / 689 | 1229 / 1240 |
| fr-FR_DT2 | fast_llm | 30 | 0 | 0.204 | 0.433 | 4.0 | 5.6 | 12.4 | - | 503 / 561 | 1108 / 1129 |
| fr-FR_DT2 | fast_mai | 30 | 0 | 0.149 | 0.400 | 4.0 | 2.3 | 12.4 | - | 483 / 505 | 1016 / 1096 |
| fr-FR_DT2 | realtime | 30 | 0 | 0.157 | 0.467 | 0.0 | 3.4 | 12.4 | 1340 / 1623 | -1638 / -1103 | 779 / 1003 |
| fr-FR_DT2 | realtime_refine | 30 | 0 | 0.099 | 0.367 | 0.0 | 2.3 | 7.9 | 1398 / 1823 | -1195 / -658 | 1225 / 1503 |
| fr-FR_JT1 | fast_default | 30 | 0 | 0.090 | 0.333 | 0.0 | 1.7 | 7.9 | - | 613 / 642 | 1207 / 1229 |
| fr-FR_JT1 | fast_llm | 30 | 0 | 0.060 | 0.267 | 0.0 | 1.1 | 5.6 | - | 496 / 558 | 1092 / 1127 |
| fr-FR_JT1 | fast_mai | 30 | 0 | 0.058 | 0.300 | 0.0 | 0.0 | 6.8 | - | 525 / 653 | 1049 / 1174 |
| fr-FR_JT1 | realtime | 30 | 0 | 0.082 | 0.300 | 0.0 | 1.1 | 7.9 | 1292 / 1627 | -1642 / -1117 | 694 / 860 |
| fr-FR_JT1 | realtime_refine | 30 | 0 | 0.085 | 0.333 | 0.0 | 1.7 | 6.8 | 1307 / 1593 | -1218 / -721 | 1128 / 1275 |

## Speech boundaries

`speech_start_s` / `speech_end_s` (CSV columns) come from the realtime SDK's word-level timestamps and anchor UPL for all services. The full per-word log lives in the sidecar `mazda_fr-FR_20260508_131357_words.jsonl` (one JSON object per realtime sample).

Boundary-fix decisions across 90 realtime samples:

- `skip`: 4
- `trim_both`: 14
- `trim_first`: 2
- `trim_last`: 6

Trimmed/skipped samples (first 20):

| Dataset | Sample ID | Action | speech_start_s | speech_end_s |
|---|---|---|---:|---:|
| fr-FR_DT1 | 1l_fr-FR_male-DT1/Monte légèrement la hauteur de l’ATH.wav | trim_both | 2.88 | 5.0 |
| fr-FR_DT1 | 1l_fr-FR_female-DT1/Coupe la climatisation pour l’avant.wav | trim_last | 3.18 | 4.74 |
| fr-FR_DT1 | 1l_fr-FR_male-DT1/Passe l’affichage en mode sombre.wav | trim_last | 2.35 | 3.87 |
| fr-FR_DT1 | 1l_fr-FR_male-DT1/Régle le chauffage du siège passager au minimum.wav | trim_both | 2.99 | 4.91 |
| fr-FR_DT1 | 1l_fr-FR_male-DT1/Active le mode scénario.wav | trim_both | 2.9 | 3.62 |
| fr-FR_DT1 | 1l_fr-FR_female-DT1/Lève légèrement le coussin s'il te plaît.wav | trim_both | 2.69 | 4.49 |
| fr-FR_DT1 | 1l_fr-FR_male-DT1/Coupe la climatisation pour l’avant.wav | trim_last | 3.22 | 4.66 |
| fr-FR_DT1 | 1l_fr-FR_male-DT1/Va à la page suivante.wav | skip | - | - |
| fr-FR_DT1 | 1l_fr-FR_male-DT1/Ferme légèrement la vitre arrière gauche.wav | skip | - | - |
| fr-FR_DT1 | 1l_fr-FR_male-DT1/Régle l’avant au minimum de température.wav | trim_both | 3.22 | 4.5 |
| fr-FR_DT2 | 1l_fr-FR_male-DT2/Monte légèrement la hauteur de l’ATH.wav | trim_both | 2.85 | 5.01 |
| fr-FR_DT2 | 1l_fr-FR_female-DT2/Coupe la climatisation pour l’avant.wav | trim_last | 3.18 | 4.74 |
| fr-FR_DT2 | 1l_fr-FR_male-DT2/Régle le chauffage du siège passager au minimum.wav | trim_both | 2.84 | 4.92 |
| fr-FR_DT2 | 1l_fr-FR_male-DT2/Passe l’affichage en mode sombre.wav | trim_both | 3.43 | 3.87 |
| fr-FR_DT2 | 1l_fr-FR_male-DT2/Désactive la fermeture automatique des vitres.wav | trim_first | 4.01 | 4.81 |
| fr-FR_DT2 | 1l_fr-FR_male-DT2/Ferme la vitre arrière droite.wav | trim_first | 4.22 | 5.34 |
| fr-FR_DT2 | 1l_fr-FR_female-DT2/Lève légèrement le coussin s'il te plaît.wav | trim_both | 2.68 | 4.56 |
| fr-FR_DT2 | 1l_fr-FR_male-DT2/Coupe la climatisation pour l’avant.wav | trim_last | 3.18 | 4.66 |
| fr-FR_DT2 | 1l_fr-FR_male-DT2/Ferme légèrement la vitre arrière gauche.wav | skip | - | - |
| fr-FR_DT2 | 1l_fr-FR_male-DT2/Régle l’avant au minimum de température.wav | trim_both | 3.18 | 4.46 |

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