# Schema Migration v0.2 → v0.3

**Source schema:** `BOUNDARY_CASE_SCHEMA_V0.2.json`  
**Target schema:** `BOUNDARY_CASE_SCHEMA_V0.3.json`  
**Source dataset:** `boundary-cases-011-020.v0.2.json`  
**Target dataset:** `boundary-cases-011-020.v0.3.json`  
**Migration script:** `migrate_boundary_cases_v0_2_to_v0_3.py`  
**Status:** Governed Additive Migration

## 1. Historical Rule

No v0.2 file is overwritten.

## 2. Structural Mapping

| v0.2 | v0.3 |
| --- | --- |
| `schema_version: 0.2` | `schema_version: 0.3` |
| summary agency modes | retained + `agency_segments` |
| arena and Spatial Functions | retained + `distributed_arena_relation` |
| participant/spectator notes | retained + `participatory_actor_relations` |
| physiological sensing labels | retained + optional `intentional_biological_control` |
| native v0.2 review state | explicit v0.3 carry-forward or human-reviewed state |

## 3. Targeted Semantic Patches

Only BC-015, BC-017, BC-018, BC-019, and BC-020 receive new human-authored semantic structures.

BC-011–BC-014 and BC-016 receive:

- empty `agency_segments`;
- an explicitly unassessed distributed-arena relation;
- empty participatory-actor relations;
- `intentional_biological_control: null`.

This prevents structural completeness from being mistaken for case-level analysis.

## 4. Evidence Appends

The v0.3 derivative appends current official or first-party technical evidence where targeted deepening required it.

Appended evidence does not modify the v0.2 record and remains subject to its declared limitations.

## 5. Review Status

- Targeted cases: `human_reviewed_v0_3`
- Non-target cases: `structural_migration_reviewed`
- Carried-forward Spatial Functions: `carried_forward_v0_3`

## 6. Prohibited Migration Behavior

The migration may not:

- infer remote integrity from co-location;
- invent observed control transitions from permitted modes;
- turn intentional brain activity into settled athletic embodiment;
- convert spectator influence into direct Performance Agency;
- add any score, level, certification, or conformance status.
