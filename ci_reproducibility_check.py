#!/usr/bin/env python3
"""Reproducibility gate for the Citation Registry.

Proves that the committed CITATION_REGISTRY_V0.1.json and
CITATION_ID_LOCK_V0.1.json are deterministically derived from the live
corpus, not hand-edited JSON that merely happens to validate.

Procedure:
  1. record the committed bytes of both artifacts;
  2. run build_citation_registry.py;
  3. require that neither artifact changed (byte-identical).

On any difference the artifacts are restored to their committed bytes and the
check fails. This never auto-commits regenerated output. Standard library
only; exit 0 on pass, 1 on drift.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ARTIFACTS = ["CITATION_REGISTRY_V0.1.json", "CITATION_ID_LOCK_V0.1.json"]


def main():
    before = {}
    for name in ARTIFACTS:
        p = ROOT / name
        if not p.exists():
            print(f"FAIL: committed artifact missing: {name}")
            sys.exit(1)
        before[name] = p.read_bytes()

    proc = subprocess.run(
        [sys.executable, "build_citation_registry.py"],
        cwd=ROOT, capture_output=True, text=True,
    )
    if proc.stdout.strip():
        print(proc.stdout.rstrip())
    if proc.returncode != 0:
        print("[stderr]", proc.stderr.rstrip())
        print("FAIL: builder did not run cleanly")
        sys.exit(1)

    drift = []
    for name in ARTIFACTS:
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

    print("PASS: reproducibility — committed registry and lock are byte-identical to a fresh build.")


if __name__ == "__main__":
    main()
