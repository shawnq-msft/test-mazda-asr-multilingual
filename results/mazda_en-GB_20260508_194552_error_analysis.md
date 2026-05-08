# Error analysis — mazda_en-GB_20260508_194552.csv

Audio links (▶) point to `results/audio/<dataset>/<sample_id>.wav` so a reviewer can play the clip directly.

## Datasets under test

- **en-GB_DT1** — Mazda en-GB DT1 voice commands (male + female pooled)
- **en-GB_DT2** — Mazda en-GB DT2 voice commands (male + female pooled)
- **en-GB_JT1** — Mazda en-GB JT1 voice commands (male + female pooled)

Total samples: **90**  

## Speech boundaries

`speech_start_s` / `speech_end_s` come from the realtime SDK's word-level timestamps and anchor UPL for all services. Per-word detail lives in the sidecar `mazda_en-GB_20260508_194552_words.jsonl`.

Boundary-fix actions across 90 realtime samples: `skip`=2, `trim_both`=4, `trim_first`=5, `trim_last`=4

## Results

INS/DEL/SUB are *rates per 100 reference words*. Their sum ≈ WER × 100.

| Dataset | Service | N | WER | SER | INS/100 | DEL/100 | SUB/100 | LBL ms (mean / p90) | UPL ms (mean / p90) |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| en-GB_DT1 | fast_default | 30 | 0.260 | 0.433 | 3.8 | 5.6 | 12.5 | 555 / 630 | 997 / 1169 |
| en-GB_DT1 | fast_llm | 30 | 0.220 | 0.367 | 4.4 | 5.0 | 8.8 | 476 / 498 | 918 / 1055 |
| en-GB_DT1 | fast_mai | 30 | 0.200 | 0.367 | 4.4 | 2.5 | 10.6 | 522 / 630 | 964 / 1171 |
| en-GB_DT1 | realtime | 30 | 0.241 | 0.500 | 2.5 | 3.8 | 13.8 | -303 / 328 | 619 / 831 |
| en-GB_DT1 | realtime_refine | 30 | 0.246 | 0.467 | 4.4 | 3.1 | 13.8 | 65 / 736 | 1126 / 1292 |
| en-GB_DT2 | fast_default | 30 | 0.356 | 0.567 | 3.1 | 12.5 | 20.0 | 594 / 652 | 1090 / 1221 |
| en-GB_DT2 | fast_llm | 30 | 0.273 | 0.500 | 1.9 | 8.1 | 16.9 | 476 / 530 | 974 / 1130 |
| en-GB_DT2 | fast_mai | 30 | 0.261 | 0.400 | 4.4 | 2.5 | 17.5 | 482 / 588 | 908 / 1120 |
| en-GB_DT2 | realtime | 30 | 0.351 | 0.600 | 5.0 | 11.9 | 16.9 | -300 / 327 | 617 / 951 |
| en-GB_DT2 | realtime_refine | 30 | 0.382 | 0.600 | 5.0 | 6.2 | 25.6 | 125 / 657 | 1243 / 1691 |
| en-GB_JT1 | fast_default | 30 | 0.086 | 0.200 | 2.5 | 3.1 | 1.9 | 603 / 768 | 1011 / 1305 |
| en-GB_JT1 | fast_llm | 30 | 0.080 | 0.200 | 1.9 | 3.8 | 1.2 | 474 / 516 | 882 / 1058 |
| en-GB_JT1 | fast_mai | 30 | 0.104 | 0.233 | 2.5 | 3.8 | 3.1 | 496 / 626 | 904 / 1062 |
| en-GB_JT1 | realtime | 30 | 0.135 | 0.300 | 2.5 | 3.1 | 5.0 | -248 / 328 | 614 / 911 |
| en-GB_JT1 | realtime_refine | 30 | 0.138 | 0.267 | 4.4 | 2.5 | 3.8 | 102 / 721 | 1112 / 1320 |

## Best / median / worst WER per (dataset, service)

### en-GB_DT1 / fast_default  (n=30)
**BEST** — `1l_en-GB_male-DT1/Play the previous song.wav` [▶](audio/en-GB_DT1/1l_en-GB_male-DT1/Play%20the%20previous%20song.wav.wav)  wer=0.000  speech=[1.07s, 2.55s]  fix=none
- ref: `Play the previous song`
- hyp: `Play the previous song.`
**MEDIAN** — `1l_en-GB_male-DT1/Turn on side mirror adjustment mode.wav` [▶](audio/en-GB_DT1/1l_en-GB_male-DT1/Turn%20on%20side%20mirror%20adjustment%20mode.wav.wav)  wer=0.000  speech=[1.06s, 3.46s]  fix=none
- ref: `Turn on side mirror adjustment mode`
- hyp: `Turn on side mirror adjustment mode.`
**WORST** — `1l_en-GB_female-DT1/Play 100.wav` [▶](audio/en-GB_DT1/1l_en-GB_female-DT1/Play%20100.wav.wav)  wer=1.500  speech=[1.63s, 3.75s]  fix=trim_both
- ref: `Play 100`
- hyp: `Hey, 100.7 FM.`

### en-GB_DT1 / fast_llm  (n=30)
**BEST** — `1l_en-GB_male-DT1/Play the previous song.wav` [▶](audio/en-GB_DT1/1l_en-GB_male-DT1/Play%20the%20previous%20song.wav.wav)  wer=0.000  speech=[1.07s, 2.55s]  fix=none
- ref: `Play the previous song`
- hyp: `Play the previous song.`
**MEDIAN** — `1l_en-GB_male-DT1/Please slide the seat forward.wav` [▶](audio/en-GB_DT1/1l_en-GB_male-DT1/Please%20slide%20the%20seat%20forward.wav.wav)  wer=0.000  speech=[1.08s, 2.92s]  fix=none
- ref: `Please slide the seat forward`
- hyp: `Please slide the seat forward.`
**WORST** — `1l_en-GB_male-DT1/Disable Apple Carplay.wav` [▶](audio/en-GB_DT1/1l_en-GB_male-DT1/Disable%20Apple%20Carplay.wav.wav)  wer=1.000  speech=[1.11s, 2.71s]  fix=none
- ref: `Disable Apple Carplay`
- hyp: `Saibo Aapo Kaapre.`

### en-GB_DT1 / fast_mai  (n=30)
**BEST** — `1l_en-GB_male-DT1/Play the previous song.wav` [▶](audio/en-GB_DT1/1l_en-GB_male-DT1/Play%20the%20previous%20song.wav.wav)  wer=0.000  speech=[1.07s, 2.55s]  fix=none
- ref: `Play the previous song`
- hyp: `Play the previous song.`
**MEDIAN** — `1l_en-GB_female-DT1/Open right rear window to 60%.wav` [▶](audio/en-GB_DT1/1l_en-GB_female-DT1/Open%20right%20rear%20window%20to%2060%25.wav.wav)  wer=0.000  speech=[1.22s, 4.06s]  fix=none
- ref: `Open right rear window to 60%`
- hyp: `Open right rear window to 60%.`
**WORST** — `1l_en-GB_female-DT1/raise the temperature by 3 degrees.wav` [▶](audio/en-GB_DT1/1l_en-GB_female-DT1/raise%20the%20temperature%20by%203%20degrees.wav.wav)  wer=1.000  speech=[1.91s, 4.15s]  fix=none
- ref: `raise the temperature by 3 degrees`
- hyp: `The town in the chat is 5.3 degrees.`

### en-GB_DT1 / realtime  (n=30)
**BEST** — `1l_en-GB_male-DT1/Play the previous song.wav` [▶](audio/en-GB_DT1/1l_en-GB_male-DT1/Play%20the%20previous%20song.wav.wav)  wer=0.000  speech=[1.07s, 2.55s]  fix=none
- ref: `Play the previous song`
- hyp: `Play the previous song.`
**MEDIAN** — `1l_en-GB_female-DT1/Can you set the voice volume to the minimum.wav` [▶](audio/en-GB_DT1/1l_en-GB_female-DT1/Can%20you%20set%20the%20voice%20volume%20to%20the%20minimum.wav.wav)  wer=0.111  speech=[1.16s, 4.12s]  fix=none
- ref: `Can you set the voice volume to the minimum`
- hyp: `Can you search the voice volume to the minimum?`
**WORST** — `1l_en-GB_female-DT1/Play 100.wav` [▶](audio/en-GB_DT1/1l_en-GB_female-DT1/Play%20100.wav.wav)  wer=1.500  speech=[1.63s, 3.75s]  fix=trim_both
- ref: `Play 100`
- hyp: `Create 100.7 FM.`

### en-GB_DT1 / realtime_refine  (n=30)
**BEST** — `1l_en-GB_male-DT1/Play the previous song.wav` [▶](audio/en-GB_DT1/1l_en-GB_male-DT1/Play%20the%20previous%20song.wav.wav)  wer=0.000  speech=[1.07s, 2.55s]  fix=none
- ref: `Play the previous song`
- hyp: `Play the previous song.`
**MEDIAN** — `1l_en-GB_female-DT1/Page 4.wav` [▶](audio/en-GB_DT1/1l_en-GB_female-DT1/Page%204.wav.wav)  wer=0.000  speech=[1.3s, 2.3s]  fix=none
- ref: `Page 4`
- hyp: `Page 4.`
**WORST** — `1l_en-GB_female-DT1/Play 100.wav` [▶](audio/en-GB_DT1/1l_en-GB_female-DT1/Play%20100.wav.wav)  wer=1.500  speech=[1.63s, 3.75s]  fix=trim_both
- ref: `Play 100`
- hyp: `100.7 FM.`

### en-GB_DT2 / fast_default  (n=30)
**BEST** — `1l_en-GB_male-DT2/Play the previous song.wav` [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/Play%20the%20previous%20song.wav.wav)  wer=0.000  speech=[1.04s, 2.64s]  fix=none
- ref: `Play the previous song`
- hyp: `Play the previous song.`
**MEDIAN** — `1l_en-GB_female-DT2/Increase the HUD brightness slightly.wav` [▶](audio/en-GB_DT2/1l_en-GB_female-DT2/Increase%20the%20HUD%20brightness%20slightly.wav.wav)  wer=0.200  speech=[2.24s, 3.96s]  fix=none
- ref: `Increase the HUD brightness slightly`
- hyp: `Reduce the HUD brightness slightly.`
**WORST** — `1l_en-GB_female-DT2/Close HUD.wav` [▶](audio/en-GB_DT2/1l_en-GB_female-DT2/Close%20HUD.wav.wav)  wer=1.000  speech=[1.99s, 2.63s]  fix=trim_first
- ref: `Close HUD`
- hyp: `Hello, HED.`

### en-GB_DT2 / fast_llm  (n=30)
**BEST** — `1l_en-GB_male-DT2/Play the previous song.wav` [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/Play%20the%20previous%20song.wav.wav)  wer=0.000  speech=[1.04s, 2.64s]  fix=none
- ref: `Play the previous song`
- hyp: `Play the previous song.`
**MEDIAN** — `1l_en-GB_female-DT2/Change the fan's direction to face.wav` [▶](audio/en-GB_DT2/1l_en-GB_female-DT2/Change%20the%20fan%27s%20direction%20to%20face.wav.wav)  wer=0.143  speech=[1.71s, 4.59s]  fix=none
- ref: `Change the fan's direction to face`
- hyp: `Change the plane's direction to face.`
**WORST** — `1l_en-GB_male-DT2/Adjust ringtone volume to 5 levels.wav` [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/Adjust%20ringtone%20volume%20to%205%20levels.wav.wav)  wer=1.167  speech=[1.13s, 2.97s]  fix=trim_last
- ref: `Adjust ringtone volume to 5 levels`
- hyp: `Just bring home volumes of fiber optics.`

### en-GB_DT2 / fast_mai  (n=30)
**BEST** — `1l_en-GB_male-DT2/Play the previous song.wav` [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/Play%20the%20previous%20song.wav.wav)  wer=0.000  speech=[1.04s, 2.64s]  fix=none
- ref: `Play the previous song`
- hyp: `Play the previous song.`
**MEDIAN** — `1l_en-GB_male-DT2/Please slide the seat forward.wav` [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/Please%20slide%20the%20seat%20forward.wav.wav)  wer=0.000  speech=[1.08s, 3.0s]  fix=none
- ref: `Please slide the seat forward`
- hyp: `Please slide the seat forward.`
**WORST** — `1l_en-GB_female-DT2/Close HUD.wav` [▶](audio/en-GB_DT2/1l_en-GB_female-DT2/Close%20HUD.wav.wav)  wer=1.500  speech=[1.99s, 2.63s]  fix=trim_first
- ref: `Close HUD`
- hyp: `Close. H-E-D.`

### en-GB_DT2 / realtime  (n=30)
**BEST** — `1l_en-GB_male-DT2/Play the previous song.wav` [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/Play%20the%20previous%20song.wav.wav)  wer=0.000  speech=[1.04s, 2.64s]  fix=none
- ref: `Play the previous song`
- hyp: `Play the previous song.`
**MEDIAN** — `1l_en-GB_male-DT2/Please slide the seat forward.wav` [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/Please%20slide%20the%20seat%20forward.wav.wav)  wer=0.200  speech=[1.08s, 3.0s]  fix=none
- ref: `Please slide the seat forward`
- hyp: `We slide the seat forward.`
**WORST** — `1l_en-GB_male-DT2/Close front row window to half.wav` [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/Close%20front%20row%20window%20to%20half.wav.wav)  wer=1.000  speech=[1.45s, 2.41s]  fix=trim_both
- ref: `Close front row window to half`
- hyp: `It's the right row window cousins.`

### en-GB_DT2 / realtime_refine  (n=30)
**BEST** — `1l_en-GB_male-DT2/Play the previous song.wav` [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/Play%20the%20previous%20song.wav.wav)  wer=0.000  speech=[1.04s, 2.64s]  fix=none
- ref: `Play the previous song`
- hyp: `Play the previous song.`
**MEDIAN** — `1l_en-GB_male-DT2/Set the front row to the lowest temperature.wav` [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/Set%20the%20front%20row%20to%20the%20lowest%20temperature.wav.wav)  wer=0.250  speech=[1.06s, 3.72s]  fix=none
- ref: `Set the front row to the lowest temperature`
- hyp: `Set your front row to the notice temperature.`
**WORST** — `1l_en-GB_female-DT2/Show the AC setting page.wav` [▶](audio/en-GB_DT2/1l_en-GB_female-DT2/Show%20the%20AC%20setting%20page.wav.wav)  wer=1.200  speech=[1.43s, 3.91s]  fix=none
- ref: `Show the AC setting page`
- hyp: `Sharon P.H.C., Duffing Coach.`

### en-GB_JT1 / fast_default  (n=30)
**BEST** — `1l_en-GB_male-JT1/Play the previous song.wav` [▶](audio/en-GB_JT1/1l_en-GB_male-JT1/Play%20the%20previous%20song.wav.wav)  wer=0.000  speech=[1.06s, 2.74s]  fix=none
- ref: `Play the previous song`
- hyp: `Play the previous song.`
**MEDIAN** — `1l_en-GB_male-JT1/Mute the voice.wav` [▶](audio/en-GB_JT1/1l_en-GB_male-JT1/Mute%20the%20voice.wav.wav)  wer=0.000  speech=[1.05s, 2.29s]  fix=none
- ref: `Mute the voice`
- hyp: `Mute the voice.`
**WORST** — `1l_en-GB_female-JT1/Play 100.wav` [▶](audio/en-GB_JT1/1l_en-GB_female-JT1/Play%20100.wav.wav)  wer=1.000  speech=[1.09s, 3.73s]  fix=trim_last
- ref: `Play 100`
- hyp: `Play 100.7 FM.`

### en-GB_JT1 / fast_llm  (n=30)
**BEST** — `1l_en-GB_male-JT1/Play the previous song.wav` [▶](audio/en-GB_JT1/1l_en-GB_male-JT1/Play%20the%20previous%20song.wav.wav)  wer=0.000  speech=[1.06s, 2.74s]  fix=none
- ref: `Play the previous song`
- hyp: `Play the previous song.`
**MEDIAN** — `1l_en-GB_male-JT1/Mute the voice.wav` [▶](audio/en-GB_JT1/1l_en-GB_male-JT1/Mute%20the%20voice.wav.wav)  wer=0.000  speech=[1.05s, 2.29s]  fix=none
- ref: `Mute the voice`
- hyp: `Mute the voice.`
**WORST** — `1l_en-GB_female-JT1/Play 100.wav` [▶](audio/en-GB_JT1/1l_en-GB_female-JT1/Play%20100.wav.wav)  wer=1.000  speech=[1.09s, 3.73s]  fix=trim_last
- ref: `Play 100`
- hyp: `Play 100.7 FM.`

### en-GB_JT1 / fast_mai  (n=30)
**BEST** — `1l_en-GB_male-JT1/Play the previous song.wav` [▶](audio/en-GB_JT1/1l_en-GB_male-JT1/Play%20the%20previous%20song.wav.wav)  wer=0.000  speech=[1.06s, 2.74s]  fix=none
- ref: `Play the previous song`
- hyp: `Play the previous song.`
**MEDIAN** — `1l_en-GB_male-JT1/Mute the voice.wav` [▶](audio/en-GB_JT1/1l_en-GB_male-JT1/Mute%20the%20voice.wav.wav)  wer=0.000  speech=[1.05s, 2.29s]  fix=none
- ref: `Mute the voice`
- hyp: `Mute the voice.`
**WORST** — `1l_en-GB_female-JT1/Play 100.wav` [▶](audio/en-GB_JT1/1l_en-GB_female-JT1/Play%20100.wav.wav)  wer=1.000  speech=[1.09s, 3.73s]  fix=trim_last
- ref: `Play 100`
- hyp: `Play 100.7 FM.`

### en-GB_JT1 / realtime  (n=30)
**BEST** — `1l_en-GB_male-JT1/Play the previous song.wav` [▶](audio/en-GB_JT1/1l_en-GB_male-JT1/Play%20the%20previous%20song.wav.wav)  wer=0.000  speech=[1.06s, 2.74s]  fix=none
- ref: `Play the previous song`
- hyp: `Play the previous song.`
**MEDIAN** — `1l_en-GB_female-JT1/Open right rear window to 60%.wav` [▶](audio/en-GB_JT1/1l_en-GB_female-JT1/Open%20right%20rear%20window%20to%2060%25.wav.wav)  wer=0.000  speech=[1.22s, 4.14s]  fix=none
- ref: `Open right rear window to 60%`
- hyp: `Open right rear window to 60%.`
**WORST** — `1l_en-GB_female-JT1/Close HUD.wav` [▶](audio/en-GB_JT1/1l_en-GB_female-JT1/Close%20HUD.wav.wav)  wer=1.000  speech=[2.03s, 2.63s]  fix=trim_first
- ref: `Close HUD`
- hyp: `Lowe's HUD.`

### en-GB_JT1 / realtime_refine  (n=30)
**BEST** — `1l_en-GB_male-JT1/Play the previous song.wav` [▶](audio/en-GB_JT1/1l_en-GB_male-JT1/Play%20the%20previous%20song.wav.wav)  wer=0.000  speech=[1.06s, 2.74s]  fix=none
- ref: `Play the previous song`
- hyp: `Play the previous song.`
**MEDIAN** — `1l_en-GB_male-JT1/Lower fan speed by 1 level.wav` [▶](audio/en-GB_JT1/1l_en-GB_male-JT1/Lower%20fan%20speed%20by%201%20level.wav.wav)  wer=0.000  speech=[1.03s, 3.27s]  fix=none
- ref: `Lower fan speed by 1 level`
- hyp: `Lower fan speed by 1 level.`
**WORST** — `1l_en-GB_female-JT1/Close HUD.wav` [▶](audio/en-GB_JT1/1l_en-GB_female-JT1/Close%20HUD.wav.wav)  wer=1.000  speech=[2.03s, 2.63s]  fix=trim_first
- ref: `Close HUD`
- hyp: `Lowe's HUD.`

## fast_llm hallucinations

`fast_llm` does not set a locale — it relies on auto-detection. When the acoustic signal is weak or ambiguous, it may produce text in the wrong language or fabricate content from its training data.

Found **8** likely hallucinations (WER ≥ 0.8 and ≤ 1 word overlap with reference):

| Audio | Dataset | Sample | WER | Boundary | Reference | Hypothesis |
|---|---|---|---:|---|---|---|
| [▶](audio/en-GB_DT1/1l_en-GB_female-DT1/Close%20HUD.wav.wav) | en-GB_DT1 | 1l_en-GB_female-DT1/Close HUD.wav | 1.000 | trim_first | `Close HUD` | `Phone Heath.` |
| [▶](audio/en-GB_DT1/1l_en-GB_male-DT1/Disable%20Apple%20Carplay.wav.wav) | en-GB_DT1 | 1l_en-GB_male-DT1/Disable Apple Carplay.wav | 1.000 | none | `Disable Apple Carplay` | `Saibo Aapo Kaapre.` |
| [▶](audio/en-GB_DT2/1l_en-GB_female-DT2/Play%20100.wav.wav) | en-GB_DT2 | 1l_en-GB_female-DT2/Play 100.wav | 1.000 | trim_last | `Play 100` | `Play 127 FM.` |
| [▶](audio/en-GB_DT2/1l_en-GB_female-DT2/Set%20the%20%20POI%20%20as%20my%20home.wav.wav) | en-GB_DT2 | 1l_en-GB_female-DT2/Set the  POI  as my home.wav | 1.167 | skip | `Set the  POI  as my home` | `Thanks, Paul. You are running a business.` |
| [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/Adjust%20ringtone%20volume%20to%205%20levels.wav.wav) | en-GB_DT2 | 1l_en-GB_male-DT2/Adjust ringtone volume to 5 levels.wav | 1.167 | trim_last | `Adjust ringtone volume to 5 levels` | `Just bring home volumes of fiber optics.` |
| [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/Close%20front%20row%20window%20to%20half.wav.wav) | en-GB_DT2 | 1l_en-GB_male-DT2/Close front row window to half.wav | 0.833 | trim_both | `Close front row window to half` | `Window.` |
| [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/Disable%20Apple%20Carplay.wav.wav) | en-GB_DT2 | 1l_en-GB_male-DT2/Disable Apple Carplay.wav | 1.000 | none | `Disable Apple Carplay` | `细胞压迫康病` |
| [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/Turn%20off%20wireless%20charging%20Turn%20off%20wireless%20charging.wav.wav) | en-GB_DT2 | 1l_en-GB_male-DT2/Turn off wireless charging Turn off wireless charging.wav | 0.875 | skip | `Turn off wireless charging Turn off wireless charging` | `Turn on Wi-Fi.` |

## Top fast_default vs realtime disagreements

### en-GB_JT1/1l_en-GB_female-JT1/Close HUD.wav [▶](audio/en-GB_JT1/1l_en-GB_female-JT1/Close%20HUD.wav.wav)  Δwer=1.000  (fast_default=0.000, realtime=1.000)  speech=[2.03s, 2.63s] fix=trim_first
- ref:           `Close HUD`
- fast_default   `Close. HUD.`
- fast_llm       `close HUD.`
- fast_mai       `Close HUD.`
- realtime       `Lowe's HUD.`
- realtime_refine `Lowe's HUD.`

### en-GB_DT1/1l_en-GB_male-DT1/Call Jane.wav [▶](audio/en-GB_DT1/1l_en-GB_male-DT1/Call%20Jane.wav.wav)  Δwer=1.000  (fast_default=0.000, realtime=1.000)  speech=[1.48s, 1.96s] fix=trim_first
- ref:           `Call Jane`
- fast_default   `Call Jane.`
- fast_llm       `Call Jane.`
- fast_mai       `Call Jane.`
- realtime       `Paul Kane.`
- realtime_refine `Call Jane.`

### en-GB_DT1/1l_en-GB_male-DT1/Disable Apple Carplay.wav [▶](audio/en-GB_DT1/1l_en-GB_male-DT1/Disable%20Apple%20Carplay.wav.wav)  Δwer=0.667  (fast_default=1.000, realtime=0.333)  speech=[1.11s, 2.71s] fix=none
- ref:           `Disable Apple Carplay`
- fast_default   `Sabo Aboka Bank.`
- fast_llm       `Saibo Aapo Kaapre.`
- fast_mai       `Say to Apple CarPlay.`
- realtime       `Disable Apple Carpet.`
- realtime_refine `Seybo apoca back.`

### en-GB_DT2/1l_en-GB_male-DT2/Mute the voice.wav [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/Mute%20the%20voice.wav.wav)  Δwer=0.667  (fast_default=0.000, realtime=0.667)  speech=[1.34s, 2.3s] fix=trim_first
- ref:           `Mute the voice`
- fast_default   `Mute the voice.`
- fast_llm       `Meet the Voice.`
- fast_mai       `Mute the voice.`
- realtime       `Mean to the voice.`
- realtime_refine `Meet the voice.`

### en-GB_DT2/1l_en-GB_female-DT2/Show the AC setting page.wav [▶](audio/en-GB_DT2/1l_en-GB_female-DT2/Show%20the%20AC%20setting%20page.wav.wav)  Δwer=0.600  (fast_default=1.000, realtime=0.400)  speech=[1.43s, 3.91s] fix=none
- ref:           `Show the AC setting page`
- fast_default   `Sharon P.K.C.`
- fast_llm       `Show the AC testing page.`
- fast_mai       `Show the ABC dressing page.`
- realtime       `Sharing the AC defing page.`
- realtime_refine `Sharon P.H.C., Duffing Coach.`

### en-GB_DT1/1l_en-GB_female-DT1/Set the  POI  as my home.wav [▶](audio/en-GB_DT1/1l_en-GB_female-DT1/Set%20the%20%20POI%20%20as%20my%20home.wav.wav)  Δwer=0.500  (fast_default=0.500, realtime=0.000)  speech=[1.38s, 4.46s] fix=none
- ref:           `Set the  POI  as my home`
- fast_default   `That's the POI at my home.`
- fast_llm       `That's the POI at my home.`
- fast_mai       `left the POI at my home.`
- realtime       `Set the POI as my home.`
- realtime_refine `That's the POI at my home.`

### en-GB_DT1/1l_en-GB_female-DT1/Page 4.wav [▶](audio/en-GB_DT1/1l_en-GB_female-DT1/Page%204.wav.wav)  Δwer=0.500  (fast_default=0.500, realtime=0.000)  speech=[1.3s, 2.3s] fix=none
- ref:           `Page 4`
- fast_default   `Page ball.`
- fast_llm       `Page 4.`
- fast_mai       `French 4.`
- realtime       `Page 4.`
- realtime_refine `Page 4.`

### en-GB_JT1/1l_en-GB_female-JT1/Show the AC setting page.wav [▶](audio/en-GB_JT1/1l_en-GB_female-JT1/Show%20the%20AC%20setting%20page.wav.wav)  Δwer=0.400  (fast_default=0.400, realtime=0.000)  speech=[2.23s, 3.88s] fix=none
- ref:           `Show the AC setting page`
- fast_default   `Go to the AC setting page.`
- fast_llm       `The AC setting page.`
- fast_mai       `the AC setting page.`
- realtime       `Show the AC setting page.`
- realtime_refine `Go to the AC setting page.`

### en-GB_DT2/1l_en-GB_male-DT2/move the driver's cushion down a little.wav [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/move%20the%20driver%27s%20cushion%20down%20a%20little.wav.wav)  Δwer=0.375  (fast_default=0.500, realtime=0.125)  speech=[1.39s, 3.47s] fix=none
- ref:           `move the driver's cushion down a little`
- fast_default   `The drivers cushioned down a little.`
- fast_llm       `Move the driver's cushion down a little.`
- fast_mai       `Move the driver's cushion down a little.`
- realtime       `The driver's cushion down a little.`
- realtime_refine `The driver's cushion down a little.`

### en-GB_DT2/1l_en-GB_male-DT2/Disable Apple Carplay.wav [▶](audio/en-GB_DT2/1l_en-GB_male-DT2/Disable%20Apple%20Carplay.wav.wav)  Δwer=0.333  (fast_default=0.667, realtime=0.333)  speech=[1.16s, 2.72s] fix=none
- ref:           `Disable Apple Carplay`
- fast_default   `Sable Apple Campaign.`
- fast_llm       `细胞压迫康病`
- fast_mai       `Save all Apple content.`
- realtime       `Disable Apple Campaign.`
- realtime_refine `Sable Apple Campaign`

## Caveats

- **UPL is anchored on the realtime SDK's word-end timestamp** for each sample, so all services use the same `speech_end`. The CSV's `upl_self_ms` column has each service's own phrase-derived value if you want to see how its boundary detection differs.
- **Mazda voice commands** are short utterances (typically 2-8 words). WER on short references is noisier — a single word error on a 3-word command gives 33% WER.