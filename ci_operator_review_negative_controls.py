#!/usr/bin/env python3
"""Negative controls for validate_asr001_operator_review_package.py.

Each control builds a deliberately invalid operator-review baseline state in an
ISOLATED temporary directory (never mutating the repo working tree) and asserts
the validator REJECTS it (exit 1). A control passes only when the corrupt
fixture produces a non-zero exit.

Controls:
  1. a single baseline hash mismatch;
  2. a missing baseline file referenced by the manifest;
  3. a mutated baseline file (content changed, hash no longer matches);
  4. an incorrect file_count;
  5. a falsified correction block (superseded hash set equal to the real file,
     i.e. claiming a defect that does not exist).

The validator reads many repo files by fixed name, so the whole repo is copied
into the sandbox. Standard library only; exit 0 if all controls behave
correctly, else 1.
"""

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VALIDATOR = "validate_asr001_operator_review_package.py"
MANIFEST = "ASR_001_REVIEW_BASELINE_MANIFEST.json"


def make_sandbox():
    d = Path(tempfile.mkdtemp(prefix="altis_opreview_negctl_"))
    # Copy the whole repo (excluding VCS and caches) so the validator's many
    # fixed-name reads resolve inside the sandbox.
    for item in ROOT.iterdir():
        if item.name in {".git", "__pycache__", "atlas"} or item.name.startswith("."):
            if item.name != "atlas":
                continue
        dest = d / item.name
        if item.is_dir():
            shutil.copytree(item, dest, ignore=shutil.ignore_patterns("__pycache__"))
        else:
            shutil.copy(item, dest)
    return d


def run(sb):
    return subprocess.run([sys.executable, VALIDATOR], cwd=sb,
                          capture_output=True, text=True).returncode


def load(sb, name):
    return json.loads((sb / name).read_text(encoding="utf-8"))


def dump(sb, name, obj):
    (sb / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def c_single_hash(sb):
    m = load(sb, MANIFEST)
    m["files"][0]["sha256"] = "0" * 64
    dump(sb, MANIFEST, m)


def c_missing_file(sb):
    m = load(sb, MANIFEST)
    target = m["files"][0]["path"]
    (sb / target).unlink()
    dump(sb, MANIFEST, m)


def c_mutated_file(sb):
    m = load(sb, MANIFEST)
    target = sb / m["files"][0]["path"]
    target.write_bytes(target.read_bytes() + b"\n<!-- tamper -->\n")


def c_bad_file_count(sb):
    m = load(sb, MANIFEST)
    m["file_count"] = m["file_count"] + 1
    dump(sb, MANIFEST, m)


def c_falsified_correction(sb):
    m = load(sb, MANIFEST)
    corr = m.get("correction")
    if not corr or not corr.get("corrected_entries"):
        # No correction present to falsify; construct a false one.
        path = m["files"][0]["path"]
        actual = hashlib.sha256((sb / path).read_bytes()).hexdigest()
        m["correction"] = {"corrected_entries": [
            {"path": path, "superseded_sha256": actual, "corrected_sha256": actual}],
            "content_changed": False, "review_activated": False}
    else:
        c = corr["corrected_entries"][0]
        actual = hashlib.sha256((sb / c["path"]).read_bytes()).hexdigest()
        c["superseded_sha256"] = actual  # claim a defect that does not exist
    dump(sb, MANIFEST, m)


CONTROLS = [
    ("single baseline hash mismatch", c_single_hash),
    ("missing baseline file", c_missing_file),
    ("mutated baseline file", c_mutated_file),
    ("incorrect file_count", c_bad_file_count),
    ("falsified correction block", c_falsified_correction),
]


def main():
    base = make_sandbox()
    try:
        if run(base) != 0:
            print("FAIL: pristine sandbox did not validate; cannot trust negative controls.")
            sys.exit(1)
    finally:
        shutil.rmtree(base, ignore_errors=True)

    failures = []
    for name, mutate in CONTROLS:
        sb = make_sandbox()
        try:
            mutate(sb)
            code = run(sb)
            ok = code != 0
            print(f"[{'PASS' if ok else 'FAIL'}] negative control: {name} -> exit={code} (expected non-zero)")
            if not ok:
                failures.append(name)
        finally:
            shutil.rmtree(sb, ignore_errors=True)

    if failures:
        print(f"\nFAIL: {len(failures)} operator-review negative control(s) not rejected: {failures}")
        sys.exit(1)
    print(f"\nPASS: {len(CONTROLS)}/{len(CONTROLS)} operator-review negative controls correctly rejected invalid states.")


if __name__ == "__main__":
    main()
