#!/usr/bin/env python3
"""Negative controls for validate_asr001_named_assignment.py.

Each control builds a deliberately invalid public-process state in an ISOLATED
temporary directory (never mutating the repo working tree) and asserts that the
validator REJECTS it (non-zero exit). A control PASSES only when the corrupt
fixture is rejected.

Controls:
  1. dispatch log marks a slot dispatched (with a real timestamp) while the
     roster remains in the pre-dispatch snapshot — the two public files must
     not tell different stories for the same RWS-*.

Standard library only; exit 0 if all controls behave correctly, else 1.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VALIDATOR = "validate_asr001_named_assignment.py"

# Everything the named-assignment validator reads by relative path.
INPUTS = [
    VALIDATOR,
    "REVIEWER_PRIVACY_BOUNDARY.md",
    "DECISION_LOG.md",
    "ASR_001_OWNER_DECISION_SPRINT_14.md",
    "ASR_001_REVIEWER_COHORT_ROSTER_V0.2.json",
    "ASR_001_INVITATION_DISPATCH_LOG_V0.1.json",
    "ASR_001_PER_CANDIDATE_INTAKE_POLICY.md",
    "ASR_001_CONTROLLED_INVITATION_PACKAGE.md",
    "ASR_001_NAMED_ASSIGNMENT_GATE.md",
    "ASR_001_REVIEW_ACTIVATION_RECORD_RW001_S14_SUPPLEMENT.md",
    "ASR_001_FIRST_WAVE_NAMED_CANDIDATE_SUMMARY.md",
    "invitations/INV-RW001-TEMPLATE.md",
    "review-intake/README.md",
]


def make_sandbox():
    d = Path(tempfile.mkdtemp(prefix="altis_named_negctl_"))
    for name in INPUTS:
        src = ROOT / name
        dest = d / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dest)
    return d


def run_validator(sandbox):
    return subprocess.run(
        [sys.executable, VALIDATOR],
        cwd=sandbox, capture_output=True, text=True,
    ).returncode


def load(sandbox, name):
    return json.loads((sandbox / name).read_text(encoding="utf-8"))


def dump(sandbox, name, obj):
    (sandbox / name).write_text(
        json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def control_dispatched_while_roster_pre_dispatch(sandbox):
    log = load(sandbox, "ASR_001_INVITATION_DISPATCH_LOG_V0.1.json")
    for entry in log["entries"]:
        if entry.get("slot") == "RWS-01":
            entry["dispatch_status"] = "dispatched"
            entry["dispatched_at"] = "2026-08-15T12:00:00Z"
            break
    dump(sandbox, "ASR_001_INVITATION_DISPATCH_LOG_V0.1.json", log)


CONTROLS = [
    ("dispatched log vs pre-dispatch roster", control_dispatched_while_roster_pre_dispatch),
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
        print(f"\nFAIL: {len(failures)} named-assignment negative control(s) not rejected: {failures}")
        sys.exit(1)
    print(f"\nPASS: {len(CONTROLS)}/{len(CONTROLS)} named-assignment negative controls correctly rejected invalid states.")


if __name__ == "__main__":
    main()
