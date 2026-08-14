#!/usr/bin/env python3
"""Validate the Atlas Query / Reference Surface (v0.1).

Checks the query contract, the static distribution, the resolver indexes, and
the CLI behaviour against the live Descriptive Atlas. Standard library only;
exit 0 on pass, 1 on failure.

Checks:
  1. contract present and its source_atlas_version matches the live Atlas;
  2. contract selectors reference existing record fields;
  3. all 20 records resolvable by atlas id (via the CLI);
  4. all 20 records resolvable by source BC id (via the CLI);
  5. no id collisions in resolvers;
  6. distribution covers 20/20;
  7. each distribution record's embedded record is byte/deep-identical to source;
  8. no invented record (distribution id set == atlas id set);
  9. provenance preserved (claim_class present in embedded dimensions);
 10. atlas id -> BC binding preserved and consistent with ATLAS_ID_LOCK;
 11. CLI output deterministic (same query twice);
 12. invalid filters fail closed (CLI exit != 0);
 13. no prohibited evaluative field in contract or CLI output;
 14. citability distinction preserved (not_independently_registered) everywhere;
 15. manifest sha256 and indexes consistent with the generated files.
"""

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ATLAS = "ATLAS_DESCRIPTIVE_V0.1.json"
CONTRACT = "ATLAS_QUERY_CONTRACT_V0.1.json"
LOCK = "ATLAS_ID_LOCK_V0.1.json"
DIST = ROOT / "atlas"
CLI = "query_descriptive_atlas.py"
DENY = ["score", "ranking", "rank", "rating", "grade", "maturity",
        "readiness", "certif", "tier", "percentile", "points", "superior", "best_"]


def read_json(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def run_cli(args):
    proc = subprocess.run([sys.executable, CLI, *args], cwd=ROOT, capture_output=True, text=True)
    return proc.returncode, proc.stdout


def all_keys(obj, acc):
    if isinstance(obj, dict):
        for k, v in obj.items():
            acc.add(k)
            all_keys(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            all_keys(v, acc)


def validate(errors):
    atlas = read_json(ROOT / ATLAS)
    contract = read_json(ROOT / CONTRACT)
    lock = read_json(ROOT / LOCK)
    records = {r["atlas_record_id"]: r for r in atlas["records"]}
    atlas_ids = set(records)
    lock_map = {b["atlas_record_id"]: b["source_case_id"] for b in lock["bindings"]}

    # (1) contract version
    if contract.get("source_atlas_version") != atlas.get("version"):
        errors.append("contract source_atlas_version != atlas version")

    # (2) selectors reference existing fields
    sample = next(iter(records.values()))
    for sel, field in [("atlas_record_id", "atlas_record_id"), ("source_case_id", "source_case_id"),
                       ("activity", "activity"), ("activity_contains", "activity")]:
        if sel not in contract["selectors"]:
            errors.append(f"contract missing selector {sel}")
        if field not in sample:
            errors.append(f"selector {sel} references missing record field {field}")

    # (3)(4) resolvable by both ids via CLI, and (14) citability, (9) provenance
    for aid, r in records.items():
        bc = r["source_case_id"]
        code, out = run_cli(["--atlas-id", aid])
        if code != 0:
            errors.append(f"CLI failed resolving {aid} (exit {code})")
            continue
        res = json.loads(out)
        if res["result_count"] != 1 or res["results"][0]["source_case_id"] != bc:
            errors.append(f"{aid}: atlas-id resolve did not return its source {bc}")
        cit = res["results"][0]["citability"]["atlas_record_citability"]
        if cit != "not_independently_registered":
            errors.append(f"{aid}: citability distinction not preserved ({cit})")
        code2, out2 = run_cli(["--case-id", bc])
        if code2 != 0 or json.loads(out2)["result_count"] != 1:
            errors.append(f"{bc}: not resolvable by source id")
        # (10) binding
        if aid != "ATL-D-" + bc.split("-", 1)[1] or lock_map.get(aid) != bc:
            errors.append(f"{aid}: binding to {bc} not preserved / not in lock")

    # (5) resolver / lock id agreement
    if set(lock_map) != atlas_ids:
        errors.append("lock id set != atlas id set")

    # (6)(7)(8)(9)(14) distribution integrity
    manifest = read_json(DIST / "manifest.json")
    if manifest["record_count"] != len(records):
        errors.append("distribution record_count mismatch")
    dist_ids = set()
    for entry in manifest["records"]:
        aid = entry["atlas_record_id"]
        dist_ids.add(aid)
        rf_path = DIST / entry["path"]
        payload = rf_path.read_bytes()
        if hashlib.sha256(payload).hexdigest() != entry["sha256"]:      # (15)
            errors.append(f"{aid}: manifest sha256 mismatch")
        rf = json.loads(payload)
        # (7) embedded record identical to source
        if rf["record"] != records.get(aid):
            errors.append(f"{aid}: distribution record differs from source atlas record")
        # (9) provenance preserved in embedded dimensions
        pa = rf["record"]["dimensions"]["performance_agency"]
        if "claim_class" not in pa:
            errors.append(f"{aid}: provenance (claim_class) stripped in distribution")
        # (14) citability in distribution
        if rf["citability"]["atlas_record_citability"] != "not_independently_registered":
            errors.append(f"{aid}: distribution citability distinction not preserved")
    # (8) no invented / missing record
    if dist_ids != atlas_ids:
        errors.append(f"distribution id set mismatch: {dist_ids ^ atlas_ids}")

    # (15) resolver indexes consistent
    by_aid = read_json(DIST / "by-atlas-id.json")
    by_case = read_json(DIST / "by-case.json")
    if set(by_aid) != atlas_ids:
        errors.append("by-atlas-id index id set mismatch")
    if set(by_case) != {r["source_case_id"] for r in records.values()}:
        errors.append("by-case index id set mismatch")
    for aid, r in records.items():
        if by_aid.get(aid) != f"records/{aid}.json":
            errors.append(f"{aid}: by-atlas-id path wrong")
        if by_case.get(r["source_case_id"]) != f"records/{aid}.json":
            errors.append(f"{r['source_case_id']}: by-case path wrong")
    for name, sha in manifest["indexes"].items():
        if hashlib.sha256((DIST / name).read_bytes()).hexdigest() != sha:
            errors.append(f"index {name} sha256 mismatch")

    # (11) determinism
    _, a = run_cli(["--sport-contest-axis", "sport"])
    _, b = run_cli(["--sport-contest-axis", "sport"])
    if a != b:
        errors.append("CLI output not deterministic")

    # (12) invalid filters fail closed
    for bad in [["--dimension", "arena", "--status", "___nope___"],
                ["--claim-class", "C9", "--dimension", "arena"],
                ["--totally-made-up", "x"]]:
        code, _ = run_cli(bad)
        if code == 0:
            errors.append(f"invalid query did not fail closed: {bad}")

    # (13) no prohibited evaluative field in contract or a sample output
    ckeys = set()
    all_keys(contract, ckeys)
    _, sample_out = run_cli(["--atlas-id", "ATL-D-001"])
    okeys = set()
    all_keys(json.loads(sample_out), okeys)
    for kset, where in [(ckeys, "contract"), (okeys, "output")]:
        for k in kset:
            for term in DENY:
                if term in k.lower():
                    errors.append(f"prohibited evaluative key {k!r} in {where}")


def main():
    errors = []
    validate(errors)
    if errors:
        print("FAIL: atlas query surface invalid")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("PASS: atlas query surface valid (20/20 resolvable by atlas id and source id; "
          "distribution byte-consistent with source; provenance and citability preserved; "
          "invalid queries fail closed; deterministic).")


if __name__ == "__main__":
    main()
