#!/usr/bin/env python3
"""Assemble the two reviewed v0.3 strata into one 20-case corpus."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain an object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", default="boundary-cases-001-010.reviewed.v0.3.json")
    parser.add_argument("--second", default="boundary-cases-011-020.reviewed.v0.3.json")
    parser.add_argument("--output", default="boundary-cases-001-020.v0.3.json")
    args = parser.parse_args()
    try:
        first, second = load(Path(args.first)), load(Path(args.second))
        cases = first["cases"] + second["cases"]
        result = {
            "dataset": "AltisSports Boundary Corpus BC-001-020 v0.3",
            "schema": "BOUNDARY_CASE_SCHEMA_V0.3.json",
            "schema_version": "0.3",
            "source_dataset": (
                "boundary-cases-001-010.reviewed.v0.3.json + "
                "boundary-cases-011-020.reviewed.v0.3.json"
            ),
            "source_schema_version": "0.3",
            "sprint": "Sprint 7 — v0.3 Corpus Application and Standardization-Readiness Gate",
            "status": "human_reviewed_research_corpus",
            "license": first.get("license") or second.get("license"),
            "access_date": max(str(first.get("access_date", "")), str(second.get("access_date", ""))),
            "case_count": len(cases),
            "cases": cases,
        }
        Path(args.output).write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print(f"ERROR: corpus assembly failed: {exc}")
        return 2
    print(f"PASS: wrote {args.output} with {len(cases)} cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
