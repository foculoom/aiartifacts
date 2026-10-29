---
name: release-evidence
description: Prepare and verify an authorized static-site release using repository deployment rules, exact artifact hashes, and live readback. Use for release handoffs and publication verification, not automatic credential setup or general feature work.
---

# Release evidence

Treat source merge, artifact preparation, upload, and live verification as separate states. Read the owning repository's deployment rules and current release evidence first. Record source commit, reviewed artifact, intended account/project, audience and authorization. A skill does not supply deployment permission.

If the owning project requires production-experience acceptance, read its
decision, reviewer scope, evidence and accepted deviations for this exact payload.
Hold publication when a required decision is missing, unverified or requests
rework. Engineering checks, asset hashes and a narrow "no findings" review do
not replace that decision. Do not infer a portfolio policy, add a new gate to an
unrelated small task, or treat this static-release workflow as native certification.

## Reuse existing access and tooling

Prefer the user's specified browser and existing signed-in session when it can complete the release. A logged-out CLI is not evidence that the service is inaccessible. Do not create broad OAuth grants or credentials merely to avoid an available dashboard. Do not extract browser cookies or tokens. If an action is blocked, identify the exact blocker; do not repeatedly ask for unrelated authentication.

Use existing repository build, stamp, manifest and verification scripts before creating replacements. Batch safe read-only checks. Keep credentials, screenshots of account settings, personal paths, and raw provider responses out of public artifacts. Store sanitized evidence with the owning project.

Follow the source index or search for records before guessing paths. A 404 or
inaccessible dashboard describes that access attempt, not product availability.
If a response is truncated, read the relevant bounded section before using it.
In progress updates as well as final handoffs, retain the observation date,
candidate, environment and stage. Report unavailable fresh evidence alongside
the last verified state; distinguish failed, untested, indeterminate and pending
review. Do not promote a probable explanation into a verified cause.

When release diagnostics conflict, isolate one suspected factor with the other
candidate/environment conditions matched. Declare the distinguishing evidence
and stop condition first; use one execution per condition within the existing
cap before deciding whether more work is justified. Correlate requests, current
provider state, operation history and asynchronous updates as applicable. Keep
acceptance and trust checks intact; an inconclusive result remains unresolved.

## Parallel preparation

When multiple agents contribute to a release, read
[parallel-release.md](references/parallel-release.md) before accepting their
handoffs. Preparation and independent review can overlap; the final production
window has one owner, from fresh history through live verification.

## Prepare once, publish once

Check complete deployment history and unsettled operations before choosing any history-derived release label. Use provider completion timestamps and the project's timezone. Refresh after a pause, approval handoff, failed upload or unknown result; do not reuse stale history just because a ZIP exists. Rebuild if intervening releases invalidate the label. Preserve one deployment owner through upload and verification.

Prepare only the allowlisted site payload, excluding repository metadata, private briefs and logs. Verify ZIP paths and hashes against the candidate manifest. Select that exact archive in the dashboard, inspect the destination and environment, and confirm the final file list. An upload is not proof of successful publication. On timeout or stale dashboard state, inspect deployment history before retrying; avoid duplicate releases.

Correlate an ambiguous upload with its operation ID, artifact and destination,
using the provider's recorded state and completion time. An empty or failed
history read cannot prove the operation did not happen. If its outcome remains
unresolved, hold that retry and continue independent authorized preparation.
Once completion is established, verify the delivered result instead of uploading
again. Keep the existing authorization separate from evidence of completion;
an evidence gap alone does not require the owner to repeat an unchanged decision.

Create an archive at a fresh path. Updating an existing ZIP can retain old files that were not named in the new command; an integrity check such as `unzip -t` will still pass. Inspect the archive itself and require its exact entry set and file hashes to match the reviewed manifest before upload. A clean staging directory or successful archive-integrity check alone does not prove the packaged inventory.

## Verify and preserve

Check the final successful deployment ID, completion time and label ordinal. Compare every deployed asset with the packaged manifest at the deployment URL and public domain. Verify useful page content, links and stylesheet appearance in the requested browser. A byte comparison and visual check establish different facts. If a browser shows old CSS, try reload without cache and record the result; do not use that as proof that cache invalidation is solved for all visitors.

The optional scripts/verify_static.py helper creates an offline payload manifest or performs anonymous HTTPS exact-hash readbacks. It does not deploy, read credentials, accept host rewrites, or certify accessibility. Any host rewrite remains a mismatch until reviewed explicitly in the product's verifier; never accept arbitrary HTML just because it contains an expected marker. For confidential deployments use the repository's authorized verifier instead of this public-site helper.

Record source/artifact hashes, deployment ID, URLs, completion time, tested scope and unresolved differences. Commit the sanitized release record through the repository's normal PR process. Reconcile all artifacts created in the task: merged source, tagged toolkit, review records and owning-product briefs. Do not sweep unrelated dirty files into a publication commit. Keep generated local screenshots as private evidence unless cleared for publication.
