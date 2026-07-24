# ASR-001 Issue Intake Procedure

**Version:** 0.1  
**Applies to:** Wave RW-001 after invitation-linked enablement  
**Current enablement:** closed

## 1. Relationship to Disposition

This procedure governs **how comments enter the system**.  
`ASR_001_COMMENT_DISPOSITION_PROCEDURE.md` governs **how accepted comments are triaged and decided**.

## 2. Pre-Enablement Rule

While external intake is closed:

- no `ORC-YYYY-NNN` identifiers are issued to external parties;
- unsolicited messages are not treated as review comments;
- repository issues or pull requests are not an authorized ASR-001 review channel unless the owner later redesignates them in writing.

## 3. Enablement Preconditions

Intake may be enabled only when all are true:

1. Wave RW-001 activation record exists;
2. at least one slot has a named assignee;
3. owner has authorized invitation sending;
4. invitation status for that assignee is no longer `not_sent`;
5. written channel remains non-public;
6. conflict declaration has been requested.

## 4. Intake Steps After Enablement

1. Receive written comment and declaration.
2. Assign `ORC-YYYY-NNN`.
3. Preserve original text.
4. Link reviewer ID, class, conflict declaration ID, and attribution preference.
5. Run completeness check from the disposition procedure.
6. Place the record under change control without silent deletion.

## 5. Rejection Without Destruction

Out-of-channel or premature submissions are logged as non-accepted correspondence when material, then closed without entering clause disposition.

## 6. Boundary

Issue intake does not create Public Review, publication, certification, or adoption.
