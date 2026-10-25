---
name: platform-boundaries
description: Review or implement multi-platform product architecture, keeping product rules and canonical content separate from store, device, provider, and distribution adapters. Use for platform ports and submission preparation; not for routine unrelated edits or permission to release.
---

# Platform boundaries

Read the repository's instructions, current product decisions, architecture map,
and release runbook. Preserve submitted builds and existing holds. Apply this
workflow to active products in development, submission preparation, and review.
Do not revive archived products or change a business model to fit an adapter.

## Design and implement

1. Identify authoritative rules, content, state schemas, and business decisions.
   Map presentation, persistence, identity, purchases, device capabilities, and
   packaging separately. Record actual paths and unresolved mixed responsibilities.
2. Keep domain dependencies pointing inward. Pass external observations and
   capabilities through narrow interfaces; put SDKs, credentials, product IDs,
   receipt verification, transport, and native lifecycle in adapters. Keep core
   outcomes deterministic when practical by injecting time/randomness/I/O.
3. Use the same core when runtimes permit. Native UI, accessibility, input,
   rendering, performance, and platform conventions can differ. When different
   implementations are justified, share schemas and behavioral fixtures instead
   of forcing an unsuitable framework or claiming source parity.
4. Separate save/progress data from store ownership. Version migrations; preserve
   recovery and unsupported bytes. If purchases exist, specify purchase, restore,
   cancellation, pending, revocation/refund and offline behavior. A local flag or
   mock provider is not verified ownership. Do not add purchases to free products.
5. For publishing, keep canonical manuscripts/data separate from retailer metadata,
   formatting, export and delivery. Make substantive channel differences explicit
   editorial decisions. For generated apps, fix the generator and regenerate;
   identify provenance rather than maintaining divergent generated patches.

## Verify proportionately

Use a small repository-owned `architecture.json` with `version: 1`, a nonempty
`review_gaps` list, and `rules`. Each rule has a unique `id`, nonempty `files`
(repository-relative glob patterns), and nonempty `checks` chosen from
`store-sdk` and `browser-effects`. Every glob must match a UTF-8 file.

Run `python scripts/check_boundaries.py --root PRODUCT --profile architecture.json`
from this skill's directory. The checker reports lexical findings in the declared
files only, including comments; it does not resolve dependency graphs, discover
new core files, certify semantics, or prove security. Empty rules are permitted
only as an explicitly reported review-only adoption, never as a passing code audit.
Keep coverage gaps honest; review new files/imports on each PR. Resolve findings
by fixing boundaries or narrowing the map with a reviewed rationale, not by
silently deleting rules. Pin the shared checker revision in consumers; run it
locally or in existing authorized CI, without adding a network fetch to builds.

Add meaningful core behavior and adapter contract tests for changed behavior.
Test unsupported capabilities and failure paths. Verify copied core assets or
shared fixture outcomes in packaged targets, then perform the required browser,
simulator, physical-device and store sandbox checks. Reuse existing tests and
release tooling. Distinguish tested, untested, mocked and unimplemented behavior.
Do not repeat expensive full suites for documentation-only changes.

## Review and handoff

Use a feature branch and focused PR. Review the complete current diff, test
evidence, dependency direction, migration compatibility, privacy and packaging
impact. Record reviewer identity and whether review was independent. Resolve
major issues and required checks/reviews before merging the exact reviewed head;
new commits require renewed review. Do not bypass protections. Source merge,
store submission, approval and public availability are separate events.

Record platform differences, commands/results, remaining gaps and release-stage
evidence in the owning repository. Use the repository release runbook and the
release-evidence skill for applicable static publication; this skill neither
replaces native release verification nor authorizes publication. Keep private
portfolio records out of public shared artifacts.
