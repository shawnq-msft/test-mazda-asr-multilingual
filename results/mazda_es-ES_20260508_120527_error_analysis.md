# Error analysis — mazda_es-ES_20260508_120527.csv

Filters out samples that look like *data* problems rather than recognition errors:
1. **Empty hypothesis** — at least one service returned no text.
2. **Reference much shorter than audio** — `words_per_s < 0.3` (with `duration ≥ 1 s`). At normal speech rates this means the label is missing content.
3. **All services agree, ref disagrees** — mean pairwise WER between hypotheses < 0.15 AND mean WER vs ref > 0.5. Multiple ASR systems converging on the same answer that differs from the reference is a strong signal of a mislabeled ground truth, not a shared error.

Audio links (▶) point to `results/audio/<dataset>/<sample_id>.wav` so a reviewer can play the clip directly.

## Datasets under test

- **es-ES_DT1** — Mazda es-ES DT1 voice commands (male + female pooled)
- **es-ES_DT2** — Mazda es-ES DT2 voice commands (male + female pooled)
- **es-ES_JT1** — Mazda es-ES JT1 voice commands (male + female pooled)

Total complete samples: **90**  
Kept after filtering: **81**  
Excluded as data issues: **9**  

- Empty hypothesis: 9
- Reference too short for audio: 0
- All services agree, ref disagrees: 0

## Speech boundaries

`speech_start_s` / `speech_end_s` come from the realtime SDK's word-level timestamps and anchor UPL for all services. Per-word detail lives in the sidecar `mazda_es-ES_20260508_120527_words.jsonl`.

Boundary-fix actions across 90 realtime samples: `skip`=12, `trim_both`=1, `trim_first`=2, `trim_last`=4

## Filtered results (excludes data issues)

INS/DEL/SUB are *rates per 100 reference words*. Their sum ≈ WER × 100.

| Dataset | Service | N | WER | SER | INS/100 | DEL/100 | SUB/100 | LBL ms (mean / p90) | UPL ms (mean / p90) |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| es-ES_DT1 | fast_default | 25 | 0.080 | 0.400 | 0.0 | 2.8 | 4.8 | 577 / 641 | 1129 / 1180 |
| es-ES_DT1 | fast_llm | 25 | 0.106 | 0.400 | 0.7 | 2.8 | 6.9 | 486 / 530 | 1039 / 1118 |
| es-ES_DT1 | fast_mai | 25 | 0.071 | 0.280 | 0.0 | 2.1 | 3.4 | 491 / 592 | 1043 / 1119 |
| es-ES_DT1 | realtime | 25 | 0.140 | 0.520 | 2.1 | 4.8 | 6.2 | -88 / 2 | 676 / 843 |
| es-ES_DT1 | realtime_refine | 25 | 0.074 | 0.400 | 0.0 | 2.1 | 4.8 | 337 / 403 | 1029 / 1201 |
| es-ES_DT2 | fast_default | 27 | 0.106 | 0.519 | 0.0 | 1.3 | 8.9 | 569 / 619 | 1114 / 1160 |
| es-ES_DT2 | fast_llm | 27 | 0.103 | 0.407 | 0.0 | 5.7 | 4.4 | 489 / 537 | 1033 / 1085 |
| es-ES_DT2 | fast_mai | 27 | 0.097 | 0.296 | 2.5 | 0.6 | 7.0 | 499 / 607 | 1043 / 1198 |
| es-ES_DT2 | realtime | 27 | 0.120 | 0.519 | 1.3 | 3.8 | 7.0 | -111 / 91 | 702 / 912 |
| es-ES_DT2 | realtime_refine | 27 | 0.142 | 0.556 | 3.2 | 1.3 | 8.9 | 343 / 654 | 1082 / 1463 |
| es-ES_JT1 | fast_default | 29 | 0.086 | 0.276 | 0.0 | 3.6 | 4.2 | 691 / 780 | 1251 / 1335 |
| es-ES_JT1 | fast_llm | 29 | 0.113 | 0.379 | 0.6 | 6.6 | 3.6 | 515 / 537 | 1083 / 1223 |
| es-ES_JT1 | fast_mai | 29 | 0.072 | 0.276 | 0.0 | 3.6 | 3.0 | 535 / 659 | 1027 / 1200 |
| es-ES_JT1 | realtime | 29 | 0.130 | 0.483 | 0.0 | 6.6 | 5.4 | -47 / 78 | 716 / 880 |
| es-ES_JT1 | realtime_refine | 29 | 0.084 | 0.310 | 0.6 | 4.2 | 3.0 | 562 / 746 | 1201 / 1306 |

## Unfiltered results (all complete samples, for reference)

| Dataset | Service | N | WER | SER | INS/100 | DEL/100 | SUB/100 |
|---|---|---:|---:|---:|---:|---:|---:|
| es-ES_DT1 | fast_default | 30 | 0.147 | 0.433 | 0.0 | 6.4 | 8.1 |
| es-ES_DT1 | fast_llm | 30 | 0.202 | 0.467 | 1.2 | 8.1 | 10.5 |
| es-ES_DT1 | fast_mai | 30 | 0.172 | 0.400 | 0.0 | 8.7 | 7.0 |
| es-ES_DT1 | realtime | 30 | 0.283 | 0.600 | 1.7 | 19.8 | 5.2 |
| es-ES_DT1 | realtime_refine | 30 | 0.162 | 0.467 | 0.0 | 11.0 | 4.7 |
| es-ES_DT2 | fast_default | 30 | 0.169 | 0.567 | 0.0 | 5.2 | 9.9 |
| es-ES_DT2 | fast_llm | 30 | 0.164 | 0.467 | 1.2 | 7.0 | 7.0 |
| es-ES_DT2 | fast_mai | 30 | 0.161 | 0.367 | 2.9 | 0.6 | 12.2 |
| es-ES_DT2 | realtime | 30 | 0.208 | 0.567 | 1.2 | 11.6 | 6.4 |
| es-ES_DT2 | realtime_refine | 30 | 0.188 | 0.567 | 2.9 | 4.1 | 9.9 |
| es-ES_JT1 | fast_default | 30 | 0.117 | 0.300 | 0.0 | 6.4 | 4.1 |
| es-ES_JT1 | fast_llm | 30 | 0.143 | 0.400 | 1.2 | 6.4 | 5.8 |
| es-ES_JT1 | fast_mai | 30 | 0.083 | 0.300 | 0.0 | 3.5 | 4.1 |
| es-ES_JT1 | realtime | 30 | 0.159 | 0.500 | 0.0 | 9.3 | 5.2 |
| es-ES_JT1 | realtime_refine | 30 | 0.115 | 0.333 | 0.6 | 7.0 | 2.9 |

## Excluded samples — examples

### Empty hypothesis

| Audio | Dataset | Sample | Empty in | Reference |
|---|---|---|---|---|
| [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/130.%C2%BFCu%C3%A1ntos%20minutos%20faltan%20para%20llegar.wav.wav) | es-ES_DT1 | 1l_es-ES_male-DT1/130.¿Cuántos minutos faltan para llegar.wav | realtime | `¿Cuántos minutos faltan para llegar` |
| [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/109.Ve%20a%20la%20p%C3%A1gina%20siguiente.wav.wav) | es-ES_DT1 | 1l_es-ES_male-DT1/109.Ve a la página siguiente.wav | realtime | `Ve a la página siguiente` |
| [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/065.Abre%20la%20pantalla%20de%20iterinario.wav.wav) | es-ES_DT1 | 1l_es-ES_male-DT1/065.Abre la pantalla de iterinario.wav | fast_mai,realtime | `Abre la pantalla de iterinario` |
| [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/023.Sube%20un%20poco%20el%20asiento.wav.wav) | es-ES_DT1 | 1l_es-ES_male-DT1/023.Sube un poco el asiento.wav | realtime | `Sube un poco el asiento` |
| [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/045.Activa%20el%20modo%20de%20mantenimiento%20de%20limpiaparabrisas.wav.wav) | es-ES_DT1 | 1l_es-ES_male-DT1/045.Activa el modo de mantenimiento de limpiaparabrisas.wav | realtime | `Activa el modo de mantenimiento de limpiaparabrisas` |
| [▶](audio/es-ES_DT2/1l_es-ES_male-DT2/065.Abre%20la%20pantalla%20de%20iterinario.wav.wav) | es-ES_DT2 | 1l_es-ES_male-DT2/065.Abre la pantalla de iterinario.wav | fast_default,realtime | `Abre la pantalla de iterinario` |
| [▶](audio/es-ES_DT2/1l_es-ES_male-DT2/080.Activa%20los%20datos%20m%C3%B3viles.wav.wav) | es-ES_DT2 | 1l_es-ES_male-DT2/080.Activa los datos móviles.wav | realtime | `Activa los datos móviles` |
| [▶](audio/es-ES_DT2/1l_es-ES_male-DT2/023.Sube%20un%20poco%20el%20asiento.wav.wav) | es-ES_DT2 | 1l_es-ES_male-DT2/023.Sube un poco el asiento.wav | realtime | `Sube un poco el asiento` |
| [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/065.Abre%20la%20pantalla%20de%20iterinario.wav.wav) | es-ES_JT1 | 1l_es-ES_male-JT1/065.Abre la pantalla de iterinario.wav | fast_default,realtime,realtime_refine | `Abre la pantalla de iterinario` |

### Reference too short for audio duration

_(none)_

### All services agree, reference disagrees (likely mislabeled)

_(none)_

## Genuine recognition errors (filtered set)

Best / median / worst WER per (dataset, service) on the kept samples.

### es-ES_DT1 / fast_default  (n=25)
**BEST** — `1l_es-ES_female-DT1/141.Apaga la música por Bluetooth.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/141.Apaga%20la%20m%C3%BAsica%20por%20Bluetooth.wav.wav)  wer=0.000  speech=[1.35s, 2.75s]  fix=none
- ref: `Apaga la música por Bluetooth`
- hyp: `Apaga la música por Bluetooth.`
**MEDIAN** — `1l_es-ES_female-DT1/082.Actualiza la lista de dispositivos Bluetooth.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/082.Actualiza%20la%20lista%20de%20dispositivos%20Bluetooth.wav.wav)  wer=0.000  speech=[1.41s, 3.73s]  fix=none
- ref: `Actualiza la lista de dispositivos Bluetooth`
- hyp: `Actualiza la lista de dispositivos Bluetooth.`
**WORST** — `1l_es-ES_female-DT1/113.Actualiza la ruta.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/113.Actualiza%20la%20ruta.wav.wav)  wer=0.333  speech=[1.5s, 2.5s]  fix=none
- ref: `Actualiza la ruta`
- hyp: `Realiza la ruta.`

### es-ES_DT1 / fast_llm  (n=25)
**BEST** — `1l_es-ES_female-DT1/126.Ajusta la vista del mapa para que el coche esté hacia arriba.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/126.Ajusta%20la%20vista%20del%20mapa%20para%20que%20el%20coche%20est%C3%A9%20hacia%20arriba.wav.wav)  wer=0.000  speech=[1.44s, 4.44s]  fix=none
- ref: `Ajusta la vista del mapa para que el coche esté hacia arriba`
- hyp: `Ajusta la vista del mapa para que el coche esté hacia arriba.`
**MEDIAN** — `1l_es-ES_female-DT1/082.Actualiza la lista de dispositivos Bluetooth.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/082.Actualiza%20la%20lista%20de%20dispositivos%20Bluetooth.wav.wav)  wer=0.000  speech=[1.41s, 3.73s]  fix=none
- ref: `Actualiza la lista de dispositivos Bluetooth`
- hyp: `Actualiza la lista de dispositivos Bluetooth.`
**WORST** — `1l_es-ES_female-DT1/014.Activa la circulación externa.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/014.Activa%20la%20circulaci%C3%B3n%20externa.wav.wav)  wer=0.500  speech=[1.88s, 3.08s]  fix=trim_first
- ref: `Activa la circulación externa`
- hyp: `Para circulación externa.`

### es-ES_DT1 / fast_mai  (n=25)
**BEST** — `1l_es-ES_female-DT1/141.Apaga la música por Bluetooth.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/141.Apaga%20la%20m%C3%BAsica%20por%20Bluetooth.wav.wav)  wer=0.000  speech=[1.35s, 2.75s]  fix=none
- ref: `Apaga la música por Bluetooth`
- hyp: `Apaga la música por Bluetooth.`
**MEDIAN** — `1l_es-ES_male-DT1/138.Añade esta emisora a favoritos.wav` [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/138.A%C3%B1ade%20esta%20emisora%20a%20favoritos.wav.wav)  wer=0.000  speech=[1.3s, 3.58s]  fix=none
- ref: `Añade esta emisora a favoritos`
- hyp: `Añade esta emisora a favoritos.`
**WORST** — `1l_es-ES_female-DT1/014.Activa la circulación externa.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/014.Activa%20la%20circulaci%C3%B3n%20externa.wav.wav)  wer=0.500  speech=[1.88s, 3.08s]  fix=trim_first
- ref: `Activa la circulación externa`
- hyp: `para circulación externa.`

### es-ES_DT1 / realtime  (n=25)
**BEST** — `1l_es-ES_female-DT1/115.Elige la distancia más corta.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/115.Elige%20la%20distancia%20m%C3%A1s%20corta.wav.wav)  wer=0.000  speech=[1.23s, 3.11s]  fix=none
- ref: `Elige la distancia más corta`
- hyp: `Elige la distancia más corta.`
**MEDIAN** — `1l_es-ES_female-DT1/013.Dirección del aire hacia los pies y el parabrisas.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/013.Direcci%C3%B3n%20del%20aire%20hacia%20los%20pies%20y%20el%20parabrisas.wav.wav)  wer=0.111  speech=[1.21s, 3.77s]  fix=none
- ref: `Dirección del aire hacia los pies y el parabrisas`
- hyp: `Dirección del aire hacia los tíos y el parabrisas.`
**WORST** — `1l_es-ES_female-DT1/014.Activa la circulación externa.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/014.Activa%20la%20circulaci%C3%B3n%20externa.wav.wav)  wer=0.500  speech=[1.88s, 3.08s]  fix=trim_first
- ref: `Activa la circulación externa`
- hyp: `Para circulación externa.`

### es-ES_DT1 / realtime_refine  (n=25)
**BEST** — `1l_es-ES_female-DT1/141.Apaga la música por Bluetooth.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/141.Apaga%20la%20m%C3%BAsica%20por%20Bluetooth.wav.wav)  wer=0.000  speech=[1.35s, 2.75s]  fix=none
- ref: `Apaga la música por Bluetooth`
- hyp: `Apaga la música por Bluetooth.`
**MEDIAN** — `1l_es-ES_female-DT1/082.Actualiza la lista de dispositivos Bluetooth.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/082.Actualiza%20la%20lista%20de%20dispositivos%20Bluetooth.wav.wav)  wer=0.000  speech=[1.41s, 3.73s]  fix=none
- ref: `Actualiza la lista de dispositivos Bluetooth`
- hyp: `Actualiza la lista de dispositivos Bluetooth.`
**WORST** — `1l_es-ES_female-DT1/113.Actualiza la ruta.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/113.Actualiza%20la%20ruta.wav.wav)  wer=0.333  speech=[1.5s, 2.5s]  fix=none
- ref: `Actualiza la ruta`
- hyp: `Realiza la ruta.`

### es-ES_DT2 / fast_default  (n=27)
**BEST** — `1l_es-ES_female-DT2/115.Elige la distancia más corta.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/115.Elige%20la%20distancia%20m%C3%A1s%20corta.wav.wav)  wer=0.000  speech=[1.23s, 2.83s]  fix=none
- ref: `Elige la distancia más corta`
- hyp: `Elige la distancia más corta.`
**MEDIAN** — `1l_es-ES_female-DT2/126.Ajusta la vista del mapa para que el coche esté hacia arriba.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/126.Ajusta%20la%20vista%20del%20mapa%20para%20que%20el%20coche%20est%C3%A9%20hacia%20arriba.wav.wav)  wer=0.083  speech=[1.44s, 4.16s]  fix=none
- ref: `Ajusta la vista del mapa para que el coche esté hacia arriba`
- hyp: `Ajusto la vista del mapa para que el coche esté hacia arriba.`
**WORST** — `1l_es-ES_female-DT2/014.Activa la circulación externa.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/014.Activa%20la%20circulaci%C3%B3n%20externa.wav.wav)  wer=0.500  speech=[1.83s, 3.07s]  fix=trim_first
- ref: `Activa la circulación externa`
- hyp: `Para circulación externa.`

### es-ES_DT2 / fast_llm  (n=27)
**BEST** — `1l_es-ES_female-DT2/141.Apaga la música por Bluetooth.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/141.Apaga%20la%20m%C3%BAsica%20por%20Bluetooth.wav.wav)  wer=0.000  speech=[1.24s, 2.64s]  fix=none
- ref: `Apaga la música por Bluetooth`
- hyp: `Apaga la música por Bluetooth.`
**MEDIAN** — `1l_es-ES_male-DT2/025.Deslice el asiento hacia adelante.wav` [▶](audio/es-ES_DT2/1l_es-ES_male-DT2/025.Deslice%20el%20asiento%20hacia%20adelante.wav.wav)  wer=0.000  speech=[1.14s, 3.3s]  fix=none
- ref: `Deslice el asiento hacia adelante`
- hyp: `Deslice el asiento hacia adelante.`
**WORST** — `1l_es-ES_female-DT2/082.Actualiza la lista de dispositivos Bluetooth.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/082.Actualiza%20la%20lista%20de%20dispositivos%20Bluetooth.wav.wav)  wer=0.500  speech=[1.43s, 3.39s]  fix=none
- ref: `Actualiza la lista de dispositivos Bluetooth`
- hyp: `Abrir lista de dispositivos.`

### es-ES_DT2 / fast_mai  (n=27)
**BEST** — `1l_es-ES_female-DT2/013.Dirección del aire hacia los pies y el parabrisas.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/013.Direcci%C3%B3n%20del%20aire%20hacia%20los%20pies%20y%20el%20parabrisas.wav.wav)  wer=0.000  speech=[1.24s, 3.88s]  fix=none
- ref: `Dirección del aire hacia los pies y el parabrisas`
- hyp: `Dirección del aire hacia los pies y el parabrisas.`
**MEDIAN** — `1l_es-ES_female-DT2/113.Actualiza la ruta.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/113.Actualiza%20la%20ruta.wav.wav)  wer=0.000  speech=[1.31s, 2.51s]  fix=none
- ref: `Actualiza la ruta`
- hyp: `Actualiza la ruta.`
**WORST** — `1l_es-ES_female-DT2/102.Dirígeme a la oficina.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/102.Dir%C3%ADgeme%20a%20la%20oficina.wav.wav)  wer=2.000  speech=[1.19s, 2.31s]  fix=none
- ref: `Dirígeme a la oficina`
- hyp: `¿Y de qué me ha hablado tu primo?`

### es-ES_DT2 / realtime  (n=27)
**BEST** — `1l_es-ES_female-DT2/141.Apaga la música por Bluetooth.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/141.Apaga%20la%20m%C3%BAsica%20por%20Bluetooth.wav.wav)  wer=0.000  speech=[1.24s, 2.64s]  fix=none
- ref: `Apaga la música por Bluetooth`
- hyp: `Apaga la música por Bluetooth.`
**MEDIAN** — `1l_es-ES_female-DT2/058.Cambia el modo de asistencia de dirección a estándar.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/058.Cambia%20el%20modo%20de%20asistencia%20de%20direcci%C3%B3n%20a%20est%C3%A1ndar.wav.wav)  wer=0.111  speech=[1.26s, 3.78s]  fix=none
- ref: `Cambia el modo de asistencia de dirección a estándar`
- hyp: `Cambia el modo de asistencia de dirección a esta.`
**WORST** — `1l_es-ES_female-DT2/014.Activa la circulación externa.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/014.Activa%20la%20circulaci%C3%B3n%20externa.wav.wav)  wer=0.500  speech=[1.83s, 3.07s]  fix=trim_first
- ref: `Activa la circulación externa`
- hyp: `Para circulación externa.`

### es-ES_DT2 / realtime_refine  (n=27)
**BEST** — `1l_es-ES_female-DT2/141.Apaga la música por Bluetooth.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/141.Apaga%20la%20m%C3%BAsica%20por%20Bluetooth.wav.wav)  wer=0.000  speech=[1.24s, 2.64s]  fix=none
- ref: `Apaga la música por Bluetooth`
- hyp: `Apaga la música por Bluetooth.`
**MEDIAN** — `1l_es-ES_female-DT2/058.Cambia el modo de asistencia de dirección a estándar.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/058.Cambia%20el%20modo%20de%20asistencia%20de%20direcci%C3%B3n%20a%20est%C3%A1ndar.wav.wav)  wer=0.111  speech=[1.26s, 3.78s]  fix=none
- ref: `Cambia el modo de asistencia de dirección a estándar`
- hyp: `Cambia el modo de asistencia de dirección a esta.`
**WORST** — `1l_es-ES_female-DT2/102.Dirígeme a la oficina.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/102.Dir%C3%ADgeme%20a%20la%20oficina.wav.wav)  wer=0.500  speech=[1.19s, 2.31s]  fix=none
- ref: `Dirígeme a la oficina`
- hyp: `Ya.Diríqueme a la oficina.`

### es-ES_JT1 / fast_default  (n=29)
**BEST** — `1l_es-ES_female-JT1/058.Cambia el modo de asistencia de dirección a estándar.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/058.Cambia%20el%20modo%20de%20asistencia%20de%20direcci%C3%B3n%20a%20est%C3%A1ndar.wav.wav)  wer=0.000  speech=[1.45s, 3.97s]  fix=none
- ref: `Cambia el modo de asistencia de dirección a estándar`
- hyp: `Cambia el modo de asistencia de dirección a estándar.`
**MEDIAN** — `1l_es-ES_male-JT1/080.Activa los datos móviles.wav` [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/080.Activa%20los%20datos%20m%C3%B3viles.wav.wav)  wer=0.000  speech=[1.32s, 2.84s]  fix=none
- ref: `Activa los datos móviles`
- hyp: `Activa los datos móviles.`
**WORST** — `1l_es-ES_male-JT1/023.Sube un poco el asiento.wav` [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/023.Sube%20un%20poco%20el%20asiento.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Sube un poco el asiento`
- hyp: `Lo siento.`

### es-ES_JT1 / fast_llm  (n=29)
**BEST** — `1l_es-ES_female-JT1/013.Dirección del aire hacia los pies y el parabrisas.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/013.Direcci%C3%B3n%20del%20aire%20hacia%20los%20pies%20y%20el%20parabrisas.wav.wav)  wer=0.000  speech=[1.22s, 3.9s]  fix=none
- ref: `Dirección del aire hacia los pies y el parabrisas`
- hyp: `Dirección del aire hacia los pies y el parabrisas.`
**MEDIAN** — `1l_es-ES_female-JT1/143.Apaga la música del USB.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/143.Apaga%20la%20m%C3%BAsica%20del%20USB.wav.wav)  wer=0.000  speech=[1.32s, 2.72s]  fix=none
- ref: `Apaga la música del USB`
- hyp: `Apaga la música del USB.`
**WORST** — `1l_es-ES_male-JT1/023.Sube un poco el asiento.wav` [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/023.Sube%20un%20poco%20el%20asiento.wav.wav)  wer=0.800  speech=[-s, -s]  fix=skip
- ref: `Sube un poco el asiento`
- hyp: `Asiento.`

### es-ES_JT1 / fast_mai  (n=29)
**BEST** — `1l_es-ES_female-JT1/013.Dirección del aire hacia los pies y el parabrisas.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/013.Direcci%C3%B3n%20del%20aire%20hacia%20los%20pies%20y%20el%20parabrisas.wav.wav)  wer=0.000  speech=[1.22s, 3.9s]  fix=none
- ref: `Dirección del aire hacia los pies y el parabrisas`
- hyp: `Dirección del aire hacia los pies y el parabrisas.`
**MEDIAN** — `1l_es-ES_female-JT1/113.Actualiza la ruta.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/113.Actualiza%20la%20ruta.wav.wav)  wer=0.000  speech=[1.39s, 2.47s]  fix=none
- ref: `Actualiza la ruta`
- hyp: `Actualiza la ruta.`
**WORST** — `1l_es-ES_male-JT1/023.Sube un poco el asiento.wav` [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/023.Sube%20un%20poco%20el%20asiento.wav.wav)  wer=0.800  speech=[-s, -s]  fix=skip
- ref: `Sube un poco el asiento`
- hyp: `Asiento.`

### es-ES_JT1 / realtime  (n=29)
**BEST** — `1l_es-ES_female-JT1/013.Dirección del aire hacia los pies y el parabrisas.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/013.Direcci%C3%B3n%20del%20aire%20hacia%20los%20pies%20y%20el%20parabrisas.wav.wav)  wer=0.000  speech=[1.22s, 3.9s]  fix=none
- ref: `Dirección del aire hacia los pies y el parabrisas`
- hyp: `Dirección del aire hacia los pies y el parabrisas.`
**MEDIAN** — `1l_es-ES_female-JT1/111.Ve a la última página.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/111.Ve%20a%20la%20%C3%BAltima%20p%C3%A1gina.wav.wav)  wer=0.000  speech=[1.27s, 2.59s]  fix=none
- ref: `Ve a la última página`
- hyp: `¿Ve a la última página?`
**WORST** — `1l_es-ES_male-JT1/023.Sube un poco el asiento.wav` [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/023.Sube%20un%20poco%20el%20asiento.wav.wav)  wer=0.800  speech=[-s, -s]  fix=skip
- ref: `Sube un poco el asiento`
- hyp: `Asiento.`

### es-ES_JT1 / realtime_refine  (n=29)
**BEST** — `1l_es-ES_female-JT1/058.Cambia el modo de asistencia de dirección a estándar.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/058.Cambia%20el%20modo%20de%20asistencia%20de%20direcci%C3%B3n%20a%20est%C3%A1ndar.wav.wav)  wer=0.000  speech=[1.45s, 3.97s]  fix=none
- ref: `Cambia el modo de asistencia de dirección a estándar`
- hyp: `Cambia el modo de asistencia de dirección a estándar.`
**MEDIAN** — `1l_es-ES_male-JT1/080.Activa los datos móviles.wav` [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/080.Activa%20los%20datos%20m%C3%B3viles.wav.wav)  wer=0.000  speech=[1.32s, 2.84s]  fix=none
- ref: `Activa los datos móviles`
- hyp: `Activa los datos móviles.`
**WORST** — `1l_es-ES_male-JT1/023.Sube un poco el asiento.wav` [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/023.Sube%20un%20poco%20el%20asiento.wav.wav)  wer=0.800  speech=[-s, -s]  fix=skip
- ref: `Sube un poco el asiento`
- hyp: `Asiento.`

## Top fast_default vs realtime disagreements (filtered)

### es-ES_DT1/1l_es-ES_male-DT1/138.Añade esta emisora a favoritos.wav [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/138.A%C3%B1ade%20esta%20emisora%20a%20favoritos.wav.wav)  Δwer=0.400  (fast_default=0.000, realtime=0.400)  speech=[1.3s, 3.58s] fix=none
- ref:           `Añade esta emisora a favoritos`
- fast_default   `Añade esta emisora a favoritos.`
- fast_llm       `Ya de esta emisora a favoritos.`
- fast_mai       `Añade esta emisora a favoritos.`
- realtime       `Ya de esta emisora a favoritos.`
- realtime_refine `Añade esta emisora a favoritos.`

### es-ES_DT1/1l_es-ES_male-DT1/025.Deslice el asiento hacia adelante.wav [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/025.Deslice%20el%20asiento%20hacia%20adelante.wav.wav)  Δwer=0.400  (fast_default=0.000, realtime=0.400)  speech=[1.16s, 3.24s] fix=none
- ref:           `Deslice el asiento hacia adelante`
- fast_default   `Deslice el asiento hacia adelante.`
- fast_llm       `Deslice el asiento hacia adelante.`
- fast_mai       `Deslice el asiento hacia adelante.`
- realtime       `Exdice el asiento hacia delante.`
- realtime_refine `Deslice el asiento hacia adelante.`

### es-ES_DT1/1l_es-ES_female-DT1/111.Ve a la última página.wav [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/111.Ve%20a%20la%20%C3%BAltima%20p%C3%A1gina.wav.wav)  Δwer=0.400  (fast_default=0.000, realtime=0.400)  speech=[1.41s, 2.01s] fix=trim_last
- ref:           `Ve a la última página`
- fast_default   `Ve a la última página.`
- fast_llm       `Ve a la última página.`
- fast_mai       `Ve a la última página.`
- realtime       `La última página.`
- realtime_refine `Ve a la última página.`

### es-ES_DT2/1l_es-ES_male-DT2/067.Quiero abrir los ajustes del sistema.wav [▶](audio/es-ES_DT2/1l_es-ES_male-DT2/067.Quiero%20abrir%20los%20ajustes%20del%20sistema.wav.wav)  Δwer=0.333  (fast_default=0.000, realtime=0.333)  speech=[1.77s, 3.29s] fix=none
- ref:           `Quiero abrir los ajustes del sistema`
- fast_default   `Quiero abrir los ajustes del sistema.`
- fast_llm       `Los ajustes del sistema.`
- fast_mai       `Quiero abrir los ajustes del sistema.`
- realtime       `Los ajustes del sistema.`
- realtime_refine `Quiero abrir los ajustes del sistema.`

### es-ES_JT1/1l_es-ES_female-JT1/080.Activa los datos móviles.wav [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/080.Activa%20los%20datos%20m%C3%B3viles.wav.wav)  Δwer=0.250  (fast_default=0.000, realtime=0.250)  speech=[1.72s, 2.24s] fix=trim_both
- ref:           `Activa los datos móviles`
- fast_default   `Activa los datos móviles.`
- fast_llm       `Los datos móviles.`
- fast_mai       `Reciba los datos móviles.`
- realtime       `¿Iba los datos móviles?`
- realtime_refine `Activa los datos móviles.`

### es-ES_JT1/1l_es-ES_female-JT1/014.Activa la circulación externa.wav [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/014.Activa%20la%20circulaci%C3%B3n%20externa.wav.wav)  Δwer=0.250  (fast_default=0.000, realtime=0.250)  speech=[-s, -s] fix=skip
- ref:           `Activa la circulación externa`
- fast_default   `Activa la circulación externa.`
- fast_llm       `Activa la circulación externa.`
- fast_mai       `Cultiva la circulación externa.`
- realtime       `Va la circulación externa.`
- realtime_refine `Activa la circulación externa.`

### es-ES_DT2/1l_es-ES_female-DT2/102.Dirígeme a la oficina.wav [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/102.Dir%C3%ADgeme%20a%20la%20oficina.wav.wav)  Δwer=0.250  (fast_default=0.250, realtime=0.000)  speech=[1.19s, 2.31s] fix=none
- ref:           `Dirígeme a la oficina`
- fast_default   `Diríteme a la oficina.`
- fast_llm       `Dirígeme a la oficina.`
- fast_mai       `¿Y de qué me ha hablado tu primo?`
- realtime       `Dirígeme a la oficina.`
- realtime_refine `Ya.Diríqueme a la oficina.`

### es-ES_DT2/1l_es-ES_female-DT2/080.Activa los datos móviles.wav [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/080.Activa%20los%20datos%20m%C3%B3viles.wav.wav)  Δwer=0.250  (fast_default=0.000, realtime=0.250)  speech=[1.72s, 2.24s] fix=trim_last
- ref:           `Activa los datos móviles`
- fast_default   `Activa los datos móviles.`
- fast_llm       `Activa los datos móviles.`
- fast_mai       `Agrega los datos móviles.`
- realtime       `Los datos móviles.`
- realtime_refine `Activa los datos móviles.`

### es-ES_DT1/1l_es-ES_female-DT1/014.Activa la circulación externa.wav [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/014.Activa%20la%20circulaci%C3%B3n%20externa.wav.wav)  Δwer=0.250  (fast_default=0.250, realtime=0.500)  speech=[1.88s, 3.08s] fix=trim_first
- ref:           `Activa la circulación externa`
- fast_default   `La circulación externa.`
- fast_llm       `Para circulación externa.`
- fast_mai       `para circulación externa.`
- realtime       `Para circulación externa.`
- realtime_refine `la circulación externa.`

### es-ES_JT1/1l_es-ES_male-JT1/130.¿Cuántos minutos faltan para llegar.wav [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/130.%C2%BFCu%C3%A1ntos%20minutos%20faltan%20para%20llegar.wav.wav)  Δwer=0.200  (fast_default=0.000, realtime=0.200)  speech=[1.34s, 3.14s] fix=none
- ref:           `¿Cuántos minutos faltan para llegar`
- fast_default   `¿Cuántos minutos faltan para llegar?`
- fast_llm       `¿Cuántos minutos faltan para llegar?`
- fast_mai       `¿Cuántos minutos faltan para llegar?`
- realtime       `2 minutos faltan para llegar.`
- realtime_refine `¿Cuántos minutos faltan para llegar?`

## Caveats

- **UPL is anchored on the realtime SDK's word-end timestamp** for each sample, so all services use the same `speech_end`. The CSV's `upl_self_ms` column has each service's own phrase-derived value if you want to see how its boundary detection differs.
- **Mazda voice commands** are short utterances (typically 2-8 words). WER on short references is noisier — a single word error on a 3-word command gives 33% WER.
- The 'all-agree-vs-ref' filter is conservative (pairwise WER < 0.15 AND mean ref WER > 0.5). True mislabels with partial agreement still survive and inflate per-service WER equally.