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

---

## DEC-011 — ASR-001 Scope Approval and Requirements-Drafting Boundary

**Status:** Ratified upon Sprint 8 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_SCOPE_DRAFT.md`, `ASR_001_SCOPE_TRACEABILITY.md`, and the reviewed BC-001–BC-020 v0.3 corpus

### Decision

1. The scope of `ASR-001 — Spatial Athletic System Evidence Profile` is approved.
2. The profiled subject is one bounded, versioned system configuration. Findings about an activity, product, platform, event, organization, or deployment may not be silently generalized across objects.
3. The approved scope contains fifteen descriptive domains covering object identity, context, agency, interface, arena, rules, sensing, measurement, officiation, spatial functions, participation, safety/accessibility disclosure, evidence, governance, and machine-readable metadata.
4. ASR-001 is an evidence-profile project. It is not a universal sport definition, product-rating system, federation-recognition mechanism, safety or clinical certification, or category-ownership claim.
5. Any future conformance model is bounded to the evidence-profile document or machine-readable profile instance. It may not certify the underlying sport, system, product quality, safety, clinical efficacy, or market superiority.
6. Requirements drafting is authorized for a governed Working Draft only.
7. Every future candidate clause must map to an approved scope domain, a defined problem, evidence or governance dependency, applicability condition, verification approach, rationale, and affected exclusions or uncertainty.
8. The research corpus schema is not automatically the ASR-001 implementation schema. A separate implementation decision is required.
9. Publication as a standard, Public Review Draft status, certification, product or sport conformance claims, scoring, maturity levels, vendor rankings, and claims of industry adoption remain unauthorized.
10. External operator review and hosted validation remain conditions before a normative public release can be considered.

### Rationale

The approved scope converts twenty adversarial cases into one bounded standardization problem: how to disclose and support evidence about a spatial-athletic system configuration without converting documentation into product judgment or category certification. This is sufficient to begin a controlled Working Draft, but not to claim a standard, adoption, or conformance program.

---

## DEC-012 — ASR-001 Working Draft Architecture and Clause-Authoring Boundary

**Status:** Ratified upon Sprint 9 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_WORKING_DRAFT_ARCHITECTURE.md`, `ASR_001_CLAUSE_CATALOG_V0.1.json`, and `ASR_001_EVIDENCE_TO_CLAUSE_MAP.md`

### Decision

1. The ASR-001 Working Draft architecture is accepted as the governing structure for clause authoring.
2. Candidate requirement identifiers use the stable form `ASR001-DNN-CNN`, with every candidate mapped to one approved scope domain D01–D15.
3. The Sprint 9 baseline contains thirty candidate obligation records, exactly two for each approved domain.
4. Candidate records are not normative clauses. They define obligation intent, applicability, evidence, governance dependencies, verification, rationale, uncertainty, and exclusion guards.
5. Every future clause must retain traceability to its candidate record or record an explicit replacement decision.
6. Applicability is conditional and evidence-aware. A non-triggered clause is not a failed clause, and missing evidence does not become an underlying-system score.
7. Verification concerns the evidence-profile document or instance. It does not validate the underlying sport, product quality, safety, clinical efficacy, federation recognition, or market superiority.
8. The boundary-case research schema is not adopted as the ASR-001 implementation schema. A separate implementation-profile decision is required.
9. Candidate clause authoring is authorized for a governed non-public Working Draft only.
10. Publication, Public Review Draft status, certification, product or sport conformance claims, scores, levels, rankings, unsupported technical tolerances, final BCI athletic classification, and claims of industry adoption remain unauthorized.

### Rationale

The approved scope is now decomposed into uniquely identified, evidence-linked, conditionally applicable, and verifiable candidate obligations. This is enough to begin clause-level drafting without losing the exclusions and uncertainty that made the research credible. It is not enough to release a standard or conformance program.

---

## DEC-013 — ASR-001 Candidate Normative Core and Internal-Trial Boundary

**Status:** Ratified upon Sprint 10 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_WORKING_DRAFT_V0.1.md`, `ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.1.json`, and `ASR_001_PROFILE_MODEL_V0.1.json`

### Decision

1. The ASR-001 Candidate Normative Core v0.1 is accepted as a non-public Working Draft.
2. The core contains exactly thirty clause-level candidate obligations using the stable identifiers authorized by DEC-012.
3. Candidate normative language is permitted only inside the governed Working Draft and does not establish publication, recognition, adoption, or a certification program.
4. Every clause retains its approved domain, applicability, evidence or governance dependency, verification approach, rationale, uncertainty handling, exclusion guards, and profile field path.
5. The candidate implementation profile model v0.1 is clause-derived and is distinct from the Boundary Case Schema.
6. Candidate profile validation checks the profile document or machine-readable instance only. It does not validate or certify the underlying sport, product, safety, clinical efficacy, quality, federation recognition, category membership, or market superiority.
7. Conditional applicability is explicit. A non-triggered clause is not a failure, and missing evidence is not converted into a zero, score, grade, or ranking.
8. Two synthetic profiles are accepted as deterministic structural fixtures. They are not market records and create no provider claims.
9. Internal implementation trials are authorized. Clause changes during those trials require recorded implementation evidence or a governance issue.
10. ASR-001 publication, Public Review Draft status, certification, public conformance claims, scores, maturity levels, vendor rankings, unsupported technical tolerances, final BCI athletic classification, and claims of industry adoption remain unauthorized.

### Rationale

The approved scope and candidate architecture now have clause-level expression and a separate operational profile model. Internal implementation is the next reliable test: it can expose clauses that are ambiguous, untestable, overbroad, duplicative, or poorly represented before any external review or publication posture is considered.

---

## DEC-014 — ASR-001 Internal Trial Refinement and Operator-Review Preparation Boundary

**Status:** Ratified upon Sprint 11 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_INTERNAL_TRIAL_RESULTS.md`, `ASR_001_CLAUSE_FRICTION_REGISTER_V0.1.json`, and `ASR_001_REFINEMENT_RESULT.md`

### Decision

1. The seven Sprint 11 internal profile artifacts are accepted as the current implementation-trial baseline.
2. The ASR-001 Working Draft advances internally from v0.1 to v0.2 without changing the approved D01–D15 scope or any clause identifier.
3. Applicability and evidence sufficiency are separate states. An applicable clause may remain `not_evidenced`, `unknown`, or `partial` without becoming non-applicable or producing a score.
4. `ASR001-D03-C02` applies when agency modes, control regimes, or handoff are present, including autonomous contest execution after human design.
5. `ASR001-D04-C02` applies when embodied demand or intentional biological control is claimed, without settling athletic membership or establishing an embodiment threshold.
6. A JSON ASR-001 profile instance declares machine-readable distribution as present.
7. Clause records distinguish declarative, supporting-evidence, lifecycle, and distribution-manifest evidence requirements.
8. Profile correction and supersession are explicit and append-only; the rehabilitation revision pair is accepted as the lifecycle test.
9. Internal trials confirm the profile-only conformance boundary across autonomous, support, BCI, human–AI, participatory-audience, and remote-control configurations.
10. Preparation of an operator-review package is authorized. Outreach, external review execution, Public Review Draft status, ASR-001 publication, certification, public conformance claims, scores, rankings, unsupported technical tolerances, final BCI athletic classification, and claims of adoption remain unauthorized.

### Rationale

Internal implementation exposed representational and verification defects that syntax-only validation could not reveal. The bounded v0.2 refinement resolves those defects while preserving all identifiers, exclusions, uncertainty, and historical artifacts. The next useful step is to prepare a review package that lets relevant operators challenge the Working Draft without prematurely opening Public Review or claiming adoption.
