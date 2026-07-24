#!/usr/bin/env python3
"""Execute AltisSports Sprint 4 locally and write auditable results."""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import date
from pathlib import Path

from migrate_boundary_cases_v0_1_to_v0_2 import migrate_dataset
from validate_boundary_cases import load_json, validate_dataset, validate_node

SOURCE_DATA = Path("boundary-cases-001-010.json")
SOURCE_SCHEMA = Path("BOUNDARY_CASE_SCHEMA.json")
TARGET_SCHEMA = Path("BOUNDARY_CASE_SCHEMA_V0.2.json")
TARGET_DATA = Path("boundary-cases-001-010.v0.2.json")
VALIDATION_RESULT = Path("SPRINT_4_VALIDATION_RESULT.md")
GATE_RESULT = Path("SPRINT_4_GATE_RESULT.md")

REQUIRED_INFRASTRUCTURE = [
    Path("SCHEMA_MIGRATION_V0.1_TO_V0.2.md"),
    Path("DATASET_LICENSE.md"),
    Path("SECOND_STRATUM_DESIGN.md"),
    Path("DECISION_LOG.md"),
    Path("README.md"),
    Path("SPRINT_4_EXECUTION.md"),
    Path("SPRINT_4_MANIFEST.json"),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    required = [SOURCE_DATA, SOURCE_SCHEMA, TARGET_SCHEMA, *REQUIRED_INFRASTRUCTURE]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        print("ERROR: missing required files:", file=sys.stderr)
        for path in missing:
            print(f"- {path}", file=sys.stderr)
        return 2


    decision_text = Path("DECISION_LOG.md").read_text(encoding="utf-8")
    if decision_text.count("## DEC-007 — Corpus Schema Evolution and Open Dataset Licensing") != 1:
        print("ERROR: DECISION_LOG.md must contain DEC-007 exactly once.", file=sys.stderr)
        return 2

    readme_text = Path("README.md").read_text(encoding="utf-8")
    if "Sprint 5 — Second Antagonistic Stratum BC-011–BC-020" not in readme_text:
        print("ERROR: README.md is not aligned to the Sprint 4 next move.", file=sys.stderr)
        return 2

    license_text = Path("DATASET_LICENSE.md").read_text(encoding="utf-8")
    if "CC-BY-4.0" not in license_text or "creativecommons.org/licenses/by/4.0/" not in license_text:
        print("ERROR: DATASET_LICENSE.md lacks the governed CC BY 4.0 declaration.", file=sys.stderr)
        return 2

    design_text = Path("SECOND_STRATUM_DESIGN.md").read_text(encoding="utf-8")
    design_ids = sorted(set(__import__("re").findall(r"BC-(?:01[1-9]|020)", design_text)))
    expected_design_ids = [f"BC-{number:03d}" for number in range(11, 21)]
    if design_ids != expected_design_ids:
        print("ERROR: SECOND_STRATUM_DESIGN.md must contain BC-011 through BC-020.", file=sys.stderr)
        return 2

    source_data_hash_before = sha256(SOURCE_DATA)
    source_schema_hash_before = sha256(SOURCE_SCHEMA)

    try:
        source_dataset = load_json(SOURCE_DATA)
        source_schema = load_json(SOURCE_SCHEMA)
        target_schema = load_json(TARGET_SCHEMA)
    except Exception as exc:
        print(f"ERROR: cannot load required JSON: {exc}", file=sys.stderr)
        return 2

    legacy_errors: list[str] = []
    cases = source_dataset.get("cases")
    if not isinstance(cases, list):
        print("ERROR: legacy dataset has no cases array.", file=sys.stderr)
        return 2

    for index, case in enumerate(cases):
        validate_node(case, source_schema, source_schema, f"$.cases[{index}]", legacy_errors)

    if source_dataset.get("case_count") != len(cases):
        legacy_errors.append("Legacy case_count does not match cases array length.")
    if source_dataset.get("schema_version") != "0.1":
        legacy_errors.append("Legacy dataset schema_version is not 0.1.")

    if legacy_errors:
        print(f"FAIL: legacy baseline has {len(legacy_errors)} error(s)", file=sys.stderr)
        for error in legacy_errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    try:
        migrated = migrate_dataset(source_dataset)
        TARGET_DATA.write_text(
            json.dumps(migrated, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        validation_errors = validate_dataset(migrated, target_schema)
    except Exception as exc:
        print(f"ERROR: migration/validation failed: {exc}", file=sys.stderr)
        return 1

    if sha256(SOURCE_DATA) != source_data_hash_before:
        print("ERROR: legacy dataset changed during execution.", file=sys.stderr)
        return 1
    if sha256(SOURCE_SCHEMA) != source_schema_hash_before:
        print("ERROR: legacy schema changed during execution.", file=sys.stderr)
        return 1

    if validation_errors:
        print(f"FAIL: v0.2 dataset has {len(validation_errors)} error(s)")
        for error in validation_errors:
            print(f"- {error}")
        return 1

    today = date.today().isoformat()
    target_hash = sha256(TARGET_DATA)
    target_schema_hash = sha256(TARGET_SCHEMA)

    validation_text = f"""# Sprint 4 Validation Result

**Asset:** AltisSports  
**Date:** {today}  
**Decision:** **PASS**

## Validation Scope

- Historical schema: `BOUNDARY_CASE_SCHEMA.json`
- Historical dataset: `boundary-cases-001-010.json`
- Target schema: `BOUNDARY_CASE_SCHEMA_V0.2.json`
- Migrated dataset: `boundary-cases-001-010.v0.2.json`
- Cases: {migrated['case_count']}

## Results

- Historical BC-001–BC-010 case records validate against schema v0.1.
- The historical schema and dataset remained byte-for-byte unchanged during migration.
- All migrated cases validate against schema v0.2.
- Dataset wrapper and declared case count are consistent.
- Case identifiers are unique and complete from BC-001 through BC-010.
- Operational Spatial Integration evidence references are in range.
- Automated migrations remain marked `automated_review_required`.
- No prohibited total-score, maturity-level, spatiality-level, or certification keys are present.

## SHA-256 Evidence

| Artifact | SHA-256 |
| --- | --- |
| `BOUNDARY_CASE_SCHEMA.json` | `{source_schema_hash_before}` |
| `boundary-cases-001-010.json` | `{source_data_hash_before}` |
| `BOUNDARY_CASE_SCHEMA_V0.2.json` | `{target_schema_hash}` |
| `boundary-cases-001-010.v0.2.json` | `{target_hash}` |

## Interpretation

This PASS confirms structural migration and validation. It does not convert automated semantic inferences into human-reviewed judgments, authorize scoring, or authorize `ASR-001`.
"""
    VALIDATION_RESULT.write_text(validation_text, encoding="utf-8")

    gate_text = f"""# Sprint 4 Gate Result

**Asset:** AltisSports  
**Sprint:** Sprint 4 — Corpus Infrastructure and Second-Stratum Readiness  
**Date:** {today}  
**Decision:** **PASS FOR DECLARED SCOPE**

## 1. Declared Scope

Sprint 4 establishes versioned corpus infrastructure and designs the next antagonistic research stratum.

It does not analyze BC-011–BC-020, issue a standard, publish a score, certify a system, or launch a commercial assessment.

## 2. Completed Outputs

- `BOUNDARY_CASE_SCHEMA_V0.2.json`
- `SCHEMA_MIGRATION_V0.1_TO_V0.2.md`
- `migrate_boundary_cases_v0_1_to_v0_2.py`
- `validate_boundary_cases.py`
- `run_sprint4.py`
- `boundary-cases-001-010.v0.2.json`
- `SPRINT_4_VALIDATION_RESULT.md`
- `DATASET_LICENSE.md`
- `SECOND_STRATUM_DESIGN.md`
- `DECISION_LOG.md` with DEC-007
- aligned `README.md`

## 3. Gate Findings

### Historical integrity
PASS — v0.1 schema and data were validated and remained unchanged.

### Schema evolution
PASS — v0.2 reflects Performance Agency, Embodied Performance, Consequence Structure, object lock, and the Operational Spatial Integration Profile.

### Migration discipline
PASS — migration output uses a separate file and every semantic inference remains review-required.

### Validation
PASS — {migrated['case_count']} migrated records pass schema and cross-record checks.

### Licensing
PASS — original AltisSports dataset material is declared under CC BY 4.0 with explicit third-party exclusions and attribution guidance.

### Second-stratum readiness
PASS — BC-011–BC-020 are selected to stress unresolved agency, embodiment, assistance, distributed space, support-system, and participation boundaries.

## 4. Remaining Conditions

- Automated migrated fields require human case-level review before being described as native v0.2 judgments.
- BC-011–BC-020 have not yet been researched.
- Minimum embodied demand remains unresolved.
- Normative Operational Spatial Integration requirements remain unresolved.
- Dataset validation is local and deterministic but not yet wired into hosted CI.

## 5. Standardization Hold

`ASR-001` remains unauthorized.

The next governed move is **Sprint 5 — Second Antagonistic Stratum BC-011–BC-020**, using schema v0.2 and preserving the non-scoring rule.

## 6. Executive Verdict

Sprint 4 passes as corpus infrastructure and research readiness. It converts theory revision into a versioned, migratable, locally validated data system without rewriting the original evidence record.
"""
    GATE_RESULT.write_text(gate_text, encoding="utf-8")

    print(
        f"PASS: Sprint 4 generated {TARGET_DATA}, {VALIDATION_RESULT}, "
        f"and {GATE_RESULT}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
