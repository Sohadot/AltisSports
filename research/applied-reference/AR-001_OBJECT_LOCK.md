# AR-001 — Object Lock

**Asset:** AltisSports  
**Case:** Applied Reference 001 — Evidence Lock  
**Corpus identity:** BC-015 (not revised by this file)  
**Status:** Internal research — not a public page, not a verdict, not a standard  
**Access date:** 2026-08-27  
**Depends on:** `boundary-cases-001-020.v0.3.json`, `AS3_STACK.md`, `CATEGORY_THESIS.md`, `SOURCE_AND_CLAIM_POLICY.md`

This file freezes the classified object for AR-001. It does not overwrite BC-015. It does not assign a score, grade, maturity level, certification, or “is / is not a sport” verdict.

---

## 1. Frozen object

**Exact frozen object:**

> World Taekwondo-governed Virtual Taekwondo contest configuration, as specified by the *WT Virtual Taekwondo Rules and Regulations*, Version 4.0 (dated 11 April 2026), operating as a co-located multi-station Field of Play under WT promotion or recognition, using the official WT Virtual Taekwondo technology-provider stack.

**Short label:** WT Virtual Taekwondo contest configuration (Rules v4.0 / co-located FOP).

**Primary object class:** contest (`CATEGORY_THESIS.md` §3.3 candidate relation remains a C5 hypothesis inherited from BC-015; AR-001 does not re-issue it).

**Performance window:** from Game Master start of a round (`Shi-jak`) until knockout, time expiry, disqualification, or authorised stop (`Keu-man` / timeout / injury / disconnection procedure).

---

## 2. Why this object, and not a broader one

The candidate formulation in the research brief was:

> World Taekwondo Virtual Taekwondo competition configuration governed by the WT Virtual Taekwondo Rules and Regulations.

That formulation is accepted, then narrowed. Without the following locks, claims slide between product, event, format, and organisation.

| Lock | Decision | Basis |
| --- | --- | --- |
| Rulebook edition | **Version 4.0, 11 April 2026** | VTKD Rule Book Archive lists this as the current edition; the WT-hosted PDF is Version 4.0 and records April 11, 2026 in the version table. |
| May 30, 2025 edition | **Superseded** | That file is Version 3.0. It remains inspectable as historical. It is not the current governing text. |
| Later than April 2026 | **Not found** | No public WT or VTKD rulebook dated after 11 April 2026 was located on 2026-08-27. |
| Event configuration | **Not locked to one named event** | Singapore 2024, Olympic Esports Series 2023, Roma Open 2026, Chuncheon Open 2026, and announced Asian Games 2026 are deployment evidence. They are not the classified object. |
| Technology configuration | **Official provider stack, versioned separately from the rules** | WT names Refract Technologies / Virtual TKD Pte. Ltd. as official VTKD technology provider. AXIS nodes, compatible PICO headsets, Game Master PC, and VTKD software are constitutive of the examined contest. Software version is a moving implementation layer (latest examined: VTKD v1.3.0, 21 August 2026). |
| Co-located vs distributed | **Co-located multi-station FOP only** | Rules, manuals, and examined championships describe two physical mats at one venue. Geographically distributed synchronous competition remains `not_evidenced`. |
| Hardware/software version | **Must be named when a claim depends on it** | Rules v4.0 and VTKD v1.3.0 are not the same artefact. Several scoring and calibration behaviours in v1.3.0 are not written in v4.0. |
| Competition rules actually evidenced | **Articles 1–6 of Rules v4.0, plus operator manuals where they implement those articles** | Practice mode, arcade mode, and marketing “level playing field” claims are outside the frozen object unless independently documented as contest rules. |

---

## 3. Object distinctions (no silent movement)

AS³ may inspect multiple object types (`AS3_STACK.md` §2). AR-001 permits inspection **only** of the frozen contest configuration. Adjacent objects may be mentioned as context. They may not inherit contest findings.

| Object type | What it is in this case | In scope for AR-001? |
| --- | --- | --- |
| **Activity** | Practising or playing Virtual Taekwondo / VTKD, including training, practice mode, and dojang use | No. Activity evidence may describe the interface; it does not establish contest integrity. |
| **Competition format** | Best-of-3, 60-second rounds, Health Bar, stun, break, age/gender categories, single elimination as written in Rules v4.0 | Yes, as the rule-bearing format of the frozen contest. |
| **Technical system** | AXIS + PICO + VTKD Game Master/VR clients + dedicated local network | Yes, only insofar as it is the official stack required to run a WT-recognised match. Product capability outside contest use is out of scope. |
| **Event / deployment** | A named championship or open (Singapore 2024, Chuncheon 2026, etc.) | No as the classified object. Yes as historical or current evidence that the contest configuration has been staged co-located. |
| **Governing organisation** | World Taekwondo; CUs/MNAs; official technology provider | No as the classified object. Yes as L10 authority and commercial-relation context. |

**Prohibited slides**

- “Virtual Taekwondo” as a VR product → contest.
- “Inclusive / no weight class / strength does not matter” marketing → evidenced comparability.
- Internet connection required for a court → geographically distributed opponents.
- Game-room join architecture → remote synchronous arena.
- AXIS as a general mocap product → WT contest tracking configuration.
- Immersion or VR headset presence → Spatial Athletic System membership.
- A future home-play aim → current contest topology.
- VTKD software patch notes → WT rule text, unless the rules cite the patch.

---

## 4. Existing BC-015 record (preserved, not improved)

The following is the current governed BC-015 state as of corpus v0.3. AR-001 may cite it. AR-001 may not silently rewrite it.

**Sources of this excerpt:** `boundary-cases-001-020.v0.3.json`; identical BC-015 body in `boundary-cases-011-020.reviewed.v0.3.json`; descriptive Atlas record `ATL-D-015` in `ATLAS_DESCRIPTIVE_V0.1.json`.

| Field | Existing value |
| --- | --- |
| `case_id` | BC-015 |
| `activity` | World Taekwondo Virtual Taekwondo competition |
| `activity_aliases` | Remote motion-tracked martial competition; Virtual Taekwondo |
| `classified_object.primary` | contest |
| `classified_object.secondary` | spatial_athletic_contest; event; organization |
| `classified_object.notes` | The object is the World Taekwondo-governed Virtual Taekwondo contest configuration. The preselected remote-distributed hypothesis is retained but marked unresolved because the cited championships were co-located. |
| `institutional_recognition` | international_federation_governed; C1 |
| `performance_agency` | supported; C4; live_performance; human_skill_causally_necessary true |
| `performance_interface` | supported; C4; tracked_xr_input |
| `embodied_performance` | supported; C4 |
| `arena` | supported; C2; remote distributed arena equivalence remains unknown |
| `rules` | supported; C1 |
| `tracking` | supported; C3 |
| `measurement` | supported; C2 |
| `comparability` | partial; C4 |
| `officiation` | supported; C2 |
| `distributed_arena_relation.status` | **not_evidenced** |
| `distributed_arena_relation.topology` | co_located_multi_station |
| `provisional_finding` | sport_like_contest / spatial_athletic_contest; C5; co-located contest supported; remote distributed arena not established |
| `confidence` | medium |
| `revision` | 0.3; Sprint 6 targeted relations retained and rechecked during Sprint 7 |
| `access_date` | 2026-07-24 |
| `review_status` | human_reviewed_v0_3 |

**BC-015 evidence then cited (access 2026-07-24):** VTKD compete page; WT Olympic Esports Series finals (historical); First WT Virtual Championships (historical); VTKD rulebook archive April 2026; VTKD User Manual 1.2.34; VTKD Patch Notes (then dated 2026-01-13).

**Sprint 6 decision retained in `TARGETED_BOUNDARY_DEEPENING.md`:** BC-015 remains a supported co-located Spatial Athletic Contest hypothesis. The remote-distributed hypothesis is closed as **not evidenced in the examined public configuration**, not as impossible.

AR-001 inherits that remote finding as a starting constraint. It does not reopen it by treating network rooms, global events, or internet-connected headsets as distributed-arena evidence.

---

## 5. Rulebook edition verification

| Edition | Version on title page | Date in version table | Host observed 2026-08-27 | Temporal status for AR-001 |
| --- | --- | --- | --- | --- |
| WT Virtual Taekwondo Rules and Regulations | 1.0 | 13 June 2024 (in-effect line on v1 PDF) | VTKD archive / Sanity CDN | historical |
| same title | 2.0 | 30 September 2024 | VTKD archive / Sanity CDN | historical |
| same title | 3.0 | 30 May 2025 | WT `att_file` PDF; WT `upload/files/2025/12/` copy | superseded |
| same title | **4.0** | **11 April 2026** | WT `upload/files/2026/03/` PDF linked from VTKD archive as current | **current governing text** |

No public Version 5.0 or later 2026 rulebook was found.

**v4.0 documented delta versus v3.0 (material, not exhaustive):**

1. Article 3.1: two possible start-position options per mat; facing constraints (not back-to-back; backs not to main spectator area).
2. Article 3.2: minimum two displays; operator/coach display and spectator display; displays ≥ 1.5 m from mats.
3. Article 6 opening: after one warning, the next offence may lose **the round**, and the opponent is declared winner **of the round** (v3.0 wording declared winner of **the match**).

Scoring, stun, break, disconnection, officials, and calibration-as-procedure are largely continuous from v3.0 to v4.0 in the public text.

---

## 6. Implementation layer (not the frozen object, but a required dependency)

The frozen object is the **rules-governed contest configuration**. The VTKD software is how that contest is currently executed. They must stay distinct.

| Artefact | Latest examined | Relation to frozen object |
| --- | --- | --- |
| WT Rules v4.0 | 11 April 2026 | Governs WT-promoted/recognised competitions |
| VTKD User Manual 1.3.0 | 21 August 2026 | Operator implementation |
| VTKD Game Mechanics 1.3.0 | 21 August 2026 | Provider description of in-game logic |
| VTKD Patch Notes v1.3.0 | 21 August 2026 | Declared software behaviour change after Rules v4.0 |
| VTKD User Manual 1.2.34 | 13 January 2026 | Superseded for current software; retained because BC-015 cited it and because it documents Surface Calibration later withdrawn |

Known divergences that **must not be collapsed** are recorded in `AR-001_GAPS_AND_FALSIFIERS.md` and L4/L7 of the evidence matrix. They include stun activation, Surface Calibration withdrawal, groin-kick damage exclusion, GM-Timeout, and optional Boundary Damage.

---

## 7. Topology lock

**Evidenced topology:** co-located multi-station Field of Play.

Documented physical arrangement:

- two 4 m × 4 m mats, ≥ 2 m apart;
- start marks 1 m from mat centre;
- safety area ≥ 1 mat beyond play area;
- Referee, Game Master, two Technical Operators at one venue;
- dedicated local router per court; VR headsets on the same Wi-Fi as the Game Master;
- current maximum of two courts/FOP in the site-assessment and user-manual materials.

**Not evidenced as the frozen object:**

- opponents in different cities or venues sharing one live match;
- public latency budget for WAN opponents;
- cross-site calibration equivalence;
- remote officiation without a shared physical FOP.

Provider text that home play is an aim “down the line” is a C6/C3 future claim. It does not alter the lock.

---

## 8. What AR-001 is allowed to conclude later

After this lock, later AR-001 writing may:

- inspect the ten AS³ layers against evidence;
- separate documented fact, attributed claim, and Altis interpretation;
- state gaps and falsifiers;
- recommend publication readiness.

Later AR-001 writing may **not**:

- score the system;
- certify it;
- declare Spatial Athletic Contest membership as a new verdict (BC-015’s C5 finding stays attributed to the corpus);
- treat VTKD marketing copy as independent fact;
- treat the May 2025 rulebook as current;
- treat remote distributed competition as demonstrated.

---

## 9. Relation to BC-015 aliases

BC-015 retains the alias “Remote motion-tracked martial competition”. That alias records the **preselected hypothesis**, not an evidenced topology. AR-001 uses the alias only when discussing that unresolved hypothesis. The frozen object name does not include “remote”.
