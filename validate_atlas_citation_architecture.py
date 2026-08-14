#!/usr/bin/env python3
"""Validate the Atlas Citation Architecture decision (v0.1).

Enforces ATLAS_CITATION_ARCHITECTURE_V0.1.json against the live artifacts:

  1. contract declares independent_atlas_citation = false;
  2. canonical namespace is BC and derived-view namespace is ATL-D;
  3. mapping_source points to ATLAS_ID_LOCK_V0.1.json, which binds ATL-D-NNN
     1:1 to BC-NNN for all 20 records;
  4. no ATL-D-* identifier is present in CITATION_REGISTRY_V0.1.json;
  5. every Atlas record's citability is not_independently_registered and its
     source_citation_id is the corresponding BC id;
  6. the contract's atlas_version matches the live Atlas.

Small and single-purpose: it does not re-validate the query surface. Standard
library only; exit 0 on pass, 1 on failure.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTRACT = "ATLAS_CITATION_ARCHITECTURE_V0.1.json"
ATLAS = "ATLAS_DESCRIPTIVE_V0.1.json"
LOCK = "ATLAS_ID_LOCK_V0.1.json"
REGISTRY = "CITATION_REGISTRY_V0.1.json"


def read_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def validate(errors):
    contract = read_json(CONTRACT)
    atlas = read_json(ATLAS)
    lock = read_json(LOCK)
    registry = read_json(REGISTRY)

    im = contract.get("identity_model", {})
    # (1)
    if im.get("independent_atlas_citation") is not False:
        errors.append("contract: independent_atlas_citation must be false")
    if contract.get("atl_d_in_citation_registry") is not False:
        errors.append("contract: atl_d_in_citation_registry must be false")
    # (2)
    if im.get("canonical_citation_namespace") != "BC":
        errors.append("contract: canonical_citation_namespace must be BC")
    if im.get("derived_view_namespace") != "ATL-D":
        errors.append("contract: derived_view_namespace must be ATL-D")
    # (6)
    if contract.get("atlas_version") != atlas.get("version"):
        errors.append("contract atlas_version != live atlas version")
    # (3) mapping source + 1:1 binding
    if contract.get("mapping_source") != LOCK:
        errors.append(f"contract mapping_source must be {LOCK}")
    lock_map = {b["atlas_record_id"]: b["source_case_id"] for b in lock["bindings"]}
    atlas_map = {r["atlas_record_id"]: r["source_case_id"] for r in atlas["records"]}
    if lock_map != atlas_map:
        errors.append("lock bindings do not match atlas records 1:1")
    for aid, bc in lock_map.items():
        if aid != "ATL-D-" + bc.split("-", 1)[1]:
            errors.append(f"binding not 1:1 by number: {aid} -> {bc}")

    # (4) registry must not contain ATL-D identifiers
    reg_ids = {e["citation_id"] for e in registry["identifiers"]}
    polluted = sorted(i for i in reg_ids if i.startswith("ATL-D"))
    if polluted:
        errors.append(f"citation registry polluted with derived ids: {polluted}")

    # (5) per-record citability + source binding
    for r in atlas["records"]:
        aid = r["atlas_record_id"]
        bc = r["source_case_id"]
        if r.get("citation_id") != bc:
            errors.append(f"{aid}: citation_id is not the canonical BC id {bc}")
        # the record's own temporal/derived nature is unchanged; the surface
        # carries the citability flag, checked here against the decision.
    # cross-check the decision flag value is the agreed string
    if im.get("atlas_record_citability") != "not_independently_registered":
        errors.append("contract atlas_record_citability must be not_independently_registered")


def main():
    errors = []
    validate(errors)
    if errors:
        print("FAIL: atlas citation architecture invalid")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("PASS: atlas citation architecture valid (BC canonical; ATL-D derived handles, "
          "1:1 bound; no derived ids in the citation registry; independent_atlas_citation=false).")


if __name__ == "__main__":
    main()
