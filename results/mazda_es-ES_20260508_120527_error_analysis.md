# Error analysis — mazda_es-ES_20260508_120527.csv

Audio links (▶) point to `results/audio/<dataset>/<sample_id>.wav` so a reviewer can play the clip directly.

## Datasets under test

- **es-ES_DT1** — Mazda es-ES DT1 voice commands (male + female pooled)
- **es-ES_DT2** — Mazda es-ES DT2 voice commands (male + female pooled)
- **es-ES_JT1** — Mazda es-ES JT1 voice commands (male + female pooled)

Total samples: **90**  

## Speech boundaries

`speech_start_s` / `speech_end_s` come from the realtime SDK's word-level timestamps and anchor UPL for all services. Per-word detail lives in the sidecar `mazda_es-ES_20260508_120527_words.jsonl`.

Boundary-fix actions across 90 realtime samples: `skip`=12, `trim_both`=1, `trim_first`=2, `trim_last`=4

## Results

INS/DEL/SUB are *rates per 100 reference words*. Their sum ≈ WER × 100.

| Dataset | Service | N | WER | SER | INS/100 | DEL/100 | SUB/100 | LBL ms (mean / p90) | UPL ms (mean / p90) |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| es-ES_DT1 | fast_default | 30 | 0.147 | 0.433 | 0.0 | 6.4 | 8.1 | 573 / 641 | 1177 / 1443 |
| es-ES_DT1 | fast_llm | 30 | 0.189 | 0.433 | 1.2 | 7.6 | 9.9 | 487 / 530 | 1097 / 1414 |
| es-ES_DT1 | fast_mai | 30 | 0.172 | 0.400 | 0.0 | 8.7 | 7.0 | 509 / 665 | 974 / 1154 |
| es-ES_DT1 | realtime | 30 | 0.283 | 0.600 | 1.7 | 19.8 | 5.2 | -88 / 2 | 676 / 843 |
| es-ES_DT1 | realtime_refine | 30 | 0.162 | 0.467 | 0.0 | 11.0 | 4.7 | 312 / 403 | 1036 / 1255 |
| es-ES_DT2 | fast_default | 30 | 0.169 | 0.567 | 0.0 | 5.2 | 9.9 | 569 / 619 | 1141 / 1179 |
| es-ES_DT2 | fast_llm | 30 | 0.151 | 0.433 | 1.2 | 6.4 | 6.4 | 488 / 537 | 1073 / 1230 |
| es-ES_DT2 | fast_mai | 30 | 0.161 | 0.367 | 2.9 | 0.6 | 12.2 | 496 / 607 | 989 / 1198 |
| es-ES_DT2 | realtime | 30 | 0.208 | 0.567 | 1.2 | 11.6 | 6.4 | -111 / 91 | 702 / 912 |
| es-ES_DT2 | realtime_refine | 30 | 0.188 | 0.567 | 2.9 | 4.1 | 9.9 | 337 / 752 | 1146 / 1542 |
| es-ES_JT1 | fast_default | 30 | 0.117 | 0.300 | 0.0 | 6.4 | 4.1 | 686 / 780 | 1251 / 1335 |
| es-ES_JT1 | fast_llm | 30 | 0.143 | 0.400 | 1.2 | 6.4 | 5.8 | 513 / 537 | 1089 / 1275 |
| es-ES_JT1 | fast_mai | 30 | 0.083 | 0.300 | 0.0 | 3.5 | 4.1 | 532 / 659 | 1010 / 1200 |
| es-ES_JT1 | realtime | 30 | 0.159 | 0.500 | 0.0 | 9.3 | 5.2 | -47 / 78 | 716 / 880 |
| es-ES_JT1 | realtime_refine | 30 | 0.115 | 0.333 | 0.6 | 7.0 | 2.9 | 562 / 746 | 1201 / 1306 |

## Best / median / worst WER per (dataset, service)

### es-ES_DT1 / fast_default  (n=30)
**BEST** — `1l_es-ES_female-DT1/141.Apaga la música por Bluetooth.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/141.Apaga%20la%20m%C3%BAsica%20por%20Bluetooth.wav.wav)  wer=0.000  speech=[1.35s, 2.75s]  fix=none
- ref: `Apaga la música por Bluetooth`
- hyp: `Apaga la música por Bluetooth.`
**MEDIAN** — `1l_es-ES_male-DT1/025.Deslice el asiento hacia adelante.wav` [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/025.Deslice%20el%20asiento%20hacia%20adelante.wav.wav)  wer=0.000  speech=[1.16s, 3.24s]  fix=none
- ref: `Deslice el asiento hacia adelante`
- hyp: `Deslice el asiento hacia adelante.`
**WORST** — `1l_es-ES_male-DT1/045.Activa el modo de mantenimiento de limpiaparabrisas.wav` [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/045.Activa%20el%20modo%20de%20mantenimiento%20de%20limpiaparabrisas.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Activa el modo de mantenimiento de limpiaparabrisas`
- hyp: `That recess.`

### es-ES_DT1 / fast_llm  (n=30)
**BEST** — `1l_es-ES_female-DT1/126.Ajusta la vista del mapa para que el coche esté hacia arriba.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/126.Ajusta%20la%20vista%20del%20mapa%20para%20que%20el%20coche%20est%C3%A9%20hacia%20arriba.wav.wav)  wer=0.000  speech=[1.44s, 4.44s]  fix=none
- ref: `Ajusta la vista del mapa para que el coche esté hacia arriba`
- hyp: `Ajusta la vista del mapa para que el coche esté hacia arriba.`
**MEDIAN** — `1l_es-ES_male-DT1/025.Deslice el asiento hacia adelante.wav` [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/025.Deslice%20el%20asiento%20hacia%20adelante.wav.wav)  wer=0.000  speech=[1.16s, 3.24s]  fix=none
- ref: `Deslice el asiento hacia adelante`
- hyp: `Deslice el asiento hacia adelante.`
**WORST** — `1l_es-ES_male-DT1/045.Activa el modo de mantenimiento de limpiaparabrisas.wav` [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/045.Activa%20el%20modo%20de%20mantenimiento%20de%20limpiaparabrisas.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Activa el modo de mantenimiento de limpiaparabrisas`
- hyp: `À l'essai.`

### es-ES_DT1 / fast_mai  (n=30)
**BEST** — `1l_es-ES_female-DT1/141.Apaga la música por Bluetooth.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/141.Apaga%20la%20m%C3%BAsica%20por%20Bluetooth.wav.wav)  wer=0.000  speech=[1.35s, 2.75s]  fix=none
- ref: `Apaga la música por Bluetooth`
- hyp: `Apaga la música por Bluetooth.`
**MEDIAN** — `1l_es-ES_female-DT1/082.Actualiza la lista de dispositivos Bluetooth.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/082.Actualiza%20la%20lista%20de%20dispositivos%20Bluetooth.wav.wav)  wer=0.000  speech=[1.41s, 3.73s]  fix=none
- ref: `Actualiza la lista de dispositivos Bluetooth`
- hyp: `Actualiza la lista de dispositivos Bluetooth.`
**WORST** — `1l_es-ES_male-DT1/045.Activa el modo de mantenimiento de limpiaparabrisas.wav` [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/045.Activa%20el%20modo%20de%20mantenimiento%20de%20limpiaparabrisas.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Activa el modo de mantenimiento de limpiaparabrisas`
- hyp: `para visas.`

### es-ES_DT1 / realtime  (n=30)
**BEST** — `1l_es-ES_female-DT1/115.Elige la distancia más corta.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/115.Elige%20la%20distancia%20m%C3%A1s%20corta.wav.wav)  wer=0.000  speech=[1.23s, 3.11s]  fix=none
- ref: `Elige la distancia más corta`
- hyp: `Elige la distancia más corta.`
**MEDIAN** — `1l_es-ES_female-DT1/126.Ajusta la vista del mapa para que el coche esté hacia arriba.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/126.Ajusta%20la%20vista%20del%20mapa%20para%20que%20el%20coche%20est%C3%A9%20hacia%20arriba.wav.wav)  wer=0.167  speech=[1.44s, 4.44s]  fix=none
- ref: `Ajusta la vista del mapa para que el coche esté hacia arriba`
- hyp: `¿Está a la vista del mapa para que el coche esté hacia arriba?`
**WORST** — `1l_es-ES_male-DT1/045.Activa el modo de mantenimiento de limpiaparabrisas.wav` [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/045.Activa%20el%20modo%20de%20mantenimiento%20de%20limpiaparabrisas.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Activa el modo de mantenimiento de limpiaparabrisas`
- hyp: ``

### es-ES_DT1 / realtime_refine  (n=30)
**BEST** — `1l_es-ES_female-DT1/141.Apaga la música por Bluetooth.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/141.Apaga%20la%20m%C3%BAsica%20por%20Bluetooth.wav.wav)  wer=0.000  speech=[1.35s, 2.75s]  fix=none
- ref: `Apaga la música por Bluetooth`
- hyp: `Apaga la música por Bluetooth.`
**MEDIAN** — `1l_es-ES_female-DT1/111.Ve a la última página.wav` [▶](audio/es-ES_DT1/1l_es-ES_female-DT1/111.Ve%20a%20la%20%C3%BAltima%20p%C3%A1gina.wav.wav)  wer=0.000  speech=[1.41s, 2.01s]  fix=trim_last
- ref: `Ve a la última página`
- hyp: `Ve a la última página.`
**WORST** — `1l_es-ES_male-DT1/045.Activa el modo de mantenimiento de limpiaparabrisas.wav` [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/045.Activa%20el%20modo%20de%20mantenimiento%20de%20limpiaparabrisas.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Activa el modo de mantenimiento de limpiaparabrisas`
- hyp: `Premisas.`

### es-ES_DT2 / fast_default  (n=30)
**BEST** — `1l_es-ES_female-DT2/115.Elige la distancia más corta.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/115.Elige%20la%20distancia%20m%C3%A1s%20corta.wav.wav)  wer=0.000  speech=[1.23s, 2.83s]  fix=none
- ref: `Elige la distancia más corta`
- hyp: `Elige la distancia más corta.`
**MEDIAN** — `1l_es-ES_female-DT2/013.Dirección del aire hacia los pies y el parabrisas.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/013.Direcci%C3%B3n%20del%20aire%20hacia%20los%20pies%20y%20el%20parabrisas.wav.wav)  wer=0.111  speech=[1.24s, 3.88s]  fix=none
- ref: `Dirección del aire hacia los pies y el parabrisas`
- hyp: `Director del aire hacia los pies y el parabrisas.`
**WORST** — `1l_es-ES_male-DT2/080.Activa los datos móviles.wav` [▶](audio/es-ES_DT2/1l_es-ES_male-DT2/080.Activa%20los%20datos%20m%C3%B3viles.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Activa los datos móviles`
- hyp: `That is good.`

### es-ES_DT2 / fast_llm  (n=30)
**BEST** — `1l_es-ES_female-DT2/141.Apaga la música por Bluetooth.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/141.Apaga%20la%20m%C3%BAsica%20por%20Bluetooth.wav.wav)  wer=0.000  speech=[1.24s, 2.64s]  fix=none
- ref: `Apaga la música por Bluetooth`
- hyp: `Apaga la música por Bluetooth.`
**MEDIAN** — `1l_es-ES_female-DT2/080.Activa los datos móviles.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/080.Activa%20los%20datos%20m%C3%B3viles.wav.wav)  wer=0.000  speech=[1.72s, 2.24s]  fix=trim_last
- ref: `Activa los datos móviles`
- hyp: `Activa los datos móviles.`
**WORST** — `1l_es-ES_male-DT2/065.Abre la pantalla de iterinario.wav` [▶](audio/es-ES_DT2/1l_es-ES_male-DT2/065.Abre%20la%20pantalla%20de%20iterinario.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Abre la pantalla de iterinario`
- hyp: `Club Deportivo Independiente.`

### es-ES_DT2 / fast_mai  (n=30)
**BEST** — `1l_es-ES_female-DT2/013.Dirección del aire hacia los pies y el parabrisas.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/013.Direcci%C3%B3n%20del%20aire%20hacia%20los%20pies%20y%20el%20parabrisas.wav.wav)  wer=0.000  speech=[1.24s, 3.88s]  fix=none
- ref: `Dirección del aire hacia los pies y el parabrisas`
- hyp: `Dirección del aire hacia los pies y el parabrisas.`
**MEDIAN** — `1l_es-ES_female-DT2/004.Activa el modo ventilación del aire acondicionado.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/004.Activa%20el%20modo%20ventilaci%C3%B3n%20del%20aire%20acondicionado.wav.wav)  wer=0.000  speech=[1.31s, 4.07s]  fix=none
- ref: `Activa el modo ventilación del aire acondicionado`
- hyp: `Activa el modo ventilación del aire acondicionado.`
**WORST** — `1l_es-ES_female-DT2/102.Dirígeme a la oficina.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/102.Dir%C3%ADgeme%20a%20la%20oficina.wav.wav)  wer=2.000  speech=[1.19s, 2.31s]  fix=none
- ref: `Dirígeme a la oficina`
- hyp: `¿Y de qué me ha hablado tu primo?`

### es-ES_DT2 / realtime  (n=30)
**BEST** — `1l_es-ES_female-DT2/141.Apaga la música por Bluetooth.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/141.Apaga%20la%20m%C3%BAsica%20por%20Bluetooth.wav.wav)  wer=0.000  speech=[1.24s, 2.64s]  fix=none
- ref: `Apaga la música por Bluetooth`
- hyp: `Apaga la música por Bluetooth.`
**MEDIAN** — `1l_es-ES_male-DT2/045.Activa el modo de mantenimiento de limpiaparabrisas.wav` [▶](audio/es-ES_DT2/1l_es-ES_male-DT2/045.Activa%20el%20modo%20de%20mantenimiento%20de%20limpiaparabrisas.wav.wav)  wer=0.143  speech=[1.39s, 4.15s]  fix=none
- ref: `Activa el modo de mantenimiento de limpiaparabrisas`
- hyp: `Acta, el modo de mantenimiento de limpiaparabrisas.`
**WORST** — `1l_es-ES_male-DT2/023.Sube un poco el asiento.wav` [▶](audio/es-ES_DT2/1l_es-ES_male-DT2/023.Sube%20un%20poco%20el%20asiento.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Sube un poco el asiento`
- hyp: ``

### es-ES_DT2 / realtime_refine  (n=30)
**BEST** — `1l_es-ES_female-DT2/141.Apaga la música por Bluetooth.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/141.Apaga%20la%20m%C3%BAsica%20por%20Bluetooth.wav.wav)  wer=0.000  speech=[1.24s, 2.64s]  fix=none
- ref: `Apaga la música por Bluetooth`
- hyp: `Apaga la música por Bluetooth.`
**MEDIAN** — `1l_es-ES_female-DT2/013.Dirección del aire hacia los pies y el parabrisas.wav` [▶](audio/es-ES_DT2/1l_es-ES_female-DT2/013.Direcci%C3%B3n%20del%20aire%20hacia%20los%20pies%20y%20el%20parabrisas.wav.wav)  wer=0.111  speech=[1.24s, 3.88s]  fix=none
- ref: `Dirección del aire hacia los pies y el parabrisas`
- hyp: `Director del aire hacia los pies y el parabrisas.`
**WORST** — `1l_es-ES_male-DT2/080.Activa los datos móviles.wav` [▶](audio/es-ES_DT2/1l_es-ES_male-DT2/080.Activa%20los%20datos%20m%C3%B3viles.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Activa los datos móviles`
- hyp: `That is more.`

### es-ES_JT1 / fast_default  (n=30)
**BEST** — `1l_es-ES_female-JT1/058.Cambia el modo de asistencia de dirección a estándar.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/058.Cambia%20el%20modo%20de%20asistencia%20de%20direcci%C3%B3n%20a%20est%C3%A1ndar.wav.wav)  wer=0.000  speech=[1.45s, 3.97s]  fix=none
- ref: `Cambia el modo de asistencia de dirección a estándar`
- hyp: `Cambia el modo de asistencia de dirección a estándar.`
**MEDIAN** — `1l_es-ES_female-JT1/143.Apaga la música del USB.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/143.Apaga%20la%20m%C3%BAsica%20del%20USB.wav.wav)  wer=0.000  speech=[1.32s, 2.72s]  fix=none
- ref: `Apaga la música del USB`
- hyp: `Apaga la música del USB.`
**WORST** — `1l_es-ES_male-JT1/023.Sube un poco el asiento.wav` [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/023.Sube%20un%20poco%20el%20asiento.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Sube un poco el asiento`
- hyp: `Lo siento.`

### es-ES_JT1 / fast_llm  (n=30)
**BEST** — `1l_es-ES_female-JT1/013.Dirección del aire hacia los pies y el parabrisas.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/013.Direcci%C3%B3n%20del%20aire%20hacia%20los%20pies%20y%20el%20parabrisas.wav.wav)  wer=0.000  speech=[1.22s, 3.9s]  fix=none
- ref: `Dirección del aire hacia los pies y el parabrisas`
- hyp: `Dirección del aire hacia los pies y el parabrisas.`
**MEDIAN** — `1l_es-ES_female-JT1/004.Activa el modo ventilación del aire acondicionado.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/004.Activa%20el%20modo%20ventilaci%C3%B3n%20del%20aire%20acondicionado.wav.wav)  wer=0.000  speech=[1.34s, 4.02s]  fix=none
- ref: `Activa el modo ventilación del aire acondicionado`
- hyp: `Activa el modo ventilación del aire acondicionado.`
**WORST** — `1l_es-ES_male-JT1/065.Abre la pantalla de iterinario.wav` [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/065.Abre%20la%20pantalla%20de%20iterinario.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Abre la pantalla de iterinario`
- hyp: `Apri la storia per il territorio.`

### es-ES_JT1 / fast_mai  (n=30)
**BEST** — `1l_es-ES_female-JT1/013.Dirección del aire hacia los pies y el parabrisas.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/013.Direcci%C3%B3n%20del%20aire%20hacia%20los%20pies%20y%20el%20parabrisas.wav.wav)  wer=0.000  speech=[1.22s, 3.9s]  fix=none
- ref: `Dirección del aire hacia los pies y el parabrisas`
- hyp: `Dirección del aire hacia los pies y el parabrisas.`
**MEDIAN** — `1l_es-ES_male-JT1/080.Activa los datos móviles.wav` [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/080.Activa%20los%20datos%20m%C3%B3viles.wav.wav)  wer=0.000  speech=[1.32s, 2.84s]  fix=none
- ref: `Activa los datos móviles`
- hyp: `Activa los datos móviles.`
**WORST** — `1l_es-ES_male-JT1/023.Sube un poco el asiento.wav` [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/023.Sube%20un%20poco%20el%20asiento.wav.wav)  wer=0.800  speech=[-s, -s]  fix=skip
- ref: `Sube un poco el asiento`
- hyp: `Asiento.`

### es-ES_JT1 / realtime  (n=30)
**BEST** — `1l_es-ES_female-JT1/013.Dirección del aire hacia los pies y el parabrisas.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/013.Direcci%C3%B3n%20del%20aire%20hacia%20los%20pies%20y%20el%20parabrisas.wav.wav)  wer=0.000  speech=[1.22s, 3.9s]  fix=none
- ref: `Dirección del aire hacia los pies y el parabrisas`
- hyp: `Dirección del aire hacia los pies y el parabrisas.`
**MEDIAN** — `1l_es-ES_female-JT1/058.Cambia el modo de asistencia de dirección a estándar.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/058.Cambia%20el%20modo%20de%20asistencia%20de%20direcci%C3%B3n%20a%20est%C3%A1ndar.wav.wav)  wer=0.111  speech=[1.45s, 3.97s]  fix=none
- ref: `Cambia el modo de asistencia de dirección a estándar`
- hyp: `El modo de asistencia de dirección a estándar.`
**WORST** — `1l_es-ES_male-JT1/065.Abre la pantalla de iterinario.wav` [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/065.Abre%20la%20pantalla%20de%20iterinario.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Abre la pantalla de iterinario`
- hyp: ``

### es-ES_JT1 / realtime_refine  (n=30)
**BEST** — `1l_es-ES_female-JT1/058.Cambia el modo de asistencia de dirección a estándar.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/058.Cambia%20el%20modo%20de%20asistencia%20de%20direcci%C3%B3n%20a%20est%C3%A1ndar.wav.wav)  wer=0.000  speech=[1.45s, 3.97s]  fix=none
- ref: `Cambia el modo de asistencia de dirección a estándar`
- hyp: `Cambia el modo de asistencia de dirección a estándar.`
**MEDIAN** — `1l_es-ES_female-JT1/143.Apaga la música del USB.wav` [▶](audio/es-ES_JT1/1l_es-ES_female-JT1/143.Apaga%20la%20m%C3%BAsica%20del%20USB.wav.wav)  wer=0.000  speech=[1.32s, 2.72s]  fix=none
- ref: `Apaga la música del USB`
- hyp: `Apaga la música del USB.`
**WORST** — `1l_es-ES_male-JT1/065.Abre la pantalla de iterinario.wav` [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/065.Abre%20la%20pantalla%20de%20iterinario.wav.wav)  wer=1.000  speech=[-s, -s]  fix=skip
- ref: `Abre la pantalla de iterinario`
- hyp: ``

## fast_llm hallucinations

`fast_llm` does not set a locale — it relies on auto-detection. When the acoustic signal is weak or ambiguous, it may produce text in the wrong language or fabricate content from its training data.

Found **6** likely hallucinations (WER ≥ 0.8 and ≤ 1 word overlap with reference):

| Audio | Dataset | Sample | WER | Boundary | Reference | Hypothesis |
|---|---|---|---:|---|---|---|
| [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/023.Sube%20un%20poco%20el%20asiento.wav.wav) | es-ES_DT1 | 1l_es-ES_male-DT1/023.Sube un poco el asiento.wav | 1.000 | skip | `Sube un poco el asiento` | `Chica, ¿cómo me hace el?` |
| [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/045.Activa%20el%20modo%20de%20mantenimiento%20de%20limpiaparabrisas.wav.wav) | es-ES_DT1 | 1l_es-ES_male-DT1/045.Activa el modo de mantenimiento de limpiaparabrisas.wav | 1.000 | skip | `Activa el modo de mantenimiento de limpiaparabrisas` | `À l'essai.` |
| [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/065.Abre%20la%20pantalla%20de%20iterinario.wav.wav) | es-ES_DT1 | 1l_es-ES_male-DT1/065.Abre la pantalla de iterinario.wav | 1.000 | skip | `Abre la pantalla de iterinario` | `眼の中に体が電信になる。` |
| [▶](audio/es-ES_DT2/1l_es-ES_male-DT2/065.Abre%20la%20pantalla%20de%20iterinario.wav.wav) | es-ES_DT2 | 1l_es-ES_male-DT2/065.Abre la pantalla de iterinario.wav | 1.000 | skip | `Abre la pantalla de iterinario` | `Club Deportivo Independiente.` |
| [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/023.Sube%20un%20poco%20el%20asiento.wav.wav) | es-ES_JT1 | 1l_es-ES_male-JT1/023.Sube un poco el asiento.wav | 0.800 | skip | `Sube un poco el asiento` | `Asiento.` |
| [▶](audio/es-ES_JT1/1l_es-ES_male-JT1/065.Abre%20la%20pantalla%20de%20iterinario.wav.wav) | es-ES_JT1 | 1l_es-ES_male-JT1/065.Abre la pantalla de iterinario.wav | 1.000 | skip | `Abre la pantalla de iterinario` | `Apri la storia per il territorio.` |

## Top fast_default vs realtime disagreements

### es-ES_DT1/1l_es-ES_male-DT1/130.¿Cuántos minutos faltan para llegar.wav [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/130.%C2%BFCu%C3%A1ntos%20minutos%20faltan%20para%20llegar.wav.wav)  Δwer=1.000  (fast_default=0.000, realtime=1.000)  speech=[-s, -s] fix=skip
- ref:           `¿Cuántos minutos faltan para llegar`
- fast_default   `¿Cuántos minutos faltan para llegar?`
- fast_llm       `¿Cuántos minutos faltan para llegar?`
- fast_mai       `Unos minutos faltan para llegar.`
- realtime       ``
- realtime_refine `para llegar.`

### es-ES_DT1/1l_es-ES_male-DT1/109.Ve a la página siguiente.wav [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/109.Ve%20a%20la%20p%C3%A1gina%20siguiente.wav.wav)  Δwer=1.000  (fast_default=0.000, realtime=1.000)  speech=[-s, -s] fix=skip
- ref:           `Ve a la página siguiente`
- fast_default   `Ve a la página siguiente.`
- fast_llm       `Vea la página siguiente.`
- fast_mai       `Vea a la página siguiente.`
- realtime       ``
- realtime_refine `Ve a la página siguiente.`

### es-ES_DT2/1l_es-ES_male-DT2/023.Sube un poco el asiento.wav [▶](audio/es-ES_DT2/1l_es-ES_male-DT2/023.Sube%20un%20poco%20el%20asiento.wav.wav)  Δwer=0.800  (fast_default=0.200, realtime=1.000)  speech=[-s, -s] fix=skip
- ref:           `Sube un poco el asiento`
- fast_default   `Un poco el asiento.`
- fast_llm       `Un poco de asiento.`
- fast_mai       `Suba un poco el asiento.`
- realtime       ``
- realtime_refine `Sube un poco el asiento.`

### es-ES_DT1/1l_es-ES_male-DT1/065.Abre la pantalla de iterinario.wav [▶](audio/es-ES_DT1/1l_es-ES_male-DT1/065.Abre%20la%20pantalla%20de%20iterinario.wav.wav)  Δwer=0.600  (fast_default=0.400, realtime=1.000)  speech=[-s, -s] fix=skip
- ref:           `Abre la pantalla de iterinario`
- fast_default   `Abre la pantalla.`
- fast_llm       `眼の中に体が電信になる。`
- fast_mai       ``
- realtime       ``
- realtime_refine `Abre la pantalla.`

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

## Caveats

- **UPL is anchored on the realtime SDK's word-end timestamp** for each sample, so all services use the same `speech_end`. The CSV's `upl_self_ms` column has each service's own phrase-derived value if you want to see how its boundary detection differs.
- **Mazda voice commands** are short utterances (typically 2-8 words). WER on short references is noisier — a single word error on a 3-word command gives 33% WER.