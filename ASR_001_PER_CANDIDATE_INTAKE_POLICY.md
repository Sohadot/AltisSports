# ASR-001 Per-Candidate Intake Enablement Policy

**Version:** 0.1  
**Wave:** RW-001  
**Global `review-intake/` status:** CLOSED

## Rule

`review-intake/` must not be opened as a global or anonymous channel.

A candidate-specific intake enablement may occur only after:

1. the candidate's invitation package is marked `dispatched` in the dispatch log;
2. the candidate remains within the authorized first-wave set;
3. no Public Review channel is created;
4. conflict declaration has been requested.

## Reviewer Transition

| State | Label |
| --- | --- |
| Before invitation dispatch | `named_candidate_assignee` / `selected_not_contacted` |
| After dispatch, before acceptance | `named_candidate_assignee` / `invited_awaiting_acceptance` |
| After written acceptance | `reviewer` |
| After first accepted comment | eligible for `ORC-YYYY-NNN` issuance |

## Explicit Non-Transitions

- Dispatch alone does not create reviewer status.
- Repository visibility does not enable intake.
- Reserve-slot candidates have no intake path in Wave RW-001 first wave.
