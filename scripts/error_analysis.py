"""Error analysis: exclude data-issue rows from the full benchmark CSV.

Exclusion rules:
  1. Empty hypothesis from any service for a (dataset, sample_id).
  2. Reference much shorter than audio (likely truncated/wrong label).
  3. All services agree (low mutual WER) but disagree with reference
     (likely mislabeled ground truth).

For every excluded or highlighted sample we additionally write a 16-kHz mono
PCM16 WAV under `results/audio/<dataset>/<sample_id>.wav` (idempotent) so a
reviewer can play the clip.
"""
from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean
from urllib.parse import quote

from rapidfuzz.distance import Levenshtein

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from benchmark.datasets_loader import iter_samples, write_pcm16_wav  # noqa: E402
from benchmark.metrics import aggregate, normalize_text  # noqa: E402

ALL_KNOWN_SERVICES = ("fast_default", "fast_llm", "fast_mai", "realtime", "realtime_refine")


def wer_calc(ref: str, hyp: str) -> float:
    ref_words = normalize_text(ref).split()
    hyp_words = normalize_text(hyp).split()
    if not ref_words:
        return 0.0 if not hyp_words else 1.0
    return min(Levenshtein.distance(ref_words, hyp_words) / len(ref_words), 1.0)


def _audio_link(out_dir: Path, ds: str, sid: str,
                cache: dict[tuple[str, str], Path | None],
                samples_by_key: dict[tuple[str, str], object]) -> str:
    key = (ds, sid)
    if key in cache:
        path = cache[key]
    else:
        sample = samples_by_key.get(key)
        if sample is None:
            cache[key] = None
            return ""
        path = out_dir / "audio" / ds / f"{sid}.wav"
        if not path.exists():
            try:
                path.parent.mkdir(parents=True, exist_ok=True)
                write_pcm16_wav(sample.pcm16_mono_16k, path)
            except Exception as e:
                print(f"[wav] failed to write {path}: {e}")
                cache[key] = None
                return ""
        cache[key] = path
    if path is None:
        return ""
    rel = path.relative_to(out_dir).as_posix()
    rel = quote(rel, safe="/:@")
    return f" [▶]({rel})"


def _load_sample_index(needed: set[tuple[str, str]]) -> dict[tuple[str, str], object]:
    out: dict[tuple[str, str], object] = {}
    by_dataset: dict[str, set[str]] = defaultdict(set)
    for ds, sid in needed:
        by_dataset[ds].add(sid)
    for ds, ids in by_dataset.items():
        if not ids:
            continue
        remaining = set(ids)
        try:
            for s in iter_samples(ds, limit=None):
                if s.sample_id in remaining:
                    out[(ds, s.sample_id)] = s
                    remaining.discard(s.sample_id)
                    if not remaining:
                        break
        except Exception as e:
            print(f"[load] {ds}: {e}")
        if remaining:
            print(f"[load] {ds}: did not find {len(remaining)} requested ids")
    return out


def _agg_breakdown(ok_rows: list[dict]) -> tuple[str, str, str]:
    ins = sum(int(r["ins"]) for r in ok_rows if r.get("ins") not in ("", None))
    dele = sum(int(r["del"]) for r in ok_rows if r.get("del") not in ("", None))
    sub = sum(int(r["sub"]) for r in ok_rows if r.get("sub") not in ("", None))
    ref_total = sum(int(r["ref_len"]) for r in ok_rows if r.get("ref_len") not in ("", None))
    if ref_total == 0:
        return "-", "-", "-"
    return (f"{100.0 * ins / ref_total:.1f}",
            f"{100.0 * dele / ref_total:.1f}",
            f"{100.0 * sub / ref_total:.1f}")


def main(csv_path: Path, out_path: Path) -> None:
    rows = []
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            rows.append(r)

    services_in_csv = sorted({r["service"] for r in rows})
    SERVICES = tuple(s for s in ALL_KNOWN_SERVICES if s in services_in_csv) or tuple(services_in_csv)

    by_sample: dict[tuple[str, str], dict[str, dict]] = defaultdict(dict)
    for r in rows:
        by_sample[(r["dataset"], r["sample_id"])][r["service"]] = r

    excluded_empty: list[tuple[str, str, str]] = []
    excluded_short_ref: list[tuple[str, str, float, str]] = []
    excluded_mislabel: list[tuple[str, str, float, str, dict]] = []
    excluded_compound: list[tuple[str, str, str, dict]] = []

    keep: set[tuple[str, str]] = set()

    for key, svcmap in by_sample.items():
        ds, sid = key
        present = [s for s in SERVICES if s in svcmap]
        if len(present) < 2:
            continue

        empties = [s for s in present
                   if not (svcmap[s].get("hypothesis") or "").strip()
                   and not svcmap[s].get("error")]
        if empties:
            excluded_empty.append((ds, sid, ",".join(empties)))
            continue
        if any(svcmap[s].get("error") for s in present):
            excluded_empty.append((ds, sid, "error:" + ",".join(
                s for s in present if svcmap[s].get("error"))))
            continue

        ref = svcmap[present[0]].get("reference", "") or ""
        ref_words = normalize_text(ref).split()
        try:
            dur_s = float(svcmap[present[0]].get("duration_s") or 0.0)
        except ValueError:
            dur_s = 0.0
        words_per_s = (len(ref_words) / dur_s) if dur_s > 0 else 0.0
        if dur_s >= 1.0 and words_per_s < 0.3:
            excluded_short_ref.append((ds, sid, words_per_s, ref))
            continue

        hyps = {s: svcmap[s].get("hypothesis", "") or "" for s in present}
        pairwise: list[float] = []
        svc_list = list(present)
        for i in range(len(svc_list)):
            for j in range(i + 1, len(svc_list)):
                pairwise.append(wer_calc(hyps[svc_list[i]], hyps[svc_list[j]]))
        mean_agree_wer = mean(pairwise) if pairwise else 1.0
        mean_ref_wer = mean(wer_calc(ref, hyps[s]) for s in present)
        if mean_agree_wer < 0.15 and mean_ref_wer > 0.5:
            excluded_mislabel.append((ds, sid, mean_agree_wer, ref, hyps))
            continue

        ref_joined = normalize_text(ref).replace(" ", "")
        all_compound = all(
            normalize_text(hyps[s]).replace(" ", "") == ref_joined
            for s in present
        )
        if all_compound and mean_ref_wer > 0:
            excluded_compound.append((ds, sid, ref, hyps))
            continue

        keep.add(key)

    by_key_filtered: dict[tuple[str, str], list[dict]] = defaultdict(list)
    by_key_all: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in rows:
        ksamp = (r["dataset"], r["sample_id"])
        by_key_all[(r["dataset"], r["service"])].append(r)
        if ksamp in keep:
            by_key_filtered[(r["dataset"], r["service"])].append(r)

    # Determine which sample ids will appear in the report so we only re-load those.
    needed: set[tuple[str, str]] = set()
    for ds, sid, _ in excluded_empty:
        needed.add((ds, sid))
    for ds, sid, _, _ in excluded_short_ref:
        needed.add((ds, sid))
    for ds, sid, _, _, _ in excluded_mislabel:
        needed.add((ds, sid))
    for ds, sid, _, _ in excluded_compound:
        needed.add((ds, sid))

    by_pair_filtered_for_needed: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in rows:
        ksamp = (r["dataset"], r["sample_id"])
        if ksamp not in keep or r["error"] or r["wer"] == "":
            continue
        by_pair_filtered_for_needed[(r["dataset"], r["service"])].append(r)
    for (ds, _svc), rs in by_pair_filtered_for_needed.items():
        if not rs:
            continue
        rs_sorted = sorted(rs, key=lambda r: float(r["wer"]))
        for r in (rs_sorted[0], rs_sorted[len(rs_sorted) // 2], rs_sorted[-1]):
            needed.add((ds, r["sample_id"]))

    # Top fast_default vs realtime disagreements
    top_diffs: list = []
    for key in keep:
        ds, sid = key
        svcmap = by_sample[key]
        if "fast_default" in svcmap and "realtime" in svcmap:
            try:
                fw = min(float(svcmap["fast_default"]["wer"]), 1.0)
                rw = min(float(svcmap["realtime"]["wer"]), 1.0)
            except ValueError:
                continue
            top_diffs.append((abs(fw - rw), ds, sid, svcmap, fw, rw))
    top_diffs.sort(reverse=True)
    for _, ds, sid, _, _, _ in top_diffs[:10]:
        needed.add((ds, sid))

    print(f"[load] indexing {len(needed)} samples for audio links ...")
    samples_by_key = _load_sample_index(needed)
    print(f"[load] resolved {len(samples_by_key)} samples")
    out_dir = out_path.parent
    audio_cache: dict[tuple[str, str], Path | None] = {}
    datasets_seen = sorted({r["dataset"] for r in rows})

    def metrics_for(rs: list[dict]) -> dict:
        ok = [r for r in rs if not r["error"]]
        wers = [min(float(r["wer"]), 1.0) for r in ok if r["wer"] != ""]
        sers = [int(r["sentence_error"]) for r in ok if r["sentence_error"] != ""]
        ll = [float(r["lbl_ms"]) for r in ok if r["lbl_ms"] not in ("", None)]
        upl = [float(r["upl_ms"]) for r in ok if r.get("upl_ms") not in ("", None)]
        ins_rate, del_rate, sub_rate = _agg_breakdown(ok)
        return {
            "n": len(rs),
            "errs": sum(1 for r in rs if r["error"]),
            "wer": (sum(wers) / len(wers)) if wers else None,
            "ser": (sum(sers) / len(sers)) if sers else None,
            "ins": ins_rate, "del": del_rate, "sub": sub_rate,
            "lbl": aggregate(ll),
            "upl": aggregate(upl),
        }

    lines: list[str] = []
    lines.append(f"# Error analysis — {csv_path.name}\n")
    lines.append("Filters out samples that look like *data* problems rather than recognition errors:")
    lines.append("1. **Empty hypothesis** — at least one service returned no text.")
    lines.append("2. **Reference much shorter than audio** — `words_per_s < 0.3` (with `duration ≥ 1 s`). At normal speech rates this means the label is missing content.")
    lines.append("3. **All services agree, ref disagrees** — mean pairwise WER between hypotheses < 0.15 AND mean WER vs ref > 0.5. Multiple ASR systems converging on the same answer that differs from the reference is a strong signal of a mislabeled ground truth, not a shared error.")
    lines.append("4. **Compound-word / segmentation artifact** — all services produce text identical to the reference after removing spaces (e.g. `stummschalten` vs `stumm schalten`). These are correct recognitions scored as errors due to tokenization.")
    lines.append("")
    lines.append("Audio links (▶) point to `results/audio/<dataset>/<sample_id>.wav` so a reviewer can play the clip directly.")
    lines.append("")

    # Datasets under test
    lines.append("## Datasets under test")
    lines.append("")
    for ds in datasets_seen:
        parts = ds.rsplit("_", 1)
        loc_name = parts[0] if len(parts) == 2 else ds
        scn = parts[1] if len(parts) == 2 else ""
        lines.append(f"- **{ds}** — Mazda {loc_name} {scn} voice commands (male + female pooled)")
    lines.append("")

    total_samples = sum(1 for k, v in by_sample.items() if len([s for s in SERVICES if s in v]) >= 2)
    kept_samples = len(keep)
    dropped = total_samples - kept_samples
    lines.append(f"Total complete samples: **{total_samples}**  ")
    lines.append(f"Kept after filtering: **{kept_samples}**  ")
    lines.append(f"Excluded as data issues: **{dropped}**  ")
    lines.append("")
    lines.append(f"- Empty hypothesis: {len(excluded_empty)}")
    lines.append(f"- Reference too short for audio: {len(excluded_short_ref)}")
    lines.append(f"- All services agree, ref disagrees: {len(excluded_mislabel)}")
    lines.append(f"- Compound-word / segmentation artifact: {len(excluded_compound)}")
    lines.append("")

    # Speech boundaries
    realtime_rows = [r for r in rows if r["service"] == "realtime"]
    fixed_rows = [r for r in realtime_rows
                  if r.get("boundary_fix_action") and r["boundary_fix_action"] != "none"]
    lines.append("## Speech boundaries")
    lines.append("")
    lines.append("`speech_start_s` / `speech_end_s` come from the realtime SDK's word-level timestamps and anchor UPL for all services. Per-word detail lives in the sidecar `" + csv_path.with_name(csv_path.stem + "_words.jsonl").name + "`.")
    lines.append("")
    if fixed_rows:
        action_counts = Counter(r["boundary_fix_action"] for r in fixed_rows)
        lines.append(f"Boundary-fix actions across {len(realtime_rows)} realtime samples: " +
                     ", ".join(f"`{a}`={n}" for a, n in sorted(action_counts.items())))
        lines.append("")
    else:
        lines.append("All realtime samples passed the boundary-fix heuristic without trimming.")
        lines.append("")

    # Filtered results
    lines.append("## Filtered results (excludes data issues)")
    lines.append("")
    lines.append("INS/DEL/SUB are *rates per 100 reference words*. Their sum ≈ WER × 100.")
    lines.append("")
    lines.append("| Dataset | Service | N | WER | SER | INS/100 | DEL/100 | SUB/100 | LBL ms (mean / p90) | UPL ms (mean / p90) |")
    lines.append("|---|---|---:|---:|---:|---:|---:|---:|---|---|")
    datasets = sorted({k[0] for k in by_key_filtered.keys()})
    for ds in datasets:
        for svc in SERVICES:
            rs = by_key_filtered.get((ds, svc), [])
            m = metrics_for(rs)
            wer_s = f"{m['wer']:.3f}" if m["wer"] is not None else "-"
            ser_s = f"{m['ser']:.3f}" if m["ser"] is not None else "-"
            lbl = m["lbl"]; upl = m["upl"]
            lbl_s = f"{lbl['mean']:.0f} / {lbl['p90']:.0f}" if lbl["n"] else "-"
            upl_s = f"{upl['mean']:.0f} / {upl['p90']:.0f}" if upl["n"] else "-"
            lines.append(f"| {ds} | {svc} | {m['n']} | {wer_s} | {ser_s} | {m['ins']} | {m['del']} | {m['sub']} | {lbl_s} | {upl_s} |")
    lines.append("")

    # Unfiltered results
    lines.append("## Unfiltered results (all complete samples, for reference)")
    lines.append("")
    lines.append("| Dataset | Service | N | WER | SER | INS/100 | DEL/100 | SUB/100 |")
    lines.append("|---|---|---:|---:|---:|---:|---:|---:|")
    for ds in datasets_seen:
        for svc in SERVICES:
            rs = by_key_all.get((ds, svc), [])
            m = metrics_for(rs)
            wer_s = f"{m['wer']:.3f}" if m["wer"] is not None else "-"
            ser_s = f"{m['ser']:.3f}" if m["ser"] is not None else "-"
            lines.append(f"| {ds} | {svc} | {m['n']} | {wer_s} | {ser_s} | {m['ins']} | {m['del']} | {m['sub']} |")
    lines.append("")

    # Excluded samples
    lines.append("## Excluded samples — examples\n")

    lines.append("### Empty hypothesis")
    lines.append("")
    if not excluded_empty:
        lines.append("_(none)_\n")
    else:
        lines.append("| Audio | Dataset | Sample | Empty in | Reference |")
        lines.append("|---|---|---|---|---|")
        for ds, sid, which in excluded_empty[:20]:
            ref = by_sample[(ds, sid)].get(SERVICES[0], {}).get("reference", "") if SERVICES else ""
            link = _audio_link(out_dir, ds, sid, audio_cache, samples_by_key).strip() or "-"
            lines.append(f"| {link} | {ds} | {sid} | {which} | `{ref}` |")
        if len(excluded_empty) > 20:
            lines.append(f"\n_(+{len(excluded_empty) - 20} more)_")
        lines.append("")

    lines.append("### Reference too short for audio duration")
    lines.append("")
    if not excluded_short_ref:
        lines.append("_(none)_\n")
    else:
        lines.append("| Audio | Dataset | Sample | words/s | Reference | Sample hypothesis (fast_default) |")
        lines.append("|---|---|---|---:|---|---|")
        for ds, sid, wps, ref in sorted(excluded_short_ref, key=lambda x: x[2])[:15]:
            hyp = by_sample[(ds, sid)].get("fast_default", {}).get("hypothesis", "")
            link = _audio_link(out_dir, ds, sid, audio_cache, samples_by_key).strip() or "-"
            lines.append(f"| {link} | {ds} | {sid} | {wps:.2f} | `{ref}` | `{hyp}` |")
        if len(excluded_short_ref) > 15:
            lines.append(f"\n_(+{len(excluded_short_ref) - 15} more)_")
        lines.append("")

    lines.append("### All services agree, reference disagrees (likely mislabeled)")
    lines.append("")
    if not excluded_mislabel:
        lines.append("_(none)_\n")
    else:
        for ds, sid, agree, ref, hyps in sorted(excluded_mislabel, key=lambda x: x[2])[:15]:
            link = _audio_link(out_dir, ds, sid, audio_cache, samples_by_key)
            lines.append(f"#### {ds}/{sid}{link} — pairwise WER between services = {agree:.3f}")
            lines.append(f"- ref:           `{ref}`")
            for s in SERVICES:
                if s in hyps:
                    lines.append(f"- {s:<14} `{hyps[s]}`")
            lines.append("")
        if len(excluded_mislabel) > 15:
            lines.append(f"_(+{len(excluded_mislabel) - 15} more)_\n")

    lines.append("### Compound-word / segmentation artifacts")
    lines.append("")
    if not excluded_compound:
        lines.append("_(none)_\n")
    else:
        for ds, sid, ref, hyps in sorted(excluded_compound)[:15]:
            link = _audio_link(out_dir, ds, sid, audio_cache, samples_by_key)
            lines.append(f"#### {ds}/{sid}{link}")
            lines.append(f"- ref:           `{ref}`")
            for s in SERVICES:
                if s in hyps:
                    lines.append(f"- {s:<14} `{hyps[s]}`")
            lines.append("")
        if len(excluded_compound) > 15:
            lines.append(f"_(+{len(excluded_compound) - 15} more)_\n")

    # Genuine recognition errors
    lines.append("## Genuine recognition errors (filtered set)\n")
    lines.append("Best / median / worst WER per (dataset, service) on the kept samples.\n")

    by_pair_filtered: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in rows:
        ksamp = (r["dataset"], r["sample_id"])
        if ksamp not in keep:
            continue
        if r["error"] or r["wer"] == "":
            continue
        by_pair_filtered[(r["dataset"], r["service"])].append(r)

    for (ds, svc) in sorted(by_pair_filtered.keys()):
        rs = sorted(by_pair_filtered[(ds, svc)], key=lambda r: float(r["wer"]))
        n = len(rs)
        if n == 0:
            continue
        best = rs[0]; med = rs[n // 2]; worst = rs[-1]
        lines.append(f"### {ds} / {svc}  (n={n})")
        for label, r in (("BEST", best), ("MEDIAN", med), ("WORST", worst)):
            link = _audio_link(out_dir, r["dataset"], r["sample_id"],
                               audio_cache, samples_by_key)
            ss = r.get("speech_start_s", "") or "-"
            se = r.get("speech_end_s", "") or "-"
            fix = r.get("boundary_fix_action", "") or "-"
            lines.append(f"**{label}** — `{r['sample_id']}`{link}  wer={float(r['wer']):.3f}  speech=[{ss}s, {se}s]  fix={fix}")
            lines.append(f"- ref: `{r.get('reference','')}`")
            lines.append(f"- hyp: `{r.get('hypothesis','')}`")
        lines.append("")

    # Top disagreements
    lines.append("## Top fast_default vs realtime disagreements (filtered)\n")
    if not top_diffs:
        lines.append("_(none)_\n")
    else:
        for delta, ds, sid, svcmap, fw, rw in top_diffs[:10]:
            link = _audio_link(out_dir, ds, sid, audio_cache, samples_by_key)
            rt = svcmap.get("realtime", {})
            ss = rt.get("speech_start_s", "") or "-"
            se = rt.get("speech_end_s", "") or "-"
            fix = rt.get("boundary_fix_action", "") or "-"
            lines.append(f"### {ds}/{sid}{link}  Δwer={delta:.3f}  (fast_default={fw:.3f}, realtime={rw:.3f})  speech=[{ss}s, {se}s] fix={fix}")
            lines.append(f"- ref:           `{svcmap['fast_default'].get('reference','')}`")
            for s in SERVICES:
                if s in svcmap:
                    lines.append(f"- {s:<14} `{svcmap[s].get('hypothesis','')}`")
            lines.append("")

    # Caveats
    lines.append("## Caveats\n")
    lines.append("- **UPL is anchored on the realtime SDK's word-end timestamp** for each sample, so all services use the same `speech_end`. The CSV's `upl_self_ms` column has each service's own phrase-derived value if you want to see how its boundary detection differs.")
    lines.append("- **Mazda voice commands** are short utterances (typically 2-8 words). WER on short references is noisier — a single word error on a 3-word command gives 33% WER.")
    lines.append("- The 'all-agree-vs-ref' filter is conservative (pairwise WER < 0.15 AND mean ref WER > 0.5). True mislabels with partial agreement still survive and inflate per-service WER equally.")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    audio_count = sum(1 for v in audio_cache.values() if v is not None)
    print(f"Wrote {out_path}")
    print(f"Total: {total_samples}, kept: {kept_samples}, dropped: {dropped}")
    print(f"  empty: {len(excluded_empty)}  short_ref: {len(excluded_short_ref)}  mislabel: {len(excluded_mislabel)}  compound: {len(excluded_compound)}")
    print(f"  audio files emitted/linked: {audio_count}")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
