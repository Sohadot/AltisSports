# AltisSports Ontology

**Version:** 0.2  
**Status:** Provisional Category Model — Not a Standard  
**Revision basis:** `INVARIANCE_FINDINGS_V0.1.md`

## 1. Purpose

This ontology provides the minimum vocabulary required to classify Spatial Sport objects without collapsing activity, contest, system, product, experience, organization, and evidence into one concept.

Terms are descriptive unless explicitly made normative by a future ASR document.

## 2. Classification Objects

### Activity

Structured participant actions performed under constraints.

### Contest

A bounded activity instance in which performances or agents are compared under an outcome structure.

### Athletic System

The arrangement through which human performance is enabled, constrained, observed, measured, compared, and interpreted.

### Spatial Athletic System

A provisional system class in which live human Performance Agency and an evidenced embodied performance channel are operationally connected to computationally mediated space.

### Spatial Athletic Contest

A Spatial Athletic System functioning as a contest with constraints, comparison conditions, and a performance-dependent open outcome.

### Computational Contest

A contest whose decisive environment is computational but whose athletic embodiment or Spatial Athletic System membership is absent, insufficiently evidenced, or unresolved.

### Spatial Support System

A system supporting training, assessment, rehabilitation, measurement, officiation, spectatorship, broadcasting, social participation, or research.

### Experience

A particular participant, official, coach, or spectator encounter with a system.

### Product

A commercial or institutional implementation providing one or more system functions or experiences.

### Platform

A technical environment enabling multiple products, experiences, integrations, or developers.

### Event

A temporally bounded organized occurrence containing one or more activities or contests.

### Organization

A legal, institutional, commercial, research, or governing entity.

## 3. Agency Terms

### Performance Agency

Meaningful in-performance influence by a human performer through skill exercised during the relevant performance window.

### Live Performance Agency

Performance Agency exercised while the result is being produced.

### Remote Performance Agency

Live Performance Agency exercised through a remote interface.

### Assisted Performance Agency

Live Performance Agency supported or modified by declared assistance while remaining materially necessary.

### Design or Engineering Agency

Human contribution to the design, programming, construction, or preparation of the performing system before the performance window.

Design or Engineering Agency is not sufficient by itself to establish athletic Performance Agency.

### Autonomous Execution

Execution during the contest window without live human Performance Agency.

### Agency Handoff

A transition of control or decision authority between human and automated components during a performance.

## 4. Human and Institutional Roles

Participant, Athlete, Coach, Official, Spectator, Operator, Developer, Governing Body, Rights Holder, and Researcher.

The term “athlete” does not by itself establish category membership.

## 5. Performance and Embodiment Terms

### Action

A participant-generated or system-recognized event.

### Performance

A temporally bounded set of actions evaluated against a task, rule, target, opponent, or reference.

### Performance Window

The time interval during which actions can materially affect the evaluated result.

### Embodied Performance

Performance in which bodily, physiological, or sensorimotor activity materially contributes to the result.

### Embodied Demand

The type and extent of bodily contribution required by the classified object.

Embodied Demand is descriptive in v0.2; no universal threshold is defined.

### Performance Interface

The mechanism through which human skill enters the system.

Interface modes may include direct bodily action, adaptive equipment, vehicle control, remote control, tracked XR input, resistance equipment, physiological sensing, or other mediated channels.

## 6. Space and Integration Terms

### Physical Arena

The material environment in which bodies, equipment, and hazards exist.

### Computational Arena

A represented, sensed, or generated environment in which digital interaction, state, or rules operate.

### Unified Arena

A system state in which physical and computational arenas jointly affect the same performance process.

### Rule-Bearing Zone

A bounded area whose position or state changes permitted actions, scoring, penalties, or measurement.

### Tracking Volume

The region within which participant, equipment, or environmental state can be detected with defined characteristics.

### Spatial Function

A role performed by computationally mediated space.

Controlled provisional roles:

- represent;
- enable;
- mediate;
- constrain;
- measure;
- compare;
- officiate.

### Operational Spatial Integration Profile

A structured description of Spatial Functions for a classified object, including observable mechanism, evidence, dependency, and failure effect.

It is not a score or maturity level.

## 7. Contest and Integrity Terms

### Constraint

A condition limiting actions, resources, spaces, timing, equipment, or eligibility.

### Rule

A declared normative constraint governing an activity or contest.

### Computational Rule

A rule implemented or enforced through software, sensors, geometry, or automated state transition.

### Constraint Integrity

The condition in which operative constraints are identifiable, sufficiently consistent, and appropriate to the intended contest.

### Outcome Openness

The condition in which the result emerges through performance rather than a predetermined script.

### Consequence Structure

The ranking, elimination, loss, qualification, cost, or other effect produced by a contest.

Consequence Structure is a derived analytical property in v0.2.

### Comparability Condition

A condition required for performances to support a stated comparison.

### Officiation

Detection, interpretation, and resolution of rule-relevant events.

### Integrity Condition

A condition required for the result, metric, or classification to remain trustworthy for its intended use.

### Failure Mode

A documented way in which an agency, interface, spatial, rule, sensing, measurement, outcome, participation, safety, or governance relationship can fail.

## 8. Measurement and Evidence Terms

Metric, Measurement, Calibration, Result, Profile, Claim, Source, Evidence Record, Provider Claim, Altis Interpretation, Confidence, and Limitation.

A Profile is multi-dimensional and must not be represented as a total score unless a later evidence-backed decision authorizes one.

## 9. System Roles

A system may perform one or more roles:

- Competition
- Training
- Assessment
- Rehabilitation
- Simulation
- Officiation
- Measurement
- Spectatorship
- Broadcasting
- Social Participation
- Research

System role does not determine category membership by itself.

## 10. Environment Modalities

Physical, Digitally Augmented, Mixed, Virtual, Remote Distributed, and Hybrid.

Modality describes environment configuration. It does not prove Operational Spatial Integration.

## 11. Core Relations

- an Organization develops, operates, governs, funds, or owns a Product;
- a Platform enables a Product or Experience;
- a Participant performs an Activity through an Athletic System;
- an Event contains Activities or Contests;
- a Contest occurs during a Performance Window;
- a human performer exercises Performance Agency;
- a Product implements one or more System Roles;
- an Athletic System operates within Arenas;
- a Spatial Function connects computationally mediated space to a classified object;
- a Rule constrains an Action;
- Officiation interprets rule-relevant events;
- Measurement produces a Metric;
- Calibration supports a Comparability Condition;
- a Consequence Structure derives from a Contest;
- a Claim is supported or challenged by an Evidence Record;
- a Failure Mode violates an Integrity Condition.

## 12. Object-Lock Rule

Every classification record must identify one primary classified object.

A conclusion about a Product must not be generalized to an Activity. A conclusion about an Experience must not be generalized to a Platform. A training configuration must not be generalized to a contest configuration.

Where multiple objects are inseparable, the record must declare the entanglement unresolved rather than switch objects silently.

## 13. Classification Discipline

No object is classified from:

- branding alone;
- use of XR terminology;
- visual immersion;
- a 3D interface;
- device compatibility;
- institutional recognition alone;
- an unsupported provider claim;
- the mere existence of a computational arena.

Classification requires evidence appropriate to the object and the claimed class.

## 14. Deferred Terms

The following remain deferred:

- minimum embodiment threshold;
- normative Operational Spatial Integration vocabulary;
- sport threshold;
- spatiality level;
- embodiment score;
- integrity score;
- readiness level;
- conformance status;
- certification status.

The ontology must describe before a standard judges.
