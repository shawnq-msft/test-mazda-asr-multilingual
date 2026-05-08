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

WER numbers below are **loose-match filtered**: compound-word splits (`stummschalten` ↔ `stumm schalten`), alphanumeric spacing (`2D` ↔ `2 D`), degree/percent symbol variants, and reference typos (`d'emergenzaa`) are normalized before scoring. Strict (unfiltered) numbers are in each language's report.

| Language | Best Service | Filtered WER Range | Samples Kept | Data Quality |
|---|---|---|---:|---|
| **es-ES** | fast_mai | 0.071 – 0.142 | 81 / 90 | Moderate (9 empty hyp) |
| **it-IT** | realtime_refine | 0.086 – 0.104 | 85 / 90 | Good (3 compound artifacts) |
| **fr-FR** | realtime_refine | 0.091 – 0.141 | 89 / 90 | Good |
| **en-GB** | fast_llm | 0.165 – 0.232 | 87 / 90 | Excellent |
| **de-DE** | fast_mai | 0.248 – 0.363 | 60 / 90 | Poor (27 empty hyp, 2 compound) |

### Key Findings

1. **Spanish is the best-performing language** — WER 0.071–0.142 across services, with fast_mai leading.

2. **Italian and French perform similarly** — both around 0.09 WER at best. The `d'emergenzaa` reference typo (double-a) previously inflated Italian WER; loose matching corrects this.

3. **English (GB) shows the largest DT vs JT gap** — JT1 WER is 0.05–0.11 (near-perfect) while DT sits at 0.20–0.34. Static commands are well-handled; dynamic ones challenge all services.

4. **German is the worst-performing language** — WER 0.25–0.36 even after excluding 30 problematic samples and applying loose matching. Services frequently misrecognize German as English. Compound words ("Außenluftzirkulation", "Rücksitzbelüftung") still cause genuine errors beyond what normalization can fix.

5. **fast_mai is the most consistent winner on accuracy** across languages, while **realtime delivers the lowest latency** (UPL 560–780 ms vs 880–1300 ms for batch services).

6. **realtime_refine helps on dynamic commands** but adds 400–600 ms UPL and sometimes degrades accuracy on static commands (en-GB DT2, it-IT JT1).

## Reports by Language

### de-DE (German)

- [Report](results/mazda_de-DE_20260508_193734_report.md)
- [Error Analysis](results/mazda_de-DE_20260508_193734_error_analysis.md)
- [CSV](results/mazda_de-DE_20260508_193734.csv)

### en-GB (British English)

- [Report](results/mazda_en-GB_20260508_194552_report.md)
- [Error Analysis](results/mazda_en-GB_20260508_194552_error_analysis.md)
- [CSV](results/mazda_en-GB_20260508_194552.csv)

### es-ES (Spanish)

- [Report](results/mazda_es-ES_20260508_120527_report.md)
- [Error Analysis](results/mazda_es-ES_20260508_120527_error_analysis.md)
- [CSV](results/mazda_es-ES_20260508_120527.csv)

### fr-FR (French)

- [Report](results/mazda_fr-FR_20260508_131357_report.md)
- [Error Analysis](results/mazda_fr-FR_20260508_131357_error_analysis.md)
- [CSV](results/mazda_fr-FR_20260508_131357.csv)

### it-IT (Italian)

- [Report](results/mazda_it-IT_20260508_133009_report.md)
- [Error Analysis](results/mazda_it-IT_20260508_133009_error_analysis.md)
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

# Apply loose matching (compound words, symbol normalization)
python3 -X utf8 scripts/loose_match.py results/mazda_it-IT_*.csv

# Regenerate reports from existing CSVs (no re-testing)
python3 -X utf8 -c "
from pathlib import Path
from benchmark.report import build_report
from scripts.error_analysis import main as ea_main
for csv_path in sorted(Path('results').glob('mazda_*.csv')):
    if '.strict' in csv_path.name: continue
    build_report(csv_path, csv_path.with_name(csv_path.stem + '_report.md'))
    ea_main(csv_path, csv_path.with_name(csv_path.stem + '_error_analysis.md'))
"
```
