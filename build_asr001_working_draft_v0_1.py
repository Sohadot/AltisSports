#!/usr/bin/env python3
"""Generate the ASR-001 Candidate Normative Core and clause-to-field map."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

CATALOG = Path("ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.1.json")

def main() -> int:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    clauses = data["clauses"]
    grouped = defaultdict(list)
    for item in clauses:
        grouped[item["domain_id"]].append(item)

    lines = [
        "# ASR-001 — Spatial Athletic System Evidence Profile",
        "",
        "**Document state:** Non-public Working Draft  ",
        "**Version:** 0.1  ",
        "**Status:** Candidate Normative Core — unpublished  ",
        "**Conformance subject:** Evidence-profile document or machine-readable profile instance only",
        "",
        "## 1. Interpretation",
        "",
        "The key words **MUST**, **MUST NOT**, **SHOULD**, and **MAY** in this Working Draft express candidate normative intent.",
        "",
        "They do not establish a published standard, certification program, industry adoption, or product approval.",
        "",
        "A conditional clause applies only when its declared trigger is present. Missing evidence is preserved as unknown, disputed, or not evidenced rather than converted into a score.",
        "",
        "## 2. Conformance Boundary",
        "",
        "Candidate conformance concerns the evidence profile. It does not certify the underlying sport, product, system quality, safety, clinical efficacy, federation recognition, category membership, or market rank.",
        "",
        "## 3. Profile Clauses",
        "",
    ]

    field_map = {
        "asr_id": "ASR-001",
        "working_draft_version": "0.1",
        "status": "candidate_non_public",
        "mapping_count": len(clauses),
        "mappings": []
    }

    for domain in sorted(grouped):
        items = sorted(grouped[domain], key=lambda item: item["clause_id"])
        lines += [f"### {domain} — {items[0]['domain_name']}", ""]
        for item in items:
            lines += [
                f"#### {item['clause_id']} — {item['title']}",
                "",
                f"**Candidate clause:** {item['normative_text']}",
                "",
                f"**Applicability:** `{item['applicability_class']}`",
                "",
                f"**Condition:** {item['applicability_condition']}",
                "",
                f"**Profile field:** `{item['profile_field_path']}`",
                "",
                f"**Verification:** {item['verification_statement']}",
                "",
                f"**Rationale:** {item['rationale']}",
                "",
                f"**Uncertainty:** {item['uncertainty_handling']}",
                "",
                f"**Evidence anchors:** {', '.join(item['evidence_case_refs']) or 'Governance dependency only'}",
                "",
                f"**Exclusion guards:** {', '.join(item['exclusions_guarded'])}",
                "",
            ]
            field_map["mappings"].append({
                "clause_id": item["clause_id"],
                "domain_id": item["domain_id"],
                "profile_field_path": item["profile_field_path"],
                "trigger_key": item["trigger_key"],
                "applicability_class": item["applicability_class"],
                "verification_modes": item["verification_modes"],
                "evidence_case_refs": item["evidence_case_refs"],
                "governance_dependencies": item["governance_dependencies"],
                "exclusions_guarded": item["exclusions_guarded"]
            })

    lines += [
        "## 4. Implementation Status",
        "",
        "The profile model and schema accompanying this Working Draft are candidate implementation artifacts for internal trial.",
        "",
        "They are not the historical Boundary Case Schema and do not alter any corpus record.",
        "",
        "## 5. Publication Status",
        "",
        "ASR-001 remains unpublished. Public Review, certification, external conformance claims, and industry-adoption claims remain unauthorized.",
        "",
    ]

    Path("ASR_001_WORKING_DRAFT_V0.1.md").write_text("\n".join(lines), encoding="utf-8")
    Path("ASR_001_CLAUSE_TO_FIELD_MAP_V0.1.json").write_text(
        json.dumps(field_map, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )
    print("PASS: wrote ASR_001_WORKING_DRAFT_V0.1.md")
    print("PASS: wrote ASR_001_CLAUSE_TO_FIELD_MAP_V0.1.json")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
