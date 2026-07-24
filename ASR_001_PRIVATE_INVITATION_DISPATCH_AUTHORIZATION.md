# ASR-001 Private Invitation Dispatch Authorization

**Decision:** **AUTHORIZED FOR OWNER-PRIVATE DISPATCH OF FOUR FIRST-WAVE INVITATIONS ONLY**  
**Execution actor:** Owner private written channel  
**Repository automation send:** not performed

## Authorized packages

- `INV-RW001-RWS-01`
- `INV-RW001-RWS-03`
- `INV-RW001-RWS-05`
- `INV-RW001-RWS-07`

## After each private send, the owner should

1. set that entry's `dispatch_status` to `dispatched` and fill `dispatched_at`;
2. keep contact secrets out of the public repository;
3. enable only that candidate's intake path if needed;
4. leave reviewer_status as `not_reviewer` until written acceptance;
5. leave reserve slots untouched.

## Suggested next governed move

**Sprint 15 — Invitation Dispatch Recording, Acceptance Intake, and First Comment Window**

Begins after at least one private invitation has actually been sent and recorded.
