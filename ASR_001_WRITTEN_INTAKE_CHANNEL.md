# ASR-001 Written Intake Channel

**Version:** 0.1  
**Channel path:** `review-intake/`  
**Status:** Prepared — external submission closed  
**Wave:** RW-001

## 1. Purpose

Provide a bounded asynchronous written channel for future operator-review comments without opening a public forum.

## 2. Current State

| Property | Value |
| --- | --- |
| Channel prepared | yes |
| External submission accepted | no |
| Public comment channel | no |
| Invitation-linked intake | not yet enabled |

External comments are rejected until:

1. named assignees exist for the relevant slots;
2. the owner authorizes invitation sending;
3. at least one invitation has been sent;
4. the activation record dates for opening are filled.

## 3. Accepted Artifact Forms After Enablement

- markdown comment using `ASR_001_CLAUSE_COMMENT_TEMPLATE.md`;
- JSON instance validating against `ASR_001_REVIEW_COMMENT_SCHEMA_V0.1.json`;
- conflict/evidence declaration paired to the reviewer slot.

## 4. Identifier Scheme

```text
ORC-YYYY-NNN
```

Assigned only after enablement, under `ASR_001_ISSUE_INTAKE_PROCEDURE.md`.

## 5. Prohibited Uses

- social-media threads as the system of record;
- anonymous public issue dumps without conflict declaration;
- marketing of comments as endorsement;
- using intake to collect sales leads or vendor rankings.

## 6. Directory Marker

The `review-intake/README.md` file states the closed state. Presence of the directory does not authorize comment collection.
