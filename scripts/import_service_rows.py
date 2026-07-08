from __future__ import annotations

import argparse
import csv
from pathlib import Path

from benchmark.runner import CSV_FIELDS


def import_rows(target: Path, source: Path) -> tuple[int, int]:
    with target.open("r", encoding="utf-8", newline="") as f:
        target_rows = list(csv.DictReader(f))
    done = {(r["dataset"], r["sample_id"], r["service"]) for r in target_rows}

    with source.open("r", encoding="utf-8", newline="") as f:
        source_rows = list(csv.DictReader(f))

    appended = 0
    skipped = 0
    with target.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        for row in source_rows:
            normalized = {field: row.get(field, "") for field in CSV_FIELDS}
            key = (normalized["dataset"], normalized["sample_id"], normalized["service"])
            if key in done:
                skipped += 1
                continue
            writer.writerow(normalized)
            done.add(key)
            appended += 1
    return appended, skipped


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=Path)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()

    appended, skipped = import_rows(args.target, args.source)
    print(f"{args.target}: appended {appended}, skipped {skipped}")


if __name__ == "__main__":
    main()
