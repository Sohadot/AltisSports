# Reviewer Privacy Boundary

**Status:** Ratified governance policy
**Applies to:** ASR review waves (RW-001 onward)

## 1. Rule

> Public governance records roles, slots, states, and process. Candidate
> identity and correspondence remain private until explicit consent to public
> attribution.

The public repository records the **process**: reviewer classes (RC-*), slots
(RWS-*), coverage rules, methodology, an anonymous invitation template,
acceptance and conflict policy, aggregate counts, and per-slot states. It does
**not** record who a candidate is before that person has consented to public
attribution.

## 2. Why

Naming a real person in a public repository as a candidate for our review is
information we create. Even when the person's role and affiliation are public
facts, linking them to an unaccepted review invitation can imply a relationship
that does not yet exist — and a candidate should not discover that their name
was published as a reviewer candidate before they had heard of the project.

## 3. Two Distinct Consents

Participation and publication are logically separate. We require **two**
consents, and one never implies the other:

1. **Review participation consent** — written agreement to review under the
   stated boundaries. This transitions a slot to `reviewer`.
2. **Public attribution consent** — separate, explicit agreement to have one's
   name published in the public record.

A person may therefore be a `reviewer` in the public record while still
identified only by slot (e.g. `RWS-01`), if they have given participation
consent but not public-attribution consent. Absent public-attribution consent,
the public record shows the slot, class, and state — never the name.

## 4. Public vs Private

| Public governance record | Private operations record |
| --- | --- |
| RC-* classes and selection criteria | Candidate identity (name, affiliation) |
| RWS-* slots and their states | Contact channel and any contact data |
| Coverage / classification rules | Personalized invitation letters ("Dear …") |
| Anonymous invitation template | Detailed dispatch log tied to a person |
| Acceptance / conflict / intake policy | Replies and personal correspondence |
| Aggregate counts (authorized / dispatched / reviewers) | Slot ↔ identity crosswalk |

Private operations are kept outside the public repository (a private repository
or an encrypted local record). The public code and validators operate on slots
and states only and must never require identity to function.

## 5. Contact Data

Personal contact addresses (email, phone) are never stored in the public
repository, in any form, at any stage.

## 6. Historical Note

Candidate names appeared in the public repository history during Sprint 14,
before this boundary was ratified. Removing them from the current tree does not
remove them from past commits. History is left unchanged for now; a deliberate
history-purge decision is reopened only if a named person requests it, if a
legal or reputational sensitivity arises, or before AltisSports reaches a level
of external distribution that gives the old history material exposure.

## 7. Consequence for Records

- The public dispatch log and cohort roster carry slots and states, not names.
- Public invitations are an anonymous template; personalized letters are private.
- Decision records state that assignments were authorized against slots;
  identities are maintained privately under this boundary.
