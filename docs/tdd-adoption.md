# Pinned TDD adaptation requirements

Owner-approved implementation, November 14, 2026 Pacific. Governing umbrella:
[toolkit PRD](PRD.md). Intended users are agents making authorized, testable
behavior changes or refactoring existing code.

Adopt only Matt Pocock's `skills/engineering/tdd` at
`5863806dd4e15c63174bee4e7515a4256792ecfa`, retaining its test examples,
mocking guidance and MIT notice. The local adaptation must retain refactoring
inside red–green–refactor, derive public test boundaries from approved
requirements without repeat confirmation, permit passing characterization tests
before pure refactoring, and replace unavailable cross-skill calls with local
guidance. Keep one behavior per cycle, independent expected results, observed
failure before correction, focused checks and required completion checks.

Acceptance: Engineering source becomes 0.2.0, discoverable from the existing
catalog and repository instructions. Record upstream and adapted file hashes,
license, maintainer and actual validation. A fresh history-free agent must load
the method and replay the completed PR29 manifest defect from baseline
`8b7d4fd92c361cb0ba8697322e50a5b7878efffa`, with its five existing tests but
without historical implementation or added tests. Retain baseline, red, green
and refactor logs. Independently verify duplicate members, invalid versions,
invalid later inventory entries, valid-entry preservation and rejection before
network/report side effects. Run existing affected tests and an independent
exact-head source/evidence review before normal PR merge.

This offline replay does not reopen PR29. No application API/schema change,
package publication, global installation, infrastructure or consumer-pin update
is included. Acceptance establishes bounded explicit loading and behavior,
not productivity, automatic discovery or organization-wide adoption. The
Engineering maintainer owns updates through the existing maintenance review.
