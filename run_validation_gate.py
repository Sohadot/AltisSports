#!/usr/bin/env python3
"""AltisSports hosted reference validation gate — unified runner.

Reads CI_VALIDATION_MANIFEST.json and runs every registered validator with
its declared invocations. Standard library only.

Contract (STANDARDIZATION_READINESS_GATE.md section 5):

  - fail-closed registration: any validate_*.py present in the repo root that
    is not registered in the manifest fails the gate;
  - every required validator (and every declared invocation) must exit 0;
  - non-required validators are still run and reported, but their failure
    does not fail the gate (each carries a documented exclusion reason);
  - validator stdout/stderr is never hidden;
  - no silent skips: anything not run is reported with a reason;
  - exit code 1 if any required invocation fails or any validator is
    unregistered; exit code 0 only on a clean gate.

A passing gate asserts structural integrity and declared-contract
satisfaction only. It does not assert ratification, adoption, conformance,
certification, external recognition, or resolution of any open blocker.
"""

import glob
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = "CI_VALIDATION_MANIFEST.json"


def load_manifest():
    return json.loads((ROOT / MANIFEST).read_text(encoding="utf-8"))


def run_one(script, args):
    proc = subprocess.run(
        [sys.executable, script, *args],
        cwd=ROOT, capture_output=True, text=True,
    )
    return proc.returncode, proc.stdout, proc.stderr


def main():
    manifest = load_manifest()
    validators = manifest["validators"]
    registered_scripts = {v["script"] for v in validators}

    print("=" * 72)
    print("AltisSports Reference Validation Gate")
    print(f"manifest: {MANIFEST} (version {manifest.get('version')})")
    print("=" * 72)

    gate_failures = []
    non_required_failures = []

    # 1. Fail-closed registration check.
    on_disk = {Path(p).name for p in glob.glob(str(ROOT / "validate_*.py"))}
    unregistered = sorted(on_disk - registered_scripts)
    missing_files = sorted(registered_scripts - on_disk)
    if unregistered:
        for s in unregistered:
            print(f"[UNREGISTERED] {s} is present but not in the manifest — gate failure (fail-closed).")
            gate_failures.append(f"unregistered validator: {s}")
    if missing_files:
        for s in missing_files:
            print(f"[MISSING] manifest references {s}, which is not present — gate failure.")
            gate_failures.append(f"missing validator file: {s}")

    # 2. Run each registered validator's declared invocations.
    for v in validators:
        script = v["script"]
        required = v.get("required", False)
        tag = "REQUIRED" if required else "non-required"
        for inv in v.get("invocations", [{"args": []}]):
            args = inv.get("args", [])
            label = f"{v['id']} [{script} {' '.join(args)}]".strip()
            if script in missing_files:
                print(f"\n--- SKIPPED (file missing): {label} ---")
                continue
            code, out, err = run_one(script, args)
            status = "PASS" if code == 0 else "FAIL"
            print(f"\n--- {status} ({tag}, exit={code}): {label} ---")
            if out.strip():
                print(out.rstrip())
            if err.strip():
                print("[stderr]", err.rstrip())
            if code != 0:
                if required:
                    gate_failures.append(f"required invocation failed: {label}")
                else:
                    reason = (v.get("exclusion") or {}).get("reason", "no reason recorded")
                    non_required_failures.append((label, reason))

    # 3. Summary.
    print("\n" + "=" * 72)
    print("GATE SUMMARY")
    print("=" * 72)
    if non_required_failures:
        print("Non-required validators that failed (reported, not gating):")
        for label, reason in non_required_failures:
            print(f"  - {label}")
            print(f"      reason: {reason}")
    if gate_failures:
        print("\nGATE: FAIL")
        for f in gate_failures:
            print(f"  - {f}")
        sys.exit(1)
    print("\nGATE: PASS — all required validators satisfied; no unregistered validators.")
    print("Scope: structural integrity and declared contracts only; not ratification,")
    print("adoption, conformance, certification, recognition, or blocker resolution.")


if __name__ == "__main__":
    main()
