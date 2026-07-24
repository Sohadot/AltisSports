#!/usr/bin/env python3
"""Generate ASR-001 Working Draft v0.2 and clause-to-field map."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

CATALOG = Path("ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.2.json")

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
        "**Version:** 0.2  ",
        "**Status:** Candidate Normative Core — internal-trial refined and unpublished  ",
        "**Conformance subject:** Evidence-profile document or machine-readable profile instance only",
        "",
        "## 1. Interpretation",
        "",
        "The key words **MUST**, **MUST NOT**, **SHOULD**, and **MAY** express candidate normative intent inside this non-public Working Draft.",
        "",
        "Applicability and evidence sufficiency are separate. A clause can be applicable while its evidence state is `not_evidenced`, `unknown`, or `partial`.",
        "",
        "No clause establishes product approval, category certification, safety or clinical certification, federation recognition, ranking, or industry adoption.",
        "",
        "## 2. Conformance Boundary",
        "",
        "Candidate conformance concerns the evidence profile only. It does not certify the underlying activity, contest, product, platform, organization, safety, clinical efficacy, athletic legitimacy, or market quality.",
        "",
        "## 3. Candidate Profile Clauses",
        "",
    ]

    field_map = {
        "asr_id": "ASR-001",
        "working_draft_version": "0.2",
        "status": "candidate_non_public_internal_trial_refined",
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
                f"**Evidence requirement:** `{item['evidence_requirement']}`",
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
                f"**v0.2 change status:** `{item['change_status']}` — {item['change_reason']}",
                "",
            ]
            field_map["mappings"].append({
                "clause_id": item["clause_id"],
                "domain_id": item["domain_id"],
                "profile_field_path": item["profile_field_path"],
                "trigger_key": item["trigger_key"],
                "applicability_class": item["applicability_class"],
                "evidence_requirement": item["evidence_requirement"],
                "verification_modes": item["verification_modes"],
                "evidence_case_refs": item["evidence_case_refs"],
                "governance_dependencies": item["governance_dependencies"],
                "exclusions_guarded": item["exclusions_guarded"],
                "change_status": item["change_status"]
            })

    lines += [
        "## 4. Implementation Status",
        "",
        "The accompanying profile model v0.2 is clause-derived and separates applicability from evidence state.",
        "",
        "The Boundary Case Schema and all historical corpus files remain independent and unchanged.",
        "",
        "## 5. Publication Status",
        "",
        "ASR-001 remains unpublished. Operator-review package preparation may be considered only after the Sprint 11 gate.",
        "",
        "External review, Public Review, certification, and public conformance claims remain unauthorized.",
        "",
    ]

    Path("ASR_001_WORKING_DRAFT_V0.2.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )
    Path("ASR_001_CLAUSE_TO_FIELD_MAP_V0.2.json").write_text(
        json.dumps(field_map, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )
    print("PASS: wrote ASR_001_WORKING_DRAFT_V0.2.md")
    print("PASS: wrote ASR_001_CLAUSE_TO_FIELD_MAP_V0.2.json")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
