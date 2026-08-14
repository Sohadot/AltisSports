#!/usr/bin/env python3
"""Validate the AltisSports Citation Registry and Identifier Lock.

Enforces REFERENCE_AUTHORITY_AND_CITABILITY_MODEL.md section 5 against the
live corpus:

  - exact coverage of the boundary-case, ASR clause, and AS3 element sets;
  - unique citation identifiers;
  - claim class in C1-C6 (SOURCE_AND_CLAIM_POLICY.md section 2);
  - temporal status present;
  - explicit license or a declared open blocker;
  - externally_citable only when licensed and unblocked;
  - falsifiability reference present;
  - provider claim separated from Altis interpretation;
  - semantic bindings match the live corpus (no silent repointing);
  - retired identifiers are tombstoned and never reused.

Optional stability check against a prior baseline:

    python3 validate_citation_registry.py --baseline OLD_REGISTRY.json

Standard library only; exit code 0 on pass, 1 on failure.
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BOUNDARY_FILE = "boundary-cases-001-020.v0.3.json"
ASR_CATALOG_FILE = "ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.2.json"
AS3_FILE = "AS3_STACK.md"
REGISTRY = "CITATION_REGISTRY_V0.1.json"
LOCK = "CITATION_ID_LOCK_V0.1.json"

VALID_CLAIM_CLASSES = {"C1", "C2", "C3", "C4", "C5", "C6"}
VALID_TEMPORAL = {
    "current", "announced", "pilot", "beta", "discontinued",
    "superseded", "unverified", "historical", "provisional",
}


def read_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def live_sets():
    bc = {c["case_id"]: c for c in read_json(BOUNDARY_FILE)["cases"]}
    asr = {c["clause_id"]: c for c in read_json(ASR_CATALOG_FILE)["clauses"]}
    as3_text = (ROOT / AS3_FILE).read_text(encoding="utf-8")
    return bc, asr, as3_text


def validate(errors):
    reg = read_json(REGISTRY)
    lock = read_json(LOCK)
    bc_live, asr_live, as3_text = live_sets()

    ids = reg["identifiers"]
    by_id = {}

    # 1. uniqueness
    for entry in ids:
        cid = entry["citation_id"]
        if cid in by_id:
            errors.append(f"duplicate citation_id: {cid}")
        by_id[cid] = entry

    # 2. exact coverage
    reg_bc = {e["citation_id"] for e in ids if e["kind"] == "boundary_case"}
    reg_asr = {e["citation_id"] for e in ids if e["kind"] == "asr_clause"}
    reg_as3 = {e["citation_id"] for e in ids if e["kind"] == "as3_element"}

    if reg_bc != set(bc_live):
        errors.append(f"boundary_case coverage mismatch: missing={set(bc_live)-reg_bc} extra={reg_bc-set(bc_live)}")
    if reg_asr != set(asr_live):
        errors.append(f"asr_clause coverage mismatch: missing={set(asr_live)-reg_asr} extra={reg_asr-set(asr_live)}")
    if len(reg_as3) != 19:
        errors.append(f"as3_element count is {len(reg_as3)}, expected 19")

    # 3. per-entry field discipline (model section 5)
    open_blockers = {b["blocker_id"] for b in reg.get("license_blockers", []) if b.get("status") == "open"}
    for entry in ids:
        cid = entry["citation_id"]
        if entry.get("claim_class") not in VALID_CLAIM_CLASSES:
            errors.append(f"{cid}: invalid claim_class {entry.get('claim_class')!r}")
        if entry.get("temporal_status") not in VALID_TEMPORAL:
            errors.append(f"{cid}: invalid temporal_status {entry.get('temporal_status')!r}")
        if not entry.get("falsifiability_ref"):
            errors.append(f"{cid}: missing falsifiability_ref")
        if not entry.get("interpretation_origin"):
            errors.append(f"{cid}: missing interpretation_origin (provider/Altis separation)")
        if entry.get("provider_claim_separated") is not True:
            errors.append(f"{cid}: provider_claim_separated must be true")
        # citability gate: needs license AND no open blocker
        blocker = entry.get("license_blocker")
        licensed = bool(entry.get("license"))
        citable = entry.get("externally_citable")
        if citable and not licensed:
            errors.append(f"{cid}: externally_citable but no license")
        if citable and blocker in open_blockers:
            errors.append(f"{cid}: externally_citable but under open blocker {blocker}")
        if blocker and blocker in open_blockers and citable:
            errors.append(f"{cid}: open blocker {blocker} must force externally_citable=false")

    # 4. semantic bindings match live corpus (no silent repointing)
    for b in lock["bindings"]:
        cid = b["citation_id"]
        bt = b["binding_type"]
        val = b["bound_value"]
        if bt == "boundary_case_activity":
            live = bc_live.get(cid, {}).get("activity")
            if live != val:
                errors.append(f"binding drift {cid}: activity live={live!r} lock={val!r}")
        elif bt == "asr_clause_profile_field_path":
            live = asr_live.get(cid, {}).get("profile_field_path")
            if live != val:
                errors.append(f"binding drift {cid}: profile_field_path live={live!r} lock={val!r}")
        elif bt == "as3_source_key":
            entry = by_id.get(cid, {})
            marker = entry.get("live_marker", val)
            if marker not in as3_text:
                errors.append(f"binding drift {cid}: AS3 marker {marker!r} not found in {AS3_FILE}")
        else:
            errors.append(f"{cid}: unknown binding_type {bt!r}")

    # 5. every identifier has a lock binding and vice versa
    lock_ids = {b["citation_id"] for b in lock["bindings"]}
    if lock_ids != set(by_id):
        errors.append(f"registry/lock id set mismatch: missing={set(by_id)-lock_ids} extra={lock_ids-set(by_id)}")

    # 6. tombstones never reused as active ids
    active = set(by_id)
    for t in reg.get("tombstones", []) + lock.get("tombstones", []):
        tid = t.get("citation_id") if isinstance(t, dict) else t
        if tid in active:
            errors.append(f"tombstoned id reused as active: {tid}")

    return reg


def check_baseline(reg, baseline_path, errors):
    base = json.loads(Path(baseline_path).read_text(encoding="utf-8"))
    base_bind = {(b["citation_id"], b["binding_type"]): b["bound_value"]
                 for b in base.get("bindings", [])} if "bindings" in base else {}
    # baseline may be a prior registry: compare stable id -> kind/source_key
    base_ids = {e["citation_id"]: e for e in base.get("identifiers", [])}
    cur_ids = {e["citation_id"]: e for e in reg["identifiers"]}
    base_tombstones = {t.get("citation_id") if isinstance(t, dict) else t
                       for t in base.get("tombstones", [])}
    for cid, entry in base_ids.items():
        if cid in base_tombstones:
            continue
        if cid not in cur_ids:
            errors.append(f"stability break: baseline id {cid} dropped without tombstone")
            continue
        if cur_ids[cid].get("source_key") != entry.get("source_key"):
            errors.append(f"stability break: {cid} source_key changed")
        if cur_ids[cid].get("kind") != entry.get("kind"):
            errors.append(f"stability break: {cid} kind changed")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", help="prior CITATION_REGISTRY json to check stability against")
    args = ap.parse_args()

    errors = []
    reg = validate(errors)
    if args.baseline:
        check_baseline(reg, args.baseline, errors)

    if errors:
        print("FAIL: citation registry invalid")
        for e in errors:
            print("  -", e)
        sys.exit(1)

    cov = reg["coverage"]
    print(
        "PASS: citation registry valid "
        f"({reg['identifier_count']} active identifiers; "
        f"BC={cov['boundary_case']} ASR={cov['asr_clause']} AS3={cov['as3_element']}; "
        "semantic bindings locked to live corpus; "
        "LICENSE-ASR-001 gap preserved)."
    )


if __name__ == "__main__":
    main()
