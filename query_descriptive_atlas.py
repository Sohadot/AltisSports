#!/usr/bin/env python3
"""Deterministic reference query surface over the Descriptive Atlas (v0.1).

Retrieves, resolves, and filters what ATLAS_DESCRIPTIVE_V0.1.json already
states, under ATLAS_QUERY_CONTRACT_V0.1.json. It never infers, scores, ranks,
or introduces a field the Atlas does not contain.

Examples:
  python3 query_descriptive_atlas.py --atlas-id ATL-D-018
  python3 query_descriptive_atlas.py --case-id BC-018
  python3 query_descriptive_atlas.py --activity "Chess"
  python3 query_descriptive_atlas.py --activity-contains "formula"
  python3 query_descriptive_atlas.py --dimension measurement --status supported
  python3 query_descriptive_atlas.py --sport-contest-axis sport

Exit codes:
  0  valid query (including zero matches: result_count 0 is not an error)
  2  invalid query (unknown field or value outside the contract vocabulary)
  3  broken source/reference (missing or unreadable Atlas / contract)

Output is deterministic JSON on stdout, ordered by atlas_record_id. Standard
library only.
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ATLAS = "ATLAS_DESCRIPTIVE_V0.1.json"
CONTRACT = "ATLAS_QUERY_CONTRACT_V0.1.json"
REGISTRY = "CITATION_REGISTRY_V0.1.json"

EXIT_OK, EXIT_INVALID, EXIT_BROKEN = 0, 2, 3


class Invalid(Exception):
    pass


class Broken(Exception):
    pass


def load(name, exc):
    try:
        return json.loads((ROOT / name).read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        raise exc(f"cannot read {name}: {e}")


def emit(obj, code):
    print(json.dumps(obj, ensure_ascii=False, indent=2))
    sys.exit(code)


def citability(bc_id, registry_index):
    entry = registry_index.get(bc_id)
    return {
        "atlas_record_citability": "not_independently_registered",
        "source_citation_id": bc_id,
        "source_citation_registered": entry is not None,
        "source_citation_externally_citable": bool(entry and entry.get("externally_citable")),
    }


def as_result(r, registry_index):
    return {
        "atlas_record_id": r["atlas_record_id"],
        "source_case_id": r["source_case_id"],
        "activity": r["activity"],
        "temporal_status": r["temporal_status"],
        "license": r["license"],
        "citability": citability(r["source_case_id"], registry_index),
        "record": r,
    }


def build_parser():
    p = argparse.ArgumentParser(add_help=True)
    p.add_argument("--atlas-id")
    p.add_argument("--case-id")
    p.add_argument("--activity")
    p.add_argument("--activity-contains")
    p.add_argument("--dimension")
    p.add_argument("--status")
    p.add_argument("--claim-class")
    p.add_argument("--has-dimension")
    p.add_argument("--sport-contest-axis")
    p.add_argument("--category-relation")
    p.add_argument("--confidence")
    return p


def check_vocab(name, value, allowed):
    if value is not None and value not in allowed:
        raise Invalid(f"{name}={value!r} is not in the allowed vocabulary: {allowed}")


def apply_query(args, atlas, contract, registry_index):
    records = sorted(atlas["records"], key=lambda r: r["atlas_record_id"])
    filters = contract["filters"]
    matched = records

    # selectors (exact resolve or activity match)
    if args.atlas_id is not None:
        matched = [r for r in matched if r["atlas_record_id"] == args.atlas_id]
    if args.case_id is not None:
        matched = [r for r in matched if r["source_case_id"] == args.case_id]
    if args.activity is not None:
        matched = [r for r in matched if r["activity"] == args.activity]
    if args.activity_contains is not None:
        needle = args.activity_contains.lower()
        matched = [r for r in matched if needle in r["activity"].lower()]

    # dimension status / claim-class filter
    if args.dimension is not None or args.status is not None or args.claim_class is not None:
        dim = args.dimension
        if dim not in filters["dimension_status"]["dimensions"]:
            raise Invalid(f"--dimension must be one of {filters['dimension_status']['dimensions']}")
        check_vocab("--status", args.status, filters["dimension_status"]["allowed_status_values"])
        check_vocab("--claim-class", args.claim_class, filters["dimension_claim_class"]["allowed_claim_classes"])

        def keep(r):
            d = r["dimensions"].get(dim)
            if not isinstance(d, dict):
                return False
            if args.status is not None and d.get("status") != args.status:
                return False
            if args.claim_class is not None and d.get("claim_class") != args.claim_class:
                return False
            return True
        matched = [r for r in matched if keep(r)]

    if args.has_dimension is not None:
        check_vocab("--has-dimension", args.has_dimension, filters["has_dimension"]["allowed"])
        matched = [r for r in matched if args.has_dimension in r["dimensions"]]

    if args.sport_contest_axis is not None:
        check_vocab("--sport-contest-axis", args.sport_contest_axis, filters["sport_contest_axis"]["allowed"])
        matched = [r for r in matched
                   if r["source_provisional_finding"].get("sport_contest_axis") == args.sport_contest_axis]

    if args.category_relation is not None:
        check_vocab("--category-relation", args.category_relation, filters["category_relation"]["allowed"])
        matched = [r for r in matched
                   if r["source_provisional_finding"].get("category_relation") == args.category_relation]

    if args.confidence is not None:
        check_vocab("--confidence", args.confidence, filters["confidence"]["allowed"])
        matched = [r for r in matched if r.get("confidence") == args.confidence]

    return matched


def main():
    parser = build_parser()
    args, unknown = parser.parse_known_args()
    try:
        if unknown:
            raise Invalid(f"unknown/arbitrary query arguments are not allowed: {unknown}")
        atlas = load(ATLAS, Broken)
        contract = load(CONTRACT, Broken)
        registry = load(REGISTRY, Broken)
        registry_index = {e["citation_id"]: e for e in registry["identifiers"]}
        if contract.get("source_atlas_version") != atlas.get("version"):
            raise Broken("query contract version does not match the Atlas version")

        matched = apply_query(args, atlas, contract, registry_index)
        query_echo = {k: v for k, v in vars(args).items() if v is not None}
        out = {
            "contract_version": contract["version"],
            "atlas_version": atlas["version"],
            "query": query_echo,
            "result_count": len(matched),
            "results": [as_result(r, registry_index) for r in matched],
        }
        emit(out, EXIT_OK)
    except Invalid as e:
        emit({"error": "invalid_query", "detail": str(e)}, EXIT_INVALID)
    except Broken as e:
        emit({"error": "broken_source", "detail": str(e)}, EXIT_BROKEN)


if __name__ == "__main__":
    main()
