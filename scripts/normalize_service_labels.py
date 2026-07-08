from __future__ import annotations

import argparse
import csv
from pathlib import Path

RENAMES = {
    "fast_mai": "fast_mai_1",
    "fast_mai_15": "fast_mai_1.5",
}


def normalize_csv(path: Path) -> int:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames
    if not fieldnames:
        return 0

    changed = 0
    seen: set[tuple[str, str, str]] = set()
    out_rows: list[dict] = []
    for row in rows:
        old_service = row.get("service", "")
        new_service = RENAMES.get(old_service, old_service)
        if new_service != old_service:
            row["service"] = new_service
            changed += 1
        key = (row.get("dataset", ""), row.get("sample_id", ""), row.get("service", ""))
        if key in seen:
            continue
        seen.add(key)
        out_rows.append(row)

    if changed or len(out_rows) != len(rows):
        with path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(out_rows)
    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", nargs="+", type=Path)
    args = parser.parse_args()

    for path in args.csv:
        changed = normalize_csv(path)
        print(f"{path}: normalized {changed} service labels")


if __name__ == "__main__":
    main()
