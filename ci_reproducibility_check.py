#!/usr/bin/env python3
"""Reproducibility gate for generated reference artifacts.

Proves that the committed Citation Registry/Lock, Descriptive Atlas/index/lock,
and the Atlas query contract + static distribution are deterministically
derived from the live corpus, not hand-edited files that merely happen to
validate.

Procedure, per builder:
  1. snapshot the committed bytes of its artifacts (files or whole directories);
  2. run the builder;
  3. require that no artifact changed, appeared, or disappeared.

On any difference the artifacts are restored to their committed state and the
check fails. This never auto-commits regenerated output. Standard library
only; exit 0 on pass, 1 on drift.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# Each entry: (builder, [paths]); a path may be a file or a directory (expanded).
BUILDS = [
    ("build_citation_registry.py",
     ["CITATION_REGISTRY_V0.1.json", "CITATION_ID_LOCK_V0.1.json"]),
    ("build_descriptive_atlas.py",
     ["ATLAS_DESCRIPTIVE_V0.1.json", "ATLAS_ID_LOCK_V0.1.json", "ATLAS_DESCRIPTIVE_V0.1.md"]),
    ("build_atlas_distribution.py",
     ["ATLAS_QUERY_CONTRACT_V0.1.json", "atlas"]),
]


def expand(paths):
    files = []
    for name in paths:
        p = ROOT / name
        if p.is_dir():
            files.extend(sorted(f for f in p.rglob("*") if f.is_file()))
        else:
            files.append(p)
    return files


def main():
    drift = []
    for builder, paths in BUILDS:
        before = {}
        for f in expand(paths):
            if not f.exists():
                print(f"FAIL: committed artifact missing: {f.relative_to(ROOT)}")
                sys.exit(1)
            before[f] = f.read_bytes()

        proc = subprocess.run(
            [sys.executable, builder], cwd=ROOT, capture_output=True, text=True,
        )
        if proc.stdout.strip():
            print(proc.stdout.rstrip())
        if proc.returncode != 0:
            print("[stderr]", proc.stderr.rstrip())
            print(f"FAIL: {builder} did not run cleanly")
            sys.exit(1)

        after_files = set(expand(paths))
        # changed or removed
        for f, data in before.items():
            if not f.exists():
                drift.append(str(f.relative_to(ROOT)) + " (removed)")
                f.write_bytes(data)
            elif f.read_bytes() != data:
                drift.append(str(f.relative_to(ROOT)))
                f.write_bytes(data)
        # newly appeared
        for f in after_files - set(before):
            drift.append(str(f.relative_to(ROOT)) + " (added)")
            f.unlink()

    if drift:
        print("FAIL: regeneration changed committed artifact(s):")
        for name in drift:
            print(f"  - {name}")
        print("Committed artifacts are not a deterministic function of the live corpus.")
        print("(Restored committed state; no auto-commit performed.)")
        sys.exit(1)

    print("PASS: reproducibility — committed registry, atlas, query contract, and "
          "static distribution are byte-identical to a fresh build.")


if __name__ == "__main__":
    main()
