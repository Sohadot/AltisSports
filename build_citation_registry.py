#!/usr/bin/env python3
"""Build the AltisSports Citation Registry and Identifier Lock.

Operationalizes REFERENCE_AUTHORITY_AND_CITABILITY_MODEL.md section 5.

The registry assigns every citable corpus element a stable identifier that
carries: claim class (SOURCE_AND_CLAIM_POLICY.md section 2, C1-C6),
attribution / interpretation origin separated from provider claim, explicit
license (or an open license blocker), a falsifiability reference, and a
temporal status. The lock binds each identifier to the semantic anchor it
must never be silently repointed away from (BC id -> activity, ASR clause id
-> profile_field_path, AS3 source_key -> citation_id).

Identifiers are derived from the live corpus, never invented. Standard
library only, so the same run works inside a hosted CI gate.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BOUNDARY_FILE = "boundary-cases-001-020.v0.3.json"
ASR_CATALOG_FILE = "ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.2.json"
AS3_FILE = "AS3_STACK.md"
REGISTRY_OUT = "CITATION_REGISTRY_V0.1.json"
LOCK_OUT = "CITATION_ID_LOCK_V0.1.json"

# AS3 is authored prose, not a structured file. Its inspectable elements are
# the ten layers, the Operational Spatial Integration Profile, and the eight
# cross-layer conditions defined in AS3_STACK.md sections 3-5. Each label
# below must appear verbatim in AS3_STACK.md; the validator enforces that.
AS3_ELEMENTS = [
    ("AS3-L1", "L1 — Performance Agency", "Performance Agency"),
    ("AS3-L2", "L2 — Performance Interface and Embodied Demand", "Performance Interface and Embodied Demand"),
    ("AS3-L3", "L3 — Arena and Spatial State", "Arena and Spatial State"),
    ("AS3-L4", "L4 — Constraint and Rule Execution", "Constraint and Rule Execution"),
    ("AS3-L5", "L5 — Sensing, Tracking, and State Estimation", "Sensing, Tracking, and State Estimation"),
    ("AS3-L6", "L6 — Measurement and Comparability", "Measurement and Comparability"),
    ("AS3-L7", "L7 — Officiation and Outcome", "Officiation and Outcome"),
    ("AS3-L8", "L8 — Presence and Participation", "Presence and Participation"),
    ("AS3-L9", "L9 — Safety, Accessibility, and Human Limits", "Safety, Accessibility, and Human Limits"),
    ("AS3-L10", "L10 — Governance, Evidence, and Change", "Governance, Evidence, and Change"),
    ("AS3-OSIP", "Operational Spatial Integration Profile", "Operational Spatial Integration Profile"),
    ("AS3-XLC-INTEGRITY", "Integrity", "Integrity"),
    ("AS3-XLC-AGENCY-HANDOFF", "Agency Handoff", "Agency Handoff"),
    ("AS3-XLC-DISTRIBUTED-ARENA", "Distributed Arena Relation", "Distributed Arena Relation"),
    ("AS3-XLC-PARTICIPATORY-ACTOR", "Participatory Actor Relation", "Participatory Actor Relation"),
    ("AS3-XLC-INTENTIONAL-BIO-CONTROL", "Intentional Biological Control", "Intentional Biological Control"),
    ("AS3-XLC-COMPARABILITY", "Comparability", "Comparability"),
    ("AS3-XLC-ACCESSIBILITY", "Accessibility", "Accessibility"),
    ("AS3-XLC-SECURITY-PRIVACY", "Security and Privacy", "Security and Privacy"),
]

LICENSE_BLOCKERS = [
    {
        "blocker_id": "LICENSE-ASR-001",
        "affects_kind": "asr_clause",
        "reason": (
            "DATASET_LICENSE.md section 1 grants CC BY 4.0 to boundary datasets, "
            "field definitions, case summaries, controlled vocabularies, schema "
            "descriptions, and corpus metadata. It does not explicitly name the "
            "ASR normative clause text. The license is not extended by inference."
        ),
        "status": "open",
        "effect": "ASR clause identifiers are recorded but not externally_citable while open.",
    }
]


def read_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def build_boundary_identifiers():
    data = read_json(BOUNDARY_FILE)
    ids, bindings = [], []
    for case in data["cases"]:
        cid = case["case_id"]
        activity = case["activity"]
        ids.append({
            "citation_id": cid,
            "kind": "boundary_case",
            "source_file": BOUNDARY_FILE,
            "source_key": cid,
            "label": activity,
            "claim_class": "C4",
            "interpretation_origin": "altis_analytical_interpretation",
            "provider_claim_separated": True,
            "temporal_status": "provisional",
            "falsifiability_ref": "what_would_change_judgment",
            "license": "CC-BY-4.0",
            "license_ref": "DATASET_LICENSE.md",
            "license_blocker": None,
            "externally_citable": True,
        })
        bindings.append({
            "citation_id": cid,
            "binding_type": "boundary_case_activity",
            "bound_value": activity,
            "source_file": BOUNDARY_FILE,
            "source_key": cid,
        })
    return ids, bindings


def build_asr_identifiers():
    catalog = read_json(ASR_CATALOG_FILE)
    ids, bindings = [], []
    for clause in catalog["clauses"]:
        cid = clause["clause_id"]
        field_path = clause["profile_field_path"]
        ids.append({
            "citation_id": cid,
            "kind": "asr_clause",
            "source_file": ASR_CATALOG_FILE,
            "source_key": cid,
            "label": clause["title"],
            "claim_class": "C5",
            "interpretation_origin": "altis_provisional_normative_proposition",
            "provider_claim_separated": True,
            "temporal_status": "provisional",
            "falsifiability_ref": "uncertainty_handling",
            "license": None,
            "license_ref": "DATASET_LICENSE.md",
            "license_blocker": "LICENSE-ASR-001",
            "externally_citable": False,
        })
        bindings.append({
            "citation_id": cid,
            "binding_type": "asr_clause_profile_field_path",
            "bound_value": field_path,
            "source_file": ASR_CATALOG_FILE,
            "source_key": cid,
        })
    return ids, bindings


def build_as3_identifiers():
    ids, bindings = [], []
    for source_key, label, live_marker in AS3_ELEMENTS:
        ids.append({
            "citation_id": source_key,
            "kind": "as3_element",
            "source_file": AS3_FILE,
            "source_key": source_key,
            "label": label,
            "live_marker": live_marker,
            "claim_class": "C5",
            "interpretation_origin": "altis_provisional_reference_definition",
            "provider_claim_separated": True,
            "temporal_status": "provisional",
            "falsifiability_ref": "AS3_STACK.md#9-revision-trigger",
            "license": "CC-BY-4.0",
            "license_ref": "DATASET_LICENSE.md",
            "license_blocker": None,
            "externally_citable": True,
        })
        bindings.append({
            "citation_id": source_key,
            "binding_type": "as3_source_key",
            "bound_value": label,
            "source_file": AS3_FILE,
            "source_key": source_key,
        })
    return ids, bindings


def main():
    bc_ids, bc_bind = build_boundary_identifiers()
    asr_ids, asr_bind = build_asr_identifiers()
    as3_ids, as3_bind = build_as3_identifiers()
    identifiers = bc_ids + asr_ids + as3_ids
    bindings = bc_bind + asr_bind + as3_bind

    registry = {
        "registry": "AltisSports Citation Registry",
        "version": "0.1",
        "status": "Foundation Draft — Not Ratified",
        "generated": "2026-08-14",
        "model_reference": "REFERENCE_AUTHORITY_AND_CITABILITY_MODEL.md",
        "claim_class_scheme": "SOURCE_AND_CLAIM_POLICY.md section 2 (C1-C6)",
        "identifier_count": len(identifiers),
        "coverage": {
            "boundary_case": len(bc_ids),
            "asr_clause": len(asr_ids),
            "as3_element": len(as3_ids),
        },
        "license_blockers": LICENSE_BLOCKERS,
        "identifiers": identifiers,
        "tombstones": [],
        "notes": (
            "Externally citable only when license present and no open blocker "
            "applies. ASR clauses remain non-citable until LICENSE-ASR-001 is "
            "resolved explicitly. Evaluative use remains gated by "
            "REFERENCE_AUTHORITY_AND_CITABILITY_MODEL.md section 6."
        ),
    }

    lock = {
        "lock": "AltisSports Citation Identifier Lock",
        "version": "0.1",
        "status": "Foundation Draft — Not Ratified",
        "generated": "2026-08-14",
        "purpose": (
            "Prevent semantic identifier reuse. A citation_id may be retired via "
            "a tombstone but must never be reassigned to a different meaning."
        ),
        "binding_count": len(bindings),
        "bindings": bindings,
        "tombstones": [],
    }

    (ROOT / REGISTRY_OUT).write_text(
        json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / LOCK_OUT).write_text(
        json.dumps(lock, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"WROTE {REGISTRY_OUT} ({len(identifiers)} identifiers)")
    print(f"WROTE {LOCK_OUT} ({len(bindings)} bindings)")


if __name__ == "__main__":
    main()
