# Error analysis — mazda_de-DE_20260508_112711.csv

Filters out samples that look like *data* problems rather than recognition errors:
1. **Empty hypothesis** — at least one service returned no text.
2. **Reference much shorter than audio** — `words_per_s < 0.3` (with `duration ≥ 1 s`). At normal speech rates this means the label is missing content.
3. **All services agree, ref disagrees** — mean pairwise WER between hypotheses < 0.15 AND mean WER vs ref > 0.5. Multiple ASR systems converging on the same answer that differs from the reference is a strong signal of a mislabeled ground truth, not a shared error.

Audio links (▶) point to `results/audio/<dataset>/<sample_id>.wav` so a reviewer can play the clip directly.

## Datasets under test

- **de-DE_DT1** — Mazda de-DE DT1 voice commands (male + female pooled)
- **de-DE_DT2** — Mazda de-DE DT2 voice commands (male + female pooled)
- **de-DE_JT1** — Mazda de-DE JT1 voice commands (male + female pooled)

Total complete samples: **90**  
Kept after filtering: **62**  
Excluded as data issues: **28**  

- Empty hypothesis: 27
- Reference too short for audio: 0
- All services agree, ref disagrees: 1

## Speech boundaries

`speech_start_s` / `speech_end_s` come from the realtime SDK's word-level timestamps and anchor UPL for all services. Per-word detail lives in the sidecar `mazda_de-DE_20260508_112711_words.jsonl`.

Boundary-fix actions across 90 realtime samples: `skip`=35, `trim_both`=6, `trim_first`=14, `trim_last`=10

## Filtered results (excludes data issues)

INS/DEL/SUB are *rates per 100 reference words*. Their sum ≈ WER × 100.

| Dataset | Service | N | WER | SER | INS/100 | DEL/100 | SUB/100 | LBL ms (mean / p90) | UPL ms (mean / p90) |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| de-DE_DT1 | fast_default | 21 | 0.434 | 0.619 | 7.1 | 15.3 | 34.1 | 584 / 654 | 1208 / 1234 |
| de-DE_DT1 | fast_llm | 21 | 0.456 | 0.667 | 8.2 | 9.4 | 36.5 | 507 / 544 | 1133 / 1147 |
| de-DE_DT1 | fast_mai | 21 | 0.319 | 0.667 | 1.2 | 9.4 | 21.2 | 473 / 554 | 996 / 1102 |
| de-DE_DT1 | realtime | 21 | 0.406 | 0.714 | 3.5 | 18.8 | 22.4 | -1142 / -585 | 762 / 922 |
| de-DE_DT1 | realtime_refine | 21 | 0.346 | 0.619 | 4.7 | 5.9 | 31.8 | -637 / 118 | 1256 / 1494 |
| de-DE_DT2 | fast_default | 13 | 0.367 | 0.615 | 8.3 | 2.1 | 29.2 | 699 / 667 | 1485 / 2587 |
| de-DE_DT2 | fast_llm | 13 | 0.280 | 0.538 | 4.2 | 4.2 | 22.9 | 500 / 530 | 1276 / 2200 |
| de-DE_DT2 | fast_mai | 13 | 0.294 | 0.615 | 2.1 | 2.1 | 22.9 | 490 / 553 | 917 / 1106 |
| de-DE_DT2 | realtime | 13 | 0.375 | 0.692 | 4.2 | 8.3 | 22.9 | -693 / -359 | 702 / 856 |
| de-DE_DT2 | realtime_refine | 13 | 0.351 | 0.615 | 4.2 | 4.2 | 25.0 | -223 / 38 | 1224 / 1304 |
| de-DE_JT1 | fast_default | 28 | 0.376 | 0.643 | 1.8 | 12.3 | 25.4 | 587 / 643 | 1272 / 2209 |
| de-DE_JT1 | fast_llm | 28 | 0.318 | 0.571 | 1.8 | 12.3 | 20.2 | 498 / 579 | 1182 / 2121 |
| de-DE_JT1 | fast_mai | 28 | 0.279 | 0.536 | 2.6 | 10.5 | 15.8 | 516 / 570 | 1006 / 1100 |
| de-DE_JT1 | realtime | 28 | 0.297 | 0.679 | 4.4 | 10.5 | 16.7 | -1029 / -430 | 664 / 861 |
| de-DE_JT1 | realtime_refine | 28 | 0.316 | 0.536 | 1.8 | 11.4 | 18.4 | -624 / -84 | 1088 / 1192 |

## Unfiltered results (all complete samples, for reference)

| Dataset | Service | N | WER | SER | INS/100 | DEL/100 | SUB/100 |
|---|---|---:|---:|---:|---:|---:|---:|
| de-DE_DT1 | fast_default | 30 | 0.582 | 0.733 | 10.2 | 27.1 | 33.9 |
| de-DE_DT1 | fast_llm | 30 | 0.581 | 0.767 | 16.1 | 12.7 | 44.9 |
| de-DE_DT1 | fast_mai | 30 | 0.510 | 0.767 | 17.8 | 12.7 | 32.2 |
| de-DE_DT1 | realtime | 30 | 0.571 | 0.800 | 2.5 | 37.3 | 18.6 |
| de-DE_DT1 | realtime_refine | 30 | 0.492 | 0.733 | 12.7 | 11.9 | 35.6 |
| de-DE_DT2 | fast_default | 30 | 0.717 | 0.833 | 13.6 | 33.1 | 38.1 |
| de-DE_DT2 | fast_llm | 30 | 0.663 | 0.800 | 19.5 | 20.3 | 46.6 |
| de-DE_DT2 | fast_mai | 30 | 0.636 | 0.833 | 23.7 | 16.9 | 42.4 |
| de-DE_DT2 | realtime | 30 | 0.718 | 0.867 | 1.7 | 61.0 | 9.3 |
| de-DE_DT2 | realtime_refine | 30 | 0.679 | 0.833 | 11.9 | 32.2 | 33.1 |
| de-DE_JT1 | fast_default | 30 | 0.417 | 0.667 | 2.5 | 13.6 | 25.4 |
| de-DE_JT1 | fast_llm | 30 | 0.363 | 0.600 | 2.5 | 13.6 | 20.3 |
| de-DE_JT1 | fast_mai | 30 | 0.327 | 0.567 | 3.4 | 11.9 | 16.1 |
| de-DE_JT1 | realtime | 30 | 0.344 | 0.700 | 5.1 | 11.9 | 16.9 |
| de-DE_JT1 | realtime_refine | 30 | 0.361 | 0.567 | 2.5 | 12.7 | 18.6 |

## Excluded samples — examples

### Empty hypothesis

| Audio | Dataset | Sample | Empty in | Reference |
|---|---|---|---|---|
| [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Fahren%20Sie%20nach%20Birmingham.wav.wav) | de-DE_DT1 | 1l_de-DE_female-DT1/Fahren Sie nach Birmingham.wav | fast_default,fast_mai,realtime,realtime_refine | `Fahren Sie nach Birmingham` |
| [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Navigation%20stummschalten.wav.wav) | de-DE_DT1 | 1l_de-DE_female-DT1/Navigation stummschalten.wav | realtime | `Navigation stummschalten` |
| [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Linke%20R%C3%BCcksitzbel%C3%BCftung%20leicht%20erh%C3%B6hen.wav.wav) | de-DE_DT1 | 1l_de-DE_female-DT1/Linke Rücksitzbelüftung leicht erhöhen.wav | fast_default,realtime | `Linke Rücksitzbelüftung leicht erhöhen` |
| [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Vorderen%20Bereich%20etwas%20erw%C3%A4rmen.wav.wav) | de-DE_DT1 | 1l_de-DE_male-DT1/Vorderen Bereich etwas erwärmen.wav | realtime | `Vorderen Bereich etwas erwärmen` |
| [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Eco-Fahrmodus%20aktivieren.wav.wav) | de-DE_DT1 | 1l_de-DE_female-DT1/Eco-Fahrmodus aktivieren.wav | fast_default,realtime,realtime_refine | `Eco-Fahrmodus aktivieren` |
| [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20deaktivieren.wav.wav) | de-DE_DT1 | 1l_de-DE_female-DT1/Automatische Belüftung beim Entriegeln deaktivieren.wav | fast_default | `Automatische Belüftung beim Entriegeln deaktivieren` |
| [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20aktivieren.wav.wav) | de-DE_DT1 | 1l_de-DE_female-DT1/Automatische Belüftung beim Entriegeln aktivieren.wav | realtime | `Automatische Belüftung beim Entriegeln aktivieren` |
| [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Linke%20R%C3%BCcksitzbel%C3%BCftung%20auf%20Maximum.wav.wav) | de-DE_DT1 | 1l_de-DE_female-DT1/Linke Rücksitzbelüftung auf Maximum.wav | realtime | `Linke Rücksitzbelüftung auf Maximum` |
| [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Klingelton%20stummschalten.wav.wav) | de-DE_DT1 | 1l_de-DE_male-DT1/Klingelton stummschalten.wav | realtime | `Klingelton stummschalten` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Fahren%20Sie%20nach%20Birmingham.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Fahren Sie nach Birmingham.wav | fast_default,fast_mai,realtime | `Fahren Sie nach Birmingham` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Autofenster%20halb%20%C3%B6ffnen.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Autofenster halb öffnen.wav | realtime | `Autofenster halb öffnen` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Navigation%20stummschalten.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Navigation stummschalten.wav | realtime,realtime_refine | `Navigation stummschalten` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/L%C3%BCfter%20um%201%20Stufe%20erh%C3%B6hen.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Lüfter um 1 Stufe erhöhen.wav | fast_default,fast_llm,fast_mai,realtime,realtime_refine | `Lüfter um 1 Stufe erhöhen` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Linke%20R%C3%BCcksitzbel%C3%BCftung%20leicht%20erh%C3%B6hen.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Linke Rücksitzbelüftung leicht erhöhen.wav | fast_default,realtime | `Linke Rücksitzbelüftung leicht erhöhen` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Die%20letzte.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Die letzte.wav | fast_default,fast_mai,realtime,realtime_refine | `Die letzte` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Eco-Fahrmodus%20aktivieren.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Eco-Fahrmodus aktivieren.wav | fast_default,fast_mai,realtime,realtime_refine | `Eco-Fahrmodus aktivieren` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20deaktivieren.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Automatische Belüftung beim Entriegeln deaktivieren.wav | realtime | `Automatische Belüftung beim Entriegeln deaktivieren` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Diesen%20Sender%20aus%20den%20Favoriten%20l%C3%B6schen.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Diesen Sender aus den Favoriten löschen.wav | realtime | `Diesen Sender aus den Favoriten löschen` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Linke%20R%C3%BCcksitzbel%C3%BCftung%20auf%20Maximum.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Linke Rücksitzbelüftung auf Maximum.wav | realtime | `Linke Rücksitzbelüftung auf Maximum` |
| [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Fenster%20%C3%B6ffnen.wav.wav) | de-DE_DT2 | 1l_de-DE_male-DT2/Fenster öffnen.wav | fast_mai,realtime | `Fenster öffnen` |

_(+7 more)_

### Reference too short for audio duration

_(none)_

### All services agree, reference disagrees (likely mislabeled)

#### de-DE_JT1/1l_de-DE_female-JT1/Navigation stummschalten.wav [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Navigation%20stummschalten.wav.wav) — pairwise WER between services = 0.000
- ref:           `Navigation stummschalten`
- fast_default   `Navigation stumm schalten.`
- fast_llm       `Navigation stumm schalten.`
- fast_mai       `Navigation stumm schalten.`
- realtime       `Navigation stumm schalten.`
- realtime_refine `Navigation stumm schalten`

## Genuine recognition errors (filtered set)

Best / median / worst WER per (dataset, service) on the kept samples.

### de-DE_DT1 / fast_default  (n=21)
**BEST** — `1l_de-DE_male-DT1/Vorherigen Titel abspielen.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Vorherigen%20Titel%20abspielen.wav.wav)  wer=0.000  speech=[1.22s, 3.26s]  fix=none
- ref: `Vorherigen Titel abspielen`
- hyp: `vorherigen Titel abspielen`
**MEDIAN** — `1l_de-DE_female-DT1/Fahrtenanzeige öffnen.wav` [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Fahrtenanzeige%20%C3%B6ffnen.wav.wav)  wer=0.500  speech=[1.95s, 2.47s]  fix=trim_both
- ref: `Fahrtenanzeige öffnen`
- hyp: `Datenanzeige öffnen.`
**WORST** — `1l_de-DE_male-DT1/Wechseln Sie in den detaillierten Berichtsmodus.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Wechseln%20Sie%20in%20den%20detaillierten%20Berichtsmodus.wav.wav)  wer=1.500  speech=[1.29s, 5.52s]  fix=none
- ref: `Wechseln Sie in den detaillierten Berichtsmodus`
- hyp: `Next term seat in the induit of Newton believes newer.`

### de-DE_DT1 / fast_llm  (n=21)
**BEST** — `1l_de-DE_male-DT1/Vorherigen Titel abspielen.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Vorherigen%20Titel%20abspielen.wav.wav)  wer=0.000  speech=[1.22s, 3.26s]  fix=none
- ref: `Vorherigen Titel abspielen`
- hyp: `Vorherigen Titel abspielen`
**MEDIAN** — `1l_de-DE_female-DT1/Fahrtenanzeige öffnen.wav` [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Fahrtenanzeige%20%C3%B6ffnen.wav.wav)  wer=0.500  speech=[1.95s, 2.47s]  fix=trim_both
- ref: `Fahrtenanzeige öffnen`
- hyp: `Datenanzeige öffnen.`
**WORST** — `1l_de-DE_male-DT1/Medienlautstärke verringern.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Medienlautst%C3%A4rke%20verringern.wav.wav)  wer=2.000  speech=[2.95s, 3.55s]  fix=trim_first
- ref: `Medienlautstärke verringern`
- hyp: `Medium loudspeaker and subwoofer.`

### de-DE_DT1 / fast_mai  (n=21)
**BEST** — `1l_de-DE_female-DT1/Autofenster halb öffnen.wav` [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Autofenster%20halb%20%C3%B6ffnen.wav.wav)  wer=0.000  speech=[1.78s, 2.9s]  fix=trim_last
- ref: `Autofenster halb öffnen`
- hyp: `Autofenster halb öffnen.`
**MEDIAN** — `1l_de-DE_male-DT1/Scheinwerferhöhe auf mittel stellen.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Scheinwerferh%C3%B6he%20auf%20mittel%20stellen.wav.wav)  wer=0.250  speech=[2.54s, 2.86s]  fix=trim_both
- ref: `Scheinwerferhöhe auf mittel stellen`
- hyp: `Scheinwerferhöhe auf Mittel.`
**WORST** — `1l_de-DE_male-DT1/Außenluftzirkulation einschalten.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Au%C3%9Fenluftzirkulation%20einschalten.wav.wav)  wer=1.000  speech=[3.36s, 3.96s]  fix=trim_first
- ref: `Außenluftzirkulation einschalten`
- hyp: `Außenluft-Zirkulation einschalten.`

### de-DE_DT1 / realtime  (n=21)
**BEST** — `1l_de-DE_male-DT1/Vorherigen Titel abspielen.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Vorherigen%20Titel%20abspielen.wav.wav)  wer=0.000  speech=[1.22s, 3.26s]  fix=none
- ref: `Vorherigen Titel abspielen`
- hyp: `Vorherigen Titel abspielen.`
**MEDIAN** — `1l_de-DE_female-DT1/Lüfter um 1 Stufe erhöhen.wav` [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/L%C3%BCfter%20um%201%20Stufe%20erh%C3%B6hen.wav.wav)  wer=0.400  speech=[3.01s, 4.05s]  fix=trim_last
- ref: `Lüfter um 1 Stufe erhöhen`
- hyp: `Um eine Stufe erhöhen.`
**WORST** — `1l_de-DE_female-DT1/Diesen Sender aus den Favoriten löschen.wav` [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Diesen%20Sender%20aus%20den%20Favoriten%20l%C3%B6schen.wav.wav)  wer=1.000  speech=[3.6s, 4.32s]  fix=trim_first
- ref: `Diesen Sender aus den Favoriten löschen`
- hyp: `Favoritenliste hinzufügen.`

### de-DE_DT1 / realtime_refine  (n=21)
**BEST** — `1l_de-DE_male-DT1/Vorherigen Titel abspielen.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Vorherigen%20Titel%20abspielen.wav.wav)  wer=0.000  speech=[1.22s, 3.26s]  fix=none
- ref: `Vorherigen Titel abspielen`
- hyp: `Vorherigen Titel abspielen.`
**MEDIAN** — `1l_de-DE_female-DT1/Fahrtenanzeige öffnen.wav` [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Fahrtenanzeige%20%C3%B6ffnen.wav.wav)  wer=0.500  speech=[1.95s, 2.47s]  fix=trim_both
- ref: `Fahrtenanzeige öffnen`
- hyp: `Datenanzeige öffnen.`
**WORST** — `1l_de-DE_male-DT1/Automatische Belüftung beim Entriegeln deaktivieren.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20deaktivieren.wav.wav)  wer=1.400  speech=[1.48s, 2.92s]  fix=trim_last
- ref: `Automatische Belüftung beim Entriegeln deaktivieren`
- hyp: `Altamonte served neutral by Centenegio, the electron.`

### de-DE_DT2 / fast_default  (n=13)
**BEST** — `1l_de-DE_male-DT2/Vorherigen Titel abspielen.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Vorherigen%20Titel%20abspielen.wav.wav)  wer=0.000  speech=[1.27s, 3.23s]  fix=none
- ref: `Vorherigen Titel abspielen`
- hyp: `Vorherigen Titel abspielen.`
**MEDIAN** — `1l_de-DE_male-DT2/Sitzheizung leicht senken.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Sitzheizung%20leicht%20senken.wav.wav)  wer=0.333  speech=[1.5s, 3.9s]  fix=none
- ref: `Sitzheizung leicht senken`
- hyp: `Sitzheizung gleich senken.`
**WORST** — `1l_de-DE_female-DT2/Automatische Belüftung beim Entriegeln aktivieren.wav` [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20aktivieren.wav.wav)  wer=1.400  speech=[-s, -s]  fix=skip
- ref: `Automatische Belüftung beim Entriegeln aktivieren`
- hyp: `A partition delivery plan can even activate.`

### de-DE_DT2 / fast_llm  (n=13)
**BEST** — `1l_de-DE_male-DT2/Vorherigen Titel abspielen.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Vorherigen%20Titel%20abspielen.wav.wav)  wer=0.000  speech=[1.27s, 3.23s]  fix=none
- ref: `Vorherigen Titel abspielen`
- hyp: `Vorherigen Titel abspielen.`
**MEDIAN** — `1l_de-DE_male-DT2/Öffne das Fenster in der ersten Reihe.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/%C3%96ffne%20das%20Fenster%20in%20der%20ersten%20Reihe.wav.wav)  wer=0.143  speech=[1.82s, 3.42s]  fix=trim_both
- ref: `Öffne das Fenster in der ersten Reihe`
- hyp: `Öffne das Fenster in der ersten Wahl.`
**WORST** — `1l_de-DE_female-DT2/Automatische Belüftung beim Entriegeln aktivieren.wav` [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20aktivieren.wav.wav)  wer=1.200  speech=[-s, -s]  fix=skip
- ref: `Automatische Belüftung beim Entriegeln aktivieren`
- hyp: `Automatische Verhütung bei einem Pilz und Antiviren.`

### de-DE_DT2 / fast_mai  (n=13)
**BEST** — `1l_de-DE_male-DT2/Vorderen Bereich etwas erwärmen.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Vorderen%20Bereich%20etwas%20erw%C3%A4rmen.wav.wav)  wer=0.000  speech=[1.35s, 3.67s]  fix=none
- ref: `Vorderen Bereich etwas erwärmen`
- hyp: `vorderen Bereich etwas erwärmen.`
**MEDIAN** — `1l_de-DE_male-DT2/Öffne das Fenster in der ersten Reihe.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/%C3%96ffne%20das%20Fenster%20in%20der%20ersten%20Reihe.wav.wav)  wer=0.286  speech=[1.82s, 3.42s]  fix=trim_both
- ref: `Öffne das Fenster in der ersten Reihe`
- hyp: `Öffne das Fenster in den ersten Ball.`
**WORST** — `1l_de-DE_male-DT2/Klingelton stummschalten.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Klingelton%20stummschalten.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Klingelton stummschalten`
- hyp: `Klingelton stumm schalten.`

### de-DE_DT2 / realtime  (n=13)
**BEST** — `1l_de-DE_male-DT2/Vorherigen Titel abspielen.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Vorherigen%20Titel%20abspielen.wav.wav)  wer=0.000  speech=[1.27s, 3.23s]  fix=none
- ref: `Vorherigen Titel abspielen`
- hyp: `Vorherigen Titel abspielen.`
**MEDIAN** — `1l_de-DE_male-DT2/Öffne das Fenster in der ersten Reihe.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/%C3%96ffne%20das%20Fenster%20in%20der%20ersten%20Reihe.wav.wav)  wer=0.429  speech=[1.82s, 3.42s]  fix=trim_both
- ref: `Öffne das Fenster in der ersten Reihe`
- hyp: `Öffne das Fenster und den ersten Ball.`
**WORST** — `1l_de-DE_male-DT2/Klingelton stummschalten.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Klingelton%20stummschalten.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Klingelton stummschalten`
- hyp: `Klingelton stumm schalten.`

### de-DE_DT2 / realtime_refine  (n=13)
**BEST** — `1l_de-DE_male-DT2/Vorherigen Titel abspielen.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Vorherigen%20Titel%20abspielen.wav.wav)  wer=0.000  speech=[1.27s, 3.23s]  fix=none
- ref: `Vorherigen Titel abspielen`
- hyp: `Vorherigen Titel abspielen.`
**MEDIAN** — `1l_de-DE_male-DT2/Sitzheizung leicht senken.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Sitzheizung%20leicht%20senken.wav.wav)  wer=0.333  speech=[1.5s, 3.9s]  fix=none
- ref: `Sitzheizung leicht senken`
- hyp: `Sitzheizung gleich senken.`
**WORST** — `1l_de-DE_male-DT2/Klingelton stummschalten.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Klingelton%20stummschalten.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Klingelton stummschalten`
- hyp: `Klingelton stumm schalten.`

### de-DE_JT1 / fast_default  (n=28)
**BEST** — `1l_de-DE_male-JT1/Scheinwerfer auf dritte Stufe einstellen.wav` [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Scheinwerfer%20auf%20dritte%20Stufe%20einstellen.wav.wav)  wer=0.000  speech=[1.59s, 4.67s]  fix=none
- ref: `Scheinwerfer auf dritte Stufe einstellen`
- hyp: `Scheinwerfer auf dritte Stufe einstellen`
**MEDIAN** — `1l_de-DE_female-JT1/Automatische Belüftung beim Entriegeln deaktivieren.wav` [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20deaktivieren.wav.wav)  wer=0.400  speech=[2.36s, 5.36s]  fix=none
- ref: `Automatische Belüftung beim Entriegeln deaktivieren`
- hyp: `Automatische Belüftung bei Endriegeln deaktivieren.`
**WORST** — `1l_de-DE_male-JT1/Klingelton stummschalten.wav` [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Klingelton%20stummschalten.wav.wav)  wer=1.000  speech=[1.37s, 3.29s]  fix=none
- ref: `Klingelton stummschalten`
- hyp: `Klingelton stumm schalten`

### de-DE_JT1 / fast_llm  (n=28)
**BEST** — `1l_de-DE_male-JT1/Scheinwerfer auf dritte Stufe einstellen.wav` [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Scheinwerfer%20auf%20dritte%20Stufe%20einstellen.wav.wav)  wer=0.000  speech=[1.59s, 4.67s]  fix=none
- ref: `Scheinwerfer auf dritte Stufe einstellen`
- hyp: `Scheinwerfer auf dritte Stufe einstellen`
**MEDIAN** — `1l_de-DE_female-JT1/Lüfter um 1 Stufe erhöhen.wav` [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/L%C3%BCfter%20um%201%20Stufe%20erh%C3%B6hen.wav.wav)  wer=0.400  speech=[3.09s, 4.05s]  fix=trim_both
- ref: `Lüfter um 1 Stufe erhöhen`
- hyp: `Möchte um eine Stufe erhöhen.`
**WORST** — `1l_de-DE_female-JT1/Fahren Sie nach Birmingham.wav` [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Fahren%20Sie%20nach%20Birmingham.wav.wav)  wer=1.250  speech=[3.2s, 4.52s]  fix=none
- ref: `Fahren Sie nach Birmingham`
- hyp: `Find the app for him.`

### de-DE_JT1 / fast_mai  (n=28)
**BEST** — `1l_de-DE_male-JT1/Scheinwerfer auf dritte Stufe einstellen.wav` [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Scheinwerfer%20auf%20dritte%20Stufe%20einstellen.wav.wav)  wer=0.000  speech=[1.59s, 4.67s]  fix=none
- ref: `Scheinwerfer auf dritte Stufe einstellen`
- hyp: `Scheinwerfer auf dritte Stufe einstellen.`
**MEDIAN** — `1l_de-DE_female-JT1/Automatische Belüftung beim Entriegeln deaktivieren.wav` [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20deaktivieren.wav.wav)  wer=0.200  speech=[2.36s, 5.36s]  fix=none
- ref: `Automatische Belüftung beim Entriegeln deaktivieren`
- hyp: `Automatische Belüftung bei Entriegeln deaktivieren`
**WORST** — `1l_de-DE_male-JT1/Klingelton stummschalten.wav` [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Klingelton%20stummschalten.wav.wav)  wer=1.000  speech=[1.37s, 3.29s]  fix=none
- ref: `Klingelton stummschalten`
- hyp: `Klingelton stumm schalten.`

### de-DE_JT1 / realtime  (n=28)
**BEST** — `1l_de-DE_male-JT1/Scheinwerfer auf dritte Stufe einstellen.wav` [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Scheinwerfer%20auf%20dritte%20Stufe%20einstellen.wav.wav)  wer=0.000  speech=[1.59s, 4.67s]  fix=none
- ref: `Scheinwerfer auf dritte Stufe einstellen`
- hyp: `Scheinwerfer auf dritte Stufe einstellen.`
**MEDIAN** — `1l_de-DE_female-JT1/Autofenster halb öffnen.wav` [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Autofenster%20halb%20%C3%B6ffnen.wav.wav)  wer=0.333  speech=[1.86s, 2.9s]  fix=trim_last
- ref: `Autofenster halb öffnen`
- hyp: `Autofenster Hype öffnen.`
**WORST** — `1l_de-DE_female-JT1/Diesen Sender aus den Favoriten löschen.wav` [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Diesen%20Sender%20aus%20den%20Favoriten%20l%C3%B6schen.wav.wav)  wer=1.000  speech=[3.6s, 4.16s]  fix=trim_first
- ref: `Diesen Sender aus den Favoriten löschen`
- hyp: `Favoritenliste hinzufügen.`

### de-DE_JT1 / realtime_refine  (n=28)
**BEST** — `1l_de-DE_male-JT1/Scheinwerfer auf dritte Stufe einstellen.wav` [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Scheinwerfer%20auf%20dritte%20Stufe%20einstellen.wav.wav)  wer=0.000  speech=[1.59s, 4.67s]  fix=none
- ref: `Scheinwerfer auf dritte Stufe einstellen`
- hyp: `Scheinwerfer auf dritte Stufe einstellen`
**MEDIAN** — `1l_de-DE_female-JT1/Kannst du die Lautstärke auf das Minimum einstellen.wav` [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Kannst%20du%20die%20Lautst%C3%A4rke%20auf%20das%20Minimum%20einstellen.wav.wav)  wer=0.375  speech=[-s, -s]  fix=skip
- ref: `Kannst du die Lautstärke auf das Minimum einstellen`
- hyp: `Lautstärke auf das Minimum einstellen`
**WORST** — `1l_de-DE_male-JT1/Klingelton stummschalten.wav` [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Klingelton%20stummschalten.wav.wav)  wer=1.000  speech=[1.37s, 3.29s]  fix=none
- ref: `Klingelton stummschalten`
- hyp: `Klingelton stumm schalten`

## Top fast_default vs realtime disagreements (filtered)

### de-DE_JT1/1l_de-DE_male-JT1/Klingelton stummschalten.wav [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Klingelton%20stummschalten.wav.wav)  Δwer=1.000  (fast_default=1.000, realtime=0.000)  speech=[1.37s, 3.29s] fix=none
- ref:           `Klingelton stummschalten`
- fast_default   `Klingelton stumm schalten`
- fast_llm       `Klingelton stummschalte.`
- fast_mai       `Klingelton stumm schalten.`
- realtime       `Klingelton stummschalten.`
- realtime_refine `Klingelton stumm schalten`

### de-DE_DT1/1l_de-DE_male-DT1/Wechseln Sie in den detaillierten Berichtsmodus.wav [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Wechseln%20Sie%20in%20den%20detaillierten%20Berichtsmodus.wav.wav)  Δwer=0.667  (fast_default=1.000, realtime=0.333)  speech=[1.29s, 5.52s] fix=none
- ref:           `Wechseln Sie in den detaillierten Berichtsmodus`
- fast_default   `Next term seat in the induit of Newton believes newer.`
- fast_llm       `Nächsten Sieg in den Blick von Jutland-Berichtsnummer.`
- fast_mai       `Wechseln Sie in den detaillierten Berichtsschnur.`
- realtime       `Wechseln Sie in den Weg zu.`
- realtime_refine `Wechseln Sie in den detaillierten Berichtsmüll.`

### de-DE_DT2/1l_de-DE_female-DT2/Automatische Belüftung beim Entriegeln aktivieren.wav [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20aktivieren.wav.wav)  Δwer=0.600  (fast_default=1.000, realtime=0.400)  speech=[-s, -s] fix=skip
- ref:           `Automatische Belüftung beim Entriegeln aktivieren`
- fast_default   `A partition delivery plan can even activate.`
- fast_llm       `Automatische Verhütung bei einem Pilz und Antiviren.`
- fast_mai       `Automatische Belüftung bei Empfohlen aktivieren`
- realtime       `Automatische Belüftung aktivieren.`
- realtime_refine `Automatische Belüftung sollen Medien aktivieren.`

### de-DE_DT1/1l_de-DE_female-DT1/Lüfter um 1 Stufe erhöhen.wav [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/L%C3%BCfter%20um%201%20Stufe%20erh%C3%B6hen.wav.wav)  Δwer=0.600  (fast_default=1.000, realtime=0.400)  speech=[3.01s, 4.05s] fix=trim_last
- ref:           `Lüfter um 1 Stufe erhöhen`
- fast_default   `I'm any stupor at lane.`
- fast_llm       `Um eine Stufe erhöhen.`
- fast_mai       `um eine Stufe erhöhen.`
- realtime       `Um eine Stufe erhöhen.`
- realtime_refine `Auf eine Stufe erhöhen.`

### de-DE_JT1/1l_de-DE_male-JT1/Kartenansicht auf 2D einstellen.wav [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Kartenansicht%20auf%202D%20einstellen.wav.wav)  Δwer=0.500  (fast_default=0.000, realtime=0.500)  speech=[1.18s, 4.54s] fix=none
- ref:           `Kartenansicht auf 2D einstellen`
- fast_default   `Kartenansicht auf 2D einstellen`
- fast_llm       `Kartenansicht auf 2 d einstellen.`
- fast_mai       `Kartenansicht auf 2D einstellen.`
- realtime       `Kartenansicht auf 2 D einstellen.`
- realtime_refine `Kartenansicht auf 2D einstellen`

### de-DE_JT1/1l_de-DE_male-JT1/Fenster öffnen.wav [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Fenster%20%C3%B6ffnen.wav.wav)  Δwer=0.500  (fast_default=0.000, realtime=0.500)  speech=[1.25s, 2.16s] fix=trim_last
- ref:           `Fenster öffnen`
- fast_default   `Fenster öffnen.`
- fast_llm       `Fenster öffnen.`
- fast_mai       `Fenster öffnen.`
- realtime       `Fenster öffnen.An.`
- realtime_refine `Fenster öffnen`

### de-DE_JT1/1l_de-DE_male-JT1/Außenluftzirkulation einschalten.wav [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Au%C3%9Fenluftzirkulation%20einschalten.wav.wav)  Δwer=0.500  (fast_default=0.500, realtime=0.000)  speech=[3.4s, 4.04s] fix=trim_first
- ref:           `Außenluftzirkulation einschalten`
- fast_default   `Aussenluftzirkulation einschalten`
- fast_llm       `Außenluftzirkulation einschalten`
- fast_mai       `Außenluftzirkulation einschalten.`
- realtime       `Außenluftzirkulation einschalten.`
- realtime_refine `Aussenluftzirkulation einschalten`

### de-DE_JT1/1l_de-DE_female-JT1/Fahren Sie nach Birmingham.wav [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Fahren%20Sie%20nach%20Birmingham.wav.wav)  Δwer=0.500  (fast_default=1.000, realtime=0.500)  speech=[3.2s, 4.52s] fix=none
- ref:           `Fahren Sie nach Birmingham`
- fast_default   `Find the afternoon.`
- fast_llm       `Find the app for him.`
- fast_mai       `Fahren Sie nach Bückelheim.`
- realtime       `Fahren wir nach Mühlheim.`
- realtime_refine `Find the upgraham.`

### de-DE_DT2/1l_de-DE_male-DT2/Außenluftzirkulation einschalten.wav [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Au%C3%9Fenluftzirkulation%20einschalten.wav.wav)  Δwer=0.500  (fast_default=0.000, realtime=0.500)  speech=[3.35s, 4.07s] fix=trim_first
- ref:           `Außenluftzirkulation einschalten`
- fast_default   `Außenluftzirkulation einschalten.`
- fast_llm       `Außenluftzirkulation einschalten.`
- fast_mai       `Außenluftzirkulation einschalten.`
- realtime       `Außenluftzirkulation einschaltet.`
- realtime_refine `Außenluftzirkulation einschalten.`

### de-DE_DT1/1l_de-DE_female-DT1/Fahrtenanzeige öffnen.wav [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Fahrtenanzeige%20%C3%B6ffnen.wav.wav)  Δwer=0.500  (fast_default=0.500, realtime=1.000)  speech=[1.95s, 2.47s] fix=trim_both
- ref:           `Fahrtenanzeige öffnen`
- fast_default   `Datenanzeige öffnen.`
- fast_llm       `Datenanzeige öffnen.`
- fast_mai       `Datenanzeige öffnen.`
- realtime       `Daten Anzeige öffnen.`
- realtime_refine `Datenanzeige öffnen.`

## Caveats

- **UPL is anchored on the realtime SDK's word-end timestamp** for each sample, so all services use the same `speech_end`. The CSV's `upl_self_ms` column has each service's own phrase-derived value if you want to see how its boundary detection differs.
- **Mazda voice commands** are short utterances (typically 2-8 words). WER on short references is noisier — a single word error on a 3-word command gives 33% WER.
- The 'all-agree-vs-ref' filter is conservative (pairwise WER < 0.15 AND mean ref WER > 0.5). True mislabels with partial agreement still survive and inflate per-service WER equally.