# Engineering retrospective

Copy this template into the repository that owns the work. Keep it proportional:
a short case may fit on one page. Use it for a failed external submission,
invalid signed artifact, escaped defect, data or recovery near miss, or repeated
costly failure. A routine test failure fixed before review, a typo, or an
owner-directed visual preference change usually needs only its normal PR record.
Do not infer customer impact from a provider rejection or source-only change.

## Snapshot

- Incident title, date and time zone:
- Owning product and accountable follow-up owner:
- Affected artifact, exact revision and channel:
- Observed customer availability and acquisition, with evidence date:
- Evidence index (links or hashes in the owning private record):
- Current status and next verification:

## What happened

| Time | Observed event | Evidence | Decision or response |
| --- | --- | --- | --- |
| | | | |

State the expected behavior, observed behavior, how the issue was found, and
the last known good state. Keep source, built artifact, provider acceptance,
deployment, and public acquisition as separate facts.

## Impact, containment and recovery

- Verified user, data, schedule or channel impact; say `none observed` only
  with its evidence and observation window:
- What was held or rolled back, and who controlled it:
- Recovery steps and proof that they worked:
- Safeguards that worked or preserved progress:
- Remaining uncertainty or checks:

## Causes and detection

| Finding | Evidence and observation date | Confidence | Detection gap or next discriminating check |
| --- | --- | --- | --- |
| Verified cause | | Verified / bounded | |
| Contributing condition | | Verified / bounded | |
| Hypothesis or unknown | | Unconfirmed | |

Explain why the earlier checks did not catch the failure. A passed test proves
only the state and inputs it actually covered. Separate a tool or process
failure from normal owner-directed iteration. Name system conditions, not blame.

For a failed or partial evidence check, record the attempted operation and its
retrieval result separately from the product outcome, with the exact candidate
and environment. An inaccessible source does not prove absence; a timeout does
not prove that a mutation had no effect. Preserve the last verified state and
its date until a new observation supersedes it.

If using five whys, identify the evidence or inference supporting each causal
link. Stop where evidence stops, even before five levels; retain competing
explanations and the next check rather than forcing a single root cause. A
recovery that works does not by itself prove why the failure occurred. Use the
[synthetic evidence-recovery cases](../evals/engineering/evidence-recovery/README.md)
when evaluating changes to this method; they do not require an incident report
for every ordinary lookup or test failure.

Choose the smallest comparison that separates the competing explanations:
change one suspected factor while matching the candidate, runtime, profile and
other relevant conditions. Before running, name the expected distinguishing
observations, evidence streams and stop condition. Start with one execution per
condition under the existing run cap; inspect those results before expanding.
Correlate the initiating request, current authoritative state, durable history
and asynchronous updates when applicable. Keep existing assertions, acceptance
criteria and trust checks intact. An inconclusive comparison leaves the cause
unresolved; it does not justify retries or looser checks until something passes.

For an unresolved consequential operation, record its correlation privately,
the authoritative state check and the contract that permits retry or clearing a
hold. Restart, elapsed time and an empty history are not cancellation receipts.
Preserve independent work that can proceed within the existing authorization.

## Prevention and closure

| Action | Owner | Due or trigger | Verification evidence | State |
| --- | --- | --- | --- | --- |
| | | | | Proposed / in progress / verified |

Close an action only after its prevention check has run on the intended
artifact or workflow. Record any deferred device, provider, or customer
verification as open. Recheck the handoff and release record so a pending stage
does not erase an achieved milestone.

## Reusable lesson

Write one or two general rules that a different project could apply. If
contributing them to a public toolkit, use fictional cases and a separate
reviewed PR. Do not copy private screenshots, account identifiers, receipts,
customer data, or confidential repository links into the public version.
