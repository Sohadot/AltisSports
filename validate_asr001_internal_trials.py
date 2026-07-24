#!/usr/bin/env python3
"""Validate the complete ASR-001 Sprint 11 internal trial set."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

GENERATED_PROFILES = [
    "ASR_001_TRIAL_PROFILE_TRIAL_01_AUTONOMOUS_V0.2.json",
    "ASR_001_TRIAL_PROFILE_TRIAL_02_REHAB_V1_V0.2.json",
    "ASR_001_TRIAL_PROFILE_TRIAL_02_REHAB_V2_V0.2.json",
    "ASR_001_TRIAL_PROFILE_TRIAL_03_BCI_V0.2.json",
    "ASR_001_TRIAL_PROFILE_TRIAL_04_HUMAN_AI_V0.2.json",
    "ASR_001_TRIAL_PROFILE_TRIAL_05_AUDIENCE_V0.2.json",
    "ASR_001_TRIAL_PROFILE_TRIAL_06_DRONE_V0.2.json",
]

PACKAGE_FILES = [
    "ASR_001_INTERNAL_TRIAL_METHOD.md",
    "ASR_001_INTERNAL_TRIAL_SPECS_V0.2.json",
    "ASR_001_CLAUSE_REFINEMENT_V0.1_TO_V0.2.md",
    "ASR_001_PROFILE_MODEL_REFINEMENT_V0.1_TO_V0.2.md",
    "ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.2.json",
    "ASR_001_PROFILE_MODEL_V0.2.json",
    "ASR_001_PROFILE_SCHEMA_V0.2.json",
    "ASR_001_INTERNAL_TRIAL_GATE.md",
    "ASR_001_WORKING_DRAFT_V0.2.md",
    "ASR_001_CLAUSE_TO_FIELD_MAP_V0.2.json",
    "ASR_001_CLAUSE_FRICTION_REGISTER_V0.1.json",
    "ASR_001_INTERNAL_TRIAL_RESULTS.md",
    "ASR_001_INTERNAL_TRIAL_INDEX_V0.2.json",
] + GENERATED_PROFILES

REPOSITORY_DEPENDENCIES = [
    "ASR_001_INTERNAL_IMPLEMENTATION_TRIAL_AUTHORIZATION.md",
    "ASR_001_NORMATIVE_CORE_GATE_RESULT.md",
    "ASR_001_WORKING_DRAFT_V0.1.md",
    "ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.1.json",
    "ASR_001_PROFILE_MODEL_V0.1.json",
    "ASR_001_PROFILE_SCHEMA_V0.1.json",
    "boundary-cases-001-020.v0.3.json",
    "DECISION_LOG.md",
]

def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain an object")
    return data

def clause_record(profile: dict[str, Any], clause_id: str) -> dict[str, Any]:
    for record in profile["clause_records"]:
        if record["clause_id"] == clause_id:
            return record
    raise KeyError(clause_id)

def validate() -> list[str]:
    errors: list[str] = []
    for name in PACKAGE_FILES + REPOSITORY_DEPENDENCIES:
        if not Path(name).exists():
            errors.append(f"missing required file: {name}")
    if errors:
        return errors

    authorization = Path(
        "ASR_001_INTERNAL_IMPLEMENTATION_TRIAL_AUTHORIZATION.md"
    ).read_text(encoding="utf-8")
    if "AUTHORIZED FOR INTERNAL IMPLEMENTATION TRIALS ONLY" not in authorization:
        errors.append("internal implementation trials are not authorized")

    prior_gate = Path(
        "ASR_001_NORMATIVE_CORE_GATE_RESULT.md"
    ).read_text(encoding="utf-8")
    if "PASS — AUTHORIZE INTERNAL IMPLEMENTATION TRIALS ONLY" not in prior_gate:
        errors.append("Sprint 10 gate authorization is missing")

    decision_log = Path("DECISION_LOG.md").read_text(encoding="utf-8")
    if "DEC-013 — ASR-001 Candidate Normative Core and Internal-Trial Boundary" not in decision_log:
        errors.append("DEC-013 is missing")

    old = load_json(Path("ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.1.json"))
    new = load_json(Path("ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.2.json"))
    old_clauses = old.get("clauses", [])
    new_clauses = new.get("clauses", [])
    old_ids = [item.get("clause_id") for item in old_clauses]
    new_ids = [item.get("clause_id") for item in new_clauses]
    if old_ids != new_ids or len(new_ids) != 30:
        errors.append("v0.2 must preserve all thirty v0.1 clause identifiers and order")

    old_by_id = {item["clause_id"]: item for item in old_clauses}
    new_by_id = {item["clause_id"]: item for item in new_clauses}
    changed_applicability = {
        cid for cid in new_ids
        if old_by_id[cid].get("applicability_class")
        != new_by_id[cid].get("applicability_class")
    }
    if changed_applicability != {"ASR001-D03-C02", "ASR001-D04-C02"}:
        errors.append(
            f"unexpected applicability changes: {sorted(changed_applicability)}"
        )
    for cid, clause in new_by_id.items():
        if not clause.get("evidence_requirement"):
            errors.append(f"{cid} lacks evidence_requirement")
        if clause.get("drafting_status") != "candidate_normative_working_draft":
            errors.append(f"{cid} drafting status changed unexpectedly")
    if new.get("publication_status") != "unpublished":
        errors.append("v0.2 catalog publication status must remain unpublished")

    model = load_json(Path("ASR_001_PROFILE_MODEL_V0.2.json"))
    vocab = model.get("state_vocabularies", {})
    if vocab.get("feature_state") != ["present", "absent", "unknown", "disputed"]:
        errors.append("v0.2 feature-state vocabulary is incorrect")
    if "not_evidenced" in vocab.get("applicability_state", []):
        errors.append("not_evidenced must not remain an applicability state")
    if "not_evidenced" not in vocab.get("evidence_state", []):
        errors.append("not_evidenced must exist as an evidence state")

    schema = load_json(Path("ASR_001_PROFILE_SCHEMA_V0.2.json"))
    machine_flag = (
        schema.get("properties", {})
        .get("feature_flags", {})
        .get("properties", {})
        .get("machine_readable_distribution_provided", {})
    )
    if machine_flag.get("const") != "present":
        errors.append("JSON schema must fix machine-readable distribution to present")

    working = Path("ASR_001_WORKING_DRAFT_V0.2.md").read_text(encoding="utf-8")
    if "**Version:** 0.2" not in working:
        errors.append("Working Draft v0.2 version marker is missing")
    if "Applicability and evidence sufficiency are separate." not in working:
        errors.append("Working Draft does not state applicability–evidence separation")
    if working.count("**Candidate clause:**") != 30:
        errors.append("Working Draft v0.2 must render thirty clauses")

    trial_index = load_json(Path("ASR_001_INTERNAL_TRIAL_INDEX_V0.2.json"))
    if trial_index.get("profile_count") != 7:
        errors.append("trial index must contain seven profile artifacts")

    profiles: dict[str, dict[str, Any]] = {}
    for name in GENERATED_PROFILES:
        result = subprocess.run(
            [sys.executable, "validate_asr001_profile_v0_2.py", name],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            errors.append(f"{name} failed validation: {result.stdout}{result.stderr}")
        else:
            profile = load_json(Path(name))
            trial_id = profile["governance"]["authority_and_versions"]["trial_id"]
            profiles[trial_id] = profile

    if len(profiles) != 7:
        return errors

    autonomous = profiles["TRIAL-01-AUTONOMOUS"]
    if autonomous["feature_flags"]["human_performance_claimed"] != "absent":
        errors.append("autonomous trial must not claim live human performance")
    if autonomous["feature_flags"]["agency_modes_or_handoff_present"] != "present":
        errors.append("autonomous trial must exercise agency regimes")
    if clause_record(autonomous, "ASR001-D03-C01")["applicability"] != "not_applicable":
        errors.append("autonomous trial D03-C01 must be not applicable")
    if clause_record(autonomous, "ASR001-D03-C02")["applicability"] != "applicable":
        errors.append("autonomous trial D03-C02 must be applicable")

    bci = profiles["TRIAL-03-BCI"]
    bci_record = clause_record(bci, "ASR001-D04-C02")
    if bci_record["applicability"] != "applicable":
        errors.append("BCI trial D04-C02 must be applicable")
    if bci_record["evidence_state"] != "partial":
        errors.append("BCI trial must preserve partial evidence for D04-C02")
    embodied = bci["performance"]["embodied_demand"]
    if embodied.get("athletic_embodiment_relation") != "unresolved":
        errors.append("BCI athletic embodiment relation must remain unresolved")

    human_ai = profiles["TRIAL-04-HUMAN-AI"]
    if clause_record(human_ai, "ASR001-D03-C02")["applicability"] != "applicable":
        errors.append("human–AI trial must apply agency-segment clause")
    if len(human_ai["performance"]["agency_segments"]) < 2:
        errors.append("human–AI trial needs at least two agency segments")

    audience = profiles["TRIAL-05-AUDIENCE"]
    if clause_record(audience, "ASR001-D11-C02")["applicability"] != "applicable":
        errors.append("audience trial must apply participatory-actor clause")
    relations = audience["actors"]["participatory_relations"]
    if not relations or relations[0].get("performance_agent") is not False:
        errors.append("audience actor must remain non-performing")

    drone = profiles["TRIAL-06-DRONE"]
    if drone["feature_flags"]["distributed_operation_claimed"] != "absent":
        errors.append("drone trial must not claim distributed competition")
    if clause_record(drone, "ASR001-D05-C02")["applicability"] != "not_applicable":
        errors.append("drone D05-C02 must be not applicable")
    reason = drone["arena"]["distributed_relation"].get("reason", "")
    if "not a claim of remote synchronous competition" not in reason:
        errors.append("drone trial must distinguish remote control from remote competition")

    rehab_v1 = profiles["TRIAL-02-REHAB-V1"]
    rehab_v2 = profiles["TRIAL-02-REHAB-V2"]
    if rehab_v1["profile_metadata"]["superseded_by_profile_id"] != rehab_v2["profile_metadata"]["profile_id"]:
        errors.append("rehab v1 must point to v2")
    if rehab_v2["profile_metadata"]["supersedes_profile_id"] != rehab_v1["profile_metadata"]["profile_id"]:
        errors.append("rehab v2 must point to v1")
    corrections = rehab_v2["governance"]["corrections_and_supersession"]
    if len(corrections) != 1:
        errors.append("rehab v2 must contain one correction")
    if rehab_v1["measurement"]["metrics"] == rehab_v2["measurement"]["metrics"]:
        errors.append("rehab correction must change the ambiguous metric")
    if clause_record(rehab_v2, "ASR001-D14-C02")["applicability"] != "applicable":
        errors.append("rehab v2 correction clause must be applicable")

    # All clause IDs and evidence-state separation across the set.
    expected_ids = set(new_ids)
    for trial_id, profile in profiles.items():
        ids = {record["clause_id"] for record in profile["clause_records"]}
        if ids != expected_ids:
            errors.append(f"{trial_id} does not contain all thirty clauses")
        for record in profile["clause_records"]:
            if record["applicability"] == "applicable" and record["evidence_state"] == "not_applicable":
                errors.append(f"{trial_id} conflates applicable with not-applicable evidence")
            if record["applicability"] == "not_applicable" and record["evidence_state"] != "not_applicable":
                errors.append(f"{trial_id} conflates non-applicability and evidence")

    friction = load_json(Path("ASR_001_CLAUSE_FRICTION_REGISTER_V0.1.json"))
    items = friction.get("items", [])
    if len(items) != 8:
        errors.append("friction register must contain eight items")
    if any(item.get("disposition") in {"hold", "unresolved"} for item in items):
        errors.append("friction register contains unresolved blocking disposition")
    if any(item.get("scope_effect") != "none" for item in items):
        errors.append("Sprint 11 refinement must not expand approved scope")

    corpus = load_json(Path("boundary-cases-001-020.v0.3.json"))
    if corpus.get("case_count") != 20 or len(corpus.get("cases", [])) != 20:
        errors.append("research corpus must remain twenty cases")

    return errors

def write_refinement_result() -> None:
    text = """# ASR-001 Internal Trial Refinement Result

**Working Draft transition:** v0.1 → v0.2  
**Decision:** **REFINEMENT ACCEPTED FOR INTERNAL TRIAL BASELINE**

## Clause Result

- thirty identifiers preserved;
- no clause added or removed;
- D03-C02 applicability clarified for autonomous agency regimes;
- D04-C02 applicability clarified for embodied or biological-control disclosures;
- D15-C02 JSON implementation trigger clarified;
- all clauses receive an explicit evidence-requirement class.

## Model Result

- applicability separated from evidence sufficiency;
- feature states simplified to present, absent, unknown, and disputed;
- evidence state remains independently expressible;
- correction and supersession become explicit;
- JSON distribution is structurally present;
- the model remains distinct from the Boundary Case Schema.

## Trial Result

- seven profiles validate;
- six distinct configuration classes are exercised;
- one correction and supersession pair validates;
- all thirty clauses are applied across every profile;
- no blocking implementation friction remains.

## Boundary

This result does not publish ASR-001, establish public conformance, certify any system, or authorize external review outreach.
"""
    Path("ASR_001_REFINEMENT_RESULT.md").write_text(text, encoding="utf-8")

def main() -> int:
    try:
        errors = validate()
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"ERROR: internal-trial validation could not run: {exc}", file=sys.stderr)
        return 2
    if errors:
        print(f"FAIL: {len(errors)} internal-trial validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    write_refinement_result()
    print("PASS: seven ASR-001 internal trial profiles validate.")
    print("PASS: clause refinement v0.1 to v0.2 is bounded and traceable.")
    print("PASS: wrote ASR_001_REFINEMENT_RESULT.md")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
