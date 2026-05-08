# German (de-DE) ASR Benchmark Justification

**Test:** Mazda voice commands | **Date:** 2026-05-08 | **Locale:** de-DE | **Datasets:** DT1, DT2, JT1 (30 samples each, 90 total)

---

## Headline numbers

| Dataset | Best service | Filtered WER | Filtered SER | N (of 30) |
|---------|-------------|---:|---:|---:|
| DT1 | fast_mai | 0.479 | 0.857 | 21 |
| DT2 | fast_llm | 0.473 | 0.692 | 13 |
| JT1 | fast_mai | 0.463 | 0.792 | 24 |

Across all datasets, filtered WER ranges from 0.46 to 0.62. German is by far the worst-performing of the five benchmarked languages.

## One-line take

German recognition is fundamentally unreliable at present: every service misrecognises roughly half of all words even after excluding broken samples, and 32 of 90 samples had to be excluded due to empty hypotheses or mislabelled references, making this the lowest-quality test run across all languages.

## Where WER is misleading

WER overstates the gap between services because of German compound-word segmentation. "Klingelton stummschalten" versus "Klingelton stumm schalten" scores as WER 1.0 for fast_default even though the semantic content is identical -- the service simply inserted a space inside a compound. Across the board, compound words like "Ausenluftzirkulation" and "Rucksitzbeluftung" inflate substitution counts because a partial misrecognition of a single long compound registers as a full-word substitution rather than a minor phonetic slip.

Conversely, WER understates the severity of the language-confusion failures. When a service returns "Next term seat in the induit" for "Wechseln Sie...", WER treats each wrong word as an ordinary substitution, but the output is functionally useless -- the engine did not even identify the input language. These catastrophic failures deserve more weight than garden-variety substitutions.

## Where services disagree

fast_mai leads on DT1 (0.479) and JT1 (0.463) while fast_llm takes DT2 (0.473). The spread between best and worst service within a dataset is modest: 14 percentage points on DT1 (0.479 vs 0.620), 10 on DT2 (0.473 vs 0.576), and 7 on JT1 (0.463 vs 0.535). No service dominates decisively.

The realtime service stands out for a different reason: it is the primary contributor to the 27 empty-hypothesis samples, concentrated on the female speaker. DT2 lost 17 of its 30 samples to empty hypotheses, leaving only 13 for scoring. This makes the DT2 numbers inherently less trustworthy -- the surviving 13 samples may not be representative.

## INS / DEL / SUB shape

The error profiles differ meaningfully across services. Insertion rates are uniformly low at 0--6 per 100 words, so no service hallucinates extra content. The important split is between deletions and substitutions.

Realtime carries the highest deletion rates at 17--27 per 100 words. It drops compound words entirely rather than attempting them, which partly explains its empty-hypothesis problem: if the engine cannot latch onto any German phonemes, it returns nothing. Fast_llm goes the other direction with the highest substitution rates at 27--43 per 100 words -- it always produces output but frequently picks the wrong word, including cross-language confusions. Fast_mai achieves the lowest overall error rates by balancing both failure modes.

## Latency

All latencies are inflated by the Tokyo-to-East-US path (233 ms TCP ping). Within that context:

| Service | UPL mean (ms) | UPL p90 (ms) |
|---------|---:|---:|
| realtime | 660--760 | 860--960 |
| fast_mai | 880--1000 | 1040--1100 |
| realtime_refine | 1090--1260 | 1190--1500 |
| fast_llm | 1100--1300 | 1150--2200 |
| fast_default | 1200--1500 | 1200--2600 |

Realtime is fastest but its high skip rate (35 of 90 boundary samples) and empty-hypothesis problem undermine the speed advantage. Fast_mai offers the best accuracy-latency trade-off: second-fastest with the tightest p90 spread and the best WER on two of three datasets.

## Recommendations

1. **fast_mai is the recommended service for German.** It leads on accuracy in DT1 and JT1, is competitive on DT2, and delivers the second-lowest latency with the most consistent p90. Its error profile is the most balanced, avoiding both the deletion failures of realtime and the substitution-heavy output of fast_llm.

2. **Retest with improved data quality before drawing deployment conclusions.** With 36% of samples excluded, the filtered results rest on a narrow foundation. The female-speaker empty-hypothesis problem on realtime needs investigation -- it may be a microphone or encoding issue rather than a service deficiency.

3. **Add a German compound-word normaliser to the evaluation pipeline.** Splitting "stummschalten" into "stumm schalten" (or vice versa) is not a recognition error in any meaningful sense. A normalisation step that merges or splits known compounds before WER calculation would give a truer picture of service quality.

4. **Investigate the language-confusion failures.** Multiple services returned English text for German input. If this is triggered by specific phonetic patterns or audio characteristics, a language-detection pre-check could route those samples to a retry or fallback path in production.
