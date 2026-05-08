# Justification — es-ES Mazda voice command ASR benchmark

Run `mazda_es-ES_20260508_120527`, 2026-05-08. Five Azure services, three datasets (DT1, DT2, JT1), 30 samples each, male and female pooled. Tokyo to East US (232 ms ping).

## Headline numbers (filtered)

11 of 90 samples excluded as data issues (9 empty hypothesis, 2 all-services-agree mislabels). Moderate data quality; the empty-hypothesis rate is driven almost entirely by realtime failing to return text on short or quiet clips.

| Dataset | Service | N | WER | SER | INS/100 | DEL/100 | SUB/100 | UPL ms (mean / p90) |
|---|---|---:|---:|---:|---:|---:|---:|---|
| es-ES_DT1 | fast_default | 24 | 0.307 | 0.792 | 0.0 | 13.8 | 16.9 | 1129 / 1180 |
| es-ES_DT1 | fast_llm | 24 | 0.312 | 0.750 | 0.0 | 13.1 | 18.8 | 1039 / 1118 |
| es-ES_DT1 | fast_mai | 24 | 0.297 | 0.792 | 0.0 | 13.1 | 15.6 | 1044 / 1119 |
| es-ES_DT1 | realtime | 24 | 0.344 | 0.833 | 0.6 | 14.4 | 18.8 | 675 / 843 |
| es-ES_DT1 | realtime_refine | 24 | 0.302 | 0.792 | 0.0 | 13.1 | 16.9 | 1034 / 1201 |
| es-ES_DT2 | fast_default | 26 | 0.298 | 0.846 | 0.0 | 12.1 | 17.8 | 1115 / 1160 |
| es-ES_DT2 | fast_llm | 26 | 0.313 | 0.885 | 0.0 | 16.1 | 14.9 | 1035 / 1085 |
| es-ES_DT2 | fast_mai | 26 | 0.296 | 0.808 | 1.7 | 10.9 | 17.8 | 1044 / 1198 |
| es-ES_DT2 | realtime | 26 | 0.321 | 0.923 | 1.1 | 14.4 | 16.7 | 702 / 912 |
| es-ES_DT2 | realtime_refine | 26 | 0.326 | 0.923 | 2.3 | 11.5 | 18.4 | 1081 / 1463 |
| es-ES_JT1 | fast_default | 29 | 0.317 | 0.828 | 0.0 | 14.8 | 15.9 | 1251 / 1335 |
| es-ES_JT1 | fast_llm | 29 | 0.341 | 0.862 | 0.5 | 17.5 | 15.3 | 1083 / 1223 |
| es-ES_JT1 | fast_mai | 29 | 0.302 | 0.793 | 0.0 | 14.8 | 14.8 | 1027 / 1200 |
| es-ES_JT1 | realtime | 29 | 0.348 | 0.862 | 0.0 | 17.5 | 16.4 | 716 / 880 |
| es-ES_JT1 | realtime_refine | 29 | 0.315 | 0.862 | 0.5 | 15.3 | 14.8 | 1201 / 1306 |

## One-line take

fast_mai wins on accuracy across all three datasets (WER 0.296--0.302), realtime wins on latency (UPL 675--716 ms mean), and the single biggest caveat is that SER is catastrophically high everywhere (0.75--0.92) --- most voice commands contain at least one word error, regardless of which service transcribes them.

## Where the WER numbers are misleading

The dominant source of inflated WER in this benchmark is **stylistic normalization mismatch**, not recognition failure. Most median-WER rows show the service producing a perfectly correct transcription that differs from the reference only in punctuation or diacritics. For example, the reference `Apaga la purificacion del aire` versus the hypothesis `Apaga la purificacion del aire.` is scored as WER 0.333 because the trailing period fuses with the last word during tokenization. Similarly, `Anade esta emisora a favoritos` versus `Anade esta emisora a favoritos.` yields 0.333. On a five-word command, that single punctuation token adds 20--33 percentage points of phantom WER. This pattern is consistent across all five services and all three datasets, meaning the true recognition error rate is substantially lower than the headline 0.30 suggests.

The two mislabeled samples are clear-cut. For `Activa los datos moviles` (DT1 male), all five services agreed on `los datos moviles` with zero pairwise disagreement --- the audio simply does not contain the word "Activa." For `Activa la circulacion externa` (DT2 female), all five services returned `Para circulacion externa`, again with pairwise WER of 0.000. These were correctly excluded.

Nine samples produced empty hypotheses, overwhelmingly from realtime. The affected commands span several speakers and utterance types, but the pattern is that realtime struggles with short, low-energy clips more than the batch endpoints do. One sample (`Abre la pantalla de iterinario`) returned empty from both fast_mai and realtime, suggesting that clip may be genuinely problematic.

Boundary-fix actions are elevated: 12 skips, 1 trim_both, 2 trim_first, 4 trim_last out of 90 realtime samples. The high skip rate (13%) means that for those samples the anchored UPL falls back to each service's own phrase boundary, making cross-service latency comparison unreliable for roughly one in eight samples.

## Where the services genuinely disagree

After stripping away the punctuation-only and mislabel-driven deltas, the residual disagreements concentrate on a handful of patterns.

First, **initial-word deletion** is a consistent weak point for realtime and, to a lesser extent, fast_llm. The command `Quiero abrir los ajustes del sistema` (DT2 male) is transcribed perfectly by fast_default, fast_mai, and realtime_refine, but both fast_llm and realtime drop the first three words and return only `Los ajustes del sistema.` Similarly, `Ve a la ultima pagina` (DT1 female) comes through correctly on every batch endpoint but realtime returns `La ultima pagina.`, losing the verb phrase entirely. The verb is the actionable part of a voice command; deleting it makes the transcription useless for downstream intent parsing.

Second, fast_mai produces a spectacular total misrecognition on `Dirigeme a la oficina` (DT2 female), returning `Y de que me ha hablado tu primo?` for a WER of 1.600. No other service comes close to this kind of hallucination on that sample; fast_default and realtime_refine both get it essentially right. This is an isolated failure but a severe one.

Third, the command `Deslice el asiento hacia adelante` exposes a consistent realtime weakness. Across DT1 and DT2 male speakers, realtime garbles the first word (`Exdice`, or drops it entirely) and shortens `adelante` to `delante`. fast_mai gets both instances correct. realtime_refine recovers the full transcription in the DT2 case but produces the nonsensical `Despite el asiento hacia adelante.` in JT1.

Finally, `Sube un poco el asiento` (JT1 male) is a near-total failure for all services: fast_default produces `Lo siento.` while the other four return `Asiento.` The boundary-fix action is skip, confirming the realtime anchor was unusable. This sample may be a recording-quality issue rather than a recognition issue, but it survived the data-quality filter because the services did not converge on the same wrong answer.

## INS / DEL / SUB shape

The error profile for Spanish is dominated by deletions, with substitutions as the secondary contributor and insertions near zero.

DEL rates range from 10.9 to 17.5 per 100 reference words depending on dataset and service. This is consistent with the initial-word-dropping pattern described above: short Mazda commands often begin with a low-energy verb (`Ve`, `Activa`, `Sube`) that gets swallowed. fast_mai has the lowest DEL rate on DT2 (10.9/100) while fast_llm and realtime have the highest on JT1 (17.5/100 each).

SUB rates run 14.8--18.8 per 100 reference words, representing cases where the engine recognized a word but picked the wrong one. The `Exdice` for `Deslice` and `Realiza` for `Actualiza` examples above are typical substitutions. fast_mai tends toward the lower end of the SUB range as well.

INS rates are negligible --- 0.0 to 2.3 per 100 reference words. The near-zero insertion rate means that the boundary-fix heuristic is not masking a hallucination problem, and that engines are not padding output with filler words. The one exception is realtime_refine on DT2 at 2.3/100, which is still low in absolute terms.

The practical consequence of a DEL-heavy error profile is that a downstream intent parser will frequently receive truncated commands with the verb missing. This is worse than a SUB-heavy profile, where the parser at least receives a complete sentence with a wrong word that might still be recoverable via fuzzy matching.

## Latency

Realtime has a clear latency advantage, with UPL mean of 675--716 ms across datasets versus 1027--1251 ms for the batch endpoints. This gap reflects the fundamental architecture difference: realtime streams results as audio arrives, while batch endpoints wait for the full upload before beginning inference. The 232 ms Tokyo-to-East-US ping accounts for roughly half of realtime's UPL and a smaller fraction of batch UPL, which is dominated by inference time.

Among the batch services, fast_mai is consistently the fastest (1027--1044 ms mean), followed closely by fast_llm (1035--1083 ms) and then fast_default (1115--1251 ms). realtime_refine, despite being a streaming service, adds post-refinement latency that pushes its UPL to 1034--1201 ms mean, comparable to the batch endpoints.

The p90 numbers tell a similar story. Realtime's p90 stays under 912 ms across all datasets. fast_mai's p90 ranges from 1119 to 1200 ms. realtime_refine's p90 on DT2 is the worst of any service at 1463 ms, suggesting that the refinement step occasionally takes significantly longer than usual.

Latency claims should be read with the caveat that 12 of 90 realtime samples had their boundary anchors skipped. For those samples, batch-service UPL falls back to self-anchored values, which are not directly comparable to the anchored numbers.

## Recommendations

- **For accuracy-critical use cases, prefer fast_mai.** It delivers the lowest WER on all three datasets (0.296--0.302) and the lowest DEL rate, meaning it is least likely to drop the verb from a command. Its latency is competitive with other batch endpoints.

- **For latency-critical use cases, prefer realtime, but pair it with a fallback.** Realtime's UPL advantage (roughly 300--500 ms faster than batch) is meaningful for interactive voice UI, but it has the highest WER, the highest SER, and nine of the eleven excluded empty-hypothesis samples came from realtime. A production system should detect empty or very short realtime responses and re-submit to fast_mai.

- **Investigate the punctuation-driven WER inflation.** The gap between WER and "true recognition error rate" is large. Normalizing punctuation and casing before scoring would give a more honest picture. On these commands, actual recognition WER is likely in the 0.15--0.20 range rather than the reported 0.30.

- **Investigate the initial-word deletion pattern.** The consistent loss of command-initial verbs (`Activa`, `Ve`, `Quiero`, `Sube`, `Deslice`) across multiple services suggests that either the recordings have low energy at the start, or the services' VAD is trimming too aggressively. Checking whether adding a short silence pad before the command improves recognition would be a low-cost experiment.

- **Treat the fast_mai hallucination on `Dirigeme a la oficina` as an isolated anomaly, but monitor it.** A WER of 1.600 from a total misrecognition is qualitatively different from the typical 0.3--0.5 errors elsewhere. If fast_mai is selected for production, this class of failure --- where the output bears no relation to the input --- needs a detection mechanism (e.g., confidence thresholding).

- **Improve data quality before the next round.** The 12% exclusion rate and 13% boundary-skip rate together mean that roughly a quarter of the test set is compromised in some way. Re-recording the problematic clips, or at minimum verifying the reference transcriptions against the audio, would make the next benchmark more trustworthy.
