# Release manifest validation — October 30, 2026

## Contract and baseline

Selected behavior: the anonymous static readback helper must reject ambiguous
JSON and invalid inventory before making requests or writing a success report.
Accept integer version 1, a nonempty file map, canonical relative file paths and
lowercase SHA-256 digests. Preserve generated manifests, nested index routes,
exact-byte comparison, HTTP failure handling and symlink rejection.

These acceptance criteria were declared before implementation. All inputs are
synthetic and all HTTP operations in the regression suite are mocked. This is a
deterministic tool test, not an agent-behavior evaluation or live release test.
Rejecting ambiguity protects the meaning of a release receipt; it does not prove
that a caller's otherwise valid manifest includes every intended asset.

Current default source inspected: `8b7d4fd92c361cb0ba8697322e50a5b7878efffa`.
Its five Release tests passed before adding cases. Existing hosted baseline
[run 41002589483](https://github.com/foculoom/aiartifacts/actions/runs/41002589483)
passed both jobs. Catalog validation checks structure and references, not skill
quality; toolkit tests do not establish consumer compatibility.

## Red

Test-only commit: `c6915d147017c219703404d51f8dc07ae091213e`.
Run from the repository root:

```sh
python3 -m unittest discover -s plugins/release/skills/release-evidence/scripts -v
```

Observed: 10 test methods, 8 failing subcases across 3 methods.

- Three duplicate-member CLI inputs printed `PASS` instead of rejecting:
  a second `files` object discarded `missing.css`; a duplicate filename replaced
  its expected hash; a second `version` replaced version 2 with version 1.
  Python's default JSON parser kept the last member silently.
- Boolean `true` and floating-point `1.0` versions were accepted because they
  compare equal to integer 1 in Python (two failures).
- A later traversal path and later invalid digest were rejected only after the
  first mocked request; the network-client assertion failed. A `.` path was
  accepted instead of rejected (three failures).

The original five methods, valid generated three-file round trip and empty-map
rejection passed. Empty inventories were already protected; no empty-inventory
defect is claimed. This was a behavioral red, not a network/setup failure.

## Green and refactor

Correction commit: `a6cbba40941a95fc07796bd8802237c051b59392`.
The CLI uses a duplicate-rejecting JSON object hook. Complete type/path/digest
validation precedes network-client creation. Version 1 must be an integer.
The same 10 methods passed, including all previously failing subcases.

After green, validation was extracted into `checked_files`, separating the
inventory contract from readback. The pattern matches Design's existing strict
parser without coupling the independently usable plugins. No new dependency,
framework, workflow or behavior-evaluation criterion was introduced.

After refactoring, the Release suite passed all 10 methods and neighboring
Design suite passed all 11. `git diff --check` passed. Commands:

```sh
python3 -m unittest discover -s plugins/release/skills/release-evidence/scripts -v
python3 -m unittest discover -s plugins/design/skills/product-identity/tests -q
git diff --check
```

Environment: managed cloud Linux x86_64, Python 3.12.14. Git transport failed
to connect to the configured proxy; exact-revision text files were retrieved
through the authorized GitHub connector and tested in a local snapshot.
The snapshot is not a Git clone of the upstream commit. Existing rendered PNGs
were not retrieved; local catalog validation stopped on a missing existing PNG
reference. That is a snapshot setup limitation, not a source regression or a
catalog pass. The normal hosted checkout must run the complete required suite.
No new credentials, infrastructure or security changes were needed.

## Scope and next action

The focused PR must retain exact-final-head independent review and hosted checks;
their final receipts belong in the PR. Agent review is not human approval.
The existing CI already discovers these regression cases.

No skill instructions changed, so no new agent-behavior evaluation is claimed.
No consumer pin changed or integration test ran. Real archive inventory, native
acceptance, signing, provider recovery, rendered quality, deployment and customer
transactions remain outside this test. Readback can only assess listed assets;
it cannot enumerate unlisted remote files or certify a reviewed allowlist.

Maintainer next action: integrate only after review/checks, then consider explicit
consumer adoption against each owning configuration. Package publication requires
separate release authority and acceptance. Existing v0.5.0 remains the latest
non-draft release in the October 30 metadata readback (published October 24);
no fresh package-download test, new release, deployment or customer outcome is
claimed. Preserve published tags and installed pins.
