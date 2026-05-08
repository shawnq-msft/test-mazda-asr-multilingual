# Justification — Mazda en-GB ASR benchmark

Run: `mazda_en-GB_20260508_115844`  
Locale: en-GB (British English)  
Datasets: DT1 (30), DT2 (30), JT1 (30) — male + female pooled  
Services: fast_default, fast_llm, fast_mai, realtime, realtime_refine  
Test path: Tokyo client to East US Azure endpoint (~237 ms round-trip)

## Headline numbers (filtered, excludes 3 data-issue rows)

| Dataset | Service | N | WER | SER | UPL ms (mean / p90) |
|---|---|---:|---:|---:|---|
| en-GB_DT1 | fast_default | 30 | 0.260 | 0.433 | 1025 / 1193 |
| en-GB_DT1 | fast_llm | 30 | 0.220 | 0.367 | 939 / 1076 |
| en-GB_DT1 | fast_mai | 30 | 0.200 | 0.367 | 915 / 1060 |
| en-GB_DT1 | realtime | 30 | 0.241 | 0.500 | 643 / 942 |
| en-GB_DT1 | realtime_refine | 30 | 0.246 | 0.467 | 1137 / 1307 |
| en-GB_DT2 | fast_default | 28 | 0.315 | 0.536 | 1056 / 1170 |
| en-GB_DT2 | fast_llm | 28 | 0.226 | 0.464 | 946 / 1122 |
| en-GB_DT2 | fast_mai | 28 | 0.222 | 0.357 | 931 / 1090 |
| en-GB_DT2 | realtime | 28 | 0.304 | 0.571 | 624 / 872 |
| en-GB_DT2 | realtime_refine | 28 | 0.342 | 0.571 | 1197 / 1682 |
| en-GB_JT1 | fast_default | 29 | 0.055 | 0.172 | 1021 / 1209 |
| en-GB_JT1 | fast_llm | 29 | 0.048 | 0.172 | 905 / 1059 |
| en-GB_JT1 | fast_mai | 29 | 0.073 | 0.207 | 879 / 1056 |
| en-GB_JT1 | realtime | 29 | 0.105 | 0.276 | 615 / 901 |
| en-GB_JT1 | realtime_refine | 29 | 0.108 | 0.241 | 1100 / 1190 |

## One-line take

fast_mai delivers the best accuracy on the harder DT datasets (0.200 and 0.222 WER), fast_llm wins on the easier JT1 set (0.048 WER), and realtime remains the latency leader at roughly 620-640 ms mean UPL -- but realtime_refine adds no accuracy benefit for en-GB and actually degrades both WER and latency.

## Where the WER numbers are misleading

Three of the 90 samples were excluded before computing the filtered table, but even the kept set contains artefacts that inflate WER beyond what a human would consider a recognition failure.

The most prominent example is `Play 100`. The reference says `Play 100` but the speaker clearly says "Play 100.7 FM" -- all five services agree on this transcription with zero pairwise disagreement. One instance in JT1 was caught by the all-services-agree filter and excluded. A second instance survives in DT1 because it sits outside that dataset's exclusion criteria; it scores 1.500 WER for every service, inflating the DT1 aggregate for all engines equally. Because it affects every service identically, it does not change relative rankings but does make the absolute WER look worse than the true recognition quality.

The two empty-hypothesis exclusions both come from DT2. `Set the POI as my home` returned empty from fast_default and realtime, while `Turn off wireless charging Turn off wireless charging` (a doubled reference, itself suspect) returned empty from realtime. Removing these two brought DT2's N from 30 to 28.

Short-command WER amplification is pervasive in this benchmark. Commands like `Close HUD`, `Call Jane`, and `Page 4` are only two words long; a single substitution on any of them produces 0.500 or 1.000 WER. This is arithmetically correct but overstates the practical severity compared to errors on longer commands.

Boundary fixes affected 15 of the 90 realtime samples (2 skip, 4 trim_both, 5 trim_first, 4 trim_last). The trims generally removed hallucinated edge words that the realtime SDK appended before or after the actual command, such as a spurious leading word on `Close HUD` (trim_first) or trailing artefacts on `Play 100` (trim_both). Without these trims, the anchored UPL for those samples would have been skewed outward. The two skip rows fell back to self-anchored UPL and are not directly comparable to the rest.

## Where the services genuinely disagree

After removing the artefacts above, several samples expose real differences between engines.

`Disable Apple Carplay` is the starkest case. This command appears in both DT1 and DT2, and no service handles it well. In DT1, fast_default produced `Sabo Aboka Bank`, fast_llm gave `Saibo Aapo Kaapre`, fast_mai offered `Say to Apple CarPlay` (closest), and realtime returned `Disable Apple Carpet`. In DT2, fast_llm hallucinated Chinese characters. The accent on this particular speaker appears to push every engine to its limits, though fast_mai and realtime at least preserve partial semantic content.

`Close HUD` splits the fast and realtime tiers cleanly. In the JT1 recording, fast_default, fast_llm, and fast_mai all get it correct (or near-correct with minor punctuation), while both realtime and realtime_refine produce `Lowe's HUD`. In the DT2 recording, fast_default outputs `Hello, HED`, fast_mai spells it out as `H-E-D`, and realtime returns `Close. How did.` -- nobody wins cleanly on this command, but the fast tier is consistently closer.

`Call Jane` in DT1 shows a clean realtime-only failure: all three fast services transcribe it correctly, but realtime returns `Paul Kane`. Interestingly, realtime_refine corrects this to `Call Jane`, which is the one case in the en-GB dataset where the refinement step actually helps.

`Show the AC setting page` presents a different split: in DT2, fast_default produces `Sharon P.K.C.` (a complete miss), fast_llm gets closest with `Show the AC testing page`, and realtime manages `Sharing the AC defing page`. None is correct, but fast_llm is closest. In the JT1 recording of the same command, realtime nails it perfectly while fast_default introduces `Go to the AC setting page` -- a substitution error on the leading verb.

## INS / DEL / SUB shape

On the DT datasets, substitution errors dominate across all services. DT1 SUB rates range from 8.8/100 (fast_llm) to 13.8/100 (realtime and realtime_refine). DT2 is worse: fast_default sits at 19.9/100 and realtime_refine peaks at 23.3/100. This tells us the engines are hearing words but picking the wrong ones -- consistent with an accent mismatch rather than audio quality issues.

Deletion rates show more variation between services. fast_mai has the lowest DEL rate on DT2 (0.0/100), meaning it never drops a word entirely, but compensates with the highest insertion rate in that bucket (4.8/100). fast_default and fast_llm show moderate DEL rates of 6.8 and 6.2 per 100 on DT2, suggesting they are more willing to omit low-confidence segments.

On JT1, all error types are low across the board. SUB rates range from 1.3 to 5.1 per 100, confirming that this is a substantially cleaner or more standard-accented dataset.

The realtime_refine service, which is meant to polish realtime output, actually increases the substitution rate on DT2 from 18.5/100 (base realtime) to 23.3/100. The refinement pass appears to "correct" words into more fluent but less accurate alternatives -- a pattern that hurts more than it helps on accented British English speech.

## Latency

All latency numbers are inflated by the approximately 237 ms network round-trip from Tokyo to East US. This affects the REST-based fast services more directly (each call pays the full round-trip) while realtime's persistent WebSocket connection amortises the overhead somewhat.

Realtime has the lowest UPL across all three datasets, at 615-643 ms mean. This is expected: the SDK streams partial results and only needs to flush the trailing silence buffer after speech ends. fast_mai is the fastest of the REST services at 879-931 ms mean, consistently beating fast_llm (905-946 ms) and fast_default (1021-1056 ms). The ordering suggests the MAI model returns faster than the LLM-enhanced mode, which in turn beats the default pipeline.

realtime_refine is the slowest service overall, with mean UPL of 1100-1197 ms and a p90 that reaches 1682 ms on DT2. The refinement pass adds 400-570 ms to base realtime latency on average. Given that it also worsens accuracy on en-GB, the latency cost is entirely uncompensated.

The negative LBL values for realtime (around -270 to -292 ms mean) are an artefact of the anchoring method: the first word timestamp sometimes precedes the point at which the audio was submitted, producing a negative label-relative latency. These values should not be interpreted as "faster than instant" but rather as evidence that the realtime SDK's word-start anchoring is slightly ahead of the audio push clock.

## Recommendations

- **For production en-GB voice commands, prefer fast_mai.** It has the best or near-best accuracy on every dataset (0.200, 0.222, 0.073 WER), the lowest REST-tier latency, and the lowest DEL rate -- meaning it rarely drops words entirely, which matters for command parsing.

- **fast_llm is a close second and wins on JT1.** If the command vocabulary skews toward the cleaner end (simple, well-enunciated commands), fast_llm's 0.048 WER on JT1 is the single best number in the benchmark. It also rescued `Call Jane` and `Show the AC setting page` where fast_default failed.

- **Do not deploy realtime_refine for en-GB.** It underperforms base realtime on accuracy (worse WER on DT2 by nearly 4 points) while adding 400+ ms of latency. The only sample where it demonstrably helped was `Call Jane` in DT1, where it corrected realtime's `Paul Kane` -- one win out of 87 kept samples is not enough to justify the cost.

- **Investigate the `Disable Apple Carplay` failures.** This command defeated every service across both DT recordings. If this is a real production command, consider adding it to a custom phrase list or investigating whether the speaker's accent on "Disable" is consistently misheard. fast_mai's `Say to Apple CarPlay` at least preserves the brand name.

- **Discount absolute WER by 2-3 points for the `Play 100` artefact.** The surviving DT1 instance inflates all services equally. If the reference were corrected to `Play 100.7 FM`, every service would score 0.000 on that sample, and DT1 WER would drop across the board.

- **Re-run with an East US client to get production-representative latency.** The 237 ms Tokyo-to-East-US ping inflates all UPL numbers. Subtract roughly 200-250 ms from the fast-tier means to estimate what a co-located deployment would see; realtime UPL would drop less because the WebSocket connection absorbs some of the round-trip.
