#!/usr/bin/env python3
"""Execute Sprint 7 corpus review, validation, and readiness gate."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Iterable


SOURCE_FILES = [
    "BOUNDARY_CASE_SCHEMA_V0.3.json",
    "boundary-cases-001-010.v0.2.json",
    "boundary-cases-011-020.v0.3.json",
]

GENERATED = [
    "boundary-cases-001-010.reviewed.v0.3.json",
    "boundary-cases-011-020.reviewed.v0.3.json",
    "boundary-cases-001-020.v0.3.json",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run(args: list[str]) -> None:
    completed = subprocess.run(args, text=True)
    if completed.returncode != 0:
        raise RuntimeError(f"Command failed ({completed.returncode}): {' '.join(args)}")


def require(paths: Iterable[str]) -> None:
    missing = [name for name in paths if not Path(name).exists()]
    if missing:
        raise FileNotFoundError(f"Missing required files: {', '.join(missing)}")


def write_results(before: dict[str, str], after: dict[str, str]) -> None:
    generated_hashes = {name: sha256(Path(name)) for name in GENERATED}

    validation_lines = [
        "# Sprint 7 Validation Result",
        "",
        "**Asset:** AltisSports  ",
        "**Sprint:** Sprint 7 — v0.3 Corpus Application and Standardization-Readiness Gate  ",
        "**Date:** 2026-07-24  ",
        "**Decision:** **PASS**",
        "",
        "## Validation",
        "",
        "- BC-001–BC-010 were converted from review-required v0.2 migration into a human-reviewed v0.3 derivative.",
        "- BC-011, BC-012, BC-013, BC-014, and BC-016 received v0.3 relations outside the cases that motivated schema v0.3.",
        "- Sprint 6 targeted relations for BC-015, BC-017, BC-018, BC-019, and BC-020 were retained and rechecked.",
        "- The assembled corpus contains exactly BC-001–BC-020.",
        "- Every record validates against `BOUNDARY_CASE_SCHEMA_V0.3.json`.",
        "- Every record and v0.3 relation is marked `human_reviewed_v0_3`.",
        "- BC-018 remains unresolved for category membership.",
        "- No total score, level, certification, conformance, or ranking key exists.",
        "- Source schema and datasets were not modified.",
        "",
        "## Source Integrity",
        "",
        "| Source file | SHA-256 before | SHA-256 after |",
        "| --- | --- | --- |",
    ]
    for name in SOURCE_FILES:
        validation_lines.append(f"| `{name}` | `{before[name]}` | `{after[name]}` |")
    validation_lines += ["", "## Generated Files", "", "| File | SHA-256 |", "| --- | --- |"]
    for name in GENERATED:
        validation_lines.append(f"| `{name}` | `{generated_hashes[name]}` |")
    validation_lines += [
        "",
        "Validation is structural and deterministic. It does not issue a standard or certify a system.",
    ]
    Path("SPRINT_7_VALIDATION_RESULT.md").write_text("\n".join(validation_lines) + "\n", encoding="utf-8")

    readiness = """# Standardization Readiness Result

**Asset:** AltisSports  
**Gate:** `STANDARDIZATION_READINESS_GATE.md`  
**Date:** 2026-07-24  
**Decision:** **AUTHORIZE SCOPE DRAFTING ONLY**

## 1. Passed for Scope Drafting

- two antagonistic strata and twenty reviewed cases exist;
- ordinary, computational, support-system, automation, assisted, distributed, and participatory cases are represented;
- candidate invariants and object classes remain coherent after correction;
- schema v0.3 works outside its motivating cases;
- uncertainty remains expressible without a score;
- source, claim, correction, version, and license rules are operational;
- the first ASR problem can be bounded as an evidence-profile problem.

## 2. Why Requirements Drafting Is Not Authorized

- no ASR scope document has yet passed approval;
- no normative causal-attribution method exists;
- no remote-synchronous latency, calibration, safety, or officiation requirements are ratified;
- BCI athletic membership remains unresolved;
- conformance, appeals, and public-review procedures have not been applied to an ASR draft;
- validation is not yet hosted in CI;
- external expert review has not occurred.

## 3. Authorized Next Artifact

A descriptive scope draft under the working title:

> **ASR-001 — Spatial Athletic System Evidence Profile**

The scope draft may define the problem, object, users, inclusions, exclusions, dependencies, evidence basis, and non-goals.

## 4. Still Prohibited

Normative requirements, certification, scoring, conformance, vendor ranking, federation recognition, and publication of ASR-001 as a standard remain unauthorized.
"""
    Path("STANDARDIZATION_READINESS_RESULT.md").write_text(readiness.strip() + "\n", encoding="utf-8")

    gate = """# Sprint 7 Gate Result

**Asset:** AltisSports  
**Sprint:** Sprint 7 — v0.3 Corpus Application and Standardization-Readiness Gate  
**Date:** 2026-07-24  
**Decision:** **PASS FOR DECLARED SCOPE**

## 1. Declared Scope

Sprint 7 applies schema v0.3 across the existing corpus, completes human review of the first migrated stratum, and decides whether ASR scope drafting may begin.

It does not issue a standard or authorize normative requirements.

## 2. What Passed

- twenty reviewed records validate under schema v0.3;
- historical source datasets remain unchanged;
- new relations work beyond their motivating cases;
- no schema v0.4 is required by the current corpus;
- uncertainty and object heterogeneity remain visible;
- ASR drafting governance and a bounded candidate problem are defined;
- non-scoring and commercial-independence rules remain intact.

## 3. Standardization Decision

**ASR-001 scope drafting is authorized.**

The authorization is limited to a descriptive scope artifact for a candidate Spatial Athletic System Evidence Profile.

## 4. What Remains Unauthorized

- normative requirements;
- conformance;
- certification;
- scoring or maturity levels;
- product or vendor ranking;
- public release of ASR-001 as a standard.

## 5. Next Governed Move

**Sprint 8 — ASR-001 Scope Draft and Scope-Approval Gate**

The next sprint must not write normative requirements.
"""
    Path("SPRINT_7_GATE_RESULT.md").write_text(gate.strip() + "\n", encoding="utf-8")


def main() -> int:
    required = SOURCE_FILES + [
        "validate_boundary_cases.py",
        "FIRST_STRATUM_REVIEW_PATCHES_V0.3.json",
        "SECOND_STRATUM_APPLICATION_PATCHES_V0.3.json",
        "apply_corpus_review_v0_3.py",
        "assemble_corpus_v0_3.py",
        "validate_corpus_application_v0_3.py",
        "STANDARDIZATION_READINESS_GATE.md",
        "ASR_DRAFTING_GOVERNANCE.md",
        "ASR_001_SCOPE_DRAFTING_AUTHORIZATION.md",
    ]
    try:
        require(required)
        before = {name: sha256(Path(name)) for name in SOURCE_FILES}

        run([sys.executable, "apply_corpus_review_v0_3.py"])
        run([sys.executable, "assemble_corpus_v0_3.py"])
        run([sys.executable, "validate_corpus_application_v0_3.py"])

        after = {name: sha256(Path(name)) for name in SOURCE_FILES}
        changed = [name for name in SOURCE_FILES if before[name] != after[name]]
        if changed:
            raise RuntimeError(f"Historical/source files changed: {changed}")

        write_results(before, after)
    except (OSError, ValueError, KeyError, RuntimeError, FileNotFoundError) as exc:
        print(f"ERROR: Sprint 7 failed: {exc}", file=sys.stderr)
        return 1

    print("PASS: Sprint 7 corpus application and standardization-readiness gate completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
