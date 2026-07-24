# AS³ — Altis Spatial Sport Stack

**Version:** 0.3  
**Status:** Provisional Reference Architecture — Not a Standard  
**Revision basis:** `INVARIANCE_FINDINGS_V0.1.md` and `SECOND_STRATUM_FINDINGS_V0.2.md`

## 1. Purpose

AS³ locates where a Spatial Sport system enables performance, carries rules, produces measurements, and can lose integrity.

It is an inspection architecture, not a maturity scale. Layers are not levels, and the number of present layers does not determine quality or category membership.

## 2. Scope Discipline

AS³ may inspect an activity, contest, athletic system, spatial athletic system, support system, experience, product, event, or organization.

The classified object must be locked before layer analysis. AS³ does not repair an ambiguous object definition.

## 3. Layers

### L1 — Performance Agency

Identifies who or what performs during the relevant performance window and how live human skill affects the result.

Inspect:

- live, remote, or assisted Performance Agency;
- design or engineering agency;
- autonomous execution;
- agency handoffs;
- phase- or regime-level control;
- the causal necessity of human skill;
- undeclared automation.

When control varies, use Agency Segments. Distinguish an observed phase from a rule-permitted manual, semi-autonomous, or autonomous regime.

Design contribution must not be confused with in-performance agency.

### L2 — Performance Interface and Embodied Demand

Describes how human skill enters the system and what bodily, physiological, cognitive, or sensorimotor demands materially contribute to performance.

Interface types may include:

- direct bodily action;
- adaptive or assistive equipment;
- vehicle mediation;
- remote control;
- tracked XR input;
- controllers;
- resistance equipment;
- physiological sensing;
- intentional biological control;
- other declared assistance.

For biological control, inspect intentional generation, task coupling, decoder mediation, trainability, and incidental-signal exclusion. Bodily origin may support Performance Agency without settling athletic embodiment.

Mediation does not by itself establish Spatiality. No normative body model or minimum embodiment threshold is authorized by v0.3.

### L3 — Arena and Spatial State

Describes physical, computational, and unified arenas, including boundaries, zones, hazards, shared state, and synchronization.

Inspect:

- physical boundaries;
- computational geometry;
- rule-bearing zones;
- tracking volumes;
- local and remote arena relationships;
- distributed-arena topology;
- shared state and synchronization;
- latency and calibration equivalence;
- cross-site officiation and safety responsibility;
- spatial state changes;
- failure when physical and computational boundaries diverge.

Global participation or a co-located network does not establish a remote synchronous arena.

### L4 — Constraint and Rule Execution

Describes where rules reside and how they become operative.

Rules may be:

- textual;
- human-enforced;
- equipment-enforced;
- sensor-enforced;
- geometry-enforced;
- code-enforced.

Inspectability, versioning, consistency, and divergence between declared and implemented rules are central.

### L5 — Sensing, Tracking, and State Estimation

Describes how participant, equipment, arena, and event state are detected or inferred.

Inspect:

- direct measurement versus estimation;
- accuracy;
- latency;
- drift;
- smoothing;
- occlusion;
- tracking loss;
- device inequality;
- confidence and failure behavior.

### L6 — Measurement and Comparability

Describes how observations become metrics and under which conditions comparisons are valid.

Inspect:

- metric definition;
- units;
- intended use;
- calibration;
- equipment classes;
- version locks;
- latency controls;
- environmental bounds;
- accessibility adaptations;
- uncertainty.

Comparability is often engineered. Missing controls create unresolved evidence, not an automatic score penalty.

### L7 — Officiation and Outcome

Describes how rule-relevant events become decisions, penalties, rankings, or results.

Inspect:

- human and automated authority;
- contestability;
- event records;
- appeals;
- correction;
- reproducibility;
- Outcome Openness;
- Consequence Structure.

An automated result may be open without containing live human Performance Agency.

### L8 — Presence and Participation

Describes how participants, coaches, officials, spectators, and remote actors perceive, communicate, and affect the system.

Inspect:

- role identity;
- information asymmetry;
- remote presence;
- communication;
- spectator influence;
- participatory rule/resource actors;
- resource or constraint modification;
- information asymmetry;
- harassment and access;
- social participation.

A spectator or external participant may alter a resource or constraint without becoming a Performance Agent or official.

Presence and immersion are not evidence of Spatial Athletic System membership.

### L9 — Safety, Accessibility, and Human Limits

Describes physical, cognitive, physiological, and social conditions of acceptable participation.

Inspect:

- collision;
- fatigue;
- overexertion;
- cybersickness;
- unsafe room assumptions;
- body variation;
- adaptive access;
- cognitive load;
- warnings;
- operational responsibility.

Accessibility is constitutive system design, not an edge-case add-on.

### L10 — Governance, Evidence, and Change

Describes ownership, accountability, evidence, versioning, correction, and commercial independence.

Inspect:

- governing authority;
- claim provenance;
- provider versus Altis interpretation;
- software and rule changes;
- incidents;
- corrections;
- data rights;
- conflicts of interest;
- external inspectability.

## 4. Operational Spatial Integration Profile

Operational Spatial Integration is a cross-layer condition, not an additional layer.

For the locked classified object, record which Spatial Functions are evidenced:

- represent;
- enable;
- mediate;
- constrain;
- measure;
- compare;
- officiate.

For every claimed function record:

1. observable mechanism;
2. supporting evidence;
3. affected AS³ layers;
4. whether the function is incidental, supportive, or constitutive in that case;
5. failure effect;
6. uncertainty.

These descriptors are qualitative research fields. They are not levels, points, weights, or a maturity sequence.

## 5. Other Cross-Layer Conditions

### Integrity

Whether the intended relationship among agency, interface, rules, sensing, measurement, and outcome remains trustworthy.

### Agency Handoff

Where control or decision authority moves between humans and automated components.

Use phase-level Agency Segments where control is time-varying. Record segment basis, active agents, primary control, transition trigger, assistance, causal attribution, evidence, and uncertainty.

### Distributed Arena Relation

How physical sites, local hubs, remote operators, or performers connect to shared computational state. The relation spans arena, sensing, measurement, comparison, officiation, safety, and governance.

### Participatory Actor Relation

How a non-performing actor changes a resource, constraint, information state, or modifier. This relation must not be silently converted into Performance Agency.

### Intentional Biological Control

How an intentional bodily-origin signal becomes task action through sensing or decoding. Inspect agency and embodiment separately.

### Comparability

A coordinated condition spanning interface, arena, tracking, calibration, rules, versions, and accessibility.

### Accessibility

A condition spanning agency, interface, arena, participation, safety, measurement, and governance.

### Security and Privacy

Conditions affecting identity, telemetry, physiological data, remote participation, result integrity, and institutional trust.

## 6. Permitted Outputs

AS³ may support:

- system profiles;
- evidence checklists;
- failure-mode maps;
- Atlas fields;
- comparison condition records;
- readiness research;
- future ASR requirement mapping.

## 7. Prohibited Outputs in v0.3

AS³ does not authorize:

- a total score;
- a spatiality level;
- a maturity ladder;
- certification;
- conformance claims;
- paid rankings;
- a single yes/no category badge without an evidence profile.

## 8. Failure Principle

> performance agency → interface → arena → rule → sensing → measurement → decision → participation → safety → governance

A broken link can invalidate conclusions produced above it.

The sequence is analytical, not necessarily chronological. Cross-layer failures may originate in more than one location.

## 9. Revision Trigger

Revise AS³ when:

- boundary cases reveal a missing function;
- layers cannot be distinguished operationally;
- a layer cannot be tied to observable evidence;
- the Operational Spatial Integration Profile fails to capture recurring mechanisms;
- phase-level agency cannot represent control changes;
- distributed-arena relations cannot represent cross-site integrity;
- participatory actors are confused with performers or officials;
- intentional biological control is reduced either to visible movement or to any incidental biosignal;
- real systems violate the assumed relationships;
- the architecture encourages misleading scoring or object collapse.
