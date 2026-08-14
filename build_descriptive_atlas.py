#!/usr/bin/env python3
"""Build the AltisSports Descriptive Atlas v0.1.

Derives a descriptive-only reference layer 1:1 from the boundary-case corpus,
under ATLAS_DESCRIPTIVE_SCHEMA_V0.1.json and the governing principle:

    The Atlas must expose what the corpus knows, not manufacture what the
    corpus does not know.

Every descriptive value is copied from the source case. Nothing is inferred,
scored, averaged, or re-judged. Per-field claim_class and status are preserved
exactly. Output is a deterministic function of the corpus: no timestamps, no
git state, stable ordering. Standard library only.

Emits:
  ATLAS_DESCRIPTIVE_V0.1.json  — machine-readable records
  ATLAS_DESCRIPTIVE_V0.1.md    — human-readable index (same data)
  ATLAS_ID_LOCK_V0.1.json      — ATL-D-NNN -> BC-NNN binding lock
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CORPUS = "boundary-cases-001-020.v0.3.json"
OUT_JSON = "ATLAS_DESCRIPTIVE_V0.1.json"
OUT_MD = "ATLAS_DESCRIPTIVE_V0.1.md"
OUT_LOCK = "ATLAS_ID_LOCK_V0.1.json"


def pick(d, keys):
    """Copy only the named keys that are present in the source dict."""
    if not isinstance(d, dict):
        return {}
    return {k: d[k] for k in keys if k in d}


def atlas_id(case_id):
    # BC-001 -> ATL-D-001
    return "ATL-D-" + case_id.split("-", 1)[1]


def build_dimensions(c):
    dims = {}
    dims["performance_agency"] = pick(c["performance_agency"], [
        "status", "claim_class", "summary", "agency_modes", "human_skill_causally_necessary"])
    dims["performance_interface"] = pick(c["performance_interface"], [
        "status", "claim_class", "summary", "interface_types"])
    dims["embodied_performance"] = pick(c["embodied_performance"], [
        "status", "claim_class", "summary", "demand_types"])
    dims["arena"] = pick(c["arena"], ["status", "claim_class", "summary"])
    dims["distributed_arena_relation"] = pick(c["distributed_arena_relation"], [
        "status", "topology", "shared_computational_state", "synchronization_mechanism",
        "calibration_equivalence", "officiation_relation", "safety_relation"])
    dims["sensing_tracking"] = pick(c["tracking"], ["status", "claim_class", "summary"])
    dims["measurement"] = pick(c["measurement"], ["status", "claim_class", "summary"])
    dims["comparability"] = pick(c["comparability"], ["status", "claim_class", "summary"])
    dims["officiation"] = pick(c["officiation"], ["status", "claim_class", "summary"])
    dims["outcome_openness"] = pick(c["outcome_openness"], ["status", "claim_class", "summary"])
    dims["consequence_structure"] = pick(c["consequence_structure"], ["status", "claim_class", "summary"])

    osi = c["operational_spatial_integration_profile"]
    dims["operational_spatial_integration"] = {
        **pick(osi, ["overall_status", "profile_status", "immersion_present", "claim_class", "summary"]),
        "functions": [pick(f, ["role", "status", "significance"]) for f in osi.get("functions", [])],
    }
    # participatory actors: preserve the source list verbatim
    dims["participatory_actor_relations"] = c.get("participatory_actor_relations", [])
    # human limits / accessibility: the source L9 note
    dims["human_limits_accessibility"] = {
        "source_field": "as3_layer_notes.L9_safety_accessibility",
        "note": c["as3_layer_notes"].get("L9_safety_accessibility"),
    }
    # optional dimension, only when the source records substantive content
    # (the key exists in all cases but is null except where it applies)
    if isinstance(c.get("intentional_biological_control"), dict):
        dims["intentional_biological_control"] = pick(c["intentional_biological_control"], [
            "status", "summary", "signal_origin", "intentional_generation", "task_coupling",
            "decoder_mediation", "human_skill_causally_necessary", "athletic_embodiment_relation"])
    return dims


def build_record(c, dataset_version):
    cid = c["case_id"]
    return {
        "atlas_record_id": atlas_id(cid),
        "source_case_id": cid,
        "citation_id": cid,
        "source_dataset": CORPUS,
        "source_version": dataset_version,
        "license": "CC-BY-4.0",
        "license_ref": "DATASET_LICENSE.md",
        "temporal_status": "provisional",
        "activity": c["activity"],
        "activity_aliases": c.get("activity_aliases", []),
        "classified_object": pick(c["classified_object"], ["primary", "secondary", "notes"]),
        "dimensions": build_dimensions(c),
        "source_provisional_finding": pick(c["provisional_finding"], [
            "sport_contest_axis", "category_relation", "claim_class", "summary"]),
        "confidence": c.get("confidence"),
        "falsifiability": {
            "source_field": "what_would_change_judgment",
            "content": c.get("what_would_change_judgment", []),
        },
        "evidence_sources": [
            pick(e, ["source_title", "publisher", "url", "source_type", "claim_class",
                     "temporal_status", "publication_or_update_date"])
            for e in c.get("evidence", [])
        ],
        "provenance_note": (
            "Per-field claim_class and status preserved verbatim from the source case. "
            "source_provisional_finding is the corpus's own attributed reading, not a new "
            "Atlas verdict. Provider claims live in evidence_sources; Altis interpretation "
            "carries C4/C5."
        ),
    }


def render_md(records):
    lines = []
    lines.append("# AltisSports Descriptive Atlas v0.1")
    lines.append("")
    lines.append("**Status:** Foundation Draft — Not Ratified  ")
    lines.append("**Generated from:** `build_descriptive_atlas.py` over "
                 f"`{CORPUS}` — do not hand-edit.  ")
    lines.append("**Nature:** Descriptive reference layer only. Not ranking, scoring, "
                 "conformance, certification, or a sport/not-sport verdict.  ")
    lines.append("")
    lines.append("> The Atlas exposes what the corpus knows, not what it does not know. "
                 "Each row's descriptive values are copied from the source boundary case, "
                 "with per-field claim class and status preserved.")
    lines.append("")
    status_dims = [
        ("agency", "performance_agency"), ("interface", "performance_interface"),
        ("embodied", "embodied_performance"), ("arena", "arena"),
        ("sensing", "sensing_tracking"), ("measure", "measurement"),
        ("comparability", "comparability"), ("officiation", "officiation"),
        ("outcome", "outcome_openness"), ("consequence", "consequence_structure"),
    ]
    for r in records:
        d = r["dimensions"]
        lines.append(f"## {r['atlas_record_id']} — {r['activity']}")
        lines.append("")
        lines.append(f"- **Source case:** `{r['source_case_id']}` "
                     f"(dataset `{r['source_dataset']}` v{r['source_version']})")
        lines.append(f"- **Citation id:** `{r['citation_id']}` · "
                     f"**License:** {r['license']} · **Temporal status:** {r['temporal_status']}")
        obj = r["classified_object"]
        lines.append(f"- **Classified object:** {obj.get('primary','?')}"
                     + (f" / {obj['secondary']}" if obj.get("secondary") else ""))
        osi = d["operational_spatial_integration"]
        roles = ", ".join(f"{f['role']}={f.get('status','?')}" for f in osi.get("functions", [])) or "none observed"
        lines.append(f"- **Spatial integration:** overall={osi.get('overall_status','?')}; "
                     f"immersion_present={osi.get('immersion_present','?')}; functions: {roles}")
        dar = d["distributed_arena_relation"]
        lines.append(f"- **Arena relation:** arena={d['arena'].get('status','?')}; "
                     f"distributed={dar.get('status','?')}"
                     + (f"; topology={dar['topology']}" if dar.get("topology") else ""))
        status_line = "; ".join(f"{label}={d[key].get('status','?')}" for label, key in status_dims)
        lines.append(f"- **Dimension status:** {status_line}")
        pf = r["source_provisional_finding"]
        lines.append(f"- **Source provisional finding ({pf.get('claim_class','?')}):** "
                     f"sport_contest_axis={pf.get('sport_contest_axis','?')}, "
                     f"category_relation={pf.get('category_relation','?')} "
                     f"— confidence={r['confidence']}")
        acc = d["human_limits_accessibility"].get("note")
        if acc:
            lines.append(f"- **Human limits / accessibility:** {acc}")
        srcs = r["evidence_sources"]
        if srcs:
            lines.append(f"- **Evidence sources ({len(srcs)}):** "
                         + "; ".join(f"{s.get('publisher') or s.get('source_title','?')} "
                                     f"[{s.get('claim_class','?')}/{s.get('temporal_status','?')}]"
                                     for s in srcs))
        fc = r["falsifiability"]["content"]
        if fc:
            lines.append(f"- **What would change the judgment:** {fc[0]}")
        lines.append("")
    return "\n".join(lines) + "\n"


def main():
    data = json.loads((ROOT / CORPUS).read_text(encoding="utf-8"))
    dataset_version = data.get("schema_version")
    cases = sorted(data["cases"], key=lambda c: c["case_id"])
    records = [build_record(c, dataset_version) for c in cases]

    atlas = {
        "atlas": "AltisSports Descriptive Atlas",
        "version": "0.1",
        "status": "Foundation Draft — Not Ratified",
        "schema": "ATLAS_DESCRIPTIVE_SCHEMA_V0.1.json",
        "source_dataset": CORPUS,
        "source_version": dataset_version,
        "license": "CC-BY-4.0",
        "license_ref": "DATASET_LICENSE.md",
        "nature": "descriptive_reference_layer_only",
        "not": ["ranking", "scoring", "recommendation", "conformance", "certification",
                "new_sport_not_sport_verdict"],
        "record_count": len(records),
        "records": records,
    }
    lock = {
        "lock": "AltisSports Descriptive Atlas Identifier Lock",
        "version": "0.1",
        "status": "Foundation Draft — Not Ratified",
        "purpose": "Bind each Atlas record id to exactly one source boundary case; prevent silent repointing.",
        "binding_count": len(records),
        "bindings": [
            {"atlas_record_id": r["atlas_record_id"], "source_case_id": r["source_case_id"]}
            for r in records
        ],
        "tombstones": [],
    }

    (ROOT / OUT_JSON).write_text(json.dumps(atlas, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / OUT_LOCK).write_text(json.dumps(lock, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / OUT_MD).write_text(render_md(records), encoding="utf-8")
    print(f"WROTE {OUT_JSON} ({len(records)} records)")
    print(f"WROTE {OUT_LOCK} ({len(records)} bindings)")
    print(f"WROTE {OUT_MD}")


if __name__ == "__main__":
    main()
