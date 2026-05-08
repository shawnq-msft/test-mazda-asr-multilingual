# Justification — mazda_fr-FR_20260508_131357

## Headline numbers (filtered, excludes data issues)

16 of 90 samples were excluded before scoring: 1 empty hypothesis and 15 where all five services agreed on a transcript that diverged from the reference. This is the highest mislabel rate of any language tested so far, and it means the filtered set is working from only 74 samples (23 DT1, 26 DT2, 25 JT1).

| Dataset | Service | N | WER | SER | INS/100 | DEL/100 | SUB/100 | UPL ms (mean / p90) |
|---|---|---:|---:|---:|---:|---:|---:|---|
| fr-FR_DT1 | fast_default | 23 | 0.318 | 0.696 | 1.4 | 13.2 | 18.8 | 1183 / 1256 |
| fr-FR_DT1 | fast_llm | 23 | 0.368 | 0.739 | 2.8 | 11.1 | 23.6 | 1038 / 1078 |
| fr-FR_DT1 | fast_mai | 23 | 0.306 | 0.783 | 2.1 | 10.4 | 20.8 | 1027 / 1124 |
| fr-FR_DT1 | realtime | 23 | 0.318 | 0.696 | 2.1 | 9.7 | 22.2 | 750 / 910 |
| fr-FR_DT1 | realtime_refine | 23 | 0.285 | 0.696 | 1.4 | 9.7 | 20.1 | 1132 / 1288 |
| fr-FR_DT2 | fast_default | 26 | 0.313 | 0.731 | 1.2 | 15.9 | 17.1 | 1170 / 1239 |
| fr-FR_DT2 | fast_llm | 26 | 0.391 | 0.769 | 5.5 | 15.2 | 22.0 | 1053 / 1122 |
| fr-FR_DT2 | fast_mai | 26 | 0.364 | 0.846 | 5.5 | 12.2 | 24.4 | 1039 / 1096 |
| fr-FR_DT2 | realtime | 26 | 0.340 | 0.769 | 1.2 | 12.8 | 22.0 | 797 / 1003 |
| fr-FR_DT2 | realtime_refine | 26 | 0.303 | 0.731 | 1.8 | 12.2 | 18.9 | 1233 / 1503 |
| fr-FR_JT1 | fast_default | 25 | 0.284 | 0.760 | 0.6 | 9.7 | 20.1 | 1150 / 1221 |
| fr-FR_JT1 | fast_llm | 25 | 0.265 | 0.760 | 0.6 | 9.1 | 18.8 | 1033 / 1101 |
| fr-FR_JT1 | fast_mai | 25 | 0.282 | 0.800 | 1.3 | 9.1 | 20.1 | 1064 / 1174 |
| fr-FR_JT1 | realtime | 25 | 0.265 | 0.720 | 0.6 | 9.1 | 18.8 | 674 / 857 |
| fr-FR_JT1 | realtime_refine | 25 | 0.285 | 0.760 | 0.6 | 9.7 | 19.5 | 1127 / 1275 |

## One-line take

Realtime_refine and realtime trade the accuracy lead depending on dataset, but the gaps are small; realtime is by far the fastest service (UPL 674-797 ms mean), while realtime_refine adds roughly 350-450 ms of post-refinement delay for marginal WER improvement. Fast_llm is the weakest engine for French and occasionally hallucinates in English. The single biggest caveat is that 15 reference labels are almost certainly wrong, making the unfiltered WER table unreliable for any service comparison.

## Where the WER numbers are misleading

The dominant source of noise in this benchmark is not recognition error but reference-label quality. Fifteen samples were flagged as probable mislabels because all five services converge on the same transcript while the reference diverges. The root cause is a character-encoding mismatch: reference labels stored with mojibake (e.g. `L├¿ve l├⌐g├¿rement le coussin s'il te pla├«t` instead of `Leve legerement le coussin s'il te plait`) produce spurious word-error counts even though every service transcribed the audio correctly. The same file names appear across DT1, DT2, and JT1, so the same encoding bug inflates WER three times over.

The single empty-hypothesis row is `Va a la page suivante` (DT1, male), where realtime returned nothing. This sample was skipped entirely rather than counted.

Beyond the filtered rows, several median-quality samples show WER inflated by stylistic deltas rather than meaning errors. For instance, `Ouvre le centre multimedia local` is transcribed correctly by every service in the filtered set, but the accented reference form (`multim├⌐dia`) versus the hypothesis `multimedia` registers as a substitution after normalization. Similarly, `Augmenter un peu la temperature du conducteur` is penalized when fast_default outputs `Augmentez` (imperative vous-form) versus the infinitive reference `Augmenter` -- a conjugation choice, not a recognition failure.

Boundary-fix trimming affected 22 of 90 realtime samples (14 trim_both, 2 trim_first, 6 trim_last). For example, `Active le mode scenario` (DT1, male) had realtime produce `Qui va le mode scenario ?` with a hallucinated leading phrase; the trim_both action removed the edge words. Without the trim, UPL for that sample would have been anchored on a later speech_end, making all five services look artificially slower.

## Where the services genuinely disagree

After stripping out encoding artifacts and mislabels, the most instructive disagreements cluster around three patterns.

First, the `Ajoute Starbucks comme etape` sample exposes fast_default's weakness on proper nouns in short context. In DT1, fast_default emitted just `Starbucks.` (WER 0.750), dropping the verb and noun entirely, while fast_llm went further off the rails with the English hallucination `I would start mix.` (WER 1.000). Fast_mai and realtime_refine both got this right. In JT1, fast_default produced `Ajoute Starbucks Computer.` while realtime nailed it. This sample is a clear win for fast_mai and realtime_refine.

Second, the male speaker's `Ferme la vitre arriere droite` (DT2) is a catastrophic failure for fast_llm (`The film is a remake of the 1992 Malayalam film.`, WER 1.667) and fast_mai (`Pour l'atomes, leur but est de parier a 2 lots.`, WER 1.833). Both services apparently language-switched to English or produced nonsense French, suggesting the audio's late speech onset (trim_first, speech starting at 4.22 s) left insufficient context for the batch endpoint. Realtime produced `Terme, arbitre arriere droite.` (WER 0.833), garbled but at least French. This is a boundary artifact: the speech was clipped to a very short window, and the batch services hallucinated.

Third, `Active le mode refroidissement` (DT2) shows a clean split: fast_default got it perfect while realtime substituted `refondation` for `refroidissement`, and fast_mai produced `mode de previsualisation`. The LLM-enhanced fast_llm dropped the last word entirely (`Active le mode.`). Only fast_default and realtime_refine handled this utterance without error.

## INS / DEL / SUB shape

Across all datasets and services, the error profile is dominated by substitutions (17-25 per 100 reference words) with deletions second (9-16 per 100) and insertions a distant third (0.6-5.5 per 100). This is the expected shape for short command utterances: words are rarely hallucinated from nothing, but the engine frequently picks the wrong word from a similar-sounding candidate (e.g. `serre` for `5`, `centre` for `sombre`, `cheval` for `chauffage`).

Fast_default consistently shows the highest deletion rate among the five services (13.2-15.9 per 100 on DT1/DT2), meaning it is the most likely to simply drop words from the hypothesis. This is visible in the `Ajoute Starbucks comme etape` example where fast_default deleted three of four words. By contrast, fast_llm and fast_mai in DT2 show the highest insertion rate (5.5 per 100 each), driven partly by the hallucinated English sentences on the `Ferme la vitre` sample.

Realtime and realtime_refine have the most balanced error profile: lower deletion rates (9.1-12.8 per 100) and modest insertion rates (0.6-2.1 per 100), with substitutions carrying most of the WER. The boundary-fix heuristic contributes to this balance by trimming hallucinated edge words that would otherwise inflate the insertion count.

## Latency

Realtime is the clear latency winner. Its mean UPL ranges from 674 ms (JT1) to 797 ms (DT2) with p90 under 1003 ms across all datasets. The negative LBL values (mean around -1600 ms) confirm that the SDK is emitting the final recognized event well before the last audio chunk is pushed -- the streaming pipeline runs ahead of I/O, so from the user's perspective the result is ready almost instantly after they stop speaking.

Realtime_refine adds its post-refinement pass on top, pushing mean UPL to 1127-1233 ms and p90 to 1275-1503 ms. The refinement adds roughly 350-450 ms of wall-clock delay versus plain realtime, which may or may not be acceptable depending on the in-car interaction design.

Among the batch (fast_*) services, fast_mai is fastest (mean UPL 1004-1049 ms), followed by fast_llm (1038-1092 ms) and fast_default (1150-1300 ms). The ordering is consistent across all three datasets. All batch UPL values include the Tokyo-to-East-US round trip (237 ms TCP ping); co-locating the client with the Azure region would shave roughly 450-500 ms of round-trip overhead from every batch call.

First latency is only measured for the realtime services and sits at 1292-1462 ms mean (p90 1593-1933 ms). This is the time from the user's first spoken word to the first partial (recognizing) event. For a voice-command system the first partial is less important than the final result, but it can be used to drive visual feedback in the HMI.

## Recommendations

- **For lowest latency, use realtime.** It delivers the final result 350-500 ms before any other service and its accuracy is competitive (best or tied-best on JT1, within 2 points of the leader on DT1/DT2). The negative LBL means the result is available before the audio stream is even fully transmitted.

- **For best accuracy, use realtime_refine on DT1/DT2 and realtime or fast_llm on JT1.** Realtime_refine leads on DT1 (0.285) and DT2 (0.303) by a small margin over the next-best service, but on JT1 it is tied or slightly behind realtime and fast_llm (0.265 each). The accuracy gain from refinement is modest -- roughly 2-4 WER points -- and comes at a latency cost.

- **Fix the reference labels before drawing production conclusions.** Sixteen exclusions out of 90 samples (17.8%) is unacceptably high. The encoding issue that produces mojibake in accented French words (e, a, i, c) should be resolved at the dataset level; once fixed, the filtered and unfiltered WER should converge and the effective sample size increases by over 20%.

- **Investigate fast_llm's language-switching behavior.** Two samples produced English-language hallucinations (`I would start mix.`, `The film is a remake of the 1992 Malayalam film.`). The LLM-enhanced endpoint does not take an explicit locale parameter (it infers language), and on short or boundary-clipped French audio it can misidentify the language. If fast_llm is considered for production, adding a locale hint (if the API supports it in future) or pre-filtering audio duration would mitigate this.

- **Do not rely on fast_default for short or clipped utterances.** Its high deletion rate means it tends to drop leading words when the speech onset is late in the audio. The `Ajoute Starbucks comme etape` and `Active le mode scenario` samples illustrate this: fast_default frequently outputs only the tail of the command. Fast_mai handles these cases better.

- **Co-locate the benchmark client with the Azure region for a production-representative latency baseline.** The current Tokyo-to-East-US path adds ~237 ms each way. The batch endpoints would benefit most, potentially bringing fast_mai UPL below 600 ms and making it competitive with realtime for use cases where streaming is not required.
