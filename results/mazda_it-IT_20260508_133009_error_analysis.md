# Error analysis — mazda_it-IT_20260508_133009.csv

Filters out samples that look like *data* problems rather than recognition errors:
1. **Empty hypothesis** — at least one service returned no text.
2. **Reference much shorter than audio** — `words_per_s < 0.3` (with `duration ≥ 1 s`). At normal speech rates this means the label is missing content.
3. **All services agree, ref disagrees** — mean pairwise WER between hypotheses < 0.15 AND mean WER vs ref > 0.5. Multiple ASR systems converging on the same answer that differs from the reference is a strong signal of a mislabeled ground truth, not a shared error.
4. **Compound-word / segmentation artifact** — all services produce text identical to the reference after removing spaces (e.g. `stummschalten` vs `stumm schalten`). These are correct recognitions scored as errors due to tokenization.

Audio links (▶) point to `results/audio/<dataset>/<sample_id>.wav` so a reviewer can play the clip directly.

## Datasets under test

- **it-IT_DT1** — Mazda it-IT DT1 voice commands (male + female pooled)
- **it-IT_DT2** — Mazda it-IT DT2 voice commands (male + female pooled)
- **it-IT_JT1** — Mazda it-IT JT1 voice commands (male + female pooled)

Total complete samples: **90**  
Kept after filtering: **85**  
Excluded as data issues: **5**  

- Empty hypothesis: 2
- Reference too short for audio: 0
- All services agree, ref disagrees: 0
- Compound-word / segmentation artifact: 3

## Speech boundaries

`speech_start_s` / `speech_end_s` come from the realtime SDK's word-level timestamps and anchor UPL for all services. Per-word detail lives in the sidecar `mazda_it-IT_20260508_133009_words.jsonl`.

Boundary-fix actions across 90 realtime samples: `skip`=2, `trim_both`=2, `trim_first`=3, `trim_last`=3

## Filtered results (excludes data issues)

INS/DEL/SUB are *rates per 100 reference words*. Their sum ≈ WER × 100.

| Dataset | Service | N | WER | SER | INS/100 | DEL/100 | SUB/100 | LBL ms (mean / p90) | UPL ms (mean / p90) |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| it-IT_DT1 | fast_default | 29 | 0.082 | 0.276 | 1.9 | 0.6 | 5.6 | 615 / 723 | 1016 / 1251 |
| it-IT_DT1 | fast_llm | 29 | 0.065 | 0.241 | 1.2 | 1.2 | 4.3 | 507 / 583 | 907 / 1123 |
| it-IT_DT1 | fast_mai | 29 | 0.090 | 0.276 | 1.9 | 0.0 | 4.9 | 490 / 608 | 890 / 1138 |
| it-IT_DT1 | realtime | 29 | 0.091 | 0.345 | 3.1 | 1.2 | 4.9 | -94 / 301 | 609 / 869 |
| it-IT_DT1 | realtime_refine | 29 | 0.075 | 0.241 | 1.2 | 1.2 | 4.3 | 354 / 748 | 1077 / 1317 |
| it-IT_DT2 | fast_default | 27 | 0.152 | 0.370 | 0.7 | 5.3 | 9.9 | 650 / 726 | 1056 / 1214 |
| it-IT_DT2 | fast_llm | 27 | 0.163 | 0.370 | 1.3 | 4.6 | 11.3 | 522 / 622 | 927 / 1095 |
| it-IT_DT2 | fast_mai | 27 | 0.140 | 0.407 | 0.7 | 2.6 | 9.9 | 498 / 570 | 904 / 1059 |
| it-IT_DT2 | realtime | 27 | 0.189 | 0.444 | 2.0 | 6.0 | 11.9 | -78 / 321 | 626 / 864 |
| it-IT_DT2 | realtime_refine | 27 | 0.135 | 0.370 | 1.3 | 2.6 | 9.9 | 423 / 782 | 1205 / 1964 |
| it-IT_JT1 | fast_default | 29 | 0.047 | 0.207 | 0.6 | 0.6 | 3.1 | 624 / 728 | 1006 / 1239 |
| it-IT_JT1 | fast_llm | 29 | 0.045 | 0.172 | 1.2 | 0.6 | 2.5 | 505 / 584 | 887 / 1114 |
| it-IT_JT1 | fast_mai | 29 | 0.033 | 0.172 | 0.6 | 0.0 | 2.5 | 550 / 724 | 932 / 1153 |
| it-IT_JT1 | realtime | 29 | 0.033 | 0.172 | 0.0 | 0.6 | 2.5 | -128 / 295 | 557 / 787 |
| it-IT_JT1 | realtime_refine | 29 | 0.047 | 0.207 | 0.6 | 0.6 | 3.1 | 349 / 712 | 1037 / 1280 |

## Unfiltered results (all complete samples, for reference)

| Dataset | Service | N | WER | SER | INS/100 | DEL/100 | SUB/100 |
|---|---|---:|---:|---:|---:|---:|---:|
| it-IT_DT1 | fast_default | 30 | 0.079 | 0.267 | 1.8 | 0.6 | 5.3 |
| it-IT_DT1 | fast_llm | 30 | 0.062 | 0.233 | 1.2 | 1.2 | 4.1 |
| it-IT_DT1 | fast_mai | 30 | 0.087 | 0.267 | 1.8 | 0.0 | 4.7 |
| it-IT_DT1 | realtime | 30 | 0.088 | 0.333 | 3.0 | 1.2 | 4.7 |
| it-IT_DT1 | realtime_refine | 30 | 0.072 | 0.233 | 1.2 | 1.2 | 4.1 |
| it-IT_DT2 | fast_default | 30 | 0.176 | 0.400 | 0.6 | 7.1 | 10.1 |
| it-IT_DT2 | fast_llm | 30 | 0.196 | 0.400 | 2.4 | 4.1 | 13.6 |
| it-IT_DT2 | fast_mai | 30 | 0.173 | 0.433 | 1.8 | 2.4 | 13.0 |
| it-IT_DT2 | realtime | 30 | 0.236 | 0.467 | 1.8 | 11.8 | 10.7 |
| it-IT_DT2 | realtime_refine | 30 | 0.170 | 0.400 | 1.2 | 5.9 | 10.1 |
| it-IT_JT1 | fast_default | 30 | 0.045 | 0.200 | 0.6 | 0.6 | 3.0 |
| it-IT_JT1 | fast_llm | 30 | 0.044 | 0.167 | 1.2 | 0.6 | 2.4 |
| it-IT_JT1 | fast_mai | 30 | 0.032 | 0.167 | 0.6 | 0.0 | 2.4 |
| it-IT_JT1 | realtime | 30 | 0.032 | 0.167 | 0.0 | 0.6 | 2.4 |
| it-IT_JT1 | realtime_refine | 30 | 0.045 | 0.200 | 0.6 | 0.6 | 3.0 |

## Excluded samples — examples

### Empty hypothesis

| Audio | Dataset | Sample | Empty in | Reference |
|---|---|---|---|---|
| [▶](audio/it-IT_DT2/1l_it-IT_female-DT2/Apri%20la%20visuale%20panoramica.wav.wav) | it-IT_DT2 | 1l_it-IT_female-DT2/Apri la visuale panoramica.wav | realtime | `Apri la visuale panoramica` |
| [▶](audio/it-IT_DT2/1l_it-IT_female-DT2/Apri%20il%20finestrino%20posteriore%20destro%C2%A0%20a%20met%C3%A0.wav.wav) | it-IT_DT2 | 1l_it-IT_female-DT2/Apri il finestrino posteriore destro  a metà.wav | realtime | `Apri il finestrino posteriore destro  a metà` |

### Reference too short for audio duration

_(none)_

### All services agree, reference disagrees (likely mislabeled)

_(none)_

### Compound-word / segmentation artifacts

#### it-IT_DT1/1l_it-IT_female-DT1/Disattiva la frenata d'emergenzaa bassa velocità.wav [▶](audio/it-IT_DT1/1l_it-IT_female-DT1/Disattiva%20la%20frenata%20d%27emergenzaa%20bassa%20velocit%C3%A0.wav.wav)
- ref:           `Disattiva la frenata d'emergenzaa bassa velocità`
- fast_default   `Disattiva la frenata d'emergenza a bassa velocità.`
- fast_llm       `Disattiva la frenata d'emergenza a bassa velocità.`
- fast_mai       `Disattiva la frenata d'emergenza a bassa velocità.`
- realtime       `Disattiva la frenata d'emergenza a bassa velocità.`
- realtime_refine `Disattiva la frenata d'emergenza a bassa velocità.`

#### it-IT_DT2/1l_it-IT_female-DT2/Disattiva la frenata d'emergenzaa bassa velocità.wav [▶](audio/it-IT_DT2/1l_it-IT_female-DT2/Disattiva%20la%20frenata%20d%27emergenzaa%20bassa%20velocit%C3%A0.wav.wav)
- ref:           `Disattiva la frenata d'emergenzaa bassa velocità`
- fast_default   `Disattiva la frenata d'emergenza a bassa velocità.`
- fast_llm       `Disattiva la frenata d'emergenza a bassa velocità.`
- fast_mai       `Disattiva la frenata d'emergenza a bassa velocità.`
- realtime       `Disattiva la frenata d'emergenza a bassa velocità.`
- realtime_refine `Disattiva la frenata d'emergenza a bassa velocità.`

#### it-IT_JT1/1l_it-IT_female-JT1/Disattiva la frenata d'emergenzaa bassa velocità.wav [▶](audio/it-IT_JT1/1l_it-IT_female-JT1/Disattiva%20la%20frenata%20d%27emergenzaa%20bassa%20velocit%C3%A0.wav.wav)
- ref:           `Disattiva la frenata d'emergenzaa bassa velocità`
- fast_default   `Disattiva la frenata d'emergenza a bassa velocità.`
- fast_llm       `Disattiva la frenata d'emergenza a bassa velocità.`
- fast_mai       `Disattiva la frenata d'emergenza a bassa velocità.`
- realtime       `Disattiva la frenata d'emergenza a bassa velocità.`
- realtime_refine `Disattiva la frenata d'emergenza a bassa velocità.`

## Genuine recognition errors (filtered set)

Best / median / worst WER per (dataset, service) on the kept samples.

### it-IT_DT1 / fast_default  (n=29)
**BEST** — `1l_it-IT_male-DT1/Disabilita l'assistenza alla retromarcia.wav` [▶](audio/it-IT_DT1/1l_it-IT_male-DT1/Disabilita%20l%27assistenza%20alla%20retromarcia.wav.wav)  wer=0.000  speech=[1.34s, 3.76s]  fix=none
- ref: `Disabilita l'assistenza alla retromarcia`
- hyp: `Disabilita l'assistenza alla retromarcia.`
**MEDIAN** — `1l_it-IT_female-DT1/Apri il finestrino posteriore destro  a metà.wav` [▶](audio/it-IT_DT1/1l_it-IT_female-DT1/Apri%20il%20finestrino%20posteriore%20destro%C2%A0%20a%20met%C3%A0.wav.wav)  wer=0.000  speech=[1.31s, 5.03s]  fix=none
- ref: `Apri il finestrino posteriore destro  a metà`
- hyp: `Apri il finestrino posteriore destro a metà.`
**WORST** — `1l_it-IT_female-DT1/Accendi gli abbaglianti intelligenti.wav` [▶](audio/it-IT_DT1/1l_it-IT_female-DT1/Accendi%20gli%20abbaglianti%20intelligenti.wav.wav)  wer=0.750  speech=[1.35s, 4.27s]  fix=none
- ref: `Accendi gli abbaglianti intelligenti`
- hyp: `Accende gli anabbaglianti più intelligenti.`

### it-IT_DT1 / fast_llm  (n=29)
**BEST** — `1l_it-IT_male-DT1/Disabilita l'assistenza alla retromarcia.wav` [▶](audio/it-IT_DT1/1l_it-IT_male-DT1/Disabilita%20l%27assistenza%20alla%20retromarcia.wav.wav)  wer=0.000  speech=[1.34s, 3.76s]  fix=none
- ref: `Disabilita l'assistenza alla retromarcia`
- hyp: `Disabilita l'assistenza alla retromarcia.`
**MEDIAN** — `1l_it-IT_female-DT1/Guida verso Birmingham.wav` [▶](audio/it-IT_DT1/1l_it-IT_female-DT1/Guida%20verso%20Birmingham.wav.wav)  wer=0.000  speech=[1.57s, 2.45s]  fix=trim_last
- ref: `Guida verso Birmingham`
- hyp: `Guida verso Birmingham.`
**WORST** — `1l_it-IT_male-DT1/Attiva telecamera 360 gradi.wav` [▶](audio/it-IT_DT1/1l_it-IT_male-DT1/Attiva%20telecamera%20360%20gradi.wav.wav)  wer=0.500  speech=[1.25s, 3.96s]  fix=none
- ref: `Attiva telecamera 360 gradi`
- hyp: `Attiva telecamera a 360°.`

### it-IT_DT1 / fast_mai  (n=29)
**BEST** — `1l_it-IT_male-DT1/Disabilita l'assistenza alla retromarcia.wav` [▶](audio/it-IT_DT1/1l_it-IT_male-DT1/Disabilita%20l%27assistenza%20alla%20retromarcia.wav.wav)  wer=0.000  speech=[1.34s, 3.76s]  fix=none
- ref: `Disabilita l'assistenza alla retromarcia`
- hyp: `Disabilita l'assistenza alla retromarcia.`
**MEDIAN** — `1l_it-IT_female-DT1/Apri il finestrino posteriore destro  a metà.wav` [▶](audio/it-IT_DT1/1l_it-IT_female-DT1/Apri%20il%20finestrino%20posteriore%20destro%C2%A0%20a%20met%C3%A0.wav.wav)  wer=0.000  speech=[1.31s, 5.03s]  fix=none
- ref: `Apri il finestrino posteriore destro  a metà`
- hyp: `Apri il finestrino posteriore destro a metà.`
**WORST** — `1l_it-IT_female-DT1/Accendi gli abbaglianti intelligenti.wav` [▶](audio/it-IT_DT1/1l_it-IT_female-DT1/Accendi%20gli%20abbaglianti%20intelligenti.wav.wav)  wer=0.750  speech=[1.35s, 4.27s]  fix=none
- ref: `Accendi gli abbaglianti intelligenti`
- hyp: `Facendo gli anabbaglianti più intelligenti.`

### it-IT_DT1 / realtime  (n=29)
**BEST** — `1l_it-IT_male-DT1/Disabilita l'assistenza alla retromarcia.wav` [▶](audio/it-IT_DT1/1l_it-IT_male-DT1/Disabilita%20l%27assistenza%20alla%20retromarcia.wav.wav)  wer=0.000  speech=[1.34s, 3.76s]  fix=none
- ref: `Disabilita l'assistenza alla retromarcia`
- hyp: `Disabilita l'assistenza alla retromarcia.`
**MEDIAN** — `1l_it-IT_male-DT1/Chiudi Lettore multimediale per il passeggero.wav` [▶](audio/it-IT_DT1/1l_it-IT_male-DT1/Chiudi%20Lettore%20multimediale%20per%20il%20passeggero.wav.wav)  wer=0.000  speech=[1.3s, 3.92s]  fix=none
- ref: `Chiudi Lettore multimediale per il passeggero`
- hyp: `Chiudi lettore multimediale per il passeggero.`
**WORST** — `1l_it-IT_female-DT1/Guida verso Birmingham.wav` [▶](audio/it-IT_DT1/1l_it-IT_female-DT1/Guida%20verso%20Birmingham.wav.wav)  wer=0.667  speech=[1.57s, 2.45s]  fix=trim_last
- ref: `Guida verso Birmingham`
- hyp: `Guida verso Birmir Milan.`

### it-IT_DT1 / realtime_refine  (n=29)
**BEST** — `1l_it-IT_male-DT1/Disabilita l'assistenza alla retromarcia.wav` [▶](audio/it-IT_DT1/1l_it-IT_male-DT1/Disabilita%20l%27assistenza%20alla%20retromarcia.wav.wav)  wer=0.000  speech=[1.34s, 3.76s]  fix=none
- ref: `Disabilita l'assistenza alla retromarcia`
- hyp: `Disabilita l'assistenza alla retromarcia.`
**MEDIAN** — `1l_it-IT_female-DT1/Guida verso Birmingham.wav` [▶](audio/it-IT_DT1/1l_it-IT_female-DT1/Guida%20verso%20Birmingham.wav.wav)  wer=0.000  speech=[1.57s, 2.45s]  fix=trim_last
- ref: `Guida verso Birmingham`
- hyp: `Guida verso Birmingham.`
**WORST** — `1l_it-IT_female-DT1/Accendi gli abbaglianti intelligenti.wav` [▶](audio/it-IT_DT1/1l_it-IT_female-DT1/Accendi%20gli%20abbaglianti%20intelligenti.wav.wav)  wer=0.750  speech=[1.35s, 4.27s]  fix=none
- ref: `Accendi gli abbaglianti intelligenti`
- hyp: `Accende gli anabbaglianti più intelligenti.`

### it-IT_DT2 / fast_default  (n=27)
**BEST** — `1l_it-IT_male-DT2/Disabilita l'assistenza alla retromarcia.wav` [▶](audio/it-IT_DT2/1l_it-IT_male-DT2/Disabilita%20l%27assistenza%20alla%20retromarcia.wav.wav)  wer=0.000  speech=[1.35s, 3.79s]  fix=none
- ref: `Disabilita l'assistenza alla retromarcia`
- hyp: `Disabilita l'assistenza alla retromarcia.`
**MEDIAN** — `1l_it-IT_male-DT2/Attiva chiusura automatica finestrini con chiusura auto.wav` [▶](audio/it-IT_DT2/1l_it-IT_male-DT2/Attiva%20chiusura%20automatica%20finestrini%20con%20chiusura%20auto.wav.wav)  wer=0.000  speech=[1.37s, 4.61s]  fix=none
- ref: `Attiva chiusura automatica finestrini con chiusura auto`
- hyp: `Attiva chiusura automatica finestrini con chiusura auto.`
**WORST** — `1l_it-IT_female-DT2/Imposta i fari più alti.wav` [▶](audio/it-IT_DT2/1l_it-IT_female-DT2/Imposta%20i%20fari%20pi%C3%B9%20alti.wav.wav)  wer=1.000  speech=[2.63s, 2.67s]  fix=trim_both
- ref: `Imposta i fari più alti`
- hyp: `Postepay One.`

### it-IT_DT2 / fast_llm  (n=27)
**BEST** — `1l_it-IT_male-DT2/Disabilita l'assistenza alla retromarcia.wav` [▶](audio/it-IT_DT2/1l_it-IT_male-DT2/Disabilita%20l%27assistenza%20alla%20retromarcia.wav.wav)  wer=0.000  speech=[1.35s, 3.79s]  fix=none
- ref: `Disabilita l'assistenza alla retromarcia`
- hyp: `Disabilita l'assistenza alla retromarcia.`
**MEDIAN** — `1l_it-IT_male-DT2/Attiva chiusura automatica finestrini con chiusura auto.wav` [▶](audio/it-IT_DT2/1l_it-IT_male-DT2/Attiva%20chiusura%20automatica%20finestrini%20con%20chiusura%20auto.wav.wav)  wer=0.000  speech=[1.37s, 4.61s]  fix=none
- ref: `Attiva chiusura automatica finestrini con chiusura auto`
- hyp: `Attiva chiusura automatica finestrini con chiusura auto.`
**WORST** — `1l_it-IT_male-DT2/Disattiva Apple Carplay per il passeggero.wav` [▶](audio/it-IT_DT2/1l_it-IT_male-DT2/Disattiva%20Apple%20Carplay%20per%20il%20passeggero.wav.wav)  wer=1.000  speech=[2.01s, 3.25s]  fix=trim_both
- ref: `Disattiva Apple Carplay per il passeggero`
- hyp: `Da viva e orgogliosa in passeggiata.`

### it-IT_DT2 / fast_mai  (n=27)
**BEST** — `1l_it-IT_male-DT2/Disabilita l'assistenza alla retromarcia.wav` [▶](audio/it-IT_DT2/1l_it-IT_male-DT2/Disabilita%20l%27assistenza%20alla%20retromarcia.wav.wav)  wer=0.000  speech=[1.35s, 3.79s]  fix=none
- ref: `Disabilita l'assistenza alla retromarcia`
- hyp: `Disabilita l'assistenza alla retromarcia.`
**MEDIAN** — `1l_it-IT_male-DT2/Voglio aprire le Impostazioni.wav` [▶](audio/it-IT_DT2/1l_it-IT_male-DT2/Voglio%20aprire%20le%20Impostazioni.wav.wav)  wer=0.000  speech=[1.34s, 3.12s]  fix=none
- ref: `Voglio aprire le Impostazioni`
- hyp: `Voglio aprire le impostazioni.`
**WORST** — `1l_it-IT_female-DT2/Imposta i fari più alti.wav` [▶](audio/it-IT_DT2/1l_it-IT_female-DT2/Imposta%20i%20fari%20pi%C3%B9%20alti.wav.wav)  wer=1.000  speech=[2.63s, 2.67s]  fix=trim_both
- ref: `Imposta i fari più alti`
- hyp: `Poste fai 4.`

### it-IT_DT2 / realtime  (n=27)
**BEST** — `1l_it-IT_female-DT2/Attiva Android Auto.wav` [▶](audio/it-IT_DT2/1l_it-IT_female-DT2/Attiva%20Android%20Auto.wav.wav)  wer=0.000  speech=[1.59s, 3.27s]  fix=none
- ref: `Attiva Android Auto`
- hyp: `Attiva Android Auto.`
**MEDIAN** — `1l_it-IT_male-DT2/Imposta le preferenze di percorso su.wav` [▶](audio/it-IT_DT2/1l_it-IT_male-DT2/Imposta%20le%20preferenze%20di%20percorso%20su.wav.wav)  wer=0.000  speech=[1.3s, 3.66s]  fix=none
- ref: `Imposta le preferenze di percorso su`
- hyp: `Imposta le preferenze di percorso, su.`
**WORST** — `1l_it-IT_female-DT2/Imposta i fari più alti.wav` [▶](audio/it-IT_DT2/1l_it-IT_female-DT2/Imposta%20i%20fari%20pi%C3%B9%20alti.wav.wav)  wer=1.000  speech=[2.63s, 2.67s]  fix=trim_both
- ref: `Imposta i fari più alti`
- hyp: `Postepay o art.`

### it-IT_DT2 / realtime_refine  (n=27)
**BEST** — `1l_it-IT_male-DT2/Disabilita l'assistenza alla retromarcia.wav` [▶](audio/it-IT_DT2/1l_it-IT_male-DT2/Disabilita%20l%27assistenza%20alla%20retromarcia.wav.wav)  wer=0.000  speech=[1.35s, 3.79s]  fix=none
- ref: `Disabilita l'assistenza alla retromarcia`
- hyp: `Disabilita l'assistenza alla retromarcia.`
**MEDIAN** — `1l_it-IT_male-DT2/Attiva chiusura automatica finestrini con chiusura auto.wav` [▶](audio/it-IT_DT2/1l_it-IT_male-DT2/Attiva%20chiusura%20automatica%20finestrini%20con%20chiusura%20auto.wav.wav)  wer=0.000  speech=[1.37s, 4.61s]  fix=none
- ref: `Attiva chiusura automatica finestrini con chiusura auto`
- hyp: `Attiva chiusura automatica finestrini con chiusura auto.`
**WORST** — `1l_it-IT_female-DT2/Imposta i fari più alti.wav` [▶](audio/it-IT_DT2/1l_it-IT_female-DT2/Imposta%20i%20fari%20pi%C3%B9%20alti.wav.wav)  wer=1.000  speech=[2.63s, 2.67s]  fix=trim_both
- ref: `Imposta i fari più alti`
- hyp: `Postepay One.`

### it-IT_JT1 / fast_default  (n=29)
**BEST** — `1l_it-IT_male-JT1/Disabilita l'assistenza alla retromarcia.wav` [▶](audio/it-IT_JT1/1l_it-IT_male-JT1/Disabilita%20l%27assistenza%20alla%20retromarcia.wav.wav)  wer=0.000  speech=[1.27s, 3.83s]  fix=none
- ref: `Disabilita l'assistenza alla retromarcia`
- hyp: `Disabilita l'assistenza alla retromarcia.`
**MEDIAN** — `1l_it-IT_female-JT1/Apri il finestrino lato passeggero al 60%.wav` [▶](audio/it-IT_JT1/1l_it-IT_female-JT1/Apri%20il%20finestrino%20lato%20passeggero%20al%2060%25.wav.wav)  wer=0.000  speech=[1.56s, 5.44s]  fix=none
- ref: `Apri il finestrino lato passeggero al 60%`
- hyp: `Apri il finestrino lato passeggero al 60%.`
**WORST** — `1l_it-IT_male-JT1/Attiva telecamera 360 gradi.wav` [▶](audio/it-IT_JT1/1l_it-IT_male-JT1/Attiva%20telecamera%20360%20gradi.wav.wav)  wer=0.500  speech=[1.24s, 3.96s]  fix=none
- ref: `Attiva telecamera 360 gradi`
- hyp: `Attiva telecamera a 360°.`

### it-IT_JT1 / fast_llm  (n=29)
**BEST** — `1l_it-IT_male-JT1/Disabilita l'assistenza alla retromarcia.wav` [▶](audio/it-IT_JT1/1l_it-IT_male-JT1/Disabilita%20l%27assistenza%20alla%20retromarcia.wav.wav)  wer=0.000  speech=[1.27s, 3.83s]  fix=none
- ref: `Disabilita l'assistenza alla retromarcia`
- hyp: `Disabilita l'assistenza alla retromarcia.`
**MEDIAN** — `1l_it-IT_female-JT1/Apri il finestrino lato passeggero al 60%.wav` [▶](audio/it-IT_JT1/1l_it-IT_female-JT1/Apri%20il%20finestrino%20lato%20passeggero%20al%2060%25.wav.wav)  wer=0.000  speech=[1.56s, 5.44s]  fix=none
- ref: `Apri il finestrino lato passeggero al 60%`
- hyp: `Apri il finestrino lato passeggero al 60%.`
**WORST** — `1l_it-IT_male-JT1/Attiva telecamera 360 gradi.wav` [▶](audio/it-IT_JT1/1l_it-IT_male-JT1/Attiva%20telecamera%20360%20gradi.wav.wav)  wer=0.500  speech=[1.24s, 3.96s]  fix=none
- ref: `Attiva telecamera 360 gradi`
- hyp: `Attiva telecamera a 360°.`

### it-IT_JT1 / fast_mai  (n=29)
**BEST** — `1l_it-IT_male-JT1/Disabilita l'assistenza alla retromarcia.wav` [▶](audio/it-IT_JT1/1l_it-IT_male-JT1/Disabilita%20l%27assistenza%20alla%20retromarcia.wav.wav)  wer=0.000  speech=[1.27s, 3.83s]  fix=none
- ref: `Disabilita l'assistenza alla retromarcia`
- hyp: `Disabilita l'assistenza alla retromarcia.`
**MEDIAN** — `1l_it-IT_female-JT1/Apri il finestrino lato passeggero al 60%.wav` [▶](audio/it-IT_JT1/1l_it-IT_female-JT1/Apri%20il%20finestrino%20lato%20passeggero%20al%2060%25.wav.wav)  wer=0.000  speech=[1.56s, 5.44s]  fix=none
- ref: `Apri il finestrino lato passeggero al 60%`
- hyp: `Apri il finestrino lato passeggero al 60%.`
**WORST** — `1l_it-IT_male-JT1/Attiva telecamera 360 gradi.wav` [▶](audio/it-IT_JT1/1l_it-IT_male-JT1/Attiva%20telecamera%20360%20gradi.wav.wav)  wer=0.250  speech=[1.24s, 3.96s]  fix=none
- ref: `Attiva telecamera 360 gradi`
- hyp: `Attiva telecamera a 360 gradi.`

### it-IT_JT1 / realtime  (n=29)
**BEST** — `1l_it-IT_male-JT1/Disabilita l'assistenza alla retromarcia.wav` [▶](audio/it-IT_JT1/1l_it-IT_male-JT1/Disabilita%20l%27assistenza%20alla%20retromarcia.wav.wav)  wer=0.000  speech=[1.27s, 3.83s]  fix=none
- ref: `Disabilita l'assistenza alla retromarcia`
- hyp: `Disabilita l'assistenza alla retromarcia.`
**MEDIAN** — `1l_it-IT_female-JT1/Apri il finestrino lato passeggero al 60%.wav` [▶](audio/it-IT_JT1/1l_it-IT_female-JT1/Apri%20il%20finestrino%20lato%20passeggero%20al%2060%25.wav.wav)  wer=0.000  speech=[1.56s, 5.44s]  fix=none
- ref: `Apri il finestrino lato passeggero al 60%`
- hyp: `Apri il finestrino lato passeggero al 60%.`
**WORST** — `1l_it-IT_male-JT1/Attiva telecamera 360 gradi.wav` [▶](audio/it-IT_JT1/1l_it-IT_male-JT1/Attiva%20telecamera%20360%20gradi.wav.wav)  wer=0.250  speech=[1.24s, 3.96s]  fix=none
- ref: `Attiva telecamera 360 gradi`
- hyp: `Attiva telecamera 360 °.`

### it-IT_JT1 / realtime_refine  (n=29)
**BEST** — `1l_it-IT_male-JT1/Disabilita l'assistenza alla retromarcia.wav` [▶](audio/it-IT_JT1/1l_it-IT_male-JT1/Disabilita%20l%27assistenza%20alla%20retromarcia.wav.wav)  wer=0.000  speech=[1.27s, 3.83s]  fix=none
- ref: `Disabilita l'assistenza alla retromarcia`
- hyp: `Disabilita l'assistenza alla retromarcia.`
**MEDIAN** — `1l_it-IT_female-JT1/Apri il finestrino lato passeggero al 60%.wav` [▶](audio/it-IT_JT1/1l_it-IT_female-JT1/Apri%20il%20finestrino%20lato%20passeggero%20al%2060%25.wav.wav)  wer=0.000  speech=[1.56s, 5.44s]  fix=none
- ref: `Apri il finestrino lato passeggero al 60%`
- hyp: `Apri il finestrino lato passeggero al 60%.`
**WORST** — `1l_it-IT_male-JT1/Attiva telecamera 360 gradi.wav` [▶](audio/it-IT_JT1/1l_it-IT_male-JT1/Attiva%20telecamera%20360%20gradi.wav.wav)  wer=0.500  speech=[1.24s, 3.96s]  fix=none
- ref: `Attiva telecamera 360 gradi`
- hyp: `Attiva telecamera a 360 °.`

## Top fast_default vs realtime disagreements (filtered)

### it-IT_DT1/1l_it-IT_female-DT1/Guida verso Birmingham.wav [▶](audio/it-IT_DT1/1l_it-IT_female-DT1/Guida%20verso%20Birmingham.wav.wav)  Δwer=0.667  (fast_default=0.000, realtime=0.667)  speech=[1.57s, 2.45s] fix=trim_last
- ref:           `Guida verso Birmingham`
- fast_default   `Guida verso Birmingham.`
- fast_llm       `Guida verso Birmingham.`
- fast_mai       `Mi dà verso Birmingham.`
- realtime       `Guida verso Birmir Milan.`
- realtime_refine `Guida verso Birmingham.`

### it-IT_DT1/1l_it-IT_female-DT1/Accendi gli abbaglianti intelligenti.wav [▶](audio/it-IT_DT1/1l_it-IT_female-DT1/Accendi%20gli%20abbaglianti%20intelligenti.wav.wav)  Δwer=0.500  (fast_default=0.750, realtime=0.250)  speech=[1.35s, 4.27s] fix=none
- ref:           `Accendi gli abbaglianti intelligenti`
- fast_default   `Accende gli anabbaglianti più intelligenti.`
- fast_llm       `Accendi gli anabbaglianti intelligenti.`
- fast_mai       `Facendo gli anabbaglianti più intelligenti.`
- realtime       `Accendi gli anabbaglianti intelligenti.`
- realtime_refine `Accende gli anabbaglianti più intelligenti.`

### it-IT_DT2/1l_it-IT_male-DT2/Disabilita l'assistenza alla retromarcia.wav [▶](audio/it-IT_DT2/1l_it-IT_male-DT2/Disabilita%20l%27assistenza%20alla%20retromarcia.wav.wav)  Δwer=0.400  (fast_default=0.000, realtime=0.400)  speech=[1.35s, 3.79s] fix=none
- ref:           `Disabilita l'assistenza alla retromarcia`
- fast_default   `Disabilita l'assistenza alla retromarcia.`
- fast_llm       `Disabilita l'assistenza alla retromarcia.`
- fast_mai       `Disabilita l'assistenza alla retromarcia.`
- realtime       `Si svilita l'assistenza alla retromarcia?`
- realtime_refine `Disabilita l'assistenza alla retromarcia.`

### it-IT_DT1/1l_it-IT_male-DT1/Minimizza la luminosità del display centrale.wav [▶](audio/it-IT_DT1/1l_it-IT_male-DT1/Minimizza%20la%20luminosit%C3%A0%20del%20display%20centrale.wav.wav)  Δwer=0.333  (fast_default=0.000, realtime=0.333)  speech=[1.27s, 3.51s] fix=trim_last
- ref:           `Minimizza la luminosità del display centrale`
- fast_default   `Minimizza la luminosità del display centrale.`
- fast_llm       `Minimizza la luminosità del display centrale.`
- fast_mai       `Minimizza la luminosità del display centrale.`
- realtime       `Minimizza la luminosità del display in centro.`
- realtime_refine `Minimizza la luminosità del display centrale.`

### it-IT_DT2/1l_it-IT_male-DT2/Metti la modalità di frenata a Standard.wav [▶](audio/it-IT_DT2/1l_it-IT_male-DT2/Metti%20la%20modalit%C3%A0%20di%20frenata%20a%20Standard.wav.wav)  Δwer=0.286  (fast_default=0.000, realtime=0.286)  speech=[1.35s, 3.43s] fix=none
- ref:           `Metti la modalità di frenata a Standard`
- fast_default   `Metti la modalità di frenata a standard.`
- fast_llm       `Metti la modalità di frenata a standard.`
- fast_mai       `Metti la modalità di frenata a standard.`
- realtime       `Metti la modalità di frenata starter.`
- realtime_refine `Metti la modalità di frenata a standard.`

### it-IT_JT1/1l_it-IT_male-JT1/Attiva telecamera 360 gradi.wav [▶](audio/it-IT_JT1/1l_it-IT_male-JT1/Attiva%20telecamera%20360%20gradi.wav.wav)  Δwer=0.250  (fast_default=0.500, realtime=0.250)  speech=[1.24s, 3.96s] fix=none
- ref:           `Attiva telecamera 360 gradi`
- fast_default   `Attiva telecamera a 360°.`
- fast_llm       `Attiva telecamera a 360°.`
- fast_mai       `Attiva telecamera a 360 gradi.`
- realtime       `Attiva telecamera 360 °.`
- realtime_refine `Attiva telecamera a 360 °.`

### it-IT_DT1/1l_it-IT_male-DT1/Attiva telecamera 360 gradi.wav [▶](audio/it-IT_DT1/1l_it-IT_male-DT1/Attiva%20telecamera%20360%20gradi.wav.wav)  Δwer=0.250  (fast_default=0.500, realtime=0.250)  speech=[1.25s, 3.96s] fix=none
- ref:           `Attiva telecamera 360 gradi`
- fast_default   `Attiva telecamera a 360 °.`
- fast_llm       `Attiva telecamera a 360°.`
- fast_mai       `Attiva telecamera a 360 gradi.`
- realtime       `Attiva telecamera 360 °.`
- realtime_refine `Attiva telecamera a 360 °.`

### it-IT_DT1/1l_it-IT_female-DT1/Abilità luminosità schermo automatica.wav [▶](audio/it-IT_DT1/1l_it-IT_female-DT1/Abilit%C3%A0%20luminosit%C3%A0%20schermo%20automatica.wav.wav)  Δwer=0.250  (fast_default=0.250, realtime=0.000)  speech=[2.47s, 4.87s] fix=trim_first
- ref:           `Abilità luminosità schermo automatica`
- fast_default   `Abilita luminosità schermo automatica.`
- fast_llm       `Abilità luminosità schermo automatica.`
- fast_mai       `Abilita Luminosità schermo automatica.`
- realtime       `Abilità, luminosità, schermo automatica.`
- realtime_refine `Abilita luminosità schermo automatica.`

### it-IT_DT2/1l_it-IT_male-DT2/Disattiva Apple Carplay per il passeggero.wav [▶](audio/it-IT_DT2/1l_it-IT_male-DT2/Disattiva%20Apple%20Carplay%20per%20il%20passeggero.wav.wav)  Δwer=0.167  (fast_default=0.500, realtime=0.667)  speech=[2.01s, 3.25s] fix=trim_both
- ref:           `Disattiva Apple Carplay per il passeggero`
- fast_default   `Disattiva Apple card per i passeggeri.`
- fast_llm       `Da viva e orgogliosa in passeggiata.`
- fast_mai       `Cattiva Apple CarPlay per i passeggeri`
- realtime       `Tentativa Apple card per i passeggeri.`
- realtime_refine `Disattiva Apple Card per i passeggeri.`

### it-IT_JT1/1l_it-IT_female-JT1/Apri il finestrino posteriore destro  a metà.wav [▶](audio/it-IT_JT1/1l_it-IT_female-JT1/Apri%20il%20finestrino%20posteriore%20destro%C2%A0%20a%20met%C3%A0.wav.wav)  Δwer=0.143  (fast_default=0.143, realtime=0.000)  speech=[1.29s, 4.89s] fix=none
- ref:           `Apri il finestrino posteriore destro  a metà`
- fast_default   `Aprì il finestrino posteriore destro a metà.`
- fast_llm       `Apri il finestrino posteriore destro a metà.`
- fast_mai       `Apri il finestrino posteriore destro a metà.`
- realtime       `Apri il finestrino posteriore destro a metà.`
- realtime_refine `Aprì il finestrino posteriore destro a metà.`

## Caveats

- **UPL is anchored on the realtime SDK's word-end timestamp** for each sample, so all services use the same `speech_end`. The CSV's `upl_self_ms` column has each service's own phrase-derived value if you want to see how its boundary detection differs.
- **Mazda voice commands** are short utterances (typically 2-8 words). WER on short references is noisier — a single word error on a 3-word command gives 33% WER.
- The 'all-agree-vs-ref' filter is conservative (pairwise WER < 0.15 AND mean ref WER > 0.5). True mislabels with partial agreement still survive and inflate per-service WER equally.