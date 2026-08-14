# Reference Authority and Citability Model

**Version:** 0.1
**Status:** Foundation Draft — Not Ratified
**Depends on:** `ASSET_THESIS.md`, `CATEGORY_THESIS.md`, `MONETIZATION_BOUNDARY.md`, `SOURCE_AND_CLAIM_POLICY.md`, `QUALITY_GATE.md`

## 1. Purpose

This model states how AltisSports becomes a strategic, sovereign, and trusted reference that specialists, analysts, technologists, engineers, artificial-intelligence systems, journalists, and operating companies can cite — without making premature claims of authority that the evidence does not yet support.

It resolves one recurring strategic error: treating recognition as a precondition for producing citable artifacts. Recognition is not a gate that opens before the work. It accrues **through** the work.

## 2. Reference Objective

AltisSports intends to become the source whose **absence from a serious inquiry into Spatial Sport is noticeable** (`ASSET_THESIS.md` §9).

That objective is served by depth, traceability, attribution, and machine-readable citability across many audiences — not by breadth of coverage claimed early, and not by any declaration of authority, sovereignty, or inevitability.

## 3. Audience Consumption Modes

The reference is one asset consumed through different layers. No layer is a separate truth; all trace to the same governed core.

| Audience | Primary consumption mode | Governing layer |
| --- | --- | --- |
| Specialists / researchers | Definitions, first principles, AS³, boundary cases | Open Authority Layer |
| Analysts / companies | Atlas records, comparison conditions, readiness research | Paid Intelligence Layer |
| Technologists / engineers | Machine-readable schemas, stable identifiers, exports | Open + API |
| Artificial-intelligence systems | Structured, attributed, licensed, citable records | Open Authority Layer + citability rules (§5) |
| Journalists | Attributed, falsifiable records with version and correction history | Open Authority Layer |

Layer separation follows `MONETIZATION_BOUNDARY.md`. This model adds only the citability rules that make each layer safely quotable.

## 4. Citability as the Mechanism of Reference Authority

Reference authority is not conferred; it accrues when a record is quoted, relied upon, and survives scrutiny. The causal order is therefore:

> attributed, falsifiable, machine-readable artifacts → citation and reliance → reference authority

not the reverse. A descriptive, source-disciplined record does not require prior fame to exist. It is one of the mechanisms **by which** the reference position is earned.

A record advances reference authority only when it satisfies the existing claim discipline (`SOURCE_AND_CLAIM_POLICY.md`): the claim class is stated, the source is inspectable, the provider claim is separated from Altis interpretation, and the uncertainty is visible.

## 5. Machine and AI Citability Requirements

`SOURCE_AND_CLAIM_POLICY.md` §8 governs AI as an internal research aid. This section governs the distinct case of **external systems — including AI — citing AltisSports as a source.**

A record is externally citable only when it carries:

1. **A stable identifier.** A durable, versioned identifier (e.g. a boundary-case ID, an ASR clause ID, an AS³ field ID) that does not change meaning across revisions. Superseded identifiers are retained, not reused.
2. **Attribution and claim class.** The claim class (C1–C6) and the separation of provider claim from Altis interpretation are machine-visible, not implied.
3. **Explicit license.** The terms under which the record may be quoted, reproduced, or ingested are declared (`DATASET_LICENSE.md`). Absence of a license is not permission.
4. **Falsifiability and correction path.** The record states what evidence would revise it and retains its correction history (`SOURCE_AND_CLAIM_POLICY.md` §9). A record that cannot be corrected cannot be a reference.
5. **Temporal status.** Current, provisional, superseded, or historical status is explicit, so a citing system cannot present an outdated record as current.

An external system that ingests a compliant record can attribute it precisely and cannot silently distort it. This — not any assertion of dominance — is the operational path by which the reference becomes difficult to bypass.

## 6. Descriptive and Evaluative Atlas Boundary

The Altis Atlas is separated into two permission classes to prevent premature judgment.

### 6.1 Descriptive Atlas — permitted now

A descriptive record states what a system is, what its provider claims, what is observably true, and what remains unresolved — each attributed and each carrying a claim class. It issues no verdict.

A descriptive record is permitted once it passes the **Dataset and Atlas Gate** (`QUALITY_GATE.md` §3). It requires no prior recognition, no ratified ASR, and no score. The existing `boundary-cases-*.json` corpus is the first descriptive stratum.

### 6.2 Evaluative Atlas — gated

An evaluative record issues a judgment: a rating, ranking, conformance statement, certification, or category verdict.

Evaluative records remain prohibited until the requirements they depend on exist and have passed their gates (`STANDARDIZATION_READINESS_GATE.md`, `QUALITY_GATE.md` §4). Payment may never purchase or alter an evaluative record (`MONETIZATION_BOUNDARY.md`).

The architectural ordering that places the Atlas after ASR (`CATEGORY_THESIS.md` §11) is a **traceability** dependency for evaluative records — not a recognition precondition for descriptive records.

## 7. Temporal Knowledge Layers and Scope Discipline

A large reference is achieved by depth in one bounded problem first, then governed expansion — not by early breadth. This preserves the precision that makes citation defensible (`STANDARDIZATION_READINESS_GATE.md` §3–§4).

The reference is intended to cover its field across three temporal knowledge layers. Each layer inherits the temporal-status discipline of `SOURCE_AND_CLAIM_POLICY.md` §6 and carries a distinct evidentiary burden:

- **Historical layer** — how the field, its systems, and its terms came to be. Governed as documented fact (C1) and multi-source synthesis (C2); historical status must be marked and must not be presented as current.
- **Present layer** — the current state of systems, providers, and evidence. This is the primary operating layer today; it uses first-party documentation and the claim classes already in force.
- **Future / foresight layer** — trajectories, open questions, and anticipated developments. Governed as forecast claims (C6) under mandatory attribution and restraint; a foresight record must never be presented as documented fact, and must state what would confirm or refute it.

These layers are **temporal coverage of the same bounded object**, not a licence to widen the object itself. Any proposal to widen the classified object of the reference — beyond Spatial Sport as currently scoped — remains a separate scope-expansion decision that must pass a governance gate with its own object lock, evidence base, and claim discipline before any coverage of it may be published or claimed.

## 8. Prohibitions

Under this model, AltisSports must not:

- declare itself sovereign, authoritative, inevitable, or non-bypassable as a marketing claim rather than an earned, evidenced position;
- publish an evaluative Atlas record before its governing requirements have passed their gates;
- publish or ingest a record that lacks a stable identifier, claim class, license, or temporal status;
- reuse a retired identifier for a new meaning;
- admit a new knowledge layer (historical, green, future, or other) into scope without a governance decision;
- present breadth of coverage as evidence of authority.

## 9. Governing Test

A step advances the reference position only when every answer is yes:

1. Is the artifact attributed, claim-classed, and falsifiable?
2. Is it machine-readable and citable under an explicit license?
3. Does it stay within the currently authorized scope?
4. Does it avoid any judgment its gates have not yet authorized?
5. Would the record survive skeptical citation by a hostile expert?

## 10. Governing Principle

> Authority is not announced before the work; it accumulates through work that others can quote, verify, and correct. The reference becomes hard to bypass because it is honest, traceable, and machine-citable — not because it claims to be.
