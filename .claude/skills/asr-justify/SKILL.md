---
name: asr-justify
description: Read a Mazda ASR benchmark CSV (and its auto-generated report, error analysis, and word-timing sidecar) and write a subjective-justification markdown file that interprets the numbers across all five services (fast_default, fast_llm, fast_mai, realtime, realtime_refine), flags dataset/scoring artifacts, and surfaces concrete best/median/worst and cross-service disagreement cases. Manual invocation only.
---

# asr-justify

Produce a human-readable companion to an ASR benchmark report. The auto
report is arithmetic; this skill writes the interpretation.

## Inputs

The benchmark covers **five Azure services**:

- `fast_default` — Azure Fast Transcription (api-version `2024-11-15`).
- `fast_llm` — Azure Fast Transcription with `enhancedMode.enabled=true`
  (LLM Speech preview, api-version `2025-10-15`).
- `fast_mai` — Azure Fast Transcription with
  `enhancedMode.model="mai-transcribe-1"` and per-language locale.
- `realtime` — Speech SDK continuous recognition with PushAudioInputStream.
- `realtime_refine` — Realtime with PostProcessingOption=PostRefinement
  (MRS Public Preview, Speech SDK 1.49.0+).

Per run, four artifacts live under `results/`:

| File | Contents |
|---|---|
| `<run>.csv` | Per-sample, per-service results. Columns include `wer`, `sentence_error`, `ins`, `del`, `sub`, `ref_len`, `first_latency_ms`, `lbl_ms`, `upl_ms`, `upl_self_ms`, `upl_anchor`, `speech_start_s`, `speech_end_s`, `boundary_fix_action`, `first_word_start_s`, `last_word_end_s`, `error`, `locale`. |
| `<run>_report.md` | Auto-generated headline aggregate table, dataset / endpoint sections, latency definitions, and a Speech-boundary section listing trimmed samples. |
| `<run>_error_analysis.md` | Companion produced by [scripts/error_analysis.py](../../scripts/error_analysis.py): excludes data-issue rows, lists best/median/worst per (dataset, service), top fast_default-vs-realtime disagreements, with `[▶]` audio links. |
| `<run>_words.jsonl` | One JSON object per realtime sample: full word-level timestamps + the boundary-fix decision. Read this when investigating any sample whose `boundary_fix_action != "none"`. |

The user typically invokes this as: *"justify results/<run>.csv"*. If
they give only the CSV path, derive the report and error-analysis paths
by replacing `.csv` with `_report.md` / `_error_analysis.md`.

## Procedure

1. **Read the auto report's aggregate table** for the headline numbers.
2. **Read the error analysis** for the data-issue exclusions and the
   per-(dataset, service) best/median/worst rows. Most narrative content
   should come from this file — the auto report is just sums.
3. **Latency QA pass.** For every row check the three latency values
   (`first_latency_ms`, `lbl_ms`, `upl_ms`) against `boundary_fix_action`
   and reasonability:
   - **`boundary_fix_action == "skip"`** → realtime's own UPL is suspect
     (no trustworthy speech_end). For fast_* rows of the same sample,
     `upl_anchor` will be `"self"` — flag those latencies as not
     comparable to anchored rows, and exclude them from any
     cross-service latency claims.
   - **`upl_ms` outliers** — for each (dataset, service) bucket, compute
     the p90 of UPL among `boundary_fix_action == "none"` rows. Any row
     whose `|upl_ms|` exceeds 2× that p90, OR whose `upl_ms` is
     negative by more than ~200 ms, is a candidate to drop from the
     headline aggregate.
   - **First-latency outliers** — only meaningful for `realtime`. If
     `first_latency_ms` is negative or > 2× p90 of clean rows, the
     `first_word_start_s` anchor was probably wrong. Note in the
     justification which sample(s) and exclude from the headline.
   - Record the row IDs that were dropped or flagged in a "QA notes"
     subsection so the reader can audit.
4. **Spot-check the word JSONL** for any sample with
   `boundary_fix_action != "none"` (or the report's "Boundary fixes"
   section). Confirm the trim made sense before relying on the anchored
   UPL for that row. If the trim looks wrong, treat the row as if it
   were `skip` for the latency QA pass above.
5. **Listen to flagged audio** when needed via the `[▶]` links in the
   error analysis (they resolve to `results/audio/<dataset>/<id>.wav`).
6. **Write the justification** to `results/<run>_justification.md`. Skeleton:

   - **Headline numbers (recap)** — copy the filtered aggregate table
     from the error analysis (not the unfiltered one from `_report.md`).
   - **One-line take** — which service wins on accuracy, which on
     latency, and the single biggest caveat.
   - **Where the WER numbers are misleading** — explicitly call out:
     - Empty-hypothesis rows. Quote ref + each service's hypothesis.
     - Dataset-mislabel rows (per-sample WER explodes because ref is
       too short for the audio). Quote ref + audio duration.
     - "All services agree, ref disagrees" rows — these survive the
       filter only when at least one service breaks ranks.
     - Stylistic deltas (punctuation, casing) that inflate WER without
       representing recognition error. Quote 3-4 median rows side-by-side.
     - Anchor-trim rows: when boundary_fix trimmed an edge word, briefly
       say what realtime hallucinated and how that would have skewed UPL
       if uncorrected.
   - **Where the services genuinely disagree** — after excluding the
     above, summarize the residue.
   - **INS / DEL / SUB shape** — the breakdown columns reveal *what kind*
     of error each engine makes:
     - High INS rate → engine adds words not in ref (often filler /
       hallucinated phrases at edges; mitigated for realtime by the
       boundary-fix heuristic but still affects WER).
     - High DEL rate → engine drops words. Common when audio is fast or
       low-confidence.
     - High SUB rate → engine recognized a word but picked the wrong one.
   - **Latency** — interpret the gap. fast_default is fastest;
     fast_llm/fast_mai add LLM/MAI inference time; realtime's UPL is
     dominated by trailing-silence flush. First-latency is omitted for
     REST endpoints because response = first token. **Use the QA-passed
     numbers** (rows excluded by the latency QA pass should not appear
     in headline mean/p90 claims; cite them by ID in a "QA notes"
     subsection instead).
   - **Recommendations** — 4-6 bullets. Be specific: which service for
     which use case, what to investigate next, what to disregard.

7. **Do not invent numbers.** Every percentage, every WER, every sample
   ID in the prose must come from the CSV / report / error analysis. If
   the data doesn't support a claim, drop the claim.

8. **Be honest about dataset quality.** Mazda voice commands are short
   utterances — WER on short references is noisier than on longer speech.
   A single word error on a 3-word command gives 33% WER. Point this out
   when relevant.

## Anchored UPL — what to know

All non-realtime services compute UPL against the **realtime SDK's** word-level
`speech_end`, not their own returned phrase boundaries. This is what
makes UPL comparable across services.

- `upl_ms` is the anchored value (what the report uses).
- `upl_self_ms` keeps each service's own phrase-derived UPL for
  diagnostics.
- `upl_anchor` is `"realtime"` when the realtime row succeeded for that
  sample, or `"self"` when it didn't (fallback).
- `boundary_fix_action` records whether the realtime word list itself
  was trimmed before being used as the anchor:
  - `"none"` — anchor used as-is.
  - `"trim_first"` / `"trim_last"` / `"trim_both"` — edge word(s)
    looked hallucinated (not present in normalized ref); we advanced
    the anchor inward by one word.
  - `"skip"` — anchor judged unreliable; fast_* fell back to self.

If a justification cites a specific UPL number, glance at
`upl_anchor` for that row first — anchored numbers are comparable, self
fallback numbers are not.

## Audio links

`results/audio/<dataset>/<sample_id>.wav` — single canonical location,
regenerated idempotently when error_analysis runs. The directory is safe
to delete; it'll be recreated next time. Markdown links in the error
analysis use a relative path so they resolve when the md is opened
directly in `results/`.

## Style

- Prose, not bullet soup. Tables only where they earn their space
  (recap, empty-hypothesis examples, side-by-side median comparisons).
- Use the literal text from ref/hyp fields — backtick-wrap so
  punctuation renders predictably.
- Mark any service that was skipped with one short paragraph at the end
  explaining why and what re-running it would require.

## Non-goals

- This skill does **not** re-run the benchmark, modify the CSV,
  regenerate the auto report, or rewrite the error analysis. It only
  reads those and writes the justification md.
- This skill is **manually invoked**. Do not wire it into hooks or
  auto-trigger it on benchmark completion.
