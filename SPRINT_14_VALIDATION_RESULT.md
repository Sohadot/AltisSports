# Sprint 14 Validation Result

**Asset:** AltisSports  
**Sprint:** Sprint 14 — Named Candidate Assignment and Controlled Invitation Release  
**Date:** 2026-07-24  
**Decision:** **PASS**

## Validation

- owner decision authorizes exactly four first-wave candidates;
- role label before acceptance is `named_candidate_assignee`;
- candidate_status remains `selected_not_contacted` until private dispatch;
- reserve slots remain invitation-unauthorized;
- required coverage groups are satisfied;
- invitation drafts exist without public contact secrets;
- dispatch log authorizes four packages and records no fake send;
- global review-intake remains CLOSED;
- ORC issuance remains gated on acceptance and later comment;
- no Public Review, certification, scoring, or adoption claim is created;
- DEC-017 was appended.

## SHA-256

**Historical record (2026-07-24).** These are the Sprint-14 hashes as recorded at the time. Under `REVIEWER_PRIVACY_BOUNDARY.md` the people-layer files (candidate identity evidence and the personalized invitation letters) were subsequently moved to a private record; their rows are removed here and their public content no longer exists. Git history before that revision is unchanged.

| File | SHA-256 (as of 2026-07-24) |
| --- | --- |
| `ASR_001_OWNER_DECISION_SPRINT_14.md` | `f554509c5cad96a926be6c921b44eb1c3541ac0829d3c29ddb556e26d12302bb` |
| `ASR_001_REVIEWER_COHORT_ROSTER_V0.2.json` | `0463f05695348869e8bb252e26631e6237e113c8269276c8962811e46e081c74` |
| `ASR_001_CONTROLLED_INVITATION_PACKAGE.md` | `f9d266ee5c314586963c9215c95252fe55f1454c66daf9633ed78cf8153c0432` |
| `ASR_001_INVITATION_DISPATCH_LOG_V0.1.json` | `c173f5f040e217b06b4e9e2436b7d04488fcf27f08bcf0ef57bcfa38c5e509a8` |
| `ASR_001_PER_CANDIDATE_INTAKE_POLICY.md` | `768d0baf0bb797002d55abde0c3e3633f800d8fb1ddbe58c2cf3c45f5323928b` |
| `ASR_001_NAMED_ASSIGNMENT_GATE.md` | `c2ec636e7f4d03a62390fa0ce07a7fd59915e52249ff9e672690a81460325fdd` |
| `ASR_001_REVIEW_ACTIVATION_RECORD_RW001_S14_SUPPLEMENT.md` | `7a54d552c0ccc43dfb98a7dd835dc6244d18f4e602b449b606b831ca4653e0cb` |

_People-layer files (moved to the private record under the privacy boundary): candidate identity evidence and `invitations/INV-RW001-RWS-01/03/05/07.md`._
