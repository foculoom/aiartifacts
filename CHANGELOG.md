# Changelog

Changes to released artifacts are recorded here. The repository and each plugin can have independent versions; consuming projects should pin a tag or commit SHA.

## Unreleased — Design 0.1.1 candidate

- Add design-kit handoff guidance for explicit source roots, new output ownership, exact public payload inventories, final-raster QR checks and separate physical/vendor proofs.
- Add a dependency-free, read-only path/inventory/hash checker and synthetic regression cases. No asset generation, QR decoding, publishing or deployment authority is implied.
- This source candidate does not change the released v0.5.0 tag or consumers' pins. CI registration and public release remain separate work.

## 0.5.0 — 2026-10-24

- Add Automation 0.1.0: local Keychain bootstrap, compiled task/profile/code pins, scoped service-account resolution, sanitized fresh-result contracts, and explicit local-only limitations.
- Add synthetic failure tests for missing/malformed/revoked/inaccessible credentials, incorrect identity/scope/field type, changed files, relative interpreter inputs, unsupported tasks, missing evidence and secret-printing children. The compiled launcher has no credential-export operation.
- Update Reporting to 0.1.1 with voluntary actual-use context, edition/build aggregation, QA and owner-test exclusions, and backward-compatible unknown context for earlier records.
- Retain Apache-2.0, existing plugin versions, and product/private data separation. No additional agent role or upstream code was vendored.

## 0.4.0 — 2026-10-24

- Add Reporting 0.1.0: normalized source adapters, private aggregate reports, freshness and missing-evidence handling.
- Add synthetic regression coverage for QA, deduplication, backlog age, and sensitive-text exclusion.
- Document authorized collection, source limitations, recurring review, and aggregate retention.

## 0.3.0 — 2026-10-23

- Add Release 0.1.0 with credential-free static readback tooling and deployment evidence workflow.
- Capture session lessons: reuse signed-in browser, refresh stale history, verify host transformations, and reconcile local artifacts.

## 0.2.0 — 2026-10-23

- Add Design plugin 0.1.0 with product-identity and experience-review skills.
- Add identity/voice brief linkage, synthetic behavior cases, and optional dependency provenance.
- Preserve Editorial plugin 0.1.0 and keep product material outside the public toolkit.

## 0.1.0 — 2026-10-23

- Establish the public artifact catalog and portable editorial plugin package.
- Add medium and audience aware editorial guidance, an optional Codex reviewer agent, and public evaluation cases.

## Engineering source candidate

Engineering 0.1.0 adds the [platform-boundaries skill](plugins/engineering/skills/platform-boundaries/SKILL.md) and a dependency-free, bounded lexical guard with synthetic failure tests. Source candidate only; existing release tags and consumer pins are unchanged. The guard does not certify dependency graphs, device behavior, purchases or store readiness.
