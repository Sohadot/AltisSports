#!/usr/bin/env python3
"""Validate PUBLIC_ASSET_PROFILE.json against the live governed state.

The public asset profile is the source from which the public-facing dossier is
projected. Because that dossier is a public surface, the profile must never be
allowed to drift: if it claims "39 externally citable" while the registry says
otherwise, or "none dispatched" after invitations were sent, this gate fails
until the profile is corrected.

Checks:
  1. identifier total and per-kind counts match CITATION_REGISTRY_V0.1.json;
  2. externally-citable count matches the registry;
  3. atlas record count matches ATLAS_DESCRIPTIVE_V0.1.json;
  4. CITE-HOLD-ASR-001 is an open hold and every ASR clause is licensed
     CC-BY-4.0 and not externally citable;
  5. licensing scope (corpus / AS3 / ASR clause text) matches the registry and
     the dataset license;
  6. RW-001 review counts match ASR_001_INVITATION_DISPATCH_LOG_V0.1.json
     (authorized / dispatched / reviewers);
  7. every canonical resource path exists in the repository;
  8. core boundaries are present (the profile states what the asset is not).

Standard library only; exit 0 on pass, 1 on failure.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROFILE = "PUBLIC_ASSET_PROFILE.json"
REGISTRY = "CITATION_REGISTRY_V0.1.json"
ATLAS = "ATLAS_DESCRIPTIVE_V0.1.json"
DISPATCH = "ASR_001_INVITATION_DISPATCH_LOG_V0.1.json"
LICENSE = "DATASET_LICENSE.md"


def read_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def validate(errors):
    profile = read_json(PROFILE)
    registry = read_json(REGISTRY)
    atlas = read_json(ATLAS)
    dispatch = read_json(DISPATCH)

    ids = profile.get("identifiers", {})
    # (1) totals + per-kind
    if ids.get("total") != registry.get("identifier_count"):
        errors.append(f"identifiers.total {ids.get('total')} != registry {registry.get('identifier_count')}")
    if ids.get("by_kind") != registry.get("coverage"):
        errors.append(f"identifiers.by_kind {ids.get('by_kind')} != registry coverage {registry.get('coverage')}")
    # (2) externally citable
    citable = sum(1 for e in registry["identifiers"] if e.get("externally_citable"))
    if ids.get("externally_citable") != citable:
        errors.append(f"identifiers.externally_citable {ids.get('externally_citable')} != registry {citable}")

    # (3) atlas records
    if profile.get("atlas", {}).get("records") != atlas.get("record_count"):
        errors.append(f"atlas.records {profile.get('atlas',{}).get('records')} != atlas {atlas.get('record_count')}")

    # (4) CITE-HOLD-ASR-001 open + ASR held/licensed
    open_holds_text = " ".join(profile.get("governance", {}).get("open_holds", []))
    if "CITE-HOLD-ASR-001" not in open_holds_text:
        errors.append("profile does not record CITE-HOLD-ASR-001 as an open hold")
    reg_holds = {b["blocker_id"] for b in registry.get("license_blockers", []) if b.get("status") == "open"}
    if "CITE-HOLD-ASR-001" not in reg_holds:
        errors.append("registry does not carry an open CITE-HOLD-ASR-001 hold")
    asr = [e for e in registry["identifiers"] if e["kind"] == "asr_clause"]
    if any(e.get("externally_citable") for e in asr):
        errors.append("some ASR clause is externally_citable while held")
    if any(e.get("license") != "CC-BY-4.0" for e in asr):
        errors.append("some ASR clause is not licensed CC-BY-4.0")

    # (5) licensing scope
    lic = profile.get("licensing", {})
    for key in ("boundary_corpus", "as3", "asr_clause_text"):
        if lic.get(key) != "CC-BY-4.0":
            errors.append(f"licensing.{key} must be CC-BY-4.0 (got {lic.get(key)!r})")
    license_text = (ROOT / LICENSE).read_text(encoding="utf-8")
    if "CC BY 4.0" not in license_text or "ASR normative clause text" not in license_text:
        errors.append("DATASET_LICENSE.md does not explicitly license ASR clause text under CC BY 4.0")

    # (6) review counts vs dispatch log
    review = profile.get("review", {})
    entries = dispatch.get("entries", [])
    authorized = sum(1 for e in entries if e.get("authorization_status") == "authorized")
    dispatched = sum(1 for e in entries if e.get("dispatch_status") == "dispatched")
    reviewers = sum(1 for e in entries if e.get("reviewer_status") == "reviewer")
    if review.get("invitations_authorized") != authorized:
        errors.append(f"review.invitations_authorized {review.get('invitations_authorized')} != dispatch log {authorized}")
    if review.get("invitations_dispatched") != dispatched:
        errors.append(f"review.invitations_dispatched {review.get('invitations_dispatched')} != dispatch log {dispatched}")
    if review.get("reviewers") != reviewers:
        errors.append(f"review.reviewers {review.get('reviewers')} != dispatch log {reviewers}")

    # (6b) semantic / status guards — numeric counts alone must not be able to
    # drift from the stated review state or prose. Ground truth is the dispatch
    # log. The future post-dispatch state name is deliberately not invented here:
    # at the first real dispatch this fails and forces a governed state transition.
    PREPARED = "controlled_first_wave_prepared"
    state = review.get("state")
    ext_layer = next((l for l in profile.get("layers", []) if l.get("layer") == "External operator review"), None)
    if ext_layer is None:
        errors.append("profile is missing the 'External operator review' layer")
    elif ext_layer.get("state") != state:
        errors.append(f"External operator review layer state {ext_layer.get('state')!r} != review.state {state!r}")
    if dispatched == 0:
        if state != PREPARED:
            errors.append(f"nothing is dispatched but review.state is {state!r} (expected {PREPARED!r})")
    else:
        if state == PREPARED:
            errors.append(f"{dispatched} invitation(s) dispatched but review.state is still {PREPARED!r} — a governed state transition is required")
    prose = " ".join([str(review.get("note", "")), str((ext_layer or {}).get("detail", ""))]).lower()
    if dispatched > 0 and "none dispatched" in prose:
        errors.append("profile prose still says 'none dispatched' after dispatch")
    if reviewers > 0 and "no reviewers" in prose:
        errors.append("profile prose still says 'no reviewers' after acceptance")

    # (6c) post-dispatch governed state. Dispatch is not review, validation,
    # endorsement, or recognition. The next name after acceptance is not
    # invented here: reviewers > 0 while this state remains forces a later
    # governed transition.
    DISPATCHED_AWAITING = "controlled_first_wave_dispatched_awaiting_acceptance"
    if dispatched > 0 and reviewers == 0 and state != DISPATCHED_AWAITING:
        errors.append(
            f"{dispatched} invitation(s) dispatched and 0 reviewers but "
            f"review.state is {state!r} (expected {DISPATCHED_AWAITING!r})"
        )
    if reviewers > 0 and state == DISPATCHED_AWAITING:
        errors.append(
            f"{reviewers} reviewer(s) recorded but review.state is still "
            f"{DISPATCHED_AWAITING!r} — a governed state transition is required"
        )

    # (6d) frozen Zenodo publication is distinct from ASR-001
    pubs = profile.get("frozen_publications") or []
    foundation = next(
        (p for p in pubs if p.get("version_doi") == "10.5281/zenodo.22015549"),
        None,
    )
    if foundation is None:
        errors.append("profile must record the Zenodo v0.1 frozen publication (10.5281/zenodo.22015549)")
    else:
        if foundation.get("concept_doi") != "10.5281/zenodo.22015548":
            errors.append("frozen publication concept_doi must be 10.5281/zenodo.22015548")
        if foundation.get("kind") != "external_frozen_publication":
            errors.append("Zenodo record must be kind external_frozen_publication")
        if foundation.get("scope") != "conceptual_and_architectural_foundation":
            errors.append("Zenodo record scope must remain conceptual_and_architectural_foundation")
        if "ASR-001" not in (foundation.get("does_not_publish") or []):
            errors.append("frozen publication must explicitly not publish ASR-001")
        means = " ".join(foundation.get("does_not_mean") or [])
        for needle in ("CITE-HOLD-ASR-001 is lifted", "external validation", "adoption", "endorsement"):
            if needle not in means:
                errors.append(f"frozen publication must state that it does not mean {needle!r}")
        if foundation.get("version") != "0.1":
            errors.append("recorded frozen publication version must be 0.1 until a new Zenodo version exists")
    zenodo_layer = next(
        (l for l in profile.get("layers", []) if l.get("state") == "external_frozen_publication"),
        None,
    )
    if zenodo_layer is None:
        errors.append("profile layers must include the Zenodo frozen publication as a distinct layer")
    elif "does not publish" not in (zenodo_layer.get("detail") or "").lower():
        errors.append("Zenodo layer must state that it does not publish ASR-001")

    # (7) canonical resources exist
    for name, path in profile.get("canonical_resources", {}).items():
        if path.startswith("http"):
            continue
        if not (ROOT / path).exists():
            errors.append(f"canonical_resource {name} -> missing file {path}")

    # (8) boundaries present
    if not profile.get("not"):
        errors.append("profile must state what the asset is not")
    if "unpublished" not in profile.get("asset", {}).get("current_state", "").lower():
        errors.append("profile current_state must record ASR-001 as an unpublished Working Draft")


def main():
    errors = []
    validate(errors)
    if errors:
        print("FAIL: public asset profile is stale or inconsistent")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("PASS: public asset profile consistent with live state "
          "(identifiers, atlas, CITE-HOLD-ASR-001, licensing, RW-001 dispatch, canonical resources).")


if __name__ == "__main__":
    main()
