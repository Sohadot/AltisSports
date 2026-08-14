#!/usr/bin/env python3
"""Build the Atlas Query / Reference Surface distribution (v0.1).

Generates, deterministically from ATLAS_DESCRIPTIVE_V0.1.json, a stable access
layer that lets a human, script, or agent retrieve Atlas data without parsing
the whole file or inventing query semantics:

  ATLAS_QUERY_CONTRACT_V0.1.json   authored semantics + data-derived vocab
  atlas/manifest.json              distribution manifest with per-file sha256
  atlas/records/ATL-D-NNN.json     one self-contained record per case
  atlas/by-atlas-id.json           resolver: atlas id  -> record path
  atlas/by-case.json               resolver: source BC -> record path

Governing principle: the surface may retrieve, filter, resolve, and expose
what the Atlas already states. It must not infer what the Atlas does not state.
No new field, taxonomy, score, or ordering is introduced. The allowed filter
vocabulary is read from the live Atlas, so it can never drift. Output is a pure
function of the Atlas: no timestamps, no git state. Standard library only.
"""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ATLAS = "ATLAS_DESCRIPTIVE_V0.1.json"
REGISTRY = "CITATION_REGISTRY_V0.1.json"
LOCK = "ATLAS_ID_LOCK_V0.1.json"
CONTRACT_OUT = "ATLAS_QUERY_CONTRACT_V0.1.json"
DIST = ROOT / "atlas"

DENY = ["score", "ranking", "rank", "rating", "grade", "maturity",
        "readiness", "certif", "tier", "percentile", "points", "superior", "best_"]

# Dimensions that carry a top-level status (filterable by status/claim_class).
STATUS_DIMENSIONS = [
    "performance_agency", "performance_interface", "embodied_performance",
    "arena", "distributed_arena_relation", "sensing_tracking", "measurement",
    "comparability", "officiation", "outcome_openness", "consequence_structure",
]
OPTIONAL_DIMENSIONS = ["intentional_biological_control"]


def read_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def dumps(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2) + "\n"


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def derive_vocab(records):
    """Enumerate the actual controlled values present, sorted for determinism."""
    status_vals, claim_vals = set(), set()
    axis_vals, cat_vals, conf_vals = set(), set(), set()
    optional_present = set()
    for r in records:
        dims = r["dimensions"]
        for dn in STATUS_DIMENSIONS:
            d = dims.get(dn)
            if isinstance(d, dict):
                if d.get("status") is not None:
                    status_vals.add(d["status"])
                if d.get("claim_class") is not None:
                    claim_vals.add(d["claim_class"])
        for dn in OPTIONAL_DIMENSIONS:
            if dn in dims:
                optional_present.add(dn)
        spf = r.get("source_provisional_finding", {})
        if spf.get("sport_contest_axis") is not None:
            axis_vals.add(spf["sport_contest_axis"])
        if spf.get("category_relation") is not None:
            cat_vals.add(spf["category_relation"])
        if r.get("confidence") is not None:
            conf_vals.add(r["confidence"])
    return {
        "dimension_status": sorted(status_vals),
        "dimension_claim_class": sorted(claim_vals),
        "source_provisional_finding.sport_contest_axis": sorted(axis_vals),
        "source_provisional_finding.category_relation": sorted(cat_vals),
        "confidence": sorted(conf_vals),
        "optional_dimensions": sorted(optional_present),
        "status_bearing_dimensions": list(STATUS_DIMENSIONS),
    }


def build_contract(atlas, records, vocab):
    return {
        "contract": "AltisSports Atlas Query / Reference Surface Contract",
        "version": "0.1",
        "status": "Foundation Draft — Not Ratified",
        "source_atlas": ATLAS,
        "source_atlas_version": atlas["version"],
        "governing_principle": (
            "The surface may retrieve, filter, resolve, and expose what the Atlas "
            "already states. It must not infer what the Atlas does not state."
        ),
        "selectors": {
            "atlas_record_id": "Exact resolve of one record by its ATL-D-NNN id.",
            "source_case_id": "Exact resolve of one record by its source BC-NNN id.",
            "activity": "Exact, case-sensitive match on the activity string.",
            "activity_contains": "Case-insensitive substring match on the activity string.",
        },
        "filters": {
            "note": "Filters combine with logical AND. Every filter retrieves an existing Atlas value; none computes a score, similarity, or ranking.",
            "dimension_status": {
                "form": "--dimension <name> --status <value>",
                "dimensions": vocab["status_bearing_dimensions"],
                "allowed_status_values": vocab["dimension_status"],
            },
            "dimension_claim_class": {
                "form": "--dimension <name> --claim-class <Cn>",
                "allowed_claim_classes": vocab["dimension_claim_class"],
            },
            "has_dimension": {
                "form": "--has-dimension <name>",
                "allowed": vocab["optional_dimensions"],
                "meaning": "Records where the named optional dimension is present.",
            },
            "sport_contest_axis": {
                "form": "--sport-contest-axis <value>",
                "allowed": vocab["source_provisional_finding.sport_contest_axis"],
                "meaning": "Retrieves the source corpus's recorded axis; not an Atlas verdict.",
            },
            "category_relation": {
                "form": "--category-relation <value>",
                "allowed": vocab["source_provisional_finding.category_relation"],
                "meaning": "Retrieves the source corpus's recorded relation; not an Atlas verdict.",
            },
            "confidence": {
                "form": "--confidence <value>",
                "allowed": vocab["confidence"],
            },
        },
        "sorting": "Results are always ordered by atlas_record_id ascending. There is no relevance ranking.",
        "empty_result_semantics": "A valid query with no matches returns exit code 0 and result_count 0. Empty is not an error.",
        "error_semantics": {
            "invalid_query": "An unknown selector/filter/field or a value outside the allowed vocabulary returns a non-zero exit and an error object. Nothing is guessed.",
            "broken_source": "A missing or unreadable source/reference returns a distinct non-zero exit, never a silent empty result.",
        },
        "output_schema": {
            "top_level": ["contract_version", "atlas_version", "query", "result_count", "results"],
            "result": ["atlas_record_id", "source_case_id", "activity", "temporal_status",
                       "license", "citability", "record"],
            "record": "The full descriptive Atlas record, verbatim, with per-field claim_class and status preserved.",
        },
        "provenance_requirements": "Every result carries atlas_record_id, source_case_id, per-field claim_class as recorded, temporal_status, and the source citation reference. Summaries are never returned without provenance.",
        "citability_semantics": {
            "rule": "ATL-D-* ids are NOT registered as externally citable identifiers in CITATION_REGISTRY_V0.1.json. The surface must not imply independent Atlas citation authority.",
            "atlas_record_citability": "not_independently_registered",
            "source_citation": "Each result exposes source_citation_id (the BC id) and whether that source id is registered and externally citable.",
        },
        "prohibited": {
            "no_arbitrary_query": "Arbitrary JSONPath or code expressions are not permitted; only the allowlisted selectors and filters above.",
            "no_evaluative_fields": "No score/rank/rating/grade/maturity/readiness/certification field may appear in a query or output.",
            "denylisted_key_substrings": DENY,
        },
    }


def citability_block(bc_id, registry_index):
    entry = registry_index.get(bc_id)
    return {
        "atlas_record_citability": "not_independently_registered",
        "source_citation_id": bc_id,
        "source_citation_registered": entry is not None,
        "source_citation_externally_citable": bool(entry and entry.get("externally_citable")),
    }


def build_distribution(atlas, records, registry_index):
    if DIST.exists():
        for p in sorted(DIST.rglob("*")):
            if p.is_file():
                p.unlink()
    (DIST / "records").mkdir(parents=True, exist_ok=True)

    manifest_records = []
    by_atlas, by_case = {}, {}
    for r in records:
        aid = r["atlas_record_id"]
        bc = r["source_case_id"]
        rel = f"records/{aid}.json"
        record_file = {
            "atlas_record_id": aid,
            "source_case_id": bc,
            "distribution_version": "0.1",
            "atlas_source_version": atlas["version"],
            "query_contract_version": "0.1",
            "license": r["license"],
            "citability": citability_block(bc, registry_index),
            "record": r,
        }
        payload = dumps(record_file).encode("utf-8")
        (DIST / rel).write_bytes(payload)
        manifest_records.append({
            "atlas_record_id": aid,
            "source_case_id": bc,
            "path": rel,
            "sha256": sha256_bytes(payload),
        })
        by_atlas[aid] = rel
        by_case[bc] = rel

    by_atlas_bytes = dumps(by_atlas).encode("utf-8")
    by_case_bytes = dumps(by_case).encode("utf-8")
    (DIST / "by-atlas-id.json").write_bytes(by_atlas_bytes)
    (DIST / "by-case.json").write_bytes(by_case_bytes)

    manifest = {
        "manifest": "AltisSports Atlas Reference Distribution",
        "distribution_version": "0.1",
        "status": "Foundation Draft — Not Ratified",
        "atlas_source": ATLAS,
        "atlas_source_version": atlas["version"],
        "query_contract": CONTRACT_OUT,
        "query_contract_version": "0.1",
        "schema_reference": atlas["schema"],
        "license": atlas["license"],
        "license_ref": atlas["license_ref"],
        "ordering": "records ordered by atlas_record_id ascending",
        "record_count": len(records),
        "records": manifest_records,
        "indexes": {
            "by-atlas-id.json": sha256_bytes(by_atlas_bytes),
            "by-case.json": sha256_bytes(by_case_bytes),
        },
    }
    (DIST / "manifest.json").write_bytes(dumps(manifest).encode("utf-8"))
    return len(records)


def main():
    atlas = read_json(ATLAS)
    records = sorted(atlas["records"], key=lambda r: r["atlas_record_id"])
    registry = read_json(REGISTRY)
    registry_index = {e["citation_id"]: e for e in registry["identifiers"]}
    vocab = derive_vocab(records)

    contract = build_contract(atlas, records, vocab)
    (ROOT / CONTRACT_OUT).write_text(dumps(contract), encoding="utf-8")
    n = build_distribution(atlas, records, registry_index)
    print(f"WROTE {CONTRACT_OUT}")
    print(f"WROTE atlas/ distribution ({n} records + 2 indexes + manifest)")


if __name__ == "__main__":
    main()
