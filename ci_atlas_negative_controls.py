#!/usr/bin/env python3
"""Negative controls for validate_descriptive_atlas.py.

Each control builds a deliberately invalid Atlas state in an ISOLATED
temporary directory (never mutating the repo working tree) and asserts the
validator REJECTS it (exit 1). A control passes only when the corrupt fixture
makes the validator exit non-zero.

Controls:
  1. atlas id repointed to a different source case;
  2. missing case (a record dropped -> coverage gap);
  3. invented extra case (a fabricated source_case_id);
  4. claim provenance deleted from a dimension;
  5. prohibited evaluative/scoring field introduced.

Standard library only; exit 0 if all controls behave correctly, else 1.
"""

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INPUTS = [
    "validate_descriptive_atlas.py",
    "boundary-cases-001-020.v0.3.json",
    "ATLAS_DESCRIPTIVE_V0.1.json",
    "ATLAS_ID_LOCK_V0.1.json",
]


def make_sandbox():
    d = Path(tempfile.mkdtemp(prefix="altis_atlas_negctl_"))
    for name in INPUTS:
        shutil.copy(ROOT / name, d / name)
    return d


def run_validator(sandbox):
    proc = subprocess.run(
        [sys.executable, "validate_descriptive_atlas.py"],
        cwd=sandbox, capture_output=True, text=True,
    )
    return proc.returncode


def load(sandbox, name):
    return json.loads((sandbox / name).read_text(encoding="utf-8"))


def dump(sandbox, name, obj):
    (sandbox / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def c_repoint(sb):
    atlas = load(sb, "ATLAS_DESCRIPTIVE_V0.1.json")
    atlas["records"][0]["source_case_id"] = "BC-002"  # ATL-D-001 -> BC-002
    dump(sb, "ATLAS_DESCRIPTIVE_V0.1.json", atlas)


def c_missing(sb):
    atlas = load(sb, "ATLAS_DESCRIPTIVE_V0.1.json")
    atlas["records"] = [r for r in atlas["records"] if r["source_case_id"] != "BC-005"]
    dump(sb, "ATLAS_DESCRIPTIVE_V0.1.json", atlas)


def c_invented(sb):
    atlas = load(sb, "ATLAS_DESCRIPTIVE_V0.1.json")
    fake = json.loads(json.dumps(atlas["records"][0]))
    fake["atlas_record_id"] = "ATL-D-099"
    fake["source_case_id"] = "BC-099"
    fake["citation_id"] = "BC-099"
    atlas["records"].append(fake)
    dump(sb, "ATLAS_DESCRIPTIVE_V0.1.json", atlas)


def c_provenance_deleted(sb):
    atlas = load(sb, "ATLAS_DESCRIPTIVE_V0.1.json")
    atlas["records"][0]["dimensions"]["performance_agency"].pop("claim_class", None)
    dump(sb, "ATLAS_DESCRIPTIVE_V0.1.json", atlas)


def c_evaluative_field(sb):
    atlas = load(sb, "ATLAS_DESCRIPTIVE_V0.1.json")
    atlas["records"][0]["dimensions"]["performance_agency"]["sport_score"] = 9.5
    dump(sb, "ATLAS_DESCRIPTIVE_V0.1.json", atlas)


CONTROLS = [
    ("atlas id repointed to another case", c_repoint),
    ("missing case (coverage gap)", c_missing),
    ("invented extra case", c_invented),
    ("claim provenance deleted", c_provenance_deleted),
    ("prohibited evaluative field", c_evaluative_field),
]


def main():
    base = make_sandbox()
    try:
        if run_validator(base) != 0:
            print("FAIL: pristine sandbox did not validate; cannot trust negative controls.")
            sys.exit(1)
    finally:
        shutil.rmtree(base, ignore_errors=True)

    failures = []
    for name, mutate in CONTROLS:
        sb = make_sandbox()
        try:
            mutate(sb)
            code = run_validator(sb)
            ok = code != 0
            print(f"[{'PASS' if ok else 'FAIL'}] negative control: {name} -> validator exit={code} (expected non-zero)")
            if not ok:
                failures.append(name)
        finally:
            shutil.rmtree(sb, ignore_errors=True)

    if failures:
        print(f"\nFAIL: {len(failures)} atlas negative control(s) not rejected: {failures}")
        sys.exit(1)
    print(f"\nPASS: {len(CONTROLS)}/{len(CONTROLS)} atlas negative controls correctly rejected invalid states.")


if __name__ == "__main__":
    main()
