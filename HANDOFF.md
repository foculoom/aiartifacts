# Maintainer handoff

## Design CI registration — October 24, 2026

The existing validation workflow now runs Design's synthetic export-evidence
suite, including duplicate-member and strict integer-version regressions.
This focused CI follow-up depends on the strict-manifest source change. It
does not release a plugin, move v0.5.0, update consumer pins, add dependencies,
or introduce product/private fixtures. Local command results and hosted CI
results are separate evidence; inspect the follow-up PR's exact commit checks.

## Strict manifest parsing — October 24, 2026

The unreleased Design 0.1.1 checker now rejects duplicate JSON members at every
object level and requires the integer version `1`. This prevents duplicate
filenames or repeated inventories from silently replacing earlier evidence.
Eleven synthetic Design tests and catalog validation passed locally, including
CLI rejection with exit 2 and no success receipt. No product fixtures or private
data are included. CI registration was left to the separate follow-up above;
this parser increment made no release, installed-plugin update, workflow or
consumer-pin change.

Checkpoint: **v0.5.0 was published on 24 October 2026**. Preserve that existing tag and release; do not recreate or move it. Design 0.1.1 below is an unreleased source increment. This public document contains reusable-method context only. Product/private account decisions, reports, manuscripts and credentials belong in their owning repositories.

## Architecture and release state

One repository holds independently versioned plugins, skills, agent templates, synthetic evaluations and templates. Do not create one repo per product or writing medium. In the released v0.5.0 snapshot, Editorial, Design, Release and Automation are 0.1.0, and Reporting is 0.1.1. The unreleased source adds Design 0.1.1 as described below. The catalog is `.agents/plugins/marketplace.json`. Repository tags pin the combined tested snapshot; they do not imply installation or listing in a universal plugin directory.

- Editorial: shared review method with audience/medium profiles and project voice brief. Never certify human authorship from lint or replace a human editor with a score.
- Design: product-identity and experience-review; shared publisher frame versus product identity, preserve approved choices, distinguish defects/preferences/hypotheses and record observed scope/revisions. Product briefs/artwork stay with their owners.
- Release: serialized release evidence, source/package/provider/live separation, sanitized hash checks; it does not grant deployment authority.
- Reporting: normalized Tally/Gmail/analytics adapters, private aggregate report format, QA and linked-notification exclusions, stale/missing/partial evidence, minimal text-free outputs. Acquisition, authentication, scheduling and retention are consumer responsibilities. Do not imply the offline generator itself connects to providers.
- Reporting 0.1.1 retains unknown context for legacy input and counts self-reported free/paid use, edition and build separately; QA and owner testing stay excluded. No purchase or identity inference.
- Automation: reviewed local tasks with a compiled Keychain launcher, exact service-account/vault checks, task-specific credentials and fresh boolean evidence. No arbitrary command/secret export, cloud runner, automatic rotation or authority expansion. The current Mac consumer demonstrated repeated read-only execution with desktop 1Password locked; that does not prove every task, Keychain lock state or provider write scope. Private evidence remains with the consumer.

v0.4.0 merged at `38b86df9513df3b5a65f02fa1acc4f949dd3e9a9`; tested tree matched the tag:15 reporting, 27 editorial and 5 release tests passed, plus catalog/skill validation. Preserve that historical tag. The v0.5.0 snapshot adds Automation 0.1.0 and advances Reporting to 0.1.1.

## Continue safely

Read README, CONTRIBUTING, CHANGELOG and the relevant plugin/skill before edits. Preserve Apache-2.0 and applicable attribution. Use synthetic or explicitly cleared fixtures. Record upstream source, tested commit, installation and license; do not silently vendor or auto-update. Add an agent configuration only after testing demonstrates a role the skills cannot cover.

For behavior changes run that plugin's tests and structural/catalog validation, update plugin version and changelog as appropriate, then tag the tested repository snapshot after review. Preserve existing tags. Consumers pin and record revisions; they should not silently switch to main.

## Future automation lessons

Prefer narrow existing connectors/service-account access, sanitized durable result files and a single deployment owner. A transient terminal PASS without target/hash/context is insufficient handoff evidence. Credential field-shape diagnostics must never print values. Browser sign-ins and provider scope limits remain explicit dependencies; a skill cannot override credential handoffs or approve broader access. Keep provider-specific normalizers strict and tested rather than accepting any HTML with a build marker.

## Resume and update discipline

Read this checkpoint before the dated history. Fetch the canonical remote, inspect branch/status and preserve other work. Dates below are observations, not a promise that external systems remain unchanged. Recheck provider status before a new release or availability claim. A merged PR is not a deployment; passing tests are not customer demand or commercial clearance. Prefer existing scoped access and service-account helpers; never store credentials in Git or chat. Keep user decisions separate from implementation and external approval. Update this checkpoint and its linked evidence when a milestone changes. Keep historical evidence rather than rewriting it as a new pass.

## v0.5.0 validation

The candidate passed 17 automation, 20 reporting, 27 editorial and 5 release tests (69 total), plus catalog validation for five plugins/six skills and skill structure validation. On macOS run the editorial suite with `TMPDIR=/private/tmp`: its no-symlink input policy deliberately rejects the default `/var` symlink path. The first run under the default temporary path failed for that environmental reason; the canonical-path rerun passed. No editorial behavior was changed.

The consumer's existing private profile also passed the final compiler guards. Live Keychain/provider evidence remains in the owning consumer, as do its exact configuration and task identities. Synthetic error cases do not claim live revocation/expiry tests.

CI initially rejected its group-writable toolcache Python as a reviewed executable. Synthetic child-process tests now use the system interpreter; a regression test explicitly preserves rejection of group-writable files. Production runner guards were not relaxed.

## Unreleased Design 0.1.1 source candidate

Design's product-identity skill now links a reusable export handoff and an
optional Python standard-library checker. Seven synthetic tests cover explicit
source roots, output preservation, linked entries, exact inventory and hash
mismatches; no product files or provider access are used. The checker establishes
local file identity only. Final-raster QR decoding and physical/vendor checks
remain separately observed actions, not results of the checker.

Run `python3 -m unittest discover -s plugins/design/skills/product-identity/tests -q`
and `python3 scripts/validate_catalog.py`. This source candidate is unreleased;
that increment introduced no tag, dependency or CI configuration. The separate
CI follow-up above registers the suite. Preserve local validation and inspect
the exact hosted commit results before any release.
