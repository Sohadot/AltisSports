# Schema Migration: Boundary Case v0.1 → v0.2

**Asset:** AltisSports  
**Migration version:** 1.0.0  
**Status:** Governed Structural Migration  
**Source:** `BOUNDARY_CASE_SCHEMA.json`  
**Target:** `BOUNDARY_CASE_SCHEMA_V0.2.json`

## 1. Purpose

This migration carries the BC-001–BC-010 dataset into the theory corrected by Sprint 3 without rewriting or deleting the original Sprint 2 record.

The v0.1 schema and dataset remain historical evidence of the method actually used. The v0.2 output is a separate derivative dataset.

## 2. Binding Rules

1. `BOUNDARY_CASE_SCHEMA.json` must remain unchanged.
2. `boundary-cases-001-010.json` must remain unchanged.
3. Migrated output must use `boundary-cases-001-010.v0.2.json`.
4. Every automated semantic inference must remain marked `automated_review_required`.
5. Structural validation does not equal human confirmation of a category judgment.
6. No migration field may introduce a total score, maturity level, spatiality level, certification, or conformance claim.
7. Failed migration or validation blocks commit.

## 3. Field Mapping

| v0.1 | v0.2 | Rule |
| --- | --- | --- |
| `human_agency` | `performance_agency` | Preserve source summary/status; add agency modes, performance window, and causal-necessity field |
| `embodied_interface` | `performance_interface` | Preserve source content; add provisional interface typology |
| `embodied_interface` | `embodied_performance` | Derive a separate descriptive demand record; mark migration review required |
| `consequence` | `consequence_structure` | Preserve as a derived property, not a candidate invariant |
| `spatial_integration` | `operational_spatial_integration_profile` | Convert old roles into qualitative function records |
| `L1_human_agency` | `L1_performance_agency` | Terminology correction |
| `L2_embodied_interface` | `L2_performance_interface_embodied_demand` | Split interface from embodiment in meaning while retaining one AS³ note field |
| `candidate_invariants.human_agency` | `candidate_invariants.performance_agency` | Preserve assessment; require review |
| `candidate_invariants.consequence` | removed | Consequence is represented separately |
| `provisional_finding.sport_axis` | `sport_contest_axis` | Rename |
| `provisional_finding.spatial_sport_axis` | `category_relation` | Map to revised sibling/core relations |
| `revision.version` | `0.2` | Identify derived record |
| — | `migration` | Record source version, script version, and review status |

## 4. Agency Mapping

The migration script uses explicit mappings only where Sprint 2 already exposed a stable distinction:

- BC-005 → `remote_performance`
- BC-010 → `design_engineering` + `autonomous_execution`
- other BC-001–BC-010 records → `live_performance` as a provisional migration default

These are not native v0.2 judgments. Human review must confirm the performance window, agency mode, and causal necessity for each record.

## 5. Interface and Embodied-Demand Mapping

Interface and demand types are case-specific migration annotations derived from the existing case narratives. They are marked provisional and may be corrected without changing the v0.1 source.

Adaptive equipment, vehicle control, remote control, tracked XR input, conventional equipment, and autonomous agents remain distinct. Mediation is not treated as Spatiality.

## 6. Operational Spatial Integration Migration

v0.1 roles map as follows:

| v0.1 role | v0.2 function |
| --- | --- |
| `represent_only` | `represent` |
| `enable_performance` | `enable` |
| `constrain_performance` | `constrain` |
| `measure_performance` | `measure` |
| `compare_performance` | `compare` |
| `officiate_performance` | `officiate` |
| `none_observed` | no function record |
| `unknown` | no inferred function record |

Each migrated function must include:

- status;
- qualitative significance;
- mechanism;
- affected AS³ layers;
- failure effect;
- evidence references;
- uncertainty;
- review status.

The migration cannot infer reliable evidence indices or failure effects from v0.1 alone. Those fields therefore remain explicitly review-required.

## 7. Category-Relation Mapping

| v0.1 `spatial_sport_axis` | v0.2 `category_relation` |
| --- | --- |
| `spatial_athletic_system` | `spatial_athletic_system` |
| `partial_spatial_integration` | `partial_spatial_integration` |
| `computational_arena_without_athletic_embodiment_claim` | `computational_contest` |
| `not_spatial_sport` | `outside_core_spatial_athletic_class` |
| `unresolved` | `unresolved` |

This mapping does not convert an activity into a different primary classified object. Object-lock review remains separate.

## 8. Execution

From the repository root:

```bash
python run_sprint4.py
```

The runner:

1. validates each original case against schema v0.1;
2. hashes the original schema and dataset;
3. creates the v0.2 derivative;
4. validates the derivative against schema v0.2;
5. checks cross-record integrity and prohibited scoring keys;
6. verifies that the original files did not change;
7. writes validation and gate results only after PASS.

## 9. Human Review After Migration

A later research pass must review, case by case:

- primary classified object;
- performance window;
- agency modes;
- embodied-demand types;
- spatial-function significance;
- failure effects;
- direct evidence links for each spatial function;
- category relation.

Until then, the migrated dataset is structurally valid but semantically provisional.
