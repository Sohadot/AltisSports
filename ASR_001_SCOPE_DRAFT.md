# ASR-001 — Spatial Athletic System Evidence Profile

**Document state:** Scope Approved upon Sprint 8 Gate PASS  
**ASR family:** Altis Spatial Reference  
**Identifier:** ASR-001  
**Version:** Scope 1.0  
**Normative status:** Descriptive scope only — no standard is issued  
**Evidence basis:** Human-reviewed BC-001–BC-020 corpus under schema v0.3

## 1. Scope Statement

ASR-001 addresses the structure of an evidence profile for a bounded system configuration whose relationship to human performance and computationally mediated space is being documented.

The profile keeps the profiled object, operating context, performance relations, spatial functions, comparison conditions, evidence, uncertainty, dependencies, and governance visible in one inspectable record.

ASR-001 concerns the quality and traceability of the profile. It does not decide whether an activity is universally a sport, certify the underlying system, or rank products.

## 2. Problem Being Addressed

Organizations currently describe spatial athletic systems through incompatible product language, technical claims, event rules, research reports, and marketing categories. Important distinctions are often lost:

- the activity is confused with the product or event;
- human participation is confused with live Performance Agency;
- immersion is confused with Operational Spatial Integration;
- physical spatial skill is confused with computational Spatiality;
- measured values are presented without comparison conditions;
- provider claims are mixed with independent evidence;
- unknown evidence is converted into absence;
- one deployment is generalized to every configuration of a platform;
- profile completeness is mistaken for product quality or certification.

The ASR-001 scope is limited to making those distinctions documentable and reviewable.

## 3. Profile Subject and Object Lock

The profile subject is one bounded, versioned system configuration.

A configuration can include a product deployment, contest configuration, training or support configuration, event implementation, or research setup. The profile identifies the primary object and any secondary objects without silently transferring findings between them.

The profile context identifies, where available:

- responsible organization;
- product, platform, or event name;
- version, ruleset, patch, equipment class, and configuration;
- operating location or site topology;
- performance window;
- system roles;
- declared dependencies;
- date and temporal status.

A generic activity, an entire company, or every deployment of a platform is not treated as one profile subject unless the evidence genuinely supports that breadth.

## 4. Intended Users

The scope serves:

- sport-governance and integrity teams;
- competition and event operators;
- XR and spatial-system product teams;
- performance-measurement and data teams;
- procurement and due-diligence functions;
- accessibility and adaptive-sport specialists;
- researchers and evaluators;
- technical integrators and platform partners;
- structured-data and intelligent-agent consumers.

## 5. Intended Uses

An ASR-001 evidence profile is intended to support:

- system documentation;
- procurement review;
- research comparability;
- event and integrity planning;
- implementation and integration review;
- evidence-gap identification;
- version and dependency tracking;
- correction and supersession;
- machine-readable exchange;
- comparison of disclosed conditions without producing a ranking.

## 6. In-Scope System Relations

The scope can document systems related to:

- competition;
- training;
- assessment;
- rehabilitation;
- simulation;
- measurement;
- officiation;
- spectatorship and participation;
- research.

Inclusion of a role does not convert a support system into a sport or a product into a governed contest.

The profile can preserve a provisional relation such as Spatial Athletic System, Spatial Athletic Contest, Spatial Support System, Computational Contest, outside the core class, partial integration, or unresolved. The relation remains an evidence-backed statement, not a certification badge.

## 7. In-Scope Profile Domains

### D01 — Subject Identity and Object Lock

Identification of the bounded object, related objects, responsible entities, configuration, version, and temporal state.

### D02 — Operating Context and System Roles

Description of the deployment context, intended function, participant setting, event or support role, and relevant dependencies.

### D03 — Performance Window and Performance Agency

Description of the interval in which actions affect the evaluated result, the human performer relation, causal necessity of skill, assistance, autonomy, and phase-level agency where control changes.

### D04 — Performance Interface and Embodied Demand

Description of the channels through which human action enters the system, including direct bodily action, equipment mediation, remote control, tracked movement, adaptive equipment, physiological sensing, and intentional biological control.

### D05 — Arena and Distributed-Arena Relation

Description of physical, computational, and unified arenas; site topology; shared state; synchronization; local or remote relations; and evidence gaps around distributed operation.

### D06 — Constraints and Rule Execution

Description of textual, physical, equipment, sensor, geometry, code, and human-enforced constraints, including their declared version and operative authority.

### D07 — Sensing, Tracking, and State Estimation

Description of what is observed directly, what is inferred, relevant tracking volumes, latency or loss conditions when disclosed, and the effect of sensing failure.

### D08 — Measurement and Comparability Conditions

Description of metrics, units, calibration, equipment classes, versions, environmental bounds, accessibility adaptations, uncertainty, and the intended comparison context.

### D09 — Officiation, Outcome, and Consequence Structure

Description of decision authority, automated and human officiation, appeals or correction paths, performance-dependent outcome, and the consequences produced by the contest or support process.

### D10 — Operational Spatial Integration Functions

Evidence profiles for the roles through which computationally mediated space can represent, enable, mediate, constrain, measure, compare, or officiate.

Each function is connected to a mechanism, affected layers, evidence, uncertainty, and failure effect rather than a numerical score.

### D11 — Presence, Participation, and External Actors

Description of participants, coaches, officials, spectators, supervisors, information actors, and participatory rule or resource actors without silently converting them into Performance Agents.

### D12 — Safety, Accessibility, and Human-Limit Disclosures

Documentation of known hazards, access conditions, body variation, fatigue, collision, cybersickness, clinical context, cognitive demand, operational responsibility, and stated limitations.

This domain records evidence and responsibility. It does not provide safety or clinical certification.

### D13 — Evidence, Claims, and Uncertainty

Separation of documented fact, provider claim, Altis or evaluator interpretation, provisional proposition, and commercial or forecast claim, together with source provenance, access date, temporal status, limitations, confidence, and unresolved states.

### D14 — Governance, Change, and Correction

Identification of responsible authority, rule and software versioning, data or documentation ownership, incidents, corrections, supersession, commercial conflicts, and review history.

### D15 — Profile Metadata and Machine Readability

Identification of profile version, schema or serialization version, creation and revision dates, language, licensing notice, dependencies, identifiers, and machine-readable distribution.

## 8. Evidence and Claim Boundary

The profile distinguishes:

- directly documented facts;
- multi-source factual synthesis;
- attributed external claims;
- Altis or evaluator interpretation;
- provisional category propositions;
- commercial or forecast claims.

A source supports identified fields or statements rather than the profile as an undifferentiated whole.

First-party documentation can establish a declared capability or configuration. It does not independently establish effectiveness, safety, superiority, or broad deployment.

## 9. Uncertainty and State Representation

The profile keeps the following states available where relevant:

- supported;
- partial;
- absent;
- disputed;
- unknown;
- not applicable;
- not evidenced.

Unknown is not treated as absence. Not evidenced is not treated as impossible. A profile can remain useful while preserving unresolved category relation or incomplete evidence.

## 10. Future Conformance Boundary

A future ASR-001 working draft can explore conformance of the evidence-profile document or machine-readable profile instance.

That future boundary concerns matters such as declared subject, traceability, state handling, evidence attachment, version disclosure, and correction metadata.

It does not extend conformance to:

- the underlying sport;
- federation recognition;
- product quality;
- athletic legitimacy;
- safety performance;
- clinical efficacy;
- market superiority;
- category ownership.

## 11. Explicit Exclusions

ASR-001 does not address:

- a universal definition of sport;
- a minimum embodiment threshold;
- a total score, spatiality level, maturity level, or quality grade;
- vendor or product ranking;
- automatic Spatial Athletic System certification;
- federation recognition;
- safety certification;
- clinical efficacy requirements;
- technical latency, calibration, or network tolerances for remote synchronous competition;
- final BCI athletic membership;
- causal-attribution scoring;
- anti-cheat certification;
- commercial endorsement;
- paid favorable classification;
- ownership of the descriptive term Spatial Sport.

## 12. Dependencies

The scope is derived from and remains subordinate to:

- `FIRST_PRINCIPLES.md`;
- `CATEGORY_THESIS.md`;
- `ONTOLOGY.md`;
- `AS3_STACK.md`;
- `SOURCE_AND_CLAIM_POLICY.md`;
- `QUALITY_GATE.md`;
- `ASR_DRAFTING_GOVERNANCE.md`;
- `BOUNDARY_CASE_SCHEMA_V0.3.json`;
- `boundary-cases-001-020.v0.3.json`;
- `CORPUS_APPLICATION_FINDINGS_V0.3.md`;
- `DECISION_LOG.md`.

The boundary-case schema is research infrastructure. It is not silently adopted as the future ASR-001 implementation schema.

## 13. Relationship to the Boundary Corpus

The twenty-case corpus provides evidence for the need to disclose the domains above and for the exclusions that bound the scope.

Boundary cases serve as informative tests, counterexamples, and traceability anchors. They do not form a hidden weighting system and do not predetermine product judgments.

## 14. Anticipated Future Artifacts

After a separate requirements-drafting authorization, future work can explore:

- a working-draft document structure;
- evidence-to-clause traceability;
- candidate profile fields and conditional applicability;
- an implementation schema distinct from the research corpus schema;
- profile validation;
- correction and supersession procedures;
- a narrowly bounded profile-conformance model;
- examples and implementation guidance.

No such artifact is issued by this scope document.

## 15. Scope Change Triggers

The approved scope is revisited when:

- repeated implementation evidence shows an included domain has no useful profile function;
- a recurring evidence need cannot be represented within the approved domains;
- the profiled object becomes ambiguous in actual implementations;
- a dependency changes materially;
- external review reveals an unbounded safety, accessibility, privacy, or governance implication;
- requirements drafting attempts to introduce an outcome listed under Explicit Exclusions.

Scope expansion is recorded through change control and a new approval decision.

## 16. Scope Verdict

ASR-001 is scoped as an evidence and disclosure profile for bounded spatial-athletic system configurations.

It is not scoped as a sport-definition authority, product-rating system, safety regime, federation-recognition mechanism, or certification program.
