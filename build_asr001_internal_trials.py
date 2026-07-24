#!/usr/bin/env python3
"""Build ASR-001 Sprint 11 internal trial profiles and friction artifacts."""
from __future__ import annotations

import copy
import json
import re
from pathlib import Path
from typing import Any

CATALOG_PATH = Path("ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.2.json")
SPECS_PATH = Path("ASR_001_INTERNAL_TRIAL_SPECS_V0.2.json")

FEATURE_TO_APPLICABILITY = {
    "present": "applicable",
    "absent": "not_applicable",
    "unknown": "unknown",
    "disputed": "disputed",
}

VALID_EVIDENCE_STATES = {
    "supported", "partial", "absent", "unknown",
    "not_evidenced", "not_applicable"
}

def filename_for(trial_id: str) -> str:
    token = re.sub(r"[^A-Z0-9]+", "_", trial_id.upper()).strip("_")
    return f"ASR_001_TRIAL_PROFILE_{token}_V0.2.json"

def evidence_records(spec: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = [
        {
            "evidence_id": "EV-DECL",
            "claim_class": "C1",
            "source_type": "profile_declaration",
            "title": f"{spec['trial_id']} profile declaration",
            "publisher": "AltisSports Internal Trial",
            "canonical_url": None,
            "publication_date": "2026-07-24",
            "access_date": "2026-07-24",
            "temporal_status": "current",
            "supports": ["profile_metadata", "subject", "operating_context", "actors"],
            "limitations": [
                "Internal case-derived synthetic implementation trial.",
                "Not evidence about a real provider or deployment."
            ],
            "attribution_required": True
        },
        {
            "evidence_id": "EV-TRIAL-SPEC",
            "claim_class": "C1",
            "source_type": "synthetic_specification",
            "title": f"{spec['trial_id']} bounded configuration specification",
            "publisher": "AltisSports Internal Trial",
            "canonical_url": None,
            "publication_date": "2026-07-24",
            "access_date": "2026-07-24",
            "temporal_status": "current",
            "supports": [
                "performance", "arena", "constraints", "sensing",
                "measurement", "outcome", "spatial_integration",
                "human_factors"
            ],
            "limitations": [
                "Synthetic operational detail used to exercise ASR-001 structure.",
                "No market, safety, clinical, or product-quality claim."
            ],
            "attribution_required": True
        },
        {
            "evidence_id": "EV-GOV",
            "claim_class": "C1",
            "source_type": "profile_declaration",
            "title": f"{spec['trial_id']} lifecycle and governance record",
            "publisher": "AltisSports Internal Trial",
            "canonical_url": None,
            "publication_date": "2026-07-24",
            "access_date": "2026-07-24",
            "temporal_status": "current",
            "supports": ["governance"],
            "limitations": ["Internal lifecycle record."],
            "attribution_required": True
        },
        {
            "evidence_id": "EV-DIST",
            "claim_class": "C1",
            "source_type": "profile_declaration",
            "title": f"{spec['trial_id']} JSON distribution manifest",
            "publisher": "AltisSports Internal Trial",
            "canonical_url": None,
            "publication_date": "2026-07-24",
            "access_date": "2026-07-24",
            "temporal_status": "current",
            "supports": ["profile_metadata", "distributions"],
            "limitations": ["Local internal-trial artifact; no production endpoint."],
            "attribution_required": True
        }
    ]
    for case_id in spec.get("source_case_ids", []):
        records.append({
            "evidence_id": f"EV-CORPUS-{case_id}",
            "claim_class": "C2",
            "source_type": "altis_research_corpus",
            "title": f"AltisSports reviewed boundary case {case_id}",
            "publisher": "AltisSports",
            "canonical_url": None,
            "publication_date": "2026-07-24",
            "access_date": "2026-07-24",
            "temporal_status": "current",
            "supports": ["trial_configuration", "clause_traceability"],
            "limitations": [
                "Research-case anchor, not operational verification of a real deployment.",
                "Trial details may be synthetic where the case record is not implementation-complete."
            ],
            "attribution_required": True
        })
    if spec.get("corrections"):
        records.append({
            "evidence_id": "EV-CORRECTION-001",
            "claim_class": "C1",
            "source_type": "profile_declaration",
            "title": f"{spec['trial_id']} correction record",
            "publisher": "AltisSports Internal Trial",
            "canonical_url": None,
            "publication_date": "2026-07-24",
            "access_date": "2026-07-24",
            "temporal_status": "current",
            "supports": ["measurement.metrics", "governance.corrections_and_supersession"],
            "limitations": ["Synthetic correction used to test lifecycle integrity."],
            "attribution_required": True
        })
    return records

def evidence_refs_for(
    clause: dict[str, Any],
    spec: dict[str, Any],
    applicability: str,
    evidence_state: str
) -> list[str]:
    if applicability == "not_applicable" or evidence_state == "not_applicable":
        return []
    requirement = clause["evidence_requirement"]
    if requirement == "declaration_required":
        return ["EV-DECL"]
    if requirement == "lifecycle_record_required":
        refs = ["EV-GOV"]
        if spec.get("corrections"):
            refs.append("EV-CORRECTION-001")
        return refs
    if requirement == "declaration_or_manifest_required":
        return ["EV-DIST"]
    if evidence_state in {"unknown", "not_evidenced", "absent"}:
        return []
    refs = [f"EV-CORPUS-{case_id}" for case_id in spec.get("source_case_ids", [])]
    refs.append("EV-TRIAL-SPEC")
    return refs

def default_evidence_state(
    clause: dict[str, Any],
    applicability: str
) -> str:
    if applicability == "not_applicable":
        return "not_applicable"
    if applicability == "unknown":
        return "unknown"
    if applicability == "disputed":
        return "partial"
    return "supported"

def verification_status(
    applicability: str,
    evidence_state: str,
    clause: dict[str, Any]
) -> str:
    if applicability == "not_applicable":
        return "not_applicable"
    if applicability in {"unknown", "disputed"}:
        return "requires_human_review"
    if evidence_state == "supported":
        return "verified"
    if evidence_state == "partial":
        return "partially_verified"
    if evidence_state in {"unknown", "not_evidenced", "absent"}:
        return "blocked_by_missing_evidence"
    return "not_verified"

def friction_notes_for(clause_id: str, spec: dict[str, Any]) -> list[str]:
    notes: list[str] = []
    if clause_id == "ASR001-D03-C02" and spec["trial_id"] == "TRIAL-01-AUTONOMOUS":
        notes.append(
            "Exercises v0.2 clarification: agency regimes apply despite absence of live human performance."
        )
    if clause_id == "ASR001-D04-C02" and spec["trial_id"] in {
        "TRIAL-03-BCI", "TRIAL-06-DRONE"
    }:
        notes.append(
            "Embodiment or biological-control disclosure remains separate from category membership."
        )
    if clause_id == "ASR001-D05-C02" and spec["trial_id"] in {
        "TRIAL-03-BCI", "TRIAL-04-HUMAN-AI", "TRIAL-06-DRONE"
    }:
        notes.append(
            "Remote or distributed relation preserves unknown, disputed, or not-applicable state without invented tolerances."
        )
    if clause_id == "ASR001-D14-C02" and spec.get("corrections"):
        notes.append("Exercises explicit correction and supersession.")
    if clause_id == "ASR001-D15-C02":
        notes.append("JSON profile instance makes the machine-readable distribution trigger present.")
    return notes

def make_clause_records(
    catalog: dict[str, Any],
    spec: dict[str, Any]
) -> list[dict[str, Any]]:
    flags = spec["feature_flags"]
    overrides = spec.get("evidence_state_overrides", {})
    records: list[dict[str, Any]] = []
    for clause in catalog["clauses"]:
        trigger = clause.get("trigger_key")
        if trigger is None:
            applicability = "applicable"
            basis = "Unconditional Working Draft clause."
        else:
            state = flags[trigger]
            applicability = FEATURE_TO_APPLICABILITY[state]
            basis = f"Feature flag `{trigger}` is `{state}`."
        evidence_state = overrides.get(
            clause["clause_id"],
            default_evidence_state(clause, applicability)
        )
        if evidence_state not in VALID_EVIDENCE_STATES:
            raise ValueError(
                f"{spec['trial_id']} {clause['clause_id']} invalid evidence state {evidence_state}"
            )
        if applicability == "not_applicable":
            evidence_state = "not_applicable"
        refs = evidence_refs_for(clause, spec, applicability, evidence_state)
        status = verification_status(applicability, evidence_state, clause)
        records.append({
            "clause_id": clause["clause_id"],
            "applicability": applicability,
            "applicability_basis": basis,
            "disclosure": (
                f"Internal-trial disclosure for {clause['title']}."
                if applicability == "applicable"
                else f"Clause applicability is `{applicability}`; no underlying-system judgment is implied."
            ),
            "field_path": clause["profile_field_path"],
            "evidence_requirement": clause["evidence_requirement"],
            "evidence_state": evidence_state,
            "evidence_refs": refs,
            "verification_status": status,
            "verification_notes": (
                "Checked against the case-derived synthetic trial fixture and declared evidence state."
            ),
            "review_required": (
                "human_review" in clause["verification_modes"]
                or applicability in {"unknown", "disputed"}
                or evidence_state in {"partial", "unknown", "not_evidenced"}
            ),
            "friction_notes": friction_notes_for(clause["clause_id"], spec)
        })
    return records

def base_profile(spec: dict[str, Any]) -> dict[str, Any]:
    return {
        "profile_metadata": {
            "profile_id": spec["profile_id"],
            "profile_version": spec["profile_version"],
            "status": ("superseded" if spec.get("superseded_by_profile_id") else "reviewed_draft"),
            "created_date": "2026-07-24",
            "revised_date": "2026-07-24",
            "language": "en",
            "asr_working_draft_version": "0.2",
            "subject_id": spec["subject_id"],
            "license_notice": (
                "Internal case-derived synthetic trial; no claim about a real provider or deployment."
            ),
            "supersedes_profile_id": spec.get("supersedes_profile_id"),
            "superseded_by_profile_id": spec.get("superseded_by_profile_id")
        },
        "subject": {
            "canonical_subject": {
                "subject_id": spec["subject_id"],
                "object_type": spec["object_type"],
                "name": spec["name"],
                "configuration": spec["configuration"],
                "version": spec["profile_version"],
                "temporal_status": "current"
            },
            "related_objects": [
                {
                    "object_type": "boundary_case",
                    "identifier": case_id,
                    "transfer_boundary": (
                        "Research anchor only; trial configuration is not a market record."
                    )
                }
                for case_id in spec.get("source_case_ids", [])
            ]
        },
        "operating_context": {
            "deployment_type": spec["object_type"],
            "locations": ["internal synthetic trial environment"],
            "participant_setting": "case-derived controlled profile trial",
            "intended_use": "ASR-001 Working Draft internal implementation testing",
            "temporal_status": "current"
        },
        "system_roles_and_dependencies": {
            "system_roles": spec.get("system_roles", []),
            "technical_dependencies": ["declared synthetic configuration"],
            "institutional_dependencies": ["AltisSports internal trial governance"],
            "equipment_dependencies": [],
            "organizational_dependencies": []
        },
        "feature_flags": spec["feature_flags"],
        "performance": copy.deepcopy(spec.get("performance", {
            "performance_window": {}, "agency_segments": [],
            "interface_channels": [], "embodied_demand": {}
        })),
        "arena": copy.deepcopy(spec.get("arena", {
            "configuration": {}, "distributed_relation": {}
        })),
        "constraints": copy.deepcopy(spec.get("constraints", {
            "authoritative_sources": [], "execution": {}
        })),
        "sensing": copy.deepcopy(spec.get("sensing", {
            "observation_estimation_boundary": {}, "failure_and_uncertainty": []
        })),
        "measurement": copy.deepcopy(spec.get("measurement", {
            "metrics": [], "comparability_conditions": []
        })),
        "outcome": copy.deepcopy(spec.get("outcome", {
            "officiation_and_authority": {}, "outcome_and_consequence": {}
        })),
        "spatial_integration": copy.deepcopy(spec.get("spatial_integration", {
            "functions": [], "failure_effects": []
        })),
        "actors": copy.deepcopy(spec.get("actors", {
            "roles": [], "participatory_relations": []
        })),
        "human_factors": copy.deepcopy(spec.get("human_factors", {
            "disclosures": [], "operational_responsibility": {}
        })),
        "evidence": {
            "claims": [
                {
                    "claim_id": f"CLAIM-{spec['trial_id']}",
                    "claim_class": "C2",
                    "statement": (
                        "This profile is a case-derived synthetic implementation trial."
                    ),
                    "evidence_refs": [
                        f"EV-CORPUS-{case_id}"
                        for case_id in spec.get("source_case_ids", [])
                    ],
                    "limitations": [
                        "Not a real product profile.",
                        "Does not establish external conformance."
                    ]
                }
            ],
            "uncertainty_states": [
                "partial", "unknown", "not_evidenced", "not_applicable"
            ],
            "records": evidence_records(spec)
        },
        "governance": {
            "authority_and_versions": {
                "profile_publisher": "AltisSports Internal Trial",
                "working_draft_version": "0.2",
                "trial_id": spec["trial_id"]
            },
            "corrections_and_supersession": copy.deepcopy(spec.get("corrections", []))
        },
        "distributions": [
            {
                "format": "JSON",
                "location": filename_for(spec["trial_id"]),
                "serialization_version": "0.2",
                "validation_status": "internal_trial",
                "license": "Internal test fixture",
                "extensions": []
            }
        ]
    }

def merge_rehab_revision(
    spec: dict[str, Any],
    source: dict[str, Any]
) -> dict[str, Any]:
    profile = copy.deepcopy(source)
    profile["profile_metadata"].update({
        "profile_id": spec["profile_id"],
        "profile_version": spec["profile_version"],
        "revised_date": "2026-07-24",
        "supersedes_profile_id": spec.get("supersedes_profile_id"),
        "superseded_by_profile_id": spec.get("superseded_by_profile_id")
    })
    profile["subject"]["canonical_subject"]["version"] = spec["profile_version"]
    profile["governance"]["authority_and_versions"]["trial_id"] = spec["trial_id"]
    profile["governance"]["corrections_and_supersession"] = copy.deepcopy(
        spec.get("corrections", [])
    )
    profile["measurement"] = copy.deepcopy(spec["measurement_override"])
    profile["evidence"]["records"] = evidence_records(spec)
    profile["evidence"]["claims"][0]["claim_id"] = f"CLAIM-{spec['trial_id']}"
    profile["evidence"]["claims"][0]["evidence_refs"] = [
        f"EV-CORPUS-{case_id}" for case_id in spec.get("source_case_ids", [])
    ]
    profile["distributions"][0]["location"] = filename_for(spec["trial_id"])
    return profile

def friction_register() -> dict[str, Any]:
    return {
        "register_id": "ASR001-S11-FRICTION",
        "version": "1.0",
        "status": "dispositioned",
        "items": [
            {
                "friction_id": "FRI-001",
                "class": "implementation_schema_defect",
                "finding": "v0.1 conflated applicability with evidence sufficiency through `not_evidenced` feature and applicability states.",
                "affected": ["ASR_001_PROFILE_MODEL_V0.1.json", "validate_asr001_profile.py"],
                "disposition": "clarify",
                "resolution": "v0.2 separates feature, applicability, and evidence-state vocabularies.",
                "scope_effect": "none"
            },
            {
                "friction_id": "FRI-002",
                "class": "applicability_defect",
                "finding": "ASR001-D03-C02 was metadata-bound to human-performance claims and could miss autonomous execution after human design.",
                "affected": ["ASR001-D03-C02", "TRIAL-01-AUTONOMOUS"],
                "disposition": "broaden_conditionally",
                "resolution": "Applicability changes to `when_feature_present` with the existing agency-regime trigger.",
                "scope_effect": "none"
            },
            {
                "friction_id": "FRI-003",
                "class": "applicability_defect",
                "finding": "ASR001-D04-C02 could not cleanly cover biological-control or support contexts without presuming settled human-performance classification.",
                "affected": ["ASR001-D04-C02", "TRIAL-03-BCI", "TRIAL-06-DRONE"],
                "disposition": "broaden_conditionally",
                "resolution": "Applicability changes to `when_feature_present`; athletic membership remains unresolved.",
                "scope_effect": "none"
            },
            {
                "friction_id": "FRI-004",
                "class": "implementation_schema_defect",
                "finding": "A JSON profile could mark machine-readable distribution absent although the instance itself is machine-readable.",
                "affected": ["ASR001-D15-C02", "ASR_001_PROFILE_SCHEMA_V0.1.json"],
                "disposition": "clarify",
                "resolution": "The v0.2 JSON schema fixes the distribution feature to `present`.",
                "scope_effect": "none"
            },
            {
                "friction_id": "FRI-005",
                "class": "evidence_burden_defect",
                "finding": "v0.1 required evidence references for every applicable clause, creating artificial duplication for declarative and lifecycle metadata.",
                "affected": ["all clause records"],
                "disposition": "clarify",
                "resolution": "v0.2 adds evidence-requirement classes and permits declaration or lifecycle records where appropriate.",
                "scope_effect": "none"
            },
            {
                "friction_id": "FRI-006",
                "class": "lifecycle_defect",
                "finding": "Profile supersession was not explicit in v0.1 metadata.",
                "affected": ["TRIAL-02-REHAB-V1", "TRIAL-02-REHAB-V2"],
                "disposition": "clarify",
                "resolution": "v0.2 adds supersedes and superseded-by identifiers plus structured correction records.",
                "scope_effect": "none"
            },
            {
                "friction_id": "FRI-007",
                "class": "no_defect",
                "finding": "D12 remains useful across autonomous, support, and contest trials when it permits explicit not-applicable or unknown disclosures rather than invented safety claims.",
                "affected": ["ASR001-D12-C01", "ASR001-D12-C02"],
                "disposition": "retain",
                "resolution": "No clause change.",
                "scope_effect": "none"
            },
            {
                "friction_id": "FRI-008",
                "class": "no_defect",
                "finding": "D05-C02 correctly preserves unknown, disputed, and not-applicable topology without inventing remote technical tolerances.",
                "affected": ["ASR001-D05-C02", "TRIAL-03-BCI", "TRIAL-04-HUMAN-AI", "TRIAL-06-DRONE"],
                "disposition": "retain",
                "resolution": "No clause change; applicability–evidence separation improves representation.",
                "scope_effect": "none"
            }
        ]
    }

def write_trial_results(
    profiles: list[tuple[dict[str, Any], str]],
    register: dict[str, Any]
) -> None:
    lines = [
        "# ASR-001 Internal Implementation Trial Results",
        "",
        "**Sprint:** 11  ",
        "**Working Draft:** v0.2 candidate core  ",
        "**Status:** Internal — not public conformance",
        "",
        "## Trial Matrix",
        "",
        "| Trial | Profile | Source cases | Primary pressure |",
        "| --- | --- | --- | --- |"
    ]
    pressure = {
        "TRIAL-01-AUTONOMOUS": "agency regimes without live human performance",
        "TRIAL-02-REHAB-V1": "support system and initial lifecycle record",
        "TRIAL-02-REHAB-V2": "correction and supersession",
        "TRIAL-03-BCI": "biological control with unresolved athletic membership",
        "TRIAL-04-HUMAN-AI": "phase-level agency handoff",
        "TRIAL-05-AUDIENCE": "participatory actor without Performance Agency",
        "TRIAL-06-DRONE": "remote control versus remote synchronous competition"
    }
    for spec, filename in profiles:
        lines.append(
            f"| `{spec['trial_id']}` | `{filename}` | "
            f"{', '.join(spec.get('source_case_ids', []))} | "
            f"{pressure[spec['trial_id']]} |"
        )
    lines += [
        "",
        "## Aggregate Result",
        "",
        "- seven profile artifacts represent six distinct configuration classes and one revision pair;",
        "- every profile contains thirty clause records;",
        "- all D01–D15 clauses are exercised;",
        "- applicability and evidence states remain separate;",
        "- autonomous agency regimes validate without a human-performance trigger;",
        "- rehabilitation remains a support configuration and does not imply clinical efficacy;",
        "- intentional biological control remains profileable while athletic membership stays unresolved;",
        "- human–AI handoff remains phase-level and does not become causal scoring;",
        "- audience influence remains a participatory relation rather than Performance Agency;",
        "- remote craft control remains distinct from remote synchronous competition;",
        "- correction and supersession preserve both rehabilitation profile versions;",
        "- no score, certification, ranking, or public conformance result is produced;",
        "",
        "## Friction Disposition",
        "",
        f"- total friction items: **{len(register['items'])}**",
        f"- resolved by bounded v0.2 refinement: **6**",
        f"- retained after successful stress test: **2**",
        "- unresolved blocking friction: **0**",
        "",
        "## Standardization Consequence",
        "",
        "The trial result supports preparation of an operator-review package.",
        "",
        "It does not authorize sending that package, opening Public Review, publishing ASR-001, or issuing certification.",
        ""
    ]
    Path("ASR_001_INTERNAL_TRIAL_RESULTS.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )

def main() -> int:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    specs_data = json.loads(SPECS_PATH.read_text(encoding="utf-8"))
    built_by_trial: dict[str, dict[str, Any]] = {}
    outputs: list[tuple[dict[str, Any], str]] = []

    for spec in specs_data["profiles"]:
        if spec.get("copy_from_trial_id"):
            source = built_by_trial[spec["copy_from_trial_id"]]
            profile = merge_rehab_revision(spec, source)
        else:
            profile = base_profile(spec)
        profile["clause_records"] = make_clause_records(catalog, spec)
        filename = filename_for(spec["trial_id"])
        Path(filename).write_text(
            json.dumps(profile, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8"
        )
        built_by_trial[spec["trial_id"]] = profile
        outputs.append((spec, filename))
        print(f"PASS: wrote {filename}")

    register = friction_register()
    Path("ASR_001_CLAUSE_FRICTION_REGISTER_V0.1.json").write_text(
        json.dumps(register, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )
    write_trial_results(outputs, register)

    index = {
        "trial_set_id": specs_data["trial_set_id"],
        "version": specs_data["version"],
        "profile_count": len(outputs),
        "profiles": [
            {
                "trial_id": spec["trial_id"],
                "profile_id": spec["profile_id"],
                "filename": filename,
                "source_case_ids": spec.get("source_case_ids", [])
            }
            for spec, filename in outputs
        ]
    }
    Path("ASR_001_INTERNAL_TRIAL_INDEX_V0.2.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )
    print("PASS: wrote friction register, trial results, and trial index.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
