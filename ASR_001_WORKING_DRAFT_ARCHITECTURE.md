# ASR-001 Working Draft Architecture

**Document state:** Working Draft Architecture  
**Version:** 0.1  
**Normative status:** Architecture for candidate requirements — ASR-001 is not published  
**Approved scope:** `ASR_001_SCOPE_DRAFT.md`

## 1. Purpose

This document defines how the ASR-001 Working Draft is organized before clause-level normative text is authored.

The architecture preserves the approved boundary: ASR-001 concerns the evidence profile for one bounded, versioned spatial-athletic system configuration. It does not certify the underlying sport, system, product quality, safety, clinical efficacy, federation recognition, or market position.

## 2. Working Draft Layers

The Working Draft is separated into five layers.

### Layer A — Status and Interpretation

Contains:

- document state;
- version;
- scope reference;
- terminology reference;
- normative-language convention;
- conformance boundary;
- exclusions;
- change history.

### Layer B — Profile Subject and Applicability

Contains:

- bounded profile subject;
- object lock;
- configuration identity;
- applicability rules;
- conditional-domain triggers;
- state handling for unknown, disputed, not applicable, and not evidenced.

### Layer C — Profile Requirements

Contains clause families mapped to the approved domains D01–D15.

Candidate clauses remain individually traceable and testable. Domain presence does not imply equal weighting, scoring, or maturity.

### Layer D — Evidence and Verification

Contains:

- evidence attachment;
- claim classification;
- source provenance;
- verification method;
- limitation and uncertainty handling;
- profile correction and supersession.

### Layer E — Informative Material

Contains:

- examples;
- boundary-case references;
- explanatory notes;
- implementation guidance;
- non-normative diagrams.

Informative content is visually and structurally separated from candidate requirements.

## 3. Clause Identifier System

Candidate requirement identifiers use:

```text
ASR001-DNN-CNN
```

Where:

- `DNN` is one approved scope domain from D01 through D15;
- `CNN` is a sequential clause number within that domain.

Example:

```text
ASR001-D03-C02
```

Clause identifiers remain stable after publication unless a formal compatibility decision authorizes renumbering.

## 4. Candidate Clause Record

Every candidate clause record contains:

- clause identifier;
- domain identifier;
- title;
- candidate obligation intent;
- applicability class;
- applicability condition;
- disclosure or evidence problem;
- evidence references;
- governance dependencies;
- verification approach;
- rationale;
- uncertainty handling;
- exclusions guarded;
- drafting status.

A candidate without this metadata does not enter clause authoring.

## 5. Clause Families

### Core Disclosure

Information needed to identify and interpret the profile.

### Conditional Disclosure

Information relevant only when a feature, role, claim, measurement, arena relation, or actor relation is present.

### Evidence Integrity

Information linking claims and fields to sources, status, limitations, and uncertainty.

### Governance and Lifecycle

Information concerning responsibility, versioning, correction, supersession, and commercial independence.

### Machine-Readable Exchange

Information supporting identifiers, serialization, validation, licensing, and machine consumption.

Clause families are organizational. They are not ranks or priorities.

## 6. Applicability Classes

- `always`
- `when_feature_present`
- `when_claim_made`
- `when_measurement_or_comparison_claimed`
- `when_contest_or_outcome_present`
- `when_distributed_operation_claimed`
- `when_human_performance_claimed`
- `when_machine_readable_distribution_provided`

A conditional clause is not failed merely because its trigger is absent.

The profile records the applicability decision and its basis.

## 7. Verification Classes

- `document_presence`
- `field_presence`
- `cross_reference_integrity`
- `evidence_traceability`
- `controlled_vocabulary`
- `conditional_logic`
- `temporal_consistency`
- `human_review`
- `machine_validation`

Verification establishes whether the profile satisfies a candidate disclosure obligation. It does not validate the underlying product claim beyond the evidence presented.

## 8. Domain Modules

The Working Draft contains one module for each approved scope domain:

- D01 — Subject Identity and Object Lock
- D02 — Operating Context and System Roles
- D03 — Performance Window and Performance Agency
- D04 — Performance Interface and Embodied Demand
- D05 — Arena and Distributed-Arena Relation
- D06 — Constraints and Rule Execution
- D07 — Sensing, Tracking, and State Estimation
- D08 — Measurement and Comparability Conditions
- D09 — Officiation, Outcome, and Consequence Structure
- D10 — Operational Spatial Integration Functions
- D11 — Presence, Participation, and External Actors
- D12 — Safety, Accessibility, and Human-Limit Disclosures
- D13 — Evidence, Claims, and Uncertainty
- D14 — Governance, Change, and Correction
- D15 — Profile Metadata and Machine Readability

Every module receives at least one core or conditional candidate clause and one traceability path.

## 9. Normative-Language Boundary

Sprint 9 defines candidate obligation intent but does not finalize normative prose.

The terms used for formal requirements are reserved for the next authorized clause-authoring sprint. This prevents architectural decisions from being mistaken for ratified clauses.

## 10. Conformance Boundary

A later conformance model can examine the evidence-profile document or machine-readable profile instance.

It cannot convert profile conformance into:

- certification of the underlying sport;
- recognition of a federation;
- approval of product quality;
- safety certification;
- clinical validation;
- category membership certification;
- ranking or endorsement.

## 11. Implementation Boundary

The boundary-case corpus schema remains research infrastructure.

The Working Draft architecture does not adopt `BOUNDARY_CASE_SCHEMA_V0.3.json` as the ASR-001 implementation schema. Candidate implementation fields can be derived only through a separate design and gate.

## 12. Change Control

Each architecture or candidate-clause change records:

- affected identifier;
- scope domain;
- evidence or issue trigger;
- expansion, narrowing, or clarification;
- compatibility impact;
- decision owner;
- date and version.

Silent clause expansion is prohibited.

## 13. Exit Condition

Sprint 9 passes when:

- D01–D15 are covered;
- candidate clauses are uniquely identified;
- every candidate maps to evidence or governance dependencies;
- applicability and verification are defined;
- implementation and informative boundaries are explicit;
- prohibited outcomes remain absent;
- a clause-authoring gate is produced.

Passing Sprint 9 does not publish ASR-001 or open Public Review.
