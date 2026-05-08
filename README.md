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

WER numbers below use **loose-match normalization**: compound-word splits (`stummschalten` ↔ `stumm schalten`), alphanumeric spacing (`2D` ↔ `2 D`), degree/percent symbol variants, and reference typos (`d'emergenzaa`) are normalized before scoring. No samples are excluded — all 90 samples per language are included. Strict (pre-normalization) CSVs are saved as `*.csv.strict`.

| Language | Best Service | WER Range | Samples |
|---|---|---|---:|
| **it-IT** | realtime_refine | 0.096 – 0.119 | 90 |
| **fr-FR** | realtime_refine | 0.094 – 0.148 | 90 |
| **es-ES** | fast_mai | 0.139 – 0.217 | 90 |
| **en-GB** | fast_mai | 0.188 – 0.255 | 90 |
| **de-DE** | fast_mai | 0.443 – 0.537 | 90 |

### Key Findings

1. **Italian and French are the best-performing languages** — both under 0.15 WER across all services.

2. **English (GB) shows the largest DT vs JT gap** — JT1 WER is 0.05–0.11 (near-perfect) while DT sits at 0.20–0.34. Static commands are well-handled; dynamic ones challenge all services.

3. **German is the worst-performing language** — WER 0.44–0.54 with many empty-hypothesis cases and frequent language confusion (fast_llm misrecognizes German as English). Compound words ("Außenluftzirkulation", "Rücksitzbelüftung") cause genuine errors beyond what normalization can fix.

4. **fast_llm hallucinates across all languages** — because it does not set a locale, it auto-detects language and often produces English text for non-English audio, or fabricates content entirely. German is worst affected (27 hallucinations). See each language's error analysis for details.

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
