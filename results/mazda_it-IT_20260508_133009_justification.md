# Mazda it-IT ASR Benchmark Justification

## Headline numbers

Italian is the strongest language in the Mazda benchmark. Across three datasets (DT1, DT2, JT1) and five Azure services, WER ranges from 0.093 to 0.232. The best single result is JT1 at 0.093 WER, achieved by both fast_mai and realtime. DT1 clusters tightly around 0.15--0.17, while DT2 is the hardest set at 0.18--0.23. SER runs 0.345--0.519, meaning roughly one-third to one-half of utterances contain at least one word-level error.

## One-line take

Italian delivers the lowest WER of any language tested, all five services perform within a narrow band, and data quality is excellent with only 4 of 90 samples excluded.

## Where WER is misleading

WER differences between services on JT1 are essentially noise: all five land between 0.093 and 0.106. Choosing a winner from that spread would be overfit to this sample. On DT2, the gap between realtime (0.232) and realtime_refine (0.180) looks meaningful, but the sample is only 27 utterances after exclusions, so the true confidence interval is wide. The tight clustering of SER values within each dataset (e.g. three services sharing 0.345 on JT1) suggests the same handful of hard utterances drive most errors regardless of engine.

## Where services disagree

Services converge more on Italian than on any other language. On JT1 the maximum WER spread is just 0.013 (0.093 to 0.106). DT2 shows the only notable divergence: realtime at 0.232 versus realtime_refine at 0.180 and fast_mai at 0.185. This suggests realtime struggles with a few DT2 utterances that the refinement pass or the MAI model corrects. On DT1 and JT1, no service stands clearly apart.

## INS/DEL/SUB shape

Deletions dominate the error profile, running 4--17 per 100 words depending on dataset and service. Substitutions are secondary at 6--16 per 100 words. Insertions are very low at 0.6--2.8 per 100 words. Realtime has the highest deletion rate on DT2 (8.8 per 100 words after filtering), which aligns with its elevated WER on that dataset. JT1 has uniformly low error rates across all three categories, consistent with its best-in-class WER. The deletion-heavy profile suggests the main failure mode is missed words rather than hallucinated or swapped ones.

## Latency

All latency figures include a 241 ms Tokyo-to-East-US network hop.

Realtime is fastest, with mean UPL around 560--625 ms and p90 around 790--870 ms. Fast_mai and fast_llm are similar at roughly 890--990 ms mean, with fast_mai showing slightly tighter p90 (1060--1155 ms versus 1115--1190 ms). Fast_default is slowest among the fast-transcription variants at 1010--1160 ms mean. Realtime_refine pays for its accuracy gains with the highest latency: 1040--1260 ms mean and p90 reaching up to 2010 ms.

## Recommendations

1. **For lowest WER on DT-style commands:** realtime_refine edges out the field (0.152 on DT1, 0.180 on DT2) but at the cost of the highest and most variable latency.
2. **For lowest latency with competitive accuracy:** realtime delivers sub-650 ms mean UPL and ties for best WER on JT1 (0.093), though it lags on DT2 (0.232).
3. **Best all-round compromise:** fast_mai offers consistently low WER across all three datasets (0.167, 0.185, 0.093) with moderate latency (~890--940 ms mean), making it the safest single-service choice if one engine must serve all command types.
4. **Data quality is not a concern for Italian.** Only 4 of 90 samples were excluded (2 empty, 2 mislabelled), and boundary adjustments were modest (2 skip, 2 trim_both, 3 trim_first, 3 trim_last). Results can be taken at face value without worrying about systematic data artefacts.
5. **Italian can serve as a baseline for evaluating other languages.** Its low error rates and tight cross-service agreement make it a useful reference point when interpreting noisier results from other locales.
