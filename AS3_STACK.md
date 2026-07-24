# AS³ — Altis Spatial Sport Stack

**Version:** 0.1  
**Status:** Provisional Reference Architecture — Not a Standard

## 1. Purpose

AS³ locates where a Spatial Sport system enables performance, carries rules, produces measurements, and can lose integrity.

It is not a maturity scale. Layers are not levels, and more layers do not imply a better system.

## 2. Layers

### L1 — Human Agency
Who or what performs, and how human skill materially influences the result.

### L2 — Embodied Interface
How human action enters the system through controllers, tracking, resistance, vehicles, assistive devices, or other interfaces.

### L3 — Arena and Spatial State
How physical, computational, and unified spaces define boundaries, zones, hazards, and shared state.

### L4 — Constraint and Rule Execution
Where rules reside and how textual, human, sensor, geometric, or code-based constraints become operational.

### L5 — Sensing, Tracking, and State Estimation
What is directly measured, what is inferred, and how accuracy, latency, drift, smoothing, and loss are handled.

### L6 — Measurement and Comparability
How observations become metrics and under which calibration, device, space, software, and participant conditions comparisons remain valid.

### L7 — Officiation and Outcome
How rule-relevant events become decisions, penalties, rankings, and results, including appeal and correction.

### L8 — Presence and Participation
How participants, coaches, officials, and spectators perceive, communicate, and affect the system.

### L9 — Safety, Accessibility, and Human Limits
How collision, fatigue, cybersickness, exclusion, body variation, cognitive demand, and responsibility are governed.

### L10 — Governance, Evidence, and Change
Who controls the system, which claims are evidenced, what changes between versions, and how corrections and conflicts are handled.

## 3. Cross-Layer Conditions

Integrity, comparability, accessibility, security, and privacy cross multiple layers and must not be reduced to one local check.

## 4. Permitted Outputs

AS³ may later support system profiles, evidence checklists, failure-mode maps, vendor comparison fields, readiness assessments, ASR mapping, and atlas schemas.

No total score is authorized by this version.

## 5. Failure Principle

> human action → interface → arena → rule → sensing → measurement → decision → participation → safety → governance

A broken link can invalidate conclusions produced above it.

## 6. Revision Trigger

Revise AS³ when boundary cases expose a missing function, two layers cannot be operationally distinguished, a layer cannot be tied to evidence, real systems violate the assumed structure, or the architecture encourages misleading scoring.
