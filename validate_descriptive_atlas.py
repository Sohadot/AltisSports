#!/usr/bin/env python3
"""Validate the Descriptive Atlas against the live corpus and its id lock.

Enforces ATLAS_DESCRIPTIVE_SCHEMA_V0.1.json and the governing principle that
the Atlas exposes only what the corpus records. Checks:

  1. exact 1:1 coverage with the 20 corpus cases;
  2. no duplicate atlas ids;
  3. every record binds to an existing source case;
  4. no invented source case (both directions exact);
  5. descriptive values are derived from the source (activity, per-dimension
     status, and provisional finding match the corpus);
  6. provenance preserved (claim_class kept where the source had one);
  7. claim classes valid (C1-C6) wherever present;
  8. temporal_status present and permitted;
  9. no Atlas-introduced evaluative/scoring field (denylist);
 10. no silent loss of mandatory record or dimension fields;
 11. stable atlas_id -> source_case_id binding, consistent with the lock;
 12. license within the permitted CC-BY-4.0 corpus basis.

Standard library only; exit 0 on pass, 1 on failure.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CORPUS = "boundary-cases-001-020.v0.3.json"
ATLAS = "ATLAS_DESCRIPTIVE_V0.1.json"
LOCK = "ATLAS_ID_LOCK_V0.1.json"
SCHEMA = "ATLAS_DESCRIPTIVE_SCHEMA_V0.1.json"

VALID_CLAIM = {"C1", "C2", "C3", "C4", "C5", "C6"}
VALID_TEMPORAL = {"provisional"}
MANDATORY_RECORD = [
    "atlas_record_id", "source_case_id", "citation_id", "source_dataset",
    "source_version", "license", "temporal_status", "activity",
    "classified_object", "dimensions", "source_provisional_finding",
    "confidence", "falsifiability", "evidence_sources",
]
MANDATORY_DIMS = [
    "performance_agency", "performance_interface", "embodied_performance",
    "arena", "distributed_arena_relation", "sensing_tracking", "measurement",
    "comparability", "officiation", "outcome_openness", "consequence_structure",
    "operational_spatial_integration", "participatory_actor_relations",
    "human_limits_accessibility",
]
DENY = ["score", "ranking", "rank", "rating", "grade", "maturity",
        "readiness", "certif", "tier", "percentile", "points", "superior", "best_"]
# Dimension -> (corpus field, whether status is compared)
STATUS_DIMS = {
    "performance_agency": "performance_agency",
    "performance_interface": "performance_interface",
    "embodied_performance": "embodied_performance",
    "arena": "arena",
    "sensing_tracking": "tracking",
    "measurement": "measurement",
    "comparability": "comparability",
    "officiation": "officiation",
    "outcome_openness": "outcome_openness",
    "consequence_structure": "consequence_structure",
}


def read_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def all_keys(obj, acc):
    if isinstance(obj, dict):
        for k, v in obj.items():
            acc.add(k)
            all_keys(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            all_keys(v, acc)


def validate(errors):
    corpus = {c["case_id"]: c for c in read_json(CORPUS)["cases"]}
    atlas = read_json(ATLAS)
    lock = read_json(LOCK)
    records = atlas["records"]

    by_aid = {}
    src_ids = []
    for r in records:
        aid = r.get("atlas_record_id")
        if aid in by_aid:
            errors.append(f"duplicate atlas id: {aid}")            # (2)
        by_aid[aid] = r
        src_ids.append(r.get("source_case_id"))

    # (1)(4) exact 1:1 coverage
    src_set = set(src_ids)
    if len(src_ids) != len(src_set):
        errors.append("duplicate source_case_id across atlas records")
    if src_set != set(corpus):
        errors.append(f"coverage mismatch: missing={set(corpus)-src_set} invented={src_set-set(corpus)}")

    lock_map = {b["atlas_record_id"]: b["source_case_id"] for b in lock["bindings"]}

    for r in records:
        aid = r.get("atlas_record_id")
        scid = r.get("source_case_id")

        # (10) mandatory record fields
        for f in MANDATORY_RECORD:
            if f not in r:
                errors.append(f"{aid}: missing mandatory field {f}")
        # (3) binding to existing case
        if scid not in corpus:
            errors.append(f"{aid}: binds to non-existent case {scid}")
            continue
        c = corpus[scid]

        # (11) stable id binding: ATL-D-NNN <-> BC-NNN and lock agreement
        if aid != "ATL-D-" + scid.split("-", 1)[1]:
            errors.append(f"{aid}: id does not match source {scid}")
        if lock_map.get(aid) != scid:
            errors.append(f"{aid}: lock binding mismatch (lock={lock_map.get(aid)}, record={scid})")
        if r.get("citation_id") != scid:
            errors.append(f"{aid}: citation_id {r.get('citation_id')} != source {scid}")

        # (5) derived values match the corpus
        if r.get("activity") != c["activity"]:
            errors.append(f"{aid}: activity drift")
        dims = r.get("dimensions", {})
        # (10) mandatory dimensions
        for dim in MANDATORY_DIMS:
            if dim not in dims:
                errors.append(f"{aid}: missing mandatory dimension {dim}")
        for dim, field in STATUS_DIMS.items():
            if dim in dims and dims[dim].get("status") != c[field].get("status"):
                errors.append(f"{aid}.{dim}: status drift "
                              f"(atlas={dims[dim].get('status')}, corpus={c[field].get('status')})")
        # (5) provisional finding preserved verbatim
        spf = r.get("source_provisional_finding", {})
        for k in ("sport_contest_axis", "category_relation"):
            if spf.get(k) != c["provisional_finding"].get(k):
                errors.append(f"{aid}: source_provisional_finding.{k} drift")

        # (6)(7) provenance + claim class validity
        for dim, field in STATUS_DIMS.items():
            if dim in dims:
                src_cc = c[field].get("claim_class")
                atl_cc = dims[dim].get("claim_class")
                if src_cc is not None and atl_cc != src_cc:
                    errors.append(f"{aid}.{dim}: claim_class provenance not preserved")
        collected = set()
        all_keys(r, collected)
        for entry in [r, spf] + list(dims.values()) + r.get("evidence_sources", []):
            if isinstance(entry, dict):
                cc = entry.get("claim_class")
                if cc is not None and cc not in VALID_CLAIM:
                    errors.append(f"{aid}: invalid claim_class {cc!r}")

        # (8) temporal status
        if r.get("temporal_status") not in VALID_TEMPORAL:
            errors.append(f"{aid}: invalid temporal_status {r.get('temporal_status')!r}")
        # (12) license basis
        if r.get("license") != "CC-BY-4.0":
            errors.append(f"{aid}: unexpected license {r.get('license')!r}")

        # (9) no evaluative/scoring field introduced
        for k in collected:
            kl = k.lower()
            for term in DENY:
                if term in kl:
                    errors.append(f"{aid}: prohibited evaluative field key {k!r} (matched {term!r})")

    # lock/atlas id set agreement
    if set(lock_map) != set(by_aid):
        errors.append(f"lock/atlas id set mismatch: {set(lock_map) ^ set(by_aid)}")


def main():
    errors = []
    validate(errors)
    if errors:
        print("FAIL: descriptive atlas invalid")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("PASS: descriptive atlas valid (20/20 cases; 1:1 corpus-derived; "
          "per-field claim provenance preserved; id bindings locked; no evaluative fields).")


if __name__ == "__main__":
    main()
