from __future__ import annotations

import argparse
import csv
import shutil
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from benchmark.audio_utils import write_pcm16_wav  # noqa: E402
from benchmark.datasets_loader import iter_samples  # noqa: E402


def export_package(csv_paths: list[Path], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    audio_root = out_dir / "audio"
    manifest_path = out_dir / "manifest.csv"
    zip_path = out_dir.with_suffix(".zip")

    needed: dict[tuple[str, str], dict] = {}
    for csv_path in csv_paths:
        with csv_path.open("r", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                key = (row["dataset"], row["sample_id"])
                needed.setdefault(key, row)

    by_dataset: dict[str, set[str]] = defaultdict(set)
    for dataset, sample_id in needed:
        by_dataset[dataset].add(sample_id)

    sample_index = {}
    for dataset, ids in by_dataset.items():
        remaining = set(ids)
        for sample in iter_samples(dataset, limit=None):
            if sample.sample_id in remaining:
                sample_index[(dataset, sample.sample_id)] = sample
                remaining.remove(sample.sample_id)
                if not remaining:
                    break
        if remaining:
            print(f"{dataset}: missing {len(remaining)} samples")

    rows = []
    for key in sorted(needed):
        sample = sample_index.get(key)
        if sample is None:
            continue
        audio_rel = Path("audio") / sample.dataset / f"{sample.sample_id.replace('/', '__')}.wav"
        audio_path = out_dir / audio_rel
        write_pcm16_wav(sample.pcm16_mono_16k, audio_path)
        rows.append({
            "dataset": sample.dataset,
            "sample_id": sample.sample_id,
            "locale": sample.locale,
            "reference": sample.reference,
            "duration_s": round(sample.duration_s, 3),
            "audio_path": audio_rel.as_posix(),
        })

    with manifest_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["dataset", "sample_id", "locale", "reference", "duration_s", "audio_path"])
        writer.writeheader()
        writer.writerows(rows)

    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in out_dir.rglob("*"):
            if path.is_file():
                zf.write(path, path.relative_to(out_dir).as_posix())

    print(f"manifest rows: {len(rows)}")
    print(f"manifest: {manifest_path}")
    print(f"zip: {zip_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", nargs="+", type=Path)
    parser.add_argument("--out-dir", type=Path, default=Path("results/mimo_colab_package"))
    args = parser.parse_args()

    if args.out_dir.exists():
        shutil.rmtree(args.out_dir)
    export_package(args.csv, args.out_dir)


if __name__ == "__main__":
    main()
