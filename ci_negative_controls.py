#!/usr/bin/env python3
"""Negative controls for validate_citation_registry.py.

These are real regression tests: each constructs a deliberately invalid
citation state in an ISOLATED temporary directory (never mutating the repo
working tree) and asserts that the validator REJECTS it (exit 1).

A control PASSES only when the corrupt fixture makes the validator exit
non-zero. A corrupt fixture that the validator accepts (exit 0) is a control
FAILURE and fails CI.

Controls:
  1. semantic binding drift (BC activity repointed);
  2. an ASR entry under an open citability hold (CITE-HOLD-ASR-001) marked externally_citable;
  3. coverage gap (a boundary-case identifier dropped);
  4. invalid claim class.

Standard library only; exit 0 if all controls behave correctly, else 1.
"""

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Everything validate_citation_registry.py reads from its own directory.
INPUTS = [
    "validate_citation_registry.py",
    "CITATION_REGISTRY_V0.1.json",
    "CITATION_ID_LOCK_V0.1.json",
    "boundary-cases-001-020.v0.3.json",
    "ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.2.json",
    "AS3_STACK.md",
]


def make_sandbox():
    d = Path(tempfile.mkdtemp(prefix="altis_negctl_"))
    for name in INPUTS:
        shutil.copy(ROOT / name, d / name)
    return d


def run_validator(sandbox):
    proc = subprocess.run(
        [sys.executable, "validate_citation_registry.py"],
        cwd=sandbox, capture_output=True, text=True,
    )
    return proc.returncode


def load(sandbox, name):
    return json.loads((sandbox / name).read_text(encoding="utf-8"))


def dump(sandbox, name, obj):
    (sandbox / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def control_binding_drift(sandbox):
    lock = load(sandbox, "CITATION_ID_LOCK_V0.1.json")
    for b in lock["bindings"]:
        if b["binding_type"] == "boundary_case_activity":
            b["bound_value"] = "DELIBERATELY WRONG ACTIVITY"
            break
    dump(sandbox, "CITATION_ID_LOCK_V0.1.json", lock)


def control_blocked_but_citable(sandbox):
    reg = load(sandbox, "CITATION_REGISTRY_V0.1.json")
    for e in reg["identifiers"]:
        if e["kind"] == "asr_clause":
            e["externally_citable"] = True
            break
    dump(sandbox, "CITATION_REGISTRY_V0.1.json", reg)


def control_coverage_gap(sandbox):
    reg = load(sandbox, "CITATION_REGISTRY_V0.1.json")
    reg["identifiers"] = [e for e in reg["identifiers"] if e["citation_id"] != "BC-005"]
    dump(sandbox, "CITATION_REGISTRY_V0.1.json", reg)


def control_invalid_claim_class(sandbox):
    reg = load(sandbox, "CITATION_REGISTRY_V0.1.json")
    reg["identifiers"][0]["claim_class"] = "C9"
    dump(sandbox, "CITATION_REGISTRY_V0.1.json", reg)


CONTROLS = [
    ("semantic binding drift", control_binding_drift),
    ("blocked-but-citable ASR entry", control_blocked_but_citable),
    ("coverage gap", control_coverage_gap),
    ("invalid claim class", control_invalid_claim_class),
]


def main():
    # Sanity: the pristine copy must PASS, so a failure below is caused by the
    # injected corruption and not by a broken sandbox.
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
            ok = code != 0  # we WANT rejection
            print(f"[{'PASS' if ok else 'FAIL'}] negative control: {name} -> validator exit={code} (expected non-zero)")
            if not ok:
                failures.append(name)
        finally:
            shutil.rmtree(sb, ignore_errors=True)

    if failures:
        print(f"\nFAIL: {len(failures)} negative control(s) not rejected: {failures}")
        sys.exit(1)
    print(f"\nPASS: {len(CONTROLS)}/{len(CONTROLS)} negative controls correctly rejected invalid states.")


if __name__ == "__main__":
    main()
