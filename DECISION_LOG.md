# AltisSports Decision Log

This log records foundational decisions that govern the asset. Decisions are append-only unless formally superseded by a later decision.

---

## DEC-001 — Category and Measurement Doctrine

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24

### Decision

1. **Spatial Sport** is the public, descriptive name of the field in which AltisSports operates.
2. AltisSports does not claim exclusive ownership of the descriptive category term.
3. Defensible intellectual authority will be built through ontology, standards, reference models, datasets, evidence structures, and operational methods.
4. The standards family will use the name **Altis Spatial Reference (ASR)** and sequential identifiers such as `ASR-001`.
5. The system architecture may use the name **Altis Spatial Sport Stack (AS³)**.
6. No scale, score, profile, level, or classification hierarchy may be fixed before the theoretical and empirical structure justifying it exists.
7. Measurement must be derived from theory and evidence; it must not be imposed for branding convenience.

### Rationale

A descriptive category term preserves discoverability and market legibility. Proprietary value is created through the governed language and infrastructure used to define and evaluate the category.

---

## DEC-002 — Invariance Research Doctrine

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24

### Decision

1. AltisSports will investigate which properties must remain invariant for an activity to remain classifiable as sport when its arena or medium changes.
2. Early invariants are treated as candidate hypotheses, not settled truths.
3. Candidate invariants must be tested against ordinary, disputed, and boundary cases.
4. No invariant becomes normative merely because it is conceptually elegant.
5. Contradictory cases must be documented rather than excluded to protect the theory.
6. The Boundary Cases Corpus is a mandatory precondition for formal standards.

### Rationale

The project must derive its theory through disciplined comparison rather than declare a closed doctrine before testing.

---

## DEC-003 — Authority–Revenue Separation

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24

### Decision

1. Foundational definitions, methods, high-level ontology, and public reference material should remain openly accessible.
2. Revenue may be generated from structured intelligence, expanded datasets, professional reports, assessments, licensed integrations, APIs, and institutional services.
3. Payment may not purchase favorable classification, suppress criticism, alter evidence thresholds, or bypass methodology.
4. Sponsored or paid participation must be visibly distinguished from independent editorial judgment.
5. Monetization must strengthen the reference layer rather than compromise it.

### Rationale

Public authority creates demand; structured intelligence captures value.

---

## DEC-004 — Interface Embodiment Doctrine

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24

### Decision

1. The interface must embody the asset thesis rather than decorate it.
2. The visual system must express the arena as a governed spatial system connecting body, rules, measurement, presence, and integrity.
3. No movement, three-dimensional scene, visual layer, or interaction is permitted without a defined explanatory function.
4. Accessibility, performance, semantic HTML, crawlability, mobile reliability, and progressive enhancement are non-negotiable.
5. The site must remain understandable and useful when scripts, animation, or advanced graphics are unavailable.
6. The interface must not resemble a generic gaming, casino, metaverse, or juvenile entertainment product.

### Rationale

Concept precedes performance; performance precedes beauty.

---

## DEC-005 — No Premature Standardization

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24

### Decision

AltisSports may publish research questions, candidate models, and provisional classifications during the foundation phase, but may not present them as settled standards until:

- the relevant terms are defined;
- boundary cases have been tested;
- evidence and claim rules are operational;
- the scope and exclusions are explicit;
- versioning and revision procedures exist.

### Rationale

Premature certainty would weaken trust and make later correction look like failure rather than disciplined refinement.

---

## DEC-006 — Evidence-Driven Theory Revision

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `INVARIANCE_FINDINGS_V0.1.md`, BC-001–BC-010

### Decision

1. **Performance Agency** replaces **Human Agency** as the candidate contest invariant. Human contribution outside the performance window is not sufficient by itself.
2. Live, remote, and assisted Performance Agency may preserve human performance; Design or Engineering Agency and Autonomous Execution must be distinguished from it.
3. Embodied Performance is not a universal condition for all sport. It remains a candidate-defining property of the provisional Spatial Athletic System class.
4. Consequence is demoted from an independent candidate invariant to a derived **Consequence Structure**, pending contrary evidence.
5. Operational Spatial Integration must be represented through a multi-dimensional evidence profile rather than a binary badge, total score, or maturity level.
6. A computational arena, visual immersion, telemetry, or mediation is not sufficient by itself to establish Spatial Athletic System membership.
7. The classified object must be locked before judgment. Activity, contest, system, product, experience, event, organization, and support system may not be silently collapsed.
8. Sprint 2 method and schema artifacts remain immutable historical records of the v0.1 test. They will not be rewritten retroactively to conceal terminology correction.
9. Any migration from `human_agency` to `performance_agency` in machine-readable records must occur through a new schema version with an explicit migration record.
10. `ASR-001` remains unauthorized until the revised theory is tested against additional antagonistic cases and the evidence infrastructure conditions are satisfied.

### Rationale

The first boundary stratum showed that design contribution can exist without live athletic performance, embodiment cannot define every recognized sport, consequence adds little independent discrimination, and operational space appears through multiple roles. A reference system gains authority by preserving the evidence trail of correction rather than rewriting its history.

---

## DEC-007 — Corpus Schema Evolution and Open Dataset Licensing

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24  
**Applies to:** Boundary-case schemas, datasets, migrations, and validation artifacts

### Decision

1. `BOUNDARY_CASE_SCHEMA.json` and `boundary-cases-001-010.json` remain immutable historical v0.1 artifacts.
2. Theory-driven schema change must use a new versioned schema and a separate derived dataset rather than overwrite the historical record.
3. Every schema migration must publish its field mapping, assumptions, review requirements, and executable migration path.
4. Automated migration may establish structural compatibility but may not present inferred semantic fields as human-reviewed findings.
5. The v0.2 corpus must remain profile-based and must not introduce total scores, maturity levels, spatiality levels, certification, or conformance claims.
6. Dataset validation must be deterministic, locally executable, and blocking: a failed migration or validation result may not be committed as a completed sprint.
7. Original AltisSports boundary-case data, schema descriptions, controlled vocabularies, and Altis-authored analytical text are released under **CC BY 4.0**, subject to the exclusions in `DATASET_LICENSE.md`.
8. Citations, external documents, trademarks, logos, and other third-party materials are not relicensed merely because they appear in or are linked from an AltisSports record.
9. BC-011–BC-020 must be authored natively against schema v0.2; migrated BC-001–BC-010 records must retain visible migration status.
10. `ASR-001` remains unauthorized after corpus infrastructure completion; a second evidence stratum and a separate standardization gate are still required.

### Rationale

A reference dataset must evolve without erasing the conditions under which earlier findings were produced. Versioned schemas, explicit migrations, deterministic validation, and clear reuse rights convert conceptual correction into durable public infrastructure while preserving attribution, uncertainty, and third-party boundaries.

---

## DEC-008 — Second-Stratum Refinement Hold

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** BC-011–BC-020 and `SECOND_STRATUM_FINDINGS_V0.2.md`

### Decision

1. BC-011–BC-020 are accepted as the first **native v0.2** research stratum, distinct from migrated BC-001–BC-010 records.
2. Embodied Performance remains a channel-based profile. No minimum quantity, level, or universal threshold is authorized.
3. Fine-motor, balance, sensorimotor, adaptive, cognitive, and intentional physiological channels may be material evidence; none establishes Spatial Athletic System membership by itself.
4. `Spatial Athletic System`, `Spatial Athletic Contest`, and `Spatial Support System` remain separate objects; system membership may exist without mature contest governance.
5. Summary-level agency modes are insufficient for cases with time-varying control. A phase-level `agency_segments` design must be evaluated before normative agency attribution.
6. The remote-distributed hypothesis in BC-015 remains unresolved. Global availability, product aspiration, or co-located championship evidence may not be presented as proof of remote arena integrity.
7. Spectators who alter resources or constraints without executing the performance are participatory rule/resource actors, not Performance Agents by default.
8. Consequence remains a derived property. The second stratum does not restore it as an independent invariant.
9. Operational Spatial Integration remains qualitative and profile-based. No total score, maturity level, or binary certification badge is authorized.
10. `ASR-001` remains unauthorized. The next move is targeted boundary deepening and a schema v0.3 decision, not standard issuance.

### Rationale

The second stratum validates the main v0.2 separations while exposing two unresolved structures: agency that changes by phase and arenas distributed across physical locations. Preserving these uncertainties increases reference integrity and prevents a premature standard from encoding a convenient but incomplete theory.
---

## DEC-009 — Targeted Representation and Schema v0.3

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `SECOND_STRATUM_FINDINGS_V0.2.md`, `TARGETED_BOUNDARY_DEEPENING.md`

### Decision

1. `BOUNDARY_CASE_SCHEMA_V0.3.json` is authorized because v0.2 cannot faithfully represent phase-varying agency, distributed-arena relations, participatory rule/resource actors, or intentional biological control.
2. Phase-varying or regime-varying control must use `agency_segments`. A rule-permitted manual, semi-autonomous, or autonomous regime may not be presented as an observed transition without evidence.
3. Distributed-arena claims must state topology, shared computational state, synchronization, latency governance, calibration equivalence, officiation, safety responsibility, evidence, and uncertainty.
4. BC-015 remains a co-located Spatial Athletic Contest in the examined evidence. Geographically distributed synchronous Virtual Taekwondo is **not evidenced**, not declared impossible.
5. Intentional biological control may establish live Performance Agency when intentionality, task coupling, causal necessity, and incidental-signal exclusion are supported.
6. Intentional biological control does not by itself establish athletic embodiment or Spatial Athletic System membership. BC-018 remains unresolved on that relation.
7. A non-performing actor who changes a rule-authorized resource or constraint is a **Participatory Rule/Resource Actor** and does not become a Performance Agent or official by default.
8. v0.2 schemas and datasets remain immutable. v0.3 is a separate derivative with explicit migration and review status.
9. No score, spatiality level, embodiment level, maturity ladder, certification, conformance claim, or paid ranking is authorized.
10. `ASR-001` remains unauthorized. Schema v0.3 must first be validated and the targeted structures must survive further corpus use.

### Rationale

The second stratum did not primarily expose missing cases; it exposed missing representational relations. A reference system must record when control changes, how sites connect, how bodily-origin signals become task actions, and how external participants alter contest conditions without collapsing those distinctions into one label.
---

## DEC-010 — ASR-001 Scope Drafting Authorization

**Status:** Ratified upon Sprint 7 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** Reviewed BC-001–BC-020 v0.3 corpus and `CORPUS_APPLICATION_FINDINGS_V0.3.md`

### Decision

1. The human-reviewed BC-001–BC-020 v0.3 corpus is accepted as the current research baseline for scope definition.
2. Schema v0.3 is adequate for the current corpus. No schema v0.4 is authorized without a repeated representational failure.
3. AltisSports authorizes drafting the **scope only** of a candidate `ASR-001`.
4. The working subject is a **Spatial Athletic System Evidence Profile**: a minimum disclosure and evidence structure, not a category-certification system.
5. Scope drafting may use object lock, Performance Agency, Embodied Performance, AS³, Operational Spatial Integration functions, comparability, evidence, uncertainty, versioning, and governance.
6. Scope drafting must exclude total scores, maturity levels, vendor rankings, federation recognition, universal sport definitions, clinical efficacy, safety certification, final BCI membership, and unresearched remote-synchronous tolerances.
7. Normative requirements, conformance clauses, certification, and publication of `ASR-001` remain unauthorized.
8. The scope draft must follow `ASR_DRAFTING_GOVERNANCE.md` and pass a separate scope-approval gate.
9. Hosted CI and external review are not required to write the scope draft, but remain conditions before a normative public release can be considered.
10. Commercial participation may not alter evidence boundaries or buy favorable inclusion.

### Rationale

Twenty adversarial cases now provide enough conceptual and representational stability to define one bounded standardization problem. They do not provide enough evidence to issue technical tolerances or certify systems. Authorizing scope drafting captures the value of the research without converting research adequacy into premature normative authority.
