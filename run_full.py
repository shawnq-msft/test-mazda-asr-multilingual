"""Full benchmark run for Mazda multilingual ASR."""
from __future__ import annotations

import argparse
import time
from pathlib import Path

from benchmark.config import AZURE_SERVICES, LOCALES, SERVICES, assert_credentials
from benchmark.datasets_loader import iter_samples, list_datasets
from benchmark.report import build_report
from benchmark.runner import run_benchmark


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--languages", nargs="*", default=list(LOCALES),
                   help="Locales to test (default: all 5)")
    p.add_argument("--max-per-dataset", type=int, default=30)
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--no-pace", action="store_true")
    p.add_argument("--services", nargs="*", default=list(SERVICES))
    p.add_argument("--resume", type=str, default=None)
    p.add_argument("--tag", type=str, default="mazda")
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()

    if any(s in AZURE_SERVICES for s in args.services):
        assert_credentials()

    for lang in args.languages:
        print(f"\n{'='*60}")
        print(f"  Language: {lang}")
        print(f"{'='*60}\n")

        if args.resume:
            csv_path = Path(args.resume)
            ts = csv_path.stem.split("_", 1)[-1]
        else:
            ts = time.strftime("%Y%m%d_%H%M%S")
            csv_path = Path(__file__).parent / "results" / f"{args.tag}_{lang}_{ts}.csv"
        md_path = csv_path.with_name(csv_path.stem + "_report.md")

        datasets = list_datasets(lang)
        print(f"[load] datasets: {datasets}")

        samples = []
        for ds in datasets:
            ds_samples = iter_samples(ds, limit=args.max_per_dataset, seed=args.seed)
            print(f"  {ds}: {len(ds_samples)} samples")
            samples.extend(ds_samples)

        if not samples:
            print(f"[skip] no samples for {lang}")
            continue

        print(f"[run] {len(samples)} samples × {len(args.services)} services, workers={args.workers}")
        run_benchmark(samples, csv_path, services=tuple(args.services),
                      workers=args.workers, pace=not args.no_pace, retries=2,
                      sequential=(args.workers <= 1))
        build_report(csv_path, md_path)
        print(f"\nCSV: {csv_path}\nReport: {md_path}")

        # Error analysis
        from scripts.error_analysis import main as error_main
        ea_path = csv_path.with_name(csv_path.stem + "_error_analysis.md")
        error_main(csv_path, ea_path)


if __name__ == "__main__":
    main()
