# Maintainer handoff

Checkpoint: repository snapshot **v0.4.0**, 23 October 2026. This public document contains reusable-method context only. Product/private account decisions, reports, manuscripts and credentials belong in their owning repositories.

## Architecture and release state

One repository holds independently versioned plugins, skills, agent templates, synthetic evaluations and templates. Do not create one repo per product or writing medium. Current plugins are Editorial, Design, Release and Reporting, each 0.1.0. The catalog is `.agents/plugins/marketplace.json`. Repository tags pin the combined tested snapshot; they do not imply installation or listing in a universal plugin directory.

- Editorial: shared review method with audience/medium profiles and project voice brief. Never certify human authorship from lint or replace a human editor with a score.
- Design: product-identity and experience-review; shared publisher frame versus product identity, preserve approved choices, distinguish defects/preferences/hypotheses and record observed scope/revisions. Product briefs/artwork stay with their owners.
- Release: serialized release evidence, source/package/provider/live separation, sanitized hash checks; it does not grant deployment authority.
- Reporting: normalized Tally/Gmail/analytics adapters, private aggregate report format, QA and linked-notification exclusions, stale/missing/partial evidence, minimal text-free outputs. Acquisition, authentication, scheduling and retention are consumer responsibilities. Do not imply the offline generator itself connects to providers.

v0.4.0 merged at `38b86df9513df3b5a65f02fa1acc4f949dd3e9a9`; tested tree matched the tag:15 reporting, 27 editorial and 5 release tests passed, plus catalog/skill validation. This documentation checkpoint does not bump plugin behavior versions or retag the tested release.

## Continue safely

Read README, CONTRIBUTING, CHANGELOG and the relevant plugin/skill before edits. Preserve Apache-2.0 and applicable attribution. Use synthetic or explicitly cleared fixtures. Record upstream source, tested commit, installation and license; do not silently vendor or auto-update. Add an agent configuration only after testing demonstrates a role the skills cannot cover.

For behavior changes run that plugin's tests and structural/catalog validation, update plugin version and changelog as appropriate, then tag the tested repository snapshot after review. Preserve existing tags. Consumers pin and record revisions; they should not silently switch to main.

## Future automation lessons

Prefer narrow existing connectors/service-account access, sanitized durable result files and a single deployment owner. A transient terminal PASS without target/hash/context is insufficient handoff evidence. Credential field-shape diagnostics must never print values. Browser sign-ins and provider scope limits remain explicit dependencies; a skill cannot override credential handoffs or approve broader access. Keep provider-specific normalizers strict and tested rather than accepting any HTML with a build marker.

## Resume and update discipline

Read this checkpoint before the dated history. Fetch the canonical remote, inspect branch/status and preserve other work. Dates below are observations, not a promise that external systems remain unchanged. Recheck provider status before a new release or availability claim. A merged PR is not a deployment; passing tests are not customer demand or commercial clearance. Prefer existing scoped access and service-account helpers; never store credentials in Git or chat. Keep user decisions separate from implementation and external approval. Update this checkpoint and its linked evidence when a milestone changes. Keep historical evidence rather than rewriting it as a new pass.
