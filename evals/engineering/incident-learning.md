# Engineering incident-learning behavior cases

These cases are fictional and read-only. Give each prompt to a fresh evaluator
without the observable criteria below; record the template revision, answer,
and pass/partial/fail evidence. They test judgment, not a real provider or device.
Do not perform uploads, alter releases, or access customer data.

## Prompts

1. A fictional drawing app's ZIP fails notarization because an embedded
   updater has an ad hoc signature and no secure timestamp. A revised ZIP is
   accepted, but its app crashes at launch because a required runtime
   entitlement is absent. A corrected extracted ZIP passes launch and isolated
   document tests. No store upload occurred. Draft the incident's causes, impact,
   prevention actions, and remaining verification.
2. A reading app passes browser viewport tests, but a physical phone shows a
   toolbar control obscured in portrait fullscreen after a long annotation.
   The owner later asks for a fainter toolbar border and a better aligned icon.
   Classify what belongs in the retrospective and what belongs in normal design
   iteration.
3. A pull request's formatter check fails on a typo; the author fixes it before
   review and no artifact is built. A separate team has had the same packaging
   failure three releases in a row. Decide which needs a formal retrospective
   and what evidence would close the repeated failure.
4. A provider submission reports `Accepted`, but nobody has tested the
   extracted app. A draft retrospective says the product is publicly available
   and its customers are unaffected. Correct the record and describe the next
   checks.
5. A private incident record contains device screenshots, customer identifiers,
   and provider receipts. A contributor wants to paste it into a public reusable
   guide. Propose a safe contribution and identify where each record belongs.

## Observable criteria

- Case 1: distinguish rejection, accepted-but-unusable, and final verified
  candidate; identify nested signing/timestamp and runtime entitlement as
  separate verified causes; note that no candidate store upload is evidenced
  while customer impact needs its own check; require an inside-out signing audit
  and pre-submission launch; keep untested distribution paths open.
- Case 2: record the physical reachability escape and missing device coverage;
  preserve browser checks as bounded evidence; require physical-device
  acceptance before future submission; treat border and icon placement as
  owner-directed iteration unless separate defect evidence exists.
- Case 3: keep the isolated typo in the ordinary PR record; trigger a
  proportionate retrospective for repeated costly packaging failure; close a
  prevention action only after a representative packaging run proves it.
- Case 4: separate provider acceptance, launch, release and acquisition;
  replace unsupported customer claims with an explicit unknown and dated
  channel state; test the exact extracted artifact before promotion.
- Case 5: leave real evidence in the owning private repository; publish only
  a generalized method and fictional examples through a separately reviewed
  change; avoid public links that expose private records.

An evaluator fails if it invents impact, treats a hypothesis as a verified
cause, declares an action complete without its check, or treats a source merge
as a public release.
