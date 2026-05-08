# Error analysis — mazda_fr-FR_20260508_131357.csv

Filters out samples that look like *data* problems rather than recognition errors:
1. **Empty hypothesis** — at least one service returned no text.
2. **Reference much shorter than audio** — `words_per_s < 0.3` (with `duration ≥ 1 s`). At normal speech rates this means the label is missing content.
3. **All services agree, ref disagrees** — mean pairwise WER between hypotheses < 0.15 AND mean WER vs ref > 0.5. Multiple ASR systems converging on the same answer that differs from the reference is a strong signal of a mislabeled ground truth, not a shared error.
4. **Compound-word / segmentation artifact** — all services produce text identical to the reference after removing spaces (e.g. `stummschalten` vs `stumm schalten`). These are correct recognitions scored as errors due to tokenization.

Audio links (▶) point to `results/audio/<dataset>/<sample_id>.wav` so a reviewer can play the clip directly.

## Datasets under test

- **fr-FR_DT1** — Mazda fr-FR DT1 voice commands (male + female pooled)
- **fr-FR_DT2** — Mazda fr-FR DT2 voice commands (male + female pooled)
- **fr-FR_JT1** — Mazda fr-FR JT1 voice commands (male + female pooled)

Total complete samples: **90**  
Kept after filtering: **89**  
Excluded as data issues: **1**  

- Empty hypothesis: 1
- Reference too short for audio: 0
- All services agree, ref disagrees: 0
- Compound-word / segmentation artifact: 0

## Speech boundaries

`speech_start_s` / `speech_end_s` come from the realtime SDK's word-level timestamps and anchor UPL for all services. Per-word detail lives in the sidecar `mazda_fr-FR_20260508_131357_words.jsonl`.

Boundary-fix actions across 90 realtime samples: `skip`=4, `trim_both`=14, `trim_first`=2, `trim_last`=6

## Filtered results (excludes data issues)

INS/DEL/SUB are *rates per 100 reference words*. Their sum ≈ WER × 100.

| Dataset | Service | N | WER | SER | INS/100 | DEL/100 | SUB/100 | LBL ms (mean / p90) | UPL ms (mean / p90) |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| fr-FR_DT1 | fast_default | 29 | 0.109 | 0.379 | 0.0 | 2.9 | 7.6 | 639 / 697 | 1239 / 1287 |
| fr-FR_DT1 | fast_llm | 29 | 0.159 | 0.345 | 1.2 | 1.2 | 12.2 | 504 / 556 | 1100 / 1137 |
| fr-FR_DT1 | fast_mai | 29 | 0.083 | 0.379 | 0.6 | 0.6 | 7.6 | 494 / 557 | 1019 / 1124 |
| fr-FR_DT1 | realtime | 29 | 0.148 | 0.448 | 1.2 | 0.6 | 13.4 | -1602 / -1098 | 769 / 921 |
| fr-FR_DT1 | realtime_refine | 29 | 0.088 | 0.310 | 1.2 | 0.6 | 8.1 | -1168 / -635 | 1193 / 1330 |
| fr-FR_DT2 | fast_default | 30 | 0.130 | 0.400 | 0.0 | 6.2 | 7.3 | 620 / 689 | 1229 / 1240 |
| fr-FR_DT2 | fast_llm | 30 | 0.204 | 0.433 | 4.0 | 5.6 | 12.4 | 503 / 561 | 1108 / 1129 |
| fr-FR_DT2 | fast_mai | 30 | 0.149 | 0.400 | 4.0 | 2.3 | 12.4 | 483 / 505 | 1016 / 1096 |
| fr-FR_DT2 | realtime | 30 | 0.157 | 0.467 | 0.0 | 3.4 | 12.4 | -1638 / -1103 | 779 / 1003 |
| fr-FR_DT2 | realtime_refine | 30 | 0.099 | 0.367 | 0.0 | 2.3 | 7.9 | -1195 / -658 | 1225 / 1503 |
| fr-FR_JT1 | fast_default | 30 | 0.090 | 0.333 | 0.0 | 1.7 | 7.9 | 613 / 642 | 1207 / 1229 |
| fr-FR_JT1 | fast_llm | 30 | 0.060 | 0.267 | 0.0 | 1.1 | 5.6 | 496 / 558 | 1092 / 1127 |
| fr-FR_JT1 | fast_mai | 30 | 0.058 | 0.300 | 0.0 | 0.0 | 6.8 | 525 / 653 | 1049 / 1174 |
| fr-FR_JT1 | realtime | 30 | 0.082 | 0.300 | 0.0 | 1.1 | 7.9 | -1642 / -1117 | 694 / 860 |
| fr-FR_JT1 | realtime_refine | 30 | 0.085 | 0.333 | 0.0 | 1.7 | 6.8 | -1218 / -721 | 1128 / 1275 |

## Unfiltered results (all complete samples, for reference)

| Dataset | Service | N | WER | SER | INS/100 | DEL/100 | SUB/100 |
|---|---|---:|---:|---:|---:|---:|---:|
| fr-FR_DT1 | fast_default | 30 | 0.132 | 0.400 | 0.0 | 5.1 | 7.3 |
| fr-FR_DT1 | fast_llm | 30 | 0.180 | 0.367 | 1.1 | 3.4 | 11.9 |
| fr-FR_DT1 | fast_mai | 30 | 0.113 | 0.400 | 1.7 | 0.6 | 9.6 |
| fr-FR_DT1 | realtime | 30 | 0.177 | 0.467 | 1.1 | 3.4 | 13.0 |
| fr-FR_DT1 | realtime_refine | 30 | 0.098 | 0.333 | 1.1 | 1.1 | 8.5 |
| fr-FR_DT2 | fast_default | 30 | 0.130 | 0.400 | 0.0 | 6.2 | 7.3 |
| fr-FR_DT2 | fast_llm | 30 | 0.204 | 0.433 | 4.0 | 5.6 | 12.4 |
| fr-FR_DT2 | fast_mai | 30 | 0.149 | 0.400 | 4.0 | 2.3 | 12.4 |
| fr-FR_DT2 | realtime | 30 | 0.157 | 0.467 | 0.0 | 3.4 | 12.4 |
| fr-FR_DT2 | realtime_refine | 30 | 0.099 | 0.367 | 0.0 | 2.3 | 7.9 |
| fr-FR_JT1 | fast_default | 30 | 0.090 | 0.333 | 0.0 | 1.7 | 7.9 |
| fr-FR_JT1 | fast_llm | 30 | 0.060 | 0.267 | 0.0 | 1.1 | 5.6 |
| fr-FR_JT1 | fast_mai | 30 | 0.058 | 0.300 | 0.0 | 0.0 | 6.8 |
| fr-FR_JT1 | realtime | 30 | 0.082 | 0.300 | 0.0 | 1.1 | 7.9 |
| fr-FR_JT1 | realtime_refine | 30 | 0.085 | 0.333 | 0.0 | 1.7 | 6.8 |

## Excluded samples — examples

### Empty hypothesis

| Audio | Dataset | Sample | Empty in | Reference |
|---|---|---|---|---|
| [▶](audio/fr-FR_DT1/1l_fr-FR_male-DT1/Va%20%C3%A0%20la%20page%20suivante.wav.wav) | fr-FR_DT1 | 1l_fr-FR_male-DT1/Va à la page suivante.wav | realtime | `Va à la page suivante` |

### Reference too short for audio duration

_(none)_

### All services agree, reference disagrees (likely mislabeled)

_(none)_

### Compound-word / segmentation artifacts

_(none)_

## Genuine recognition errors (filtered set)

Best / median / worst WER per (dataset, service) on the kept samples.

### fr-FR_DT1 / fast_default  (n=29)
**BEST** — `1l_fr-FR_female-DT1/Active la fermeture automatique des vitres à la fermeture du véhicule.wav` [▶](audio/fr-FR_DT1/1l_fr-FR_female-DT1/Active%20la%20fermeture%20automatique%20des%20vitres%20%C3%A0%20la%20fermeture%20du%20v%C3%A9hicule.wav.wav)  wer=0.000  speech=[2.04s, 6.52s]  fix=none
- ref: `Active la fermeture automatique des vitres à la fermeture du véhicule`
- hyp: `Active la fermeture automatique des vitres à la fermeture du véhicule.`
**MEDIAN** — `1l_fr-FR_male-DT1/Désactive la ventilation du siège conducteur.wav` [▶](audio/fr-FR_DT1/1l_fr-FR_male-DT1/D%C3%A9sactive%20la%20ventilation%20du%20si%C3%A8ge%20conducteur.wav.wav)  wer=0.000  speech=[3.17s, 5.85s]  fix=none
- ref: `Désactive la ventilation du siège conducteur`
- hyp: `Désactive la ventilation du siège conducteur.`
**WORST** — `1l_fr-FR_male-DT1/Ajoute Starbucks comme étape.wav` [▶](audio/fr-FR_DT1/1l_fr-FR_male-DT1/Ajoute%20Starbucks%20comme%20%C3%A9tape.wav.wav)  wer=0.750  speech=[3.29s, 5.61s]  fix=none
- ref: `Ajoute Starbucks comme étape`
- hyp: `Starbucks.`

### fr-FR_DT1 / fast_llm  (n=29)
**BEST** — `1l_fr-FR_male-DT1/Régle le volume de la navigation sur 5.wav` [▶](audio/fr-FR_DT1/1l_fr-FR_male-DT1/R%C3%A9gle%20le%20volume%20de%20la%20navigation%20sur%205.wav.wav)  wer=0.000  speech=[2.86s, 5.34s]  fix=none
- ref: `Régle le volume de la navigation sur 5`
- hyp: `Régle le volume de la navigation sur 5.`
**MEDIAN** — `1l_fr-FR_male-DT1/Ferme légèrement la vitre arrière gauche.wav` [▶](audio/fr-FR_DT1/1l_fr-FR_male-DT1/Ferme%20l%C3%A9g%C3%A8rement%20la%20vitre%20arri%C3%A8re%20gauche.wav.wav)  wer=0.000  speech=[-s, -s]  fix=skip
- ref: `Ferme légèrement la vitre arrière gauche`
- hyp: `Ferme légèrement la vitre arrière gauche.`
**WORST** — `1l_fr-FR_male-DT1/Ajoute Starbucks comme étape.wav` [▶](audio/fr-FR_DT1/1l_fr-FR_male-DT1/Ajoute%20Starbucks%20comme%20%C3%A9tape.wav.wav)  wer=1.000  speech=[3.29s, 5.61s]  fix=none
- ref: `Ajoute Starbucks comme étape`
- hyp: `I would start mix.`

### fr-FR_DT1 / fast_mai  (n=29)
**BEST** — `1l_fr-FR_female-DT1/Active la fermeture automatique des vitres à la fermeture du véhicule.wav` [▶](audio/fr-FR_DT1/1l_fr-FR_female-DT1/Active%20la%20fermeture%20automatique%20des%20vitres%20%C3%A0%20la%20fermeture%20du%20v%C3%A9hicule.wav.wav)  wer=0.000  speech=[2.04s, 6.52s]  fix=none
- ref: `Active la fermeture automatique des vitres à la fermeture du véhicule`
- hyp: `Active la fermeture automatique des vitres à la fermeture du véhicule.`
**MEDIAN** — `1l_fr-FR_male-DT1/Ouvre le centre multimédia local.wav` [▶](audio/fr-FR_DT1/1l_fr-FR_male-DT1/Ouvre%20le%20centre%20multim%C3%A9dia%20local.wav.wav)  wer=0.000  speech=[3.54s, 6.1s]  fix=none
- ref: `Ouvre le centre multimédia local`
- hyp: `Ouvre le centre multimédia local.`
**WORST** — `1l_fr-FR_male-DT1/Ferme la vitre arrière droite.wav` [▶](audio/fr-FR_DT1/1l_fr-FR_male-DT1/Ferme%20la%20vitre%20arri%C3%A8re%20droite.wav.wav)  wer=0.400  speech=[3.46s, 5.38s]  fix=none
- ref: `Ferme la vitre arrière droite`
- hyp: `La ferme, la douce arrière droite.`

### fr-FR_DT1 / realtime  (n=29)
**BEST** — `1l_fr-FR_female-DT1/Active la fermeture automatique des vitres à la fermeture du véhicule.wav` [▶](audio/fr-FR_DT1/1l_fr-FR_female-DT1/Active%20la%20fermeture%20automatique%20des%20vitres%20%C3%A0%20la%20fermeture%20du%20v%C3%A9hicule.wav.wav)  wer=0.000  speech=[2.04s, 6.52s]  fix=none
- ref: `Active la fermeture automatique des vitres à la fermeture du véhicule`
- hyp: `Active la fermeture automatique des vitres à la fermeture du véhicule.`
**MEDIAN** — `1l_fr-FR_female-DT1/Monte la sonnerie.wav` [▶](audio/fr-FR_DT1/1l_fr-FR_female-DT1/Monte%20la%20sonnerie.wav.wav)  wer=0.000  speech=[2.16s, 3.36s]  fix=none
- ref: `Monte la sonnerie`
- hyp: `Monte la sonnerie.`
**WORST** — `1l_fr-FR_male-DT1/Régle l’avant au minimum de température.wav` [▶](audio/fr-FR_DT1/1l_fr-FR_male-DT1/R%C3%A9gle%20l%E2%80%99avant%20au%20minimum%20de%20temp%C3%A9rature.wav.wav)  wer=0.571  speech=[3.22s, 4.5s]  fix=trim_both
- ref: `Régle l’avant au minimum de température`
- hyp: `Règle l'avant au maximum des températures.`

### fr-FR_DT1 / realtime_refine  (n=29)
**BEST** — `1l_fr-FR_female-DT1/Active la fermeture automatique des vitres à la fermeture du véhicule.wav` [▶](audio/fr-FR_DT1/1l_fr-FR_female-DT1/Active%20la%20fermeture%20automatique%20des%20vitres%20%C3%A0%20la%20fermeture%20du%20v%C3%A9hicule.wav.wav)  wer=0.000  speech=[2.04s, 6.52s]  fix=none
- ref: `Active la fermeture automatique des vitres à la fermeture du véhicule`
- hyp: `Active la fermeture automatique des vitres à la fermeture du véhicule.`
**MEDIAN** — `1l_fr-FR_female-DT1/Désactive le mode muet.wav` [▶](audio/fr-FR_DT1/1l_fr-FR_female-DT1/D%C3%A9sactive%20le%20mode%20muet.wav.wav)  wer=0.000  speech=[1.96s, 3.72s]  fix=none
- ref: `Désactive le mode muet`
- hyp: `Désactive le mode muet.`
**WORST** — `1l_fr-FR_male-DT1/Régle l’avant au minimum de température.wav` [▶](audio/fr-FR_DT1/1l_fr-FR_male-DT1/R%C3%A9gle%20l%E2%80%99avant%20au%20minimum%20de%20temp%C3%A9rature.wav.wav)  wer=0.571  speech=[3.22s, 4.5s]  fix=trim_both
- ref: `Régle l’avant au minimum de température`
- hyp: `Règle l'avant au maximum des températures.`

### fr-FR_DT2 / fast_default  (n=30)
**BEST** — `1l_fr-FR_female-DT2/Active la fermeture automatique des vitres à la fermeture du véhicule.wav` [▶](audio/fr-FR_DT2/1l_fr-FR_female-DT2/Active%20la%20fermeture%20automatique%20des%20vitres%20%C3%A0%20la%20fermeture%20du%20v%C3%A9hicule.wav.wav)  wer=0.000  speech=[2.04s, 6.4s]  fix=none
- ref: `Active la fermeture automatique des vitres à la fermeture du véhicule`
- hyp: `Active la fermeture automatique des vitres à la fermeture du véhicule.`
**MEDIAN** — `1l_fr-FR_male-DT2/Ouvre le centre multimédia local.wav` [▶](audio/fr-FR_DT2/1l_fr-FR_male-DT2/Ouvre%20le%20centre%20multim%C3%A9dia%20local.wav.wav)  wer=0.000  speech=[3.54s, 6.14s]  fix=none
- ref: `Ouvre le centre multimédia local`
- hyp: `Ouvre le centre multimédia local.`
**WORST** — `1l_fr-FR_male-DT2/Régle le chauffage du siège passager au minimum.wav` [▶](audio/fr-FR_DT2/1l_fr-FR_male-DT2/R%C3%A9gle%20le%20chauffage%20du%20si%C3%A8ge%20passager%20au%20minimum.wav.wav)  wer=0.625  speech=[2.84s, 4.92s]  fix=trim_both
- ref: `Régle le chauffage du siège passager au minimum`
- hyp: `Le cheval du ciel, passager.`

### fr-FR_DT2 / fast_llm  (n=30)
**BEST** — `1l_fr-FR_female-DT2/Active la fermeture automatique des vitres à la fermeture du véhicule.wav` [▶](audio/fr-FR_DT2/1l_fr-FR_female-DT2/Active%20la%20fermeture%20automatique%20des%20vitres%20%C3%A0%20la%20fermeture%20du%20v%C3%A9hicule.wav.wav)  wer=0.000  speech=[2.04s, 6.4s]  fix=none
- ref: `Active la fermeture automatique des vitres à la fermeture du véhicule`
- hyp: `Active la fermeture automatique des vitres à la fermeture du véhicule.`
**MEDIAN** — `1l_fr-FR_male-DT2/Ouvre le centre multimédia local.wav` [▶](audio/fr-FR_DT2/1l_fr-FR_male-DT2/Ouvre%20le%20centre%20multim%C3%A9dia%20local.wav.wav)  wer=0.000  speech=[3.54s, 6.14s]  fix=none
- ref: `Ouvre le centre multimédia local`
- hyp: `Ouvre le centre multimédia local.`
**WORST** — `1l_fr-FR_male-DT2/Ferme la vitre arrière droite.wav` [▶](audio/fr-FR_DT2/1l_fr-FR_male-DT2/Ferme%20la%20vitre%20arri%C3%A8re%20droite.wav.wav)  wer=2.000  speech=[4.22s, 5.34s]  fix=trim_first
- ref: `Ferme la vitre arrière droite`
- hyp: `The film is a remake of the 1992 Malayalam film.`

### fr-FR_DT2 / fast_mai  (n=30)
**BEST** — `1l_fr-FR_female-DT2/Coupe la climatisation pour l’avant.wav` [▶](audio/fr-FR_DT2/1l_fr-FR_female-DT2/Coupe%20la%20climatisation%20pour%20l%E2%80%99avant.wav.wav)  wer=0.000  speech=[3.18s, 4.74s]  fix=trim_last
- ref: `Coupe la climatisation pour l’avant`
- hyp: `Coupe la climatisation pour l'avant.`
**MEDIAN** — `1l_fr-FR_male-DT2/Ouvre le centre multimédia local.wav` [▶](audio/fr-FR_DT2/1l_fr-FR_male-DT2/Ouvre%20le%20centre%20multim%C3%A9dia%20local.wav.wav)  wer=0.000  speech=[3.54s, 6.14s]  fix=none
- ref: `Ouvre le centre multimédia local`
- hyp: `Ouvre le centre multimédia local.`
**WORST** — `1l_fr-FR_male-DT2/Ferme la vitre arrière droite.wav` [▶](audio/fr-FR_DT2/1l_fr-FR_male-DT2/Ferme%20la%20vitre%20arri%C3%A8re%20droite.wav.wav)  wer=2.200  speech=[4.22s, 5.34s]  fix=trim_first
- ref: `Ferme la vitre arrière droite`
- hyp: `Pour l'atomes, leur but est de parier à 2 lots.`

### fr-FR_DT2 / realtime  (n=30)
**BEST** — `1l_fr-FR_female-DT2/Active la fermeture automatique des vitres à la fermeture du véhicule.wav` [▶](audio/fr-FR_DT2/1l_fr-FR_female-DT2/Active%20la%20fermeture%20automatique%20des%20vitres%20%C3%A0%20la%20fermeture%20du%20v%C3%A9hicule.wav.wav)  wer=0.000  speech=[2.04s, 6.4s]  fix=none
- ref: `Active la fermeture automatique des vitres à la fermeture du véhicule`
- hyp: `Active la fermeture automatique des vitres à la fermeture du véhicule.`
**MEDIAN** — `1l_fr-FR_female-DT2/Monte la sonnerie.wav` [▶](audio/fr-FR_DT2/1l_fr-FR_female-DT2/Monte%20la%20sonnerie.wav.wav)  wer=0.000  speech=[2.16s, 3.36s]  fix=none
- ref: `Monte la sonnerie`
- hyp: `Monte la sonnerie.`
**WORST** — `1l_fr-FR_male-DT2/Ferme la vitre arrière droite.wav` [▶](audio/fr-FR_DT2/1l_fr-FR_male-DT2/Ferme%20la%20vitre%20arri%C3%A8re%20droite.wav.wav)  wer=0.600  speech=[4.22s, 5.34s]  fix=trim_first
- ref: `Ferme la vitre arrière droite`
- hyp: `Terme, arbitre arrière droite.`

### fr-FR_DT2 / realtime_refine  (n=30)
**BEST** — `1l_fr-FR_female-DT2/Active la fermeture automatique des vitres à la fermeture du véhicule.wav` [▶](audio/fr-FR_DT2/1l_fr-FR_female-DT2/Active%20la%20fermeture%20automatique%20des%20vitres%20%C3%A0%20la%20fermeture%20du%20v%C3%A9hicule.wav.wav)  wer=0.000  speech=[2.04s, 6.4s]  fix=none
- ref: `Active la fermeture automatique des vitres à la fermeture du véhicule`
- hyp: `Active la fermeture automatique des vitres à la fermeture du véhicule.`
**MEDIAN** — `1l_fr-FR_female-DT2/Désactive le mode muet.wav` [▶](audio/fr-FR_DT2/1l_fr-FR_female-DT2/D%C3%A9sactive%20le%20mode%20muet.wav.wav)  wer=0.000  speech=[1.93s, 3.65s]  fix=none
- ref: `Désactive le mode muet`
- hyp: `Désactive le mode muet.`
**WORST** — `1l_fr-FR_male-DT2/Régle le chauffage du siège passager au minimum.wav` [▶](audio/fr-FR_DT2/1l_fr-FR_male-DT2/R%C3%A9gle%20le%20chauffage%20du%20si%C3%A8ge%20passager%20au%20minimum.wav.wav)  wer=0.500  speech=[2.84s, 4.92s]  fix=trim_both
- ref: `Régle le chauffage du siège passager au minimum`
- hyp: `Règle le cheval du ciel passager au maximum.`

### fr-FR_JT1 / fast_default  (n=30)
**BEST** — `1l_fr-FR_female-JT1/Active la fermeture automatique des vitres à la fermeture du véhicule.wav` [▶](audio/fr-FR_JT1/1l_fr-FR_female-JT1/Active%20la%20fermeture%20automatique%20des%20vitres%20%C3%A0%20la%20fermeture%20du%20v%C3%A9hicule.wav.wav)  wer=0.000  speech=[2.01s, 6.37s]  fix=none
- ref: `Active la fermeture automatique des vitres à la fermeture du véhicule`
- hyp: `Active la fermeture automatique des vitres à la fermeture du véhicule.`
**MEDIAN** — `1l_fr-FR_female-JT1/Désactive le mode muet.wav` [▶](audio/fr-FR_JT1/1l_fr-FR_female-JT1/D%C3%A9sactive%20le%20mode%20muet.wav.wav)  wer=0.000  speech=[1.95s, 3.71s]  fix=none
- ref: `Désactive le mode muet`
- hyp: `Désactive le mode muet.`
**WORST** — `1l_fr-FR_male-JT1/Régle l’avant au minimum de température.wav` [▶](audio/fr-FR_JT1/1l_fr-FR_male-JT1/R%C3%A9gle%20l%E2%80%99avant%20au%20minimum%20de%20temp%C3%A9rature.wav.wav)  wer=0.571  speech=[3.18s, 4.5s]  fix=trim_both
- ref: `Régle l’avant au minimum de température`
- hyp: `Règle l'avant au maximum des températures.`

### fr-FR_JT1 / fast_llm  (n=30)
**BEST** — `1l_fr-FR_female-JT1/Active la fermeture automatique des vitres à la fermeture du véhicule.wav` [▶](audio/fr-FR_JT1/1l_fr-FR_female-JT1/Active%20la%20fermeture%20automatique%20des%20vitres%20%C3%A0%20la%20fermeture%20du%20v%C3%A9hicule.wav.wav)  wer=0.000  speech=[2.01s, 6.37s]  fix=none
- ref: `Active la fermeture automatique des vitres à la fermeture du véhicule`
- hyp: `Active la fermeture automatique des vitres à la fermeture du véhicule.`
**MEDIAN** — `1l_fr-FR_male-JT1/Ferme légèrement la vitre arrière gauche.wav` [▶](audio/fr-FR_JT1/1l_fr-FR_male-JT1/Ferme%20l%C3%A9g%C3%A8rement%20la%20vitre%20arri%C3%A8re%20gauche.wav.wav)  wer=0.000  speech=[-s, -s]  fix=skip
- ref: `Ferme légèrement la vitre arrière gauche`
- hyp: `Ferme légèrement la vitre arrière gauche.`
**WORST** — `1l_fr-FR_female-JT1/Passe en mode annonces concises.wav` [▶](audio/fr-FR_JT1/1l_fr-FR_female-JT1/Passe%20en%20mode%20annonces%20concises.wav.wav)  wer=0.400  speech=[2.7s, 4.86s]  fix=none
- ref: `Passe en mode annonces concises`
- hyp: `Passe en mode annonce concise.`

### fr-FR_JT1 / fast_mai  (n=30)
**BEST** — `1l_fr-FR_female-JT1/Coupe la climatisation pour l’avant.wav` [▶](audio/fr-FR_JT1/1l_fr-FR_female-JT1/Coupe%20la%20climatisation%20pour%20l%E2%80%99avant.wav.wav)  wer=0.000  speech=[3.18s, 4.74s]  fix=trim_last
- ref: `Coupe la climatisation pour l’avant`
- hyp: `Coupe la climatisation pour l'avant.`
**MEDIAN** — `1l_fr-FR_female-JT1/Désactive le mode muet.wav` [▶](audio/fr-FR_JT1/1l_fr-FR_female-JT1/D%C3%A9sactive%20le%20mode%20muet.wav.wav)  wer=0.000  speech=[1.95s, 3.71s]  fix=none
- ref: `Désactive le mode muet`
- hyp: `Désactive le mode muet.`
**WORST** — `1l_fr-FR_female-JT1/Passe en mode annonces concises.wav` [▶](audio/fr-FR_JT1/1l_fr-FR_female-JT1/Passe%20en%20mode%20annonces%20concises.wav.wav)  wer=0.400  speech=[2.7s, 4.86s]  fix=none
- ref: `Passe en mode annonces concises`
- hyp: `Passe en mode annonce concise.`

### fr-FR_JT1 / realtime  (n=30)
**BEST** — `1l_fr-FR_female-JT1/Active la fermeture automatique des vitres à la fermeture du véhicule.wav` [▶](audio/fr-FR_JT1/1l_fr-FR_female-JT1/Active%20la%20fermeture%20automatique%20des%20vitres%20%C3%A0%20la%20fermeture%20du%20v%C3%A9hicule.wav.wav)  wer=0.000  speech=[2.01s, 6.37s]  fix=none
- ref: `Active la fermeture automatique des vitres à la fermeture du véhicule`
- hyp: `Active la fermeture automatique des vitres à la fermeture du véhicule.`
**MEDIAN** — `1l_fr-FR_male-JT1/Ferme légèrement la vitre arrière gauche.wav` [▶](audio/fr-FR_JT1/1l_fr-FR_male-JT1/Ferme%20l%C3%A9g%C3%A8rement%20la%20vitre%20arri%C3%A8re%20gauche.wav.wav)  wer=0.000  speech=[-s, -s]  fix=skip
- ref: `Ferme légèrement la vitre arrière gauche`
- hyp: `Ferme légèrement la vitre arrière gauche.`
**WORST** — `1l_fr-FR_male-JT1/Régle l’avant au minimum de température.wav` [▶](audio/fr-FR_JT1/1l_fr-FR_male-JT1/R%C3%A9gle%20l%E2%80%99avant%20au%20minimum%20de%20temp%C3%A9rature.wav.wav)  wer=0.571  speech=[3.18s, 4.5s]  fix=trim_both
- ref: `Régle l’avant au minimum de température`
- hyp: `Règle l'avant au maximum des températures.`

### fr-FR_JT1 / realtime_refine  (n=30)
**BEST** — `1l_fr-FR_female-JT1/Active la fermeture automatique des vitres à la fermeture du véhicule.wav` [▶](audio/fr-FR_JT1/1l_fr-FR_female-JT1/Active%20la%20fermeture%20automatique%20des%20vitres%20%C3%A0%20la%20fermeture%20du%20v%C3%A9hicule.wav.wav)  wer=0.000  speech=[2.01s, 6.37s]  fix=none
- ref: `Active la fermeture automatique des vitres à la fermeture du véhicule`
- hyp: `Active la fermeture automatique des vitres à la fermeture du véhicule.`
**MEDIAN** — `1l_fr-FR_male-JT1/Ferme légèrement la vitre arrière gauche.wav` [▶](audio/fr-FR_JT1/1l_fr-FR_male-JT1/Ferme%20l%C3%A9g%C3%A8rement%20la%20vitre%20arri%C3%A8re%20gauche.wav.wav)  wer=0.000  speech=[-s, -s]  fix=skip
- ref: `Ferme légèrement la vitre arrière gauche`
- hyp: `Ferme légèrement la vitre arrière gauche.`
**WORST** — `1l_fr-FR_male-JT1/Ajoute Starbucks comme étape.wav` [▶](audio/fr-FR_JT1/1l_fr-FR_male-JT1/Ajoute%20Starbucks%20comme%20%C3%A9tape.wav.wav)  wer=0.500  speech=[3.27s, 5.59s]  fix=none
- ref: `Ajoute Starbucks comme étape`
- hyp: `Ajoute Starbucks Computer.`

## Top fast_default vs realtime disagreements (filtered)

### fr-FR_JT1/1l_fr-FR_male-JT1/Ajoute Starbucks comme étape.wav [▶](audio/fr-FR_JT1/1l_fr-FR_male-JT1/Ajoute%20Starbucks%20comme%20%C3%A9tape.wav.wav)  Δwer=0.500  (fast_default=0.500, realtime=0.000)  speech=[3.27s, 5.59s] fix=none
- ref:           `Ajoute Starbucks comme étape`
- fast_default   `Ajoute Starbucks Computer.`
- fast_llm       `Ajoute Starbucks comme étape.`
- fast_mai       `Ajoute Starbucks comme étape.`
- realtime       `Ajoute Starbucks comme étape.`
- realtime_refine `Ajoute Starbucks Computer.`

### fr-FR_DT2/1l_fr-FR_male-DT2/Coupe la climatisation pour l’avant.wav [▶](audio/fr-FR_DT2/1l_fr-FR_male-DT2/Coupe%20la%20climatisation%20pour%20l%E2%80%99avant.wav.wav)  Δwer=0.500  (fast_default=0.000, realtime=0.500)  speech=[3.18s, 4.66s] fix=trim_last
- ref:           `Coupe la climatisation pour l’avant`
- fast_default   `Coupe la climatisation pour l'avant.`
- fast_llm       `La climatisation pour la vente.`
- fast_mai       `Coupe la climatisation pour l'avant.`
- realtime       `Pour la climatisation, pour la vente.`
- realtime_refine `Coupe la climatisation pour l'avant.`

### fr-FR_DT1/1l_fr-FR_male-DT1/Ajoute Starbucks comme étape.wav [▶](audio/fr-FR_DT1/1l_fr-FR_male-DT1/Ajoute%20Starbucks%20comme%20%C3%A9tape.wav.wav)  Δwer=0.500  (fast_default=0.750, realtime=0.250)  speech=[3.29s, 5.61s] fix=none
- ref:           `Ajoute Starbucks comme étape`
- fast_default   `Starbucks.`
- fast_llm       `I would start mix.`
- fast_mai       `Ajoute Starbucks comme étape.`
- realtime       `Ajoute Starbucks comme portable.`
- realtime_refine `Ajoute Starbucks comme étape.`

### fr-FR_DT1/1l_fr-FR_male-DT1/Coupe la climatisation pour l’avant.wav [▶](audio/fr-FR_DT1/1l_fr-FR_male-DT1/Coupe%20la%20climatisation%20pour%20l%E2%80%99avant.wav.wav)  Δwer=0.333  (fast_default=0.167, realtime=0.500)  speech=[3.22s, 4.66s] fix=trim_last
- ref:           `Coupe la climatisation pour l’avant`
- fast_default   `Pour la climatisation pour l'avant.`
- fast_llm       `Pour la climatisation, pour l'avant.`
- fast_mai       `Coupe la climatisation pour l'avant.`
- realtime       `Pour la climatisation, pour la vente.`
- realtime_refine `Coupe la climatisation pour l'avant.`

### fr-FR_JT1/1l_fr-FR_male-JT1/Coupe la climatisation pour l’avant.wav [▶](audio/fr-FR_JT1/1l_fr-FR_male-JT1/Coupe%20la%20climatisation%20pour%20l%E2%80%99avant.wav.wav)  Δwer=0.333  (fast_default=0.000, realtime=0.333)  speech=[3.18s, 4.98s] fix=none
- ref:           `Coupe la climatisation pour l’avant`
- fast_default   `Coupe la climatisation pour l'avant.`
- fast_llm       `Coupe la climatisation pour l'avant.`
- fast_mai       `Coupe la climatisation pour l'avant.`
- realtime       `Coupe la climatisation pour la vente.`
- realtime_refine `Coupe la climatisation pour l'avant.`

### fr-FR_DT2/1l_fr-FR_male-DT2/Régle l’avant au minimum de température.wav [▶](audio/fr-FR_DT2/1l_fr-FR_male-DT2/R%C3%A9gle%20l%E2%80%99avant%20au%20minimum%20de%20temp%C3%A9rature.wav.wav)  Δwer=0.286  (fast_default=0.571, realtime=0.286)  speech=[3.18s, 4.46s] fix=trim_both
- ref:           `Régle l’avant au minimum de température`
- fast_default   `Règle l'avant au maximum des températures.`
- fast_llm       `Règle l'avant au maximum de température.`
- fast_mai       `Règle l'avant au maximum de température.`
- realtime       `Règle l'avant au maximum de température.`
- realtime_refine `Règle l'avant au maximum de température.`

### fr-FR_DT1/1l_fr-FR_male-DT1/Régle l’avant au minimum de température.wav [▶](audio/fr-FR_DT1/1l_fr-FR_male-DT1/R%C3%A9gle%20l%E2%80%99avant%20au%20minimum%20de%20temp%C3%A9rature.wav.wav)  Δwer=0.286  (fast_default=0.286, realtime=0.571)  speech=[3.22s, 4.5s] fix=trim_both
- ref:           `Régle l’avant au minimum de température`
- fast_default   `Règle l'avant au maximum de température.`
- fast_llm       `Règle l'avant au maximum des températures.`
- fast_mai       `Règle l'avant au maximum de température.`
- realtime       `Règle l'avant au maximum des températures.`
- realtime_refine `Règle l'avant au maximum des températures.`

### fr-FR_DT1/1l_fr-FR_male-DT1/Monte légèrement la hauteur de l’ATH.wav [▶](audio/fr-FR_DT1/1l_fr-FR_male-DT1/Monte%20l%C3%A9g%C3%A8rement%20la%20hauteur%20de%20l%E2%80%99ATH.wav.wav)  Δwer=0.286  (fast_default=0.143, realtime=0.429)  speech=[2.88s, 5.0s] fix=trim_both
- ref:           `Monte légèrement la hauteur de l’ATH`
- fast_default   `Montre légèrement la hauteur de l'ath.`
- fast_llm       `Montre légèrement la hauteur de l'a. th.`
- fast_mai       `Montre légèrement la hauteur de l'ATH.`
- realtime       `Montre légèrement la hauteur de la page.`
- realtime_refine `Montre légèrement la hauteur de l'ath.`

### fr-FR_DT2/1l_fr-FR_male-DT2/Active le mode refroidissement.wav [▶](audio/fr-FR_DT2/1l_fr-FR_male-DT2/Active%20le%20mode%20refroidissement.wav.wav)  Δwer=0.250  (fast_default=0.000, realtime=0.250)  speech=[3.07s, 4.99s] fix=none
- ref:           `Active le mode refroidissement`
- fast_default   `Active le mode refroidissement.`
- fast_llm       `Active le mode.`
- fast_mai       `Active le mode de prévisualisation.`
- realtime       `Active le mode refondation.`
- realtime_refine `Active le mode refroidissement.`

### fr-FR_DT1/1l_fr-FR_male-DT1/Active le mode scénario.wav [▶](audio/fr-FR_DT1/1l_fr-FR_male-DT1/Active%20le%20mode%20sc%C3%A9nario.wav.wav)  Δwer=0.250  (fast_default=0.250, realtime=0.500)  speech=[2.9s, 3.62s] fix=trim_both
- ref:           `Active le mode scénario`
- fast_default   `Le mode scénario.`
- fast_llm       `Le mode scénario.`
- fast_mai       `suivre le mode scénario.`
- realtime       `Qui va le mode scénario ?`
- realtime_refine `Active le mode scénario.`

## Caveats

- **UPL is anchored on the realtime SDK's word-end timestamp** for each sample, so all services use the same `speech_end`. The CSV's `upl_self_ms` column has each service's own phrase-derived value if you want to see how its boundary detection differs.
- **Mazda voice commands** are short utterances (typically 2-8 words). WER on short references is noisier — a single word error on a 3-word command gives 33% WER.
- The 'all-agree-vs-ref' filter is conservative (pairwise WER < 0.15 AND mean ref WER > 0.5). True mislabels with partial agreement still survive and inflate per-service WER equally.