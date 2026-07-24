#!/usr/bin/env python3
"""Build ASR-001 evidence-to-clause and coverage reports from the candidate catalog."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

CATALOG = Path("ASR_001_CLAUSE_CATALOG_V0.1.json")

def main() -> int:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    clauses = data["candidate_clauses"]

    lines = [
        "# ASR-001 Evidence-to-Clause Map",
        "",
        "**Catalog:** `ASR_001_CLAUSE_CATALOG_V0.1.json`  ",
        "**Status:** Candidate mapping — not normative",
        "",
        "## Mapping",
        "",
        "| Clause | Domain | Candidate intent | Applicability | Evidence cases | Governance dependencies | Verification |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in clauses:
        cases = ", ".join(item["evidence_case_refs"]) or "—"
        deps = ", ".join(f"`{x}`" for x in item["governance_dependencies"]) or "—"
        checks = ", ".join(item["verification_modes"])
        intent = item["candidate_obligation_intent"].replace("|", "\\|")
        lines.append(
            f"| `{item['clause_id']}` | {item['domain_id']} | {intent} | "
            f"`{item['applicability_class']}` | {cases} | {deps} | {checks} |"
        )
    lines += [
        "",
        "## Interpretation",
        "",
        "The map demonstrates provenance for clause authoring. It does not establish weights, scores, certification, or publication status.",
        "",
    ]
    Path("ASR_001_EVIDENCE_TO_CLAUSE_MAP.md").write_text("\n".join(lines), encoding="utf-8")

    counts = Counter(item["domain_id"] for item in clauses)
    app_counts = Counter(item["applicability_class"] for item in clauses)
    family_counts = Counter(item["clause_family"] for item in clauses)
    verification_counts = Counter(v for item in clauses for v in item["verification_modes"])
    evidence_cases = sorted({case for item in clauses for case in item["evidence_case_refs"]})
    guarded = sorted({guard for item in clauses for guard in item["exclusions_guarded"]})

    coverage = [
        "# ASR-001 Candidate Clause Coverage Report",
        "",
        "**Status:** Structural coverage — not clause approval",
        "",
        "## Summary",
        "",
        f"- candidate clauses: **{len(clauses)}**",
        f"- approved domains covered: **{len(counts)}**",
        f"- boundary cases referenced: **{len(evidence_cases)}**",
        f"- exclusion guards referenced: **{len(guarded)}**",
        "",
        "## Domain Coverage",
        "",
        "| Domain | Candidate clauses |",
        "| --- | ---: |",
    ]
    for domain in sorted(counts):
        coverage.append(f"| {domain} | {counts[domain]} |")
    coverage += ["", "## Applicability Coverage", "", "| Class | Count |", "| --- | ---: |"]
    for key, value in sorted(app_counts.items()):
        coverage.append(f"| `{key}` | {value} |")
    coverage += ["", "## Clause Family Coverage", "", "| Family | Count |", "| --- | ---: |"]
    for key, value in sorted(family_counts.items()):
        coverage.append(f"| `{key}` | {value} |")
    coverage += ["", "## Verification Coverage", "", "| Mode | Count |", "| --- | ---: |"]
    for key, value in sorted(verification_counts.items()):
        coverage.append(f"| `{key}` | {value} |")
    coverage += [
        "",
        "## Evidence Case Coverage",
        "",
        ", ".join(evidence_cases),
        "",
        "Coverage is necessary for architecture completeness. It does not make any candidate clause normative.",
        "",
    ]
    Path("ASR_001_CLAUSE_COVERAGE_REPORT.md").write_text("\n".join(coverage), encoding="utf-8")

    print("PASS: wrote ASR_001_EVIDENCE_TO_CLAUSE_MAP.md")
    print("PASS: wrote ASR_001_CLAUSE_COVERAGE_REPORT.md")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
