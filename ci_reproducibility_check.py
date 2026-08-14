#!/usr/bin/env python3
"""Reproducibility gate for generated reference artifacts.

Proves that the committed Citation Registry, Citation Lock, Descriptive Atlas,
Atlas index, and Atlas lock are deterministically derived from the live
corpus, not hand-edited files that merely happen to validate.

Procedure, per builder:
  1. record the committed bytes of its artifacts;
  2. run the builder;
  3. require that no artifact changed (byte-identical).

On any difference the artifacts are restored to their committed bytes and the
check fails. This never auto-commits regenerated output. Standard library
only; exit 0 on pass, 1 on drift.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUILDS = [
    ("build_citation_registry.py",
     ["CITATION_REGISTRY_V0.1.json", "CITATION_ID_LOCK_V0.1.json"]),
    ("build_descriptive_atlas.py",
     ["ATLAS_DESCRIPTIVE_V0.1.json", "ATLAS_ID_LOCK_V0.1.json", "ATLAS_DESCRIPTIVE_V0.1.md"]),
]


def main():
    drift = []
    for builder, artifacts in BUILDS:
        before = {}
        for name in artifacts:
            p = ROOT / name
            if not p.exists():
                print(f"FAIL: committed artifact missing: {name}")
                sys.exit(1)
            before[name] = p.read_bytes()

        proc = subprocess.run(
            [sys.executable, builder], cwd=ROOT, capture_output=True, text=True,
        )
        if proc.stdout.strip():
            print(proc.stdout.rstrip())
        if proc.returncode != 0:
            print("[stderr]", proc.stderr.rstrip())
            print(f"FAIL: {builder} did not run cleanly")
            sys.exit(1)

        for name in artifacts:
            after = (ROOT / name).read_bytes()
            if after != before[name]:
                drift.append(name)
                (ROOT / name).write_bytes(before[name])  # restore committed bytes

    if drift:
        print("FAIL: regeneration changed committed artifact(s):")
        for name in drift:
            print(f"  - {name}")
        print("Committed artifacts are not a deterministic function of the live corpus.")
        print("(Restored committed bytes; no auto-commit performed.)")
        sys.exit(1)

    print("PASS: reproducibility — committed registry, lock, and descriptive atlas "
          "are byte-identical to a fresh build.")


if __name__ == "__main__":
    main()
