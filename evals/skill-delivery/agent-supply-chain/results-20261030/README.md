# Preparation evidence — October 30, 2026

The reviewed contribution candidate is
[`74d289660e954dbe03342bf0c3d8241b007b5125`](https://github.com/hellofoculoom/awesome-copilot/commit/74d289660e954dbe03342bf0c3d8241b007b5125),
based on Awesome Copilot main `5269f7ea2d6c3a9bfda5ed878b6726cf509121fd`.
Its public contribution-fork source was read back after pushing. It has **not**
been submitted to or accepted by Awesome Copilot. The existing upstream skill
is publicly cataloged; the improved candidate is not the upstream version.

## Achieved evidence

- [47 helper tests](unittest.txt), zero skips, Python 3.12.14/macOS. Includes
  actual denied reads, instrumented prevention of outside-file access, malformed
  manifests, additions, symlinks, exclusive output and legacy handling.
- [Vally 0.20.0](vally.json) passes specification/reference checks. Upstream
  [skill validation](skills.txt), [plugin validation](plugins.txt),
  [README generation](readme.txt), [marketplace generation](marketplace.txt)
  and [line-ending normalization](line-endings.txt) completed. Existing external
  license-identifier warnings remain unrelated to this skill.
- [Two fresh exports](packaging.json) produced identical archives, SHA-256
  `55ee676b9fe0a231b38cab272dd3e294818301c0db0360790c08c4b02f705449`.
  The [export manifest](export-manifest.json) records five approved files,
  hashes and modes; archive verification passed.
- [Local installation receipts](local-installations.json): skills 1.7.4 copied
  all five files/modes unchanged, without links, into the shared project skill
  location for Codex and Copilot. GitHub CLI 2.97.0 installed five files and
  changed SKILL.md through [documented tracking metadata](installer-transform.json).
  Semantic frontmatter/body comparison confirmed only the recorded transform.
  These are local-source installation receipts, not public acquisition or two
  runtime passes. Installer telemetry was disabled.
- An independent agent reviewed the exact final source, reran all 47 tests and
  found no remaining source/privacy blocker. The MIT notice matches upstream;
  no substantial copied Apache implementation was found. This is agent review.
- The owner reviewed the [recorded helper example](../human-review.md) and
  responded **“Useful and clear”** on October 30. This is human feedback on
  the output, not evidence of human execution or runtime evaluation.

## Failed and superseded attempts

Preserve initial commit `8c0ef34dedbda3266bb1755fe85799d96b854947`; it passed
40 tests but failed independent review. CLI path normalization removed `..`
before rejecting symlink ancestors, and `//` bypassed the filesystem-root
guard. The follow-up commit fixes both. Seven added regression methods failed
against the old implementation (ten failure records across subtests) and pass
against the corrected source. The test author and independent reviewer confirmed
the reproductions. Passing the first test suite did not establish correctness.

Earlier test development had two mocked-open failures caused by checking a
patched function's identity for runtime capability detection; the cached
capability check resolved them. An initial system-Python compilation attempt
hit a sandbox cache-write restriction; subsequent checks use bundled Python
with bytecode writing disabled. These are development diagnostics, not models.

The first GitHub local installation used the exact skill path and failed with
`skill "skills/agent-supply-chain" not found in local directory`. A new attempt
using the skill name succeeded. The source checkout's unbuilt skills CLI lacked
its dist bundle; the previously reviewed installed 1.7.4 package was then used,
with entrypoint/bundle hashes matching the earlier acquisition receipt.
The local skill-creator validator rejects the standard `compatibility` field;
the official Vally checks accept it, so the dependency declaration was retained.
An initial metadata-comparison harness used a nonexistent js-yaml default export;
correcting the import made semantic comparison pass. No candidate change follows
from those harness/installer corrections.

Independent pre-publication evidence review also caught a wrapped home-relative
path in installer output. It was redacted before pushing. The unpublished
evidence commit is retained privately and excluded from public branch history;
the bounded privacy regression now includes this pilot and home-relative work
paths. This automated screen still does not replace human privacy review.

## Remaining gates and limits

[Status](status.json) retains zero model trials for this candidate. The prior
Copilot fixed-model access and actual Codex context-isolation blockers remain;
no unchanged denied inference was repeated. No saved authorized cloud
environment was listed. A local Docker client was present but its daemon socket
was absent. Linux/Python 3.11 CI is prepared but has not run. The scoped helper
tests do not establish the enforced F1/F2 model failure environments.

Next: establish supported clean runtime contexts and authorized fixed-model
access, run the prepared functional and paired cases, then independently grade
complete outputs. Unknown loading, missing identity, contaminated context or
unavailable failure enforcement cannot pass. Only after acceptance, recheck
duplicates and current contribution requirements and open one upstream update
PR. Maintainers control approval and merge; then verify public installation at
the merged SHA. skills.sh indexing remains unverified.

The helper compares a quiet staged directory; it does not establish an atomic
snapshot against a hostile concurrent writer, publisher authenticity or release
authority. Source review, metadata lint, helper tests, installation, model
behavior and human feedback are distinct receipts. Existing Editorial public
GitHub acquisition achieved October 30 and the earlier v0.5.0 release remain.

Published text captures normalize trailing whitespace; private originals retain
the original bytes. Raw local installer output, machine paths and original review captures remain
private. The public receipts retain source identities, inventories, results and
limitations. Review this exact evidence revision before publishing it.
