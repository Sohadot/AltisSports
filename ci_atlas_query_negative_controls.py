#!/usr/bin/env python3
"""Negative controls for the Atlas Query / Reference Surface.

Each control builds a deliberately invalid surface state in an ISOLATED
temporary directory (never mutating the repo working tree) and asserts that
the surface validator (or the CLI) REJECTS it. A control passes only when the
corrupt fixture produces a non-zero exit.

Controls:
  1. resolver repoints an atlas id to the wrong BC (by-case index tampered);
  2. duplicate mapping in a resolver index;
  3. distribution record file missing;
  4. invented record added to the manifest/index;
  5. provenance stripped from a distribution record;
  6. undeclared/arbitrary query field (CLI must fail closed);
  7. evaluative field (sport_score) injected into a distribution record;
  8. distribution record claims independent citability.

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
    "validate_atlas_query_surface.py",
    "query_descriptive_atlas.py",
    "ATLAS_DESCRIPTIVE_V0.1.json",
    "ATLAS_QUERY_CONTRACT_V0.1.json",
    "ATLAS_ID_LOCK_V0.1.json",
    "CITATION_REGISTRY_V0.1.json",
]


def make_sandbox():
    d = Path(tempfile.mkdtemp(prefix="altis_atlasq_negctl_"))
    for name in INPUTS:
        shutil.copy(ROOT / name, d / name)
    shutil.copytree(ROOT / "atlas", d / "atlas")
    return d


def run_validator(sb):
    return subprocess.run([sys.executable, "validate_atlas_query_surface.py"],
                          cwd=sb, capture_output=True, text=True).returncode


def run_cli(sb, args):
    return subprocess.run([sys.executable, "query_descriptive_atlas.py", *args],
                          cwd=sb, capture_output=True, text=True).returncode


def load(sb, rel):
    return json.loads((sb / rel).read_text(encoding="utf-8"))


def dump(sb, rel, obj):
    (sb / rel).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def c_repoint(sb):
    idx = load(sb, "atlas/by-case.json")
    idx["BC-001"] = "records/ATL-D-002.json"  # wrong target
    dump(sb, "atlas/by-case.json", idx)
    return run_validator(sb)


def c_duplicate(sb):
    idx = load(sb, "atlas/by-atlas-id.json")
    idx["ATL-D-001"] = "records/ATL-D-002.json"
    dump(sb, "atlas/by-atlas-id.json", idx)
    return run_validator(sb)


def c_missing_record(sb):
    (sb / "atlas/records/ATL-D-005.json").unlink()
    return run_validator(sb)


def c_invented(sb):
    m = load(sb, "atlas/manifest.json")
    m["records"].append({"atlas_record_id": "ATL-D-099", "source_case_id": "BC-099",
                         "path": "records/ATL-D-099.json", "sha256": "0" * 64})
    m["record_count"] = len(m["records"])
    dump(sb, "atlas/manifest.json", m)
    return run_validator(sb)


def c_provenance_stripped(sb):
    rf = load(sb, "atlas/records/ATL-D-001.json")
    rf["record"]["dimensions"]["performance_agency"].pop("claim_class", None)
    dump(sb, "atlas/records/ATL-D-001.json", rf)
    return run_validator(sb)


def c_arbitrary_field(sb):
    return run_cli(sb, ["--totally-made-up", "x"])  # must be non-zero


def c_evaluative_field(sb):
    rf = load(sb, "atlas/records/ATL-D-001.json")
    rf["record"]["dimensions"]["performance_agency"]["sport_score"] = 9.5
    dump(sb, "atlas/records/ATL-D-001.json", rf)
    return run_validator(sb)


def c_false_citability(sb):
    rf = load(sb, "atlas/records/ATL-D-018.json")
    rf["citability"]["atlas_record_citability"] = "independently_registered"
    dump(sb, "atlas/records/ATL-D-018.json", rf)
    return run_validator(sb)


CONTROLS = [
    ("resolver repoints atlas id to wrong BC", c_repoint),
    ("duplicate mapping", c_duplicate),
    ("distribution record missing", c_missing_record),
    ("invented record", c_invented),
    ("provenance stripped", c_provenance_stripped),
    ("undeclared/arbitrary query field", c_arbitrary_field),
    ("evaluative field injected", c_evaluative_field),
    ("false independent citability", c_false_citability),
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
    for name, fn in CONTROLS:
        sb = make_sandbox()
        try:
            code = fn(sb)
            ok = code != 0
            print(f"[{'PASS' if ok else 'FAIL'}] negative control: {name} -> exit={code} (expected non-zero)")
            if not ok:
                failures.append(name)
        finally:
            shutil.rmtree(sb, ignore_errors=True)

    if failures:
        print(f"\nFAIL: {len(failures)} query-surface negative control(s) not rejected: {failures}")
        sys.exit(1)
    print(f"\nPASS: {len(CONTROLS)}/{len(CONTROLS)} query-surface negative controls correctly rejected invalid states.")


if __name__ == "__main__":
    main()
