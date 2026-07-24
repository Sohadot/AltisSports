# ASR-001 Named Candidate Assignment and Invitation-Release Gate

**Version:** 1.0  
**Sprint:** Sprint 14

## Gate Checks

| ID | Check |
| --- | --- |
| N01 | DEC-016 and Wave RW-001 apparatus exist |
| N02 | Owner decision text is recorded and matches the four authorized names |
| N03 | Roster v0.2 assigns exactly four first-wave named candidate assignees |
| N04 | Those four use role_label `named_candidate_assignee` |
| N05 | Those four keep candidate_status `selected_not_contacted` |
| N06 | Reserve slots RWS-02/04/06 remain `not_authorized` for invitation |
| N07 | Required coverage groups are satisfied by RC-01, RC-03, RC-05, RC-07 |
| N08 | Four invitation drafts exist and contain non-endorsement language |
| N09 | No email address or phone number appears in Sprint 14 artifacts |
| N10 | Dispatch log authorizes four packages and records no fake send timestamps |
| N11 | Global review-intake remains CLOSED |
| N12 | Per-candidate intake policy forbids ORC before acceptance+comment |
| N13 | No Public Review, certification, scoring, or adoption claim is introduced |
| N14 | DEC-017 is appendable and unique |

## Allowed Decision

```text
PASS — NAMED CANDIDATE ASSIGNMENT AND CONTROLLED INVITATION
RELEASE AUTHORIZED FOR RWS-01, RWS-03, RWS-05, RWS-07;
PRIVATE DISPATCH REMAINS OWNER-EXECUTED
```
