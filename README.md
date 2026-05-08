# Mazda ASR Multilingual WER Benchmark

Benchmarks Azure Speech-to-Text services on Mazda in-car voice commands across 5 European languages, measuring Word Error Rate (WER), Sentence Error Rate (SER), and latency.

## Test Configuration

| Parameter | Value |
|---|---|
| Azure region | East US |
| Tester location | Tokyo, Japan (Microsoft Corporation) |
| TCP ping | ~233 ms |
| Samples per dataset | 30 (random, seed=42) |
| Speakers | Male + female pooled |
| Date | 2026-05-08 |

## Services Under Test

| Service | Description |
|---|---|
| `fast_default` | Azure Fast Transcription (REST, api-version 2024-11-15) |
| `fast_llm` | Fast Transcription + LLM enhanced mode (preview, 2025-10-15) |
| `fast_mai` | Fast Transcription + mai-transcribe-1 model (preview) |
| `realtime` | Speech SDK continuous recognition (WebSocket) |
| `realtime_refine` | Speech SDK + Post-Stream Refinement (MRS preview, SDK 1.49.0+) |

## Datasets

Each language has 3 datasets:
- **DT1** / **DT2** — Dynamic voice commands (two recording sessions)
- **JT1** — Static/fixed voice commands

Total: 5 languages × 3 datasets × 30 samples × 5 services = **2,250 transcriptions**

## Summary of Results

| Language | Best Service | Filtered WER Range | Samples Kept | Data Quality |
|---|---|---|---:|---|
| **it-IT** | fast_mai / realtime | 0.093 – 0.232 | 86 / 90 | Excellent |
| **en-GB** | fast_llm (JT), fast_mai (DT) | 0.048 – 0.342 | 87 / 90 | Excellent |
| **es-ES** | fast_mai | 0.296 – 0.348 | 79 / 90 | Moderate |
| **fr-FR** | realtime_refine | 0.324 – 0.422 | 74 / 90 | Poor (15 mislabels) |
| **de-DE** | fast_mai | 0.463 – 0.620 | 58 / 90 | Poor (27 empty hyp) |

### Key Findings

1. **Italian is the best-performing language** — JT1 achieves 0.093 WER with fast_mai and realtime tied. All services perform within a narrow band.

2. **English (GB) shows the largest DT vs JT gap** — JT1 WER is 0.05–0.11 (near-perfect) while DT sits at 0.20–0.34. Static commands are well-handled; dynamic ones challenge all services.

3. **German is the worst-performing language** — WER 0.46–0.62 even after excluding 32 problematic samples. Services frequently misrecognize German as English. Compound words ("Außenluftzirkulation", "Rücksitzbelüftung") and word segmentation ("stummschalten" vs "stumm schalten") inflate errors.

4. **Spanish has uniformly high SER (0.75–0.92)** despite moderate WER — nearly every command has at least one word wrong. Initial-word deletion ("Activa" dropped) is the dominant error pattern.

5. **French suffers from label quality** — 15 of 90 samples excluded as mislabeled (reference encoding issues). After filtering, WER is 0.32–0.42.

6. **fast_mai is the most consistent winner on accuracy** across languages, while **realtime delivers the lowest latency** (UPL 560–780 ms vs 880–1300 ms for batch services).

7. **realtime_refine helps on dynamic commands** but adds 400–600 ms UPL and sometimes degrades accuracy on static commands (en-GB DT2, it-IT JT1).

## Reports by Language

### de-DE (German)

- [Report](results/mazda_de-DE_20260508_112711_report.md)
- [Error Analysis](results/mazda_de-DE_20260508_112711_error_analysis.md)
- [Justification](results/mazda_de-DE_20260508_112711_justification.md)
- [CSV](results/mazda_de-DE_20260508_112711.csv)

### en-GB (British English)

- [Report](results/mazda_en-GB_20260508_115844_report.md)
- [Error Analysis](results/mazda_en-GB_20260508_115844_error_analysis.md)
- [Justification](results/mazda_en-GB_20260508_115844_justification.md)
- [CSV](results/mazda_en-GB_20260508_115844.csv)

### es-ES (Spanish)

- [Report](results/mazda_es-ES_20260508_120527_report.md)
- [Error Analysis](results/mazda_es-ES_20260508_120527_error_analysis.md)
- [Justification](results/mazda_es-ES_20260508_120527_justification.md)
- [CSV](results/mazda_es-ES_20260508_120527.csv)

### fr-FR (French)

- [Report](results/mazda_fr-FR_20260508_131357_report.md)
- [Error Analysis](results/mazda_fr-FR_20260508_131357_error_analysis.md)
- [Justification](results/mazda_fr-FR_20260508_131357_justification.md)
- [CSV](results/mazda_fr-FR_20260508_131357.csv)

### it-IT (Italian)

- [Report](results/mazda_it-IT_20260508_133009_report.md)
- [Error Analysis](results/mazda_it-IT_20260508_133009_error_analysis.md)
- [Justification](results/mazda_it-IT_20260508_133009_justification.md)
- [CSV](results/mazda_it-IT_20260508_133009.csv)

## Latency Note

All tests were run from Tokyo to Azure East US (~233 ms TCP ping). Absolute latency numbers are inflated by this cross-Pacific round trip. Relative comparisons between services remain valid since all share the same network path.

## Reproduction

```bash
# Install dependencies
python3 -m pip install -r requirements.txt

# Run one language
python3 -X utf8 run_full.py --languages it-IT --max-per-dataset 30

# Run all languages
python3 -X utf8 run_full.py

# Regenerate reports from existing CSVs (no re-testing)
python3 -X utf8 -c "
from pathlib import Path
from benchmark.report import build_report
from scripts.error_analysis import main as ea_main
for csv_path in sorted(Path('results').glob('mazda_*.csv')):
    build_report(csv_path, csv_path.with_name(csv_path.stem + '_report.md'))
    ea_main(csv_path, csv_path.with_name(csv_path.stem + '_error_analysis.md'))
"
```
