#!/usr/bin/env python3
"""Run AltisSports Sprint 6 generation, migration, validation, and gate output."""
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path


SOURCE_SCHEMA = Path("BOUNDARY_CASE_SCHEMA_V0.2.json")
SOURCE_DATA = Path("boundary-cases-011-020.v0.2.json")
TARGET_SCHEMA = Path("BOUNDARY_CASE_SCHEMA_V0.3.json")
TARGET_DATA = Path("boundary-cases-011-020.v0.3.json")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_step(args: list[str]) -> None:
    completed = subprocess.run(args, text=True)
    if completed.returncode != 0:
        raise SystemExit(completed.returncode)


def require_files(paths: list[Path]) -> None:
    missing = [str(path) for path in paths if not path.exists()]
    if missing:
        print("ERROR: missing required file(s):")
        for item in missing:
            print(f"- {item}")
        raise SystemExit(2)


def main() -> int:
    required = [
        SOURCE_SCHEMA,
        SOURCE_DATA,
        Path("validate_boundary_cases.py"),
        Path("SECOND_STRATUM_FINDINGS_V0.2.md"),
        Path("TARGETED_BOUNDARY_DEEPENING.md"),
        Path("SCHEMA_V0.3_DECISION.md"),
        Path("TARGETED_DEEPENING_PATCHES_V0.3.json"),
        Path("build_boundary_case_schema_v0_3.py"),
        Path("migrate_boundary_cases_v0_2_to_v0_3.py"),
        Path("validate_boundary_cases_v0_3.py"),
        Path("FIRST_PRINCIPLES.md"),
        Path("ONTOLOGY.md"),
        Path("AS3_STACK.md"),
        Path("DECISION_LOG.md"),
        Path("README.md"),
    ]
    require_files(required)

    before_schema = sha256(SOURCE_SCHEMA)
    before_data = sha256(SOURCE_DATA)

    run_step([
        sys.executable,
        "build_boundary_case_schema_v0_3.py",
        "--source",
        str(SOURCE_SCHEMA),
        "--output",
        str(TARGET_SCHEMA),
    ])
    run_step([
        sys.executable,
        "migrate_boundary_cases_v0_2_to_v0_3.py",
        "--source",
        str(SOURCE_DATA),
        "--patches",
        "TARGETED_DEEPENING_PATCHES_V0.3.json",
        "--output",
        str(TARGET_DATA),
    ])
    run_step([
        sys.executable,
        "validate_boundary_cases_v0_3.py",
        "--schema",
        str(TARGET_SCHEMA),
        "--data",
        str(TARGET_DATA),
    ])

    after_schema = sha256(SOURCE_SCHEMA)
    after_data = sha256(SOURCE_DATA)
    if before_schema != after_schema or before_data != after_data:
        print("FAIL: a v0.2 immutable input changed during Sprint 6")
        return 1

    output_hashes = {
        SOURCE_SCHEMA.name: after_schema,
        SOURCE_DATA.name: after_data,
        TARGET_SCHEMA.name: sha256(TARGET_SCHEMA),
        TARGET_DATA.name: sha256(TARGET_DATA),
        "TARGETED_BOUNDARY_DEEPENING.md": sha256(Path("TARGETED_BOUNDARY_DEEPENING.md")),
        "SCHEMA_V0.3_DECISION.md": sha256(Path("SCHEMA_V0.3_DECISION.md")),
        "FIRST_PRINCIPLES.md": sha256(Path("FIRST_PRINCIPLES.md")),
        "ONTOLOGY.md": sha256(Path("ONTOLOGY.md")),
        "AS3_STACK.md": sha256(Path("AS3_STACK.md")),
    }

    validation_lines = [
        "# Sprint 6 Validation Result",
        "",
        "**Asset:** AltisSports  ",
        "**Sprint:** Sprint 6 — Targeted Boundary Deepening and Schema v0.3 Decision  ",
        "**Date:** 2026-07-24  ",
        "**Decision:** **PASS**",
        "",
        "## Validation",
        "",
        "- `BOUNDARY_CASE_SCHEMA_V0.3.json` was generated additively from v0.2.",
        "- `boundary-cases-011-020.v0.3.json` contains exactly BC-011–BC-020.",
        "- BC-015 retains remote-distributed status as `not_evidenced`.",
        "- BC-017 and BC-019 contain phase/regime-level Agency Segments.",
        "- BC-018 contains an Intentional Biological Control profile while athletic embodiment remains unresolved.",
        "- BC-020 contains a Participatory Rule/Resource Actor relation without direct Performance Agency.",
        "- Evidence references are in range.",
        "- Prohibited score, level, certification, and conformance keys are absent.",
        "- v0.2 schema and dataset hashes are unchanged.",
        "",
        "## SHA-256",
        "",
        "| File | SHA-256 |",
        "| --- | --- |",
    ]
    for name, value in output_hashes.items():
        validation_lines.append(f"| `{name}` | `{value}` |")
    validation_lines.extend([
        "",
        "Validation is structural and deterministic. It does not convert provisional analytical findings into a standard or certification.",
        "",
    ])
    Path("SPRINT_6_VALIDATION_RESULT.md").write_text(
        "\n".join(validation_lines), encoding="utf-8"
    )

    gate = """# Sprint 6 Gate Result

**Asset:** AltisSports  
**Sprint:** Sprint 6 — Targeted Boundary Deepening and Schema v0.3 Decision  
**Gate:** `QUALITY_GATE.md` + schema v0.3 validation  
**Date:** 2026-07-24  
**Decision:** **PASS FOR DECLARED SCOPE**

## 1. Declared Scope

Sprint 6 deepens BC-015, BC-017, BC-018, BC-019, and BC-020 and decides whether corpus schema v0.3 is necessary.

It does not issue a standard, define an embodiment threshold, certify a system, rank vendors, or launch a commercial assessment.

## 2. What Passed

- schema v0.3 is justified by repeated representational gaps rather than release cadence;
- phase/regime Agency Segments preserve observed versus merely permitted control;
- Distributed Arena Relation preserves the difference between co-location, remote synchrony, and remote supervision;
- BC-015 remains `not_evidenced` for geographically distributed synchronous competition;
- Intentional Biological Control supports Performance Agency without settling athletic embodiment;
- Participatory Rule/Resource Actors remain distinct from performers and officials;
- v0.2 historical/native records remain unchanged;
- deterministic local validation passes;
- no total score, level, certification, conformance, or paid ranking exists.

## 3. Remaining Uncertainty

- no normative causal-attribution method exists for agency segments;
- no remote synchronous latency, calibration, safety, or officiation requirements are ratified;
- BC-018 remains unresolved for Spatial Athletic System membership;
- new v0.3 structures have been tested only on their motivating cases;
- hosted CI is still absent.

## 4. Standardization Hold

`ASR-001` remains unauthorized.

Schema adequacy does not itself justify normative requirements.

## 5. Next Governed Move

**Sprint 7 — v0.3 Corpus Application and Standardization-Readiness Gate**

Sprint 7 should apply the new fields to additional existing cases that did not motivate them, review migration-derived BC-001–BC-010 fields, and decide whether an ASR scope document may be drafted.

Any authorization must be a separate gate. It must not automatically issue `ASR-001`.

## 6. Executive Verdict

Sprint 6 passes because it converts four exposed ambiguities into explicit, evidence-linked relations without erasing uncertainty or introducing a score.
"""
    Path("SPRINT_6_GATE_RESULT.md").write_text(gate, encoding="utf-8")

    print(
        "PASS: Sprint 6 generated and validated schema v0.3 and the targeted derivative."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
