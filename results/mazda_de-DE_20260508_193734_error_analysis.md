# Error analysis — mazda_de-DE_20260508_193734.csv

Audio links (▶) point to `results/audio/<dataset>/<sample_id>.wav` so a reviewer can play the clip directly.

## Datasets under test

- **de-DE_DT1** — Mazda de-DE DT1 voice commands (male + female pooled)
- **de-DE_DT2** — Mazda de-DE DT2 voice commands (male + female pooled)
- **de-DE_JT1** — Mazda de-DE JT1 voice commands (male + female pooled)

Total samples: **90**  

## Speech boundaries

`speech_start_s` / `speech_end_s` come from the realtime SDK's word-level timestamps and anchor UPL for all services. Per-word detail lives in the sidecar `mazda_de-DE_20260508_193734_words.jsonl`.

Boundary-fix actions across 90 realtime samples: `skip`=33, `trim_first`=6, `trim_last`=4

## Results

INS/DEL/SUB are *rates per 100 reference words*. Their sum ≈ WER × 100.

| Dataset | Service | N | WER | SER | INS/100 | DEL/100 | SUB/100 | LBL ms (mean / p90) | UPL ms (mean / p90) |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| de-DE_DT1 | fast_default | 30 | 0.575 | 0.733 | 9.3 | 26.3 | 33.9 | 717 / 1146 | 1659 / 2986 |
| de-DE_DT1 | fast_llm | 30 | 0.549 | 0.700 | 15.3 | 10.2 | 45.8 | 563 / 595 | 1586 / 2784 |
| de-DE_DT1 | fast_mai | 30 | 0.475 | 0.700 | 16.9 | 10.2 | 33.9 | 502 / 590 | 865 / 1147 |
| de-DE_DT1 | realtime | 30 | 0.571 | 0.800 | 2.5 | 37.3 | 18.6 | -1133 / -580 | 771 / 958 |
| de-DE_DT1 | realtime_refine | 30 | 0.492 | 0.733 | 12.7 | 11.9 | 35.6 | -492 / 58 | 1368 / 1745 |
| de-DE_DT2 | fast_default | 30 | 0.684 | 0.800 | 13.6 | 33.1 | 37.3 | 671 / 821 | 1894 / 3062 |
| de-DE_DT2 | fast_llm | 30 | 0.663 | 0.800 | 21.2 | 20.3 | 45.8 | 492 / 564 | 2162 / 4145 |
| de-DE_DT2 | fast_mai | 30 | 0.602 | 0.800 | 22.9 | 16.9 | 41.5 | 543 / 643 | 769 / 1181 |
| de-DE_DT2 | realtime | 30 | 0.685 | 0.833 | 0.8 | 61.0 | 8.5 | -779 / -371 | 835 / 970 |
| de-DE_DT2 | realtime_refine | 30 | 0.646 | 0.800 | 11.0 | 32.2 | 32.2 | -414 / 474 | 1342 / 2035 |
| de-DE_JT1 | fast_default | 30 | 0.351 | 0.600 | 0.8 | 12.7 | 24.6 | 636 / 800 | 1263 / 1461 |
| de-DE_JT1 | fast_llm | 30 | 0.320 | 0.533 | 1.7 | 13.6 | 18.6 | 484 / 539 | 1114 / 1106 |
| de-DE_JT1 | fast_mai | 30 | 0.252 | 0.500 | 1.7 | 11.0 | 13.6 | 497 / 575 | 991 / 1141 |
| de-DE_JT1 | realtime | 30 | 0.294 | 0.633 | 3.4 | 11.9 | 15.3 | -1022 / -419 | 671 / 877 |
| de-DE_JT1 | realtime_refine | 30 | 0.295 | 0.500 | 0.8 | 12.7 | 16.9 | -560 / 65 | 1151 / 1228 |

## Best / median / worst WER per (dataset, service)

### de-DE_DT1 / fast_default  (n=30)
**BEST** — `1l_de-DE_male-DT1/Vorherigen Titel abspielen.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Vorherigen%20Titel%20abspielen.wav.wav)  wer=0.000  speech=[1.22s, 3.26s]  fix=none
- ref: `Vorherigen Titel abspielen`
- hyp: `vorherigen Titel abspielen`
**MEDIAN** — `1l_de-DE_female-DT1/Linkes Hinterfenster auf 60 % öffnen.wav` [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Linkes%20Hinterfenster%20auf%2060%20%25%20%C3%B6ffnen.wav.wav)  wer=0.600  speech=[3.71s, 5.91s]  fix=none
- ref: `Linkes Hinterfenster auf 60 % öffnen`
- hyp: `auf 16% öffnen.`
**WORST** — `1l_de-DE_male-DT1/Klingelton stummschalten.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Klingelton%20stummschalten.wav.wav)  wer=2.500  speech=[-s, -s]  fix=skip
- ref: `Klingelton stummschalten`
- hyp: `Meaning for all its constant.`

### de-DE_DT1 / fast_llm  (n=30)
**BEST** — `1l_de-DE_male-DT1/Vorherigen Titel abspielen.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Vorherigen%20Titel%20abspielen.wav.wav)  wer=0.000  speech=[1.22s, 3.26s]  fix=none
- ref: `Vorherigen Titel abspielen`
- hyp: `Vorherigen Titel abspielen`
**MEDIAN** — `1l_de-DE_female-DT1/Automatische Belüftung beim Entriegeln aktivieren.wav` [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20aktivieren.wav.wav)  wer=0.600  speech=[-s, -s]  fix=skip
- ref: `Automatische Belüftung beim Entriegeln aktivieren`
- hyp: `Automatische Umlüftung bei Entgegen aktivieren.`
**WORST** — `1l_de-DE_male-DT1/Klingelton stummschalten.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Klingelton%20stummschalten.wav.wav)  wer=2.500  speech=[-s, -s]  fix=skip
- ref: `Klingelton stummschalten`
- hyp: `Ring it for all expenses.`

### de-DE_DT1 / fast_mai  (n=30)
**BEST** — `1l_de-DE_female-DT1/Autofenster halb öffnen.wav` [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Autofenster%20halb%20%C3%B6ffnen.wav.wav)  wer=0.000  speech=[1.78s, 3.46s]  fix=none
- ref: `Autofenster halb öffnen`
- hyp: `Autofenster halb öffnen.`
**MEDIAN** — `1l_de-DE_female-DT1/Fahrtenanzeige öffnen.wav` [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Fahrtenanzeige%20%C3%B6ffnen.wav.wav)  wer=0.500  speech=[1.95s, 3.07s]  fix=trim_first
- ref: `Fahrtenanzeige öffnen`
- hyp: `Datenanzeige öffnen.`
**WORST** — `1l_de-DE_male-DT1/Klingelton stummschalten.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Klingelton%20stummschalten.wav.wav)  wer=3.000  speech=[-s, -s]  fix=skip
- ref: `Klingelton stummschalten`
- hyp: `Länge vor uns können es sein.`

### de-DE_DT1 / realtime  (n=30)
**BEST** — `1l_de-DE_male-DT1/Vorherigen Titel abspielen.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Vorherigen%20Titel%20abspielen.wav.wav)  wer=0.000  speech=[1.22s, 3.26s]  fix=none
- ref: `Vorherigen Titel abspielen`
- hyp: `Vorherigen Titel abspielen.`
**MEDIAN** — `1l_de-DE_female-DT1/Automatische Belüftung beim Entriegeln deaktivieren.wav` [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20deaktivieren.wav.wav)  wer=0.600  speech=[-s, -s]  fix=skip
- ref: `Automatische Belüftung beim Entriegeln deaktivieren`
- hyp: `Automatische Belastung bei den Deaktivieren.`
**WORST** — `1l_de-DE_male-DT1/Klingelton stummschalten.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Klingelton%20stummschalten.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Klingelton stummschalten`
- hyp: ``

### de-DE_DT1 / realtime_refine  (n=30)
**BEST** — `1l_de-DE_male-DT1/Vorherigen Titel abspielen.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Vorherigen%20Titel%20abspielen.wav.wav)  wer=0.000  speech=[1.22s, 3.26s]  fix=none
- ref: `Vorherigen Titel abspielen`
- hyp: `Vorherigen Titel abspielen.`
**MEDIAN** — `1l_de-DE_male-DT1/Scheinwerferhöhe auf mittel stellen.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Scheinwerferh%C3%B6he%20auf%20mittel%20stellen.wav.wav)  wer=0.500  speech=[1.22s, 3.82s]  fix=none
- ref: `Scheinwerferhöhe auf mittel stellen`
- hyp: `Scheinwerferhöhe auf Mittelstand`
**WORST** — `1l_de-DE_male-DT1/Klingelton stummschalten.wav` [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Klingelton%20stummschalten.wav.wav)  wer=3.000  speech=[-s, -s]  fix=skip
- ref: `Klingelton stummschalten`
- hyp: `being it for all its constant.`

### de-DE_DT2 / fast_default  (n=30)
**BEST** — `1l_de-DE_male-DT2/Vorherigen Titel abspielen.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Vorherigen%20Titel%20abspielen.wav.wav)  wer=0.000  speech=[1.27s, 3.23s]  fix=none
- ref: `Vorherigen Titel abspielen`
- hyp: `Vorherigen Titel abspielen.`
**MEDIAN** — `1l_de-DE_female-DT2/Lüfter um 1 Stufe erhöhen.wav` [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/L%C3%BCfter%20um%201%20Stufe%20erh%C3%B6hen.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Lüfter um 1 Stufe erhöhen`
- hyp: ``
**WORST** — `1l_de-DE_female-DT2/Navigation stummschalten.wav` [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Navigation%20stummschalten.wav.wav)  wer=3.000  speech=[-s, -s]  fix=skip
- ref: `Navigation stummschalten`
- hyp: `Now that's certain by me.`

### de-DE_DT2 / fast_llm  (n=30)
**BEST** — `1l_de-DE_male-DT2/Vorherigen Titel abspielen.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Vorherigen%20Titel%20abspielen.wav.wav)  wer=0.000  speech=[1.27s, 3.23s]  fix=none
- ref: `Vorherigen Titel abspielen`
- hyp: `Vorherigen Titel abspielen.`
**MEDIAN** — `1l_de-DE_female-DT2/Fahren Sie nach Birmingham.wav` [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Fahren%20Sie%20nach%20Birmingham.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Fahren Sie nach Birmingham`
- hyp: `I think.`
**WORST** — `1l_de-DE_female-DT2/Linke Rücksitzbelüftung leicht erhöhen.wav` [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Linke%20R%C3%BCcksitzbel%C3%BCftung%20leicht%20erh%C3%B6hen.wav.wav)  wer=3.500  speech=[-s, -s]  fix=skip
- ref: `Linke Rücksitzbelüftung leicht erhöhen`
- hyp: `The last appearance of the character was in the 2000 issue of the series.`

### de-DE_DT2 / fast_mai  (n=30)
**BEST** — `1l_de-DE_male-DT2/Vorderen Bereich etwas erwärmen.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Vorderen%20Bereich%20etwas%20erw%C3%A4rmen.wav.wav)  wer=0.000  speech=[1.35s, 3.67s]  fix=none
- ref: `Vorderen Bereich etwas erwärmen`
- hyp: `vorderen Bereich etwas erwärmen.`
**MEDIAN** — `1l_de-DE_male-DT2/Scheinwerfer auf dritte Stufe einstellen.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Scheinwerfer%20auf%20dritte%20Stufe%20einstellen.wav.wav)  wer=0.600  speech=[-s, -s]  fix=skip
- ref: `Scheinwerfer auf dritte Stufe einstellen`
- hyp: `Steinwerfer auf Mittelstufe einstellen.`
**WORST** — `1l_de-DE_female-DT2/Navigation stummschalten.wav` [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Navigation%20stummschalten.wav.wav)  wer=3.500  speech=[-s, -s]  fix=skip
- ref: `Navigation stummschalten`
- hyp: `Ich glaube, das sollten wir bei uns`

### de-DE_DT2 / realtime  (n=30)
**BEST** — `1l_de-DE_male-DT2/Vorherigen Titel abspielen.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Vorherigen%20Titel%20abspielen.wav.wav)  wer=0.000  speech=[1.27s, 3.23s]  fix=none
- ref: `Vorherigen Titel abspielen`
- hyp: `Vorherigen Titel abspielen.`
**MEDIAN** — `1l_de-DE_female-DT2/Autofenster halb öffnen.wav` [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Autofenster%20halb%20%C3%B6ffnen.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Autofenster halb öffnen`
- hyp: ``
**WORST** — `1l_de-DE_female-DT2/Linke Rücksitzbelüftung auf Minimum.wav` [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Linke%20R%C3%BCcksitzbel%C3%BCftung%20auf%20Minimum.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Linke Rücksitzbelüftung auf Minimum`
- hyp: ``

### de-DE_DT2 / realtime_refine  (n=30)
**BEST** — `1l_de-DE_male-DT2/Vorherigen Titel abspielen.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Vorherigen%20Titel%20abspielen.wav.wav)  wer=0.000  speech=[1.27s, 3.23s]  fix=none
- ref: `Vorherigen Titel abspielen`
- hyp: `Vorherigen Titel abspielen.`
**MEDIAN** — `1l_de-DE_female-DT2/Linkes Hinterfenster auf 60 % öffnen.wav` [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Linkes%20Hinterfenster%20auf%2060%20%25%20%C3%B6ffnen.wav.wav)  wer=0.800  speech=[-s, -s]  fix=skip
- ref: `Linkes Hinterfenster auf 60 % öffnen`
- hyp: `Auf 60 Prozent signieren.`
**WORST** — `1l_de-DE_male-DT2/Autofenster halb öffnen.wav` [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Autofenster%20halb%20%C3%B6ffnen.wav.wav)  wer=2.000  speech=[-s, -s]  fix=skip
- ref: `Autofenster halb öffnen`
- hyp: `How could pet start IPS?Okay.`

### de-DE_JT1 / fast_default  (n=30)
**BEST** — `1l_de-DE_male-JT1/Scheinwerfer auf dritte Stufe einstellen.wav` [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Scheinwerfer%20auf%20dritte%20Stufe%20einstellen.wav.wav)  wer=0.000  speech=[1.59s, 4.67s]  fix=none
- ref: `Scheinwerfer auf dritte Stufe einstellen`
- hyp: `Scheinwerfer auf dritte Stufe einstellen`
**MEDIAN** — `1l_de-DE_female-JT1/Lüfter um 1 Stufe erhöhen.wav` [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/L%C3%BCfter%20um%201%20Stufe%20erh%C3%B6hen.wav.wav)  wer=0.400  speech=[2.73s, 4.69s]  fix=none
- ref: `Lüfter um 1 Stufe erhöhen`
- hyp: `Luft um eine Stufe erhöhen.`
**WORST** — `1l_de-DE_female-JT1/Diesen Sender aus den Favoriten löschen.wav` [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Diesen%20Sender%20aus%20den%20Favoriten%20l%C3%B6schen.wav.wav)  wer=1.000  speech=[3.6s, 4.16s]  fix=trim_first
- ref: `Diesen Sender aus den Favoriten löschen`
- hyp: `Favoritenliste hinzufügen.`

### de-DE_JT1 / fast_llm  (n=30)
**BEST** — `1l_de-DE_male-JT1/Scheinwerfer auf dritte Stufe einstellen.wav` [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Scheinwerfer%20auf%20dritte%20Stufe%20einstellen.wav.wav)  wer=0.000  speech=[1.59s, 4.67s]  fix=none
- ref: `Scheinwerfer auf dritte Stufe einstellen`
- hyp: `Scheinwerfer auf dritte Stufe einstellen`
**MEDIAN** — `1l_de-DE_female-JT1/Kannst du die Lautstärke auf das Minimum einstellen.wav` [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Kannst%20du%20die%20Lautst%C3%A4rke%20auf%20das%20Minimum%20einstellen.wav.wav)  wer=0.375  speech=[2.76s, 4.72s]  fix=none
- ref: `Kannst du die Lautstärke auf das Minimum einstellen`
- hyp: `Lautstärke auf das Minimum einstellen.`
**WORST** — `1l_de-DE_female-JT1/Fahren Sie nach Birmingham.wav` [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Fahren%20Sie%20nach%20Birmingham.wav.wav)  wer=1.250  speech=[3.2s, 4.52s]  fix=none
- ref: `Fahren Sie nach Birmingham`
- hyp: `Find the app for him.`

### de-DE_JT1 / fast_mai  (n=30)
**BEST** — `1l_de-DE_male-JT1/Scheinwerfer auf dritte Stufe einstellen.wav` [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Scheinwerfer%20auf%20dritte%20Stufe%20einstellen.wav.wav)  wer=0.000  speech=[1.59s, 4.67s]  fix=none
- ref: `Scheinwerfer auf dritte Stufe einstellen`
- hyp: `Scheinwerfer auf dritte Stufe einstellen.`
**MEDIAN** — `1l_de-DE_female-JT1/Lüfter um 1 Stufe erhöhen.wav` [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/L%C3%BCfter%20um%201%20Stufe%20erh%C3%B6hen.wav.wav)  wer=0.200  speech=[2.73s, 4.69s]  fix=none
- ref: `Lüfter um 1 Stufe erhöhen`
- hyp: `Lüfter um eine Stufe erhöhen.`
**WORST** — `1l_de-DE_female-JT1/Diesen Sender aus den Favoriten löschen.wav` [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Diesen%20Sender%20aus%20den%20Favoriten%20l%C3%B6schen.wav.wav)  wer=1.000  speech=[3.6s, 4.16s]  fix=trim_first
- ref: `Diesen Sender aus den Favoriten löschen`
- hyp: `zur Favoritenliste hinzufügen.`

### de-DE_JT1 / realtime  (n=30)
**BEST** — `1l_de-DE_male-JT1/Scheinwerfer auf dritte Stufe einstellen.wav` [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Scheinwerfer%20auf%20dritte%20Stufe%20einstellen.wav.wav)  wer=0.000  speech=[1.59s, 4.67s]  fix=none
- ref: `Scheinwerfer auf dritte Stufe einstellen`
- hyp: `Scheinwerfer auf dritte Stufe einstellen.`
**MEDIAN** — `1l_de-DE_male-JT1/Scheinwerferhöhe auf mittel stellen.wav` [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Scheinwerferh%C3%B6he%20auf%20mittel%20stellen.wav.wav)  wer=0.250  speech=[1.32s, 3.84s]  fix=none
- ref: `Scheinwerferhöhe auf mittel stellen`
- hyp: `Scheinwerferhöhe auf Mittel stelle.`
**WORST** — `1l_de-DE_female-JT1/Diesen Sender aus den Favoriten löschen.wav` [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Diesen%20Sender%20aus%20den%20Favoriten%20l%C3%B6schen.wav.wav)  wer=1.000  speech=[3.6s, 4.16s]  fix=trim_first
- ref: `Diesen Sender aus den Favoriten löschen`
- hyp: `Favoritenliste hinzufügen.`

### de-DE_JT1 / realtime_refine  (n=30)
**BEST** — `1l_de-DE_male-JT1/Scheinwerfer auf dritte Stufe einstellen.wav` [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Scheinwerfer%20auf%20dritte%20Stufe%20einstellen.wav.wav)  wer=0.000  speech=[1.59s, 4.67s]  fix=none
- ref: `Scheinwerfer auf dritte Stufe einstellen`
- hyp: `Scheinwerfer auf dritte Stufe einstellen`
**MEDIAN** — `1l_de-DE_female-JT1/Automatische Belüftung beim Entriegeln deaktivieren.wav` [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20deaktivieren.wav.wav)  wer=0.200  speech=[2.36s, 5.36s]  fix=none
- ref: `Automatische Belüftung beim Entriegeln deaktivieren`
- hyp: `Automatische Belüftung bei Entriegeln deaktivieren`
**WORST** — `1l_de-DE_female-JT1/Diesen Sender aus den Favoriten löschen.wav` [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Diesen%20Sender%20aus%20den%20Favoriten%20l%C3%B6schen.wav.wav)  wer=1.000  speech=[3.6s, 4.16s]  fix=trim_first
- ref: `Diesen Sender aus den Favoriten löschen`
- hyp: `zur Favoritenliste hinzufügen`

## fast_llm hallucinations

`fast_llm` does not set a locale — it relies on auto-detection. When the acoustic signal is weak or ambiguous, it may produce text in the wrong language or fabricate content from its training data.

Found **27** likely hallucinations (WER ≥ 0.8 and ≤ 1 word overlap with reference):

| Audio | Dataset | Sample | WER | Boundary | Reference | Hypothesis |
|---|---|---|---:|---|---|---|
| [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20deaktivieren.wav.wav) | de-DE_DT1 | 1l_de-DE_female-DT1/Automatische Belüftung beim Entriegeln deaktivieren.wav | 2.000 | skip | `Automatische Belüftung beim Entriegeln deaktivieren` | `Smart trip planner by Nitin P. A. P. V. A.` |
| [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Die%20letzte.wav.wav) | de-DE_DT1 | 1l_de-DE_female-DT1/Die letzte.wav | 1.500 | none | `Die letzte` | `He left the...` |
| [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Diesen%20Sender%20aus%20den%20Favoriten%20l%C3%B6schen.wav.wav) | de-DE_DT1 | 1l_de-DE_female-DT1/Diesen Sender aus den Favoriten löschen.wav | 1.000 | trim_first | `Diesen Sender aus den Favoriten löschen` | `Favoreció un despeje en su espíritu.` |
| [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Eco-Fahrmodus%20aktivieren.wav.wav) | de-DE_DT1 | 1l_de-DE_female-DT1/Eco-Fahrmodus aktivieren.wav | 2.000 | skip | `Eco-Fahrmodus aktivieren` | `Est-ce que tu es un?` |
| [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Fahren%20Sie%20nach%20Birmingham.wav.wav) | de-DE_DT1 | 1l_de-DE_female-DT1/Fahren Sie nach Birmingham.wav | 1.000 | skip | `Fahren Sie nach Birmingham` | `And.` |
| [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Kannst%20du%20die%20Lautst%C3%A4rke%20auf%20das%20Minimum%20einstellen.wav.wav) | de-DE_DT1 | 1l_de-DE_female-DT1/Kannst du die Lautstärke auf das Minimum einstellen.wav | 0.875 | skip | `Kannst du die Lautstärke auf das Minimum einstellen` | `The large check off minimum action.` |
| [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Linke%20R%C3%BCcksitzbel%C3%BCftung%20leicht%20erh%C3%B6hen.wav.wav) | de-DE_DT1 | 1l_de-DE_female-DT1/Linke Rücksitzbelüftung leicht erhöhen.wav | 1.000 | skip | `Linke Rücksitzbelüftung leicht erhöhen` | `Last week.` |
| [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20deaktivieren.wav.wav) | de-DE_DT1 | 1l_de-DE_male-DT1/Automatische Belüftung beim Entriegeln deaktivieren.wav | 1.200 | skip | `Automatische Belüftung beim Entriegeln deaktivieren` | `Automatischer Refill bei San Diego, Elias.` |
| [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Klingelton%20stummschalten.wav.wav) | de-DE_DT1 | 1l_de-DE_male-DT1/Klingelton stummschalten.wav | 2.500 | skip | `Klingelton stummschalten` | `Ring it for all expenses.` |
| [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Medienlautst%C3%A4rke%20verringern.wav.wav) | de-DE_DT1 | 1l_de-DE_male-DT1/Medienlautstärke verringern.wav | 2.000 | none | `Medienlautstärke verringern` | `Medium loudspeaker and subwoofer.` |
| [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Vorderen%20Bereich%20etwas%20erw%C3%A4rmen.wav.wav) | de-DE_DT1 | 1l_de-DE_male-DT1/Vorderen Bereich etwas erwärmen.wav | 1.250 | skip | `Vorderen Bereich etwas erwärmen` | `What are the nearby restaurants?` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Autofenster%20halb%20%C3%B6ffnen.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Autofenster halb öffnen.wav | 1.000 | skip | `Autofenster halb öffnen` | `How to answer?` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20deaktivieren.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Automatische Belüftung beim Entriegeln deaktivieren.wav | 1.800 | skip | `Automatische Belüftung beim Entriegeln deaktivieren` | `Not sure if a little bit of anything, the.` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Die%20letzte.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Die letzte.wav | 1.000 | skip | `Die letzte` | `No.` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Diesen%20Sender%20aus%20den%20Favoriten%20l%C3%B6schen.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Diesen Sender aus den Favoriten löschen.wav | 1.000 | skip | `Diesen Sender aus den Favoriten löschen` | `And that's a problem.` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Eco-Fahrmodus%20aktivieren.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Eco-Fahrmodus aktivieren.wav | 1.000 | skip | `Eco-Fahrmodus aktivieren` | `Yeah.` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Fahren%20Sie%20nach%20Birmingham.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Fahren Sie nach Birmingham.wav | 1.000 | skip | `Fahren Sie nach Birmingham` | `I think.` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Linke%20R%C3%BCcksitzbel%C3%BCftung%20leicht%20erh%C3%B6hen.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Linke Rücksitzbelüftung leicht erhöhen.wav | 3.500 | skip | `Linke Rücksitzbelüftung leicht erhöhen` | `The last appearance of the character was in the 2000 issue of the series.` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Linkes%20Hinterfenster%20auf%2060%20%25%20%C3%B6ffnen.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Linkes Hinterfenster auf 60 % öffnen.wav | 1.200 | skip | `Linkes Hinterfenster auf 60 % öffnen` | `OK, so thank you for that.` |
| [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Navigation%20stummschalten.wav.wav) | de-DE_DT2 | 1l_de-DE_female-DT2/Navigation stummschalten.wav | 3.000 | skip | `Navigation stummschalten` | `Love that's there to buy.` |
| [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Autofenster%20halb%20%C3%B6ffnen.wav.wav) | de-DE_DT2 | 1l_de-DE_male-DT2/Autofenster halb öffnen.wav | 1.000 | skip | `Autofenster halb öffnen` | `Open.` |
| [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Fenster%20%C3%B6ffnen.wav.wav) | de-DE_DT2 | 1l_de-DE_male-DT2/Fenster öffnen.wav | 1.000 | skip | `Fenster öffnen` | `Thanks, guys.` |
| [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Scheinwerfer%20auf%20dritte%20Stufe%20einstellen.wav.wav) | de-DE_DT2 | 1l_de-DE_male-DT2/Scheinwerfer auf dritte Stufe einstellen.wav | 0.800 | skip | `Scheinwerfer auf dritte Stufe einstellen` | `Einwerfer Mittelstufe einstellen.` |
| [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Scheinwerferh%C3%B6he%20auf%20mittel%20stellen.wav.wav) | de-DE_DT2 | 1l_de-DE_male-DT2/Scheinwerferhöhe auf mittel stellen.wav | 1.500 | skip | `Scheinwerferhöhe auf mittel stellen` | `Science and Technology has made it.` |
| [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Wechseln%20Sie%20in%20den%20detaillierten%20Berichtsmodus.wav.wav) | de-DE_DT2 | 1l_de-DE_male-DT2/Wechseln Sie in den detaillierten Berichtsmodus.wav | 1.000 | skip | `Wechseln Sie in den detaillierten Berichtsmodus` | `Excellent!` |
| [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Diesen%20Sender%20aus%20den%20Favoriten%20l%C3%B6schen.wav.wav) | de-DE_JT1 | 1l_de-DE_female-JT1/Diesen Sender aus den Favoriten löschen.wav | 1.000 | trim_first | `Diesen Sender aus den Favoriten löschen` | `Favoritenliste hinzufügen.` |
| [▶](audio/de-DE_JT1/1l_de-DE_female-JT1/Fahren%20Sie%20nach%20Birmingham.wav.wav) | de-DE_JT1 | 1l_de-DE_female-JT1/Fahren Sie nach Birmingham.wav | 1.250 | none | `Fahren Sie nach Birmingham` | `Find the app for him.` |

## Top fast_default vs realtime disagreements

### de-DE_DT1/1l_de-DE_male-DT1/Wechseln Sie in den detaillierten Berichtsmodus.wav [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Wechseln%20Sie%20in%20den%20detaillierten%20Berichtsmodus.wav.wav)  Δwer=0.667  (fast_default=1.000, realtime=0.333)  speech=[1.29s, 5.52s] fix=none
- ref:           `Wechseln Sie in den detaillierten Berichtsmodus`
- fast_default   `Next term seat in the induit of Newton believes newer.`
- fast_llm       `Nächsten Sieg in den Blick von Jutland-Berichtsnummer.`
- fast_mai       `Wechseln Sie in den detaillierten Berichtsschnur.`
- realtime       `Wechseln Sie in den Weg zu.`
- realtime_refine `Wechseln Sie in den detaillierten Berichtsmüll.`

### de-DE_DT2/1l_de-DE_female-DT2/Automatische Belüftung beim Entriegeln aktivieren.wav [▶](audio/de-DE_DT2/1l_de-DE_female-DT2/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20aktivieren.wav.wav)  Δwer=0.600  (fast_default=1.000, realtime=0.400)  speech=[3.15s, 5.75s] fix=none
- ref:           `Automatische Belüftung beim Entriegeln aktivieren`
- fast_default   `A particular delivery plan to need an antiviral.`
- fast_llm       `Automatische Belüftung bei einem Unimog A 4 B L.`
- fast_mai       `Automatische Belüftung bei Empfohlen aktivieren.`
- realtime       `Automatische Belüftung aktivieren.`
- realtime_refine `Automatische Belüftung sollen Medien aktivieren.`

### de-DE_JT1/1l_de-DE_male-JT1/Fenster öffnen.wav [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Fenster%20%C3%B6ffnen.wav.wav)  Δwer=0.500  (fast_default=0.000, realtime=0.500)  speech=[1.25s, 2.16s] fix=trim_last
- ref:           `Fenster öffnen`
- fast_default   `Fenster öffnen.`
- fast_llm       `Fenster öffnen.`
- fast_mai       `Fenster öffnen.`
- realtime       `Fenster öffnen.An.`
- realtime_refine `Fenster öffnen`

### de-DE_JT1/1l_de-DE_male-JT1/Außenluftzirkulation einschalten.wav [▶](audio/de-DE_JT1/1l_de-DE_male-JT1/Au%C3%9Fenluftzirkulation%20einschalten.wav.wav)  Δwer=0.500  (fast_default=0.500, realtime=0.000)  speech=[1.28s, 4.04s] fix=none
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

### de-DE_DT2/1l_de-DE_male-DT2/Außenluftzirkulation einschalten.wav [▶](audio/de-DE_DT2/1l_de-DE_male-DT2/Au%C3%9Fenluftzirkulation%20einschalten.wav.wav)  Δwer=0.500  (fast_default=0.000, realtime=0.500)  speech=[1.31s, 4.07s] fix=none
- ref:           `Außenluftzirkulation einschalten`
- fast_default   `Außenluftzirkulation einschalten.`
- fast_llm       `Außenluftzirkulation einschalten.`
- fast_mai       `Außenluftzirkulation einschalten.`
- realtime       `Außenluftzirkulation einschaltet.`
- realtime_refine `Außenluftzirkulation einschalten.`

### de-DE_DT1/1l_de-DE_female-DT1/Fahrtenanzeige öffnen.wav [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Fahrtenanzeige%20%C3%B6ffnen.wav.wav)  Δwer=0.500  (fast_default=0.500, realtime=1.000)  speech=[1.95s, 3.07s] fix=trim_first
- ref:           `Fahrtenanzeige öffnen`
- fast_default   `Datenanzeige öffnen.`
- fast_llm       `Datenanzeige öffnen.`
- fast_mai       `Datenanzeige öffnen.`
- realtime       `Daten Anzeige öffnen.`
- realtime_refine `Datenanzeige öffnen.`

### de-DE_DT1/1l_de-DE_male-DT1/Automatische Belüftung beim Entriegeln deaktivieren.wav [▶](audio/de-DE_DT1/1l_de-DE_male-DT1/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20deaktivieren.wav.wav)  Δwer=0.400  (fast_default=1.000, realtime=0.600)  speech=[-s, -s] fix=skip
- ref:           `Automatische Belüftung beim Entriegeln deaktivieren`
- fast_default   `Altamonte server neutral by Centenegio.`
- fast_llm       `Automatischer Refill bei San Diego, Elias.`
- fast_mai       `Automatische Benutzung bei 3D-Druck.`
- realtime       `Automatische Belüftung.`
- realtime_refine `Altamonte served neutral by Centenegio, the electron.`

### de-DE_DT1/1l_de-DE_female-DT1/Automatische Belüftung beim Entriegeln deaktivieren.wav [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20deaktivieren.wav.wav)  Δwer=0.400  (fast_default=1.000, realtime=0.600)  speech=[-s, -s] fix=skip
- ref:           `Automatische Belüftung beim Entriegeln deaktivieren`
- fast_default   ``
- fast_llm       `Smart trip planner by Nitin P. A. P. V. A.`
- fast_mai       `Automatische Belüftung bei Enten, Gänse und wie auch immer.`
- realtime       `Automatische Belastung bei den Deaktivieren.`
- realtime_refine `Automatische Belüftung bei den Dingern deaktivieren.`

### de-DE_DT1/1l_de-DE_female-DT1/Automatische Belüftung beim Entriegeln aktivieren.wav [▶](audio/de-DE_DT1/1l_de-DE_female-DT1/Automatische%20Bel%C3%BCftung%20beim%20Entriegeln%20aktivieren.wav.wav)  Δwer=0.400  (fast_default=0.600, realtime=1.000)  speech=[-s, -s] fix=skip
- ref:           `Automatische Belüftung beim Entriegeln aktivieren`
- fast_default   `Automatische Beliftung bei Enreaging aktivieren.`
- fast_llm       `Automatische Umlüftung bei Entgegen aktivieren.`
- fast_mai       `Automatische Vernetzung der Entwederung aktivieren`
- realtime       ``
- realtime_refine `Automatische Belüftung bei Entregeln aktivieren.`

## Caveats

- **UPL is anchored on the realtime SDK's word-end timestamp** for each sample, so all services use the same `speech_end`. The CSV's `upl_self_ms` column has each service's own phrase-derived value if you want to see how its boundary detection differs.
- **Mazda voice commands** are short utterances (typically 2-8 words). WER on short references is noisier — a single word error on a 3-word command gives 33% WER.