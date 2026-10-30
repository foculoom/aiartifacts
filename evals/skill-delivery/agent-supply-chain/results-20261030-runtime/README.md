# Runtime preparation follow-up — October 30, 2026

The contribution remains `74d289660e954dbe03342bf0c3d8241b007b5125`.
[Earlier preparation](../results-20261030/README.md), human feedback and
Foculoom [PR #33](https://github.com/foculoom/aiartifacts/pull/33) remain achieved.
This follow-up changes evaluation tooling and evidence, not the exported skill.

## Linux helper execution

[All 47 tests passed](linux-unittest.txt), with zero skips, in a disposable
Linux container using Python 3.12.14. The [receipt](linux.json) pins the source
files and existing local image by hash. Execution used UID 65534, no network,
read-only source/root filesystem and disposable temporary storage. No image
was downloaded. The source stayed unchanged and the container was removed.

This was Linux amd64 through Docker Desktop's arm64 daemon on the authorized
local Mac, after no saved cloud environment was available. It is not hosted
Python 3.11 CI and does not establish model behavior or enforced model failures.
Private image tags, environment metadata and machine paths are excluded.

## Codex context preparation

The [preview receipt](context-preview.json) preserves two no-inference attempts.
A separate supported `CODEX_HOME` removed the company-global instructions.
The first preview nevertheless included built-in skills initialized by Codex;
enumerating and disabling the actual entries removed the catalog. Independent
agent review inspected the complete revised context. Flags alone were not
accepted as evidence.

The evaluation runner now accepts an explicit existing profile outside the
project, uses it for authentication, skill discovery and its own session capture,
and retains its ChatGPT-only authentication guard. Ambient overrides remain
ignored. Authentication uses the normal sign-in flow; credentials are never
copied. Managed controls remain in effect.

The owner completed the normal ChatGPT browser sign-in on October 30; the
isolated profile's login check succeeded. Independent agent review of the
post-login preview found the same content and tool schemas as the accepted
pre-login preview, with only generated identifiers/timestamps changed. This
closes that preparation step. The subsequent explicit X1 diagnostic observed
skill loading and a correct clean comparison, with inputs preserved.

Initial-context isolation does not restrict all filesystem reads. Model access,
observed identity, actual skill loading, functional cases, enforced failures
and paired usefulness require separate execution and review. A context preview
cannot pass those gates.

## Actual Codex trials and comparison

[Functional review](functional-review-corrected.json) inspected all twelve
corrected fresh sessions: six skill positives, three negatives with the skill
available, and three no-skill comparison arms. Positives loaded the exact
candidate; negatives made no tool calls and did not load it. Inputs were
preserved, except P1's requested new manifest. Requested and runtime-recorded
gpt-6.1-sol/medium matched; the actual tool schema and base instructions matched
across runs. Backend identity was not supplied. No measurement or previous-case
contents were read. The P4 baseline's model-catalog refresh timeout warning is
preserved; execution completed under the fixed recorded configuration.

The [original review](functional-review-original.json) retains all twelve first
attempts. P2's baseline read an evaluator inventory exposed in the project;
P4's prompt ambiguously prohibited reading its named manifest. Those attempts
are excluded from comparative acceptance. All twelve cases were rerun with
external inventories and the clarified P4 boundary, without changing the skill.

The [independent comparison](blind-review.md) judged P2, P4 and P5 **three ties**,
with no material regressions demonstrated. This is zero wins against the
predeclared requirement of concrete benefit in at least two pairs: **the
usefulness gate was not met**. Anonymous labels and the [arm mapping](blind-map.json)
were separated until the verdict; full traces expose methods, so this was not
method-blind. It is directional agent-reviewed evidence, not human testing or
a statistical estimate. Do not select favorable reruns to erase this result.

Complete sanitized answers, event traces, prompts, runner receipts and generated
artifacts are retained under `codex-X1/`, `codex-original/` and
`codex-corrected/`. Each artifact map binds original and published hashes.
Raw sessions remain private because they include account/harness metadata;
their hashes and independent context checks remain in the public receipts.
The [MIT notice](upstream-LICENSE.txt) applies to upstream skill text reproduced
in tool output. The implementation remains canonical in the contribution fork.
Independent pre-publication review caught local ownership columns in terminal
listings; these were replaced with placeholders before pushing. Raw originals
remain private, published hashes were updated, and a synthetic regression now
checks both plain and JSON-escaped listings. This is a bounded screen, not a
complete privacy audit. Historical cleared synthetic owner labels stay intact.

## Enforced-failure preparation

The [three offline F2 preflights](f2-preflight/README.md) preserve a configuration
syntax failure, an exposed pre-existing hardlink, and a successful guarded
alias-free fixture. The last check enforces the denied path for local commands;
it does not prove inode-wide protection, absence of outside copies, other-tool
restrictions or actual agent behavior. No F2 model trial followed. F1 still
lacks demonstrated interpreter confinement. Neither is recorded as a passed
model failure case.

## Distribution status

As observed October 30, the original skill is publicly cataloged upstream and
the improved candidate source is public in the contribution fork. Candidate
local-source installation remains achieved; merged upstream acquisition and
skills.sh indexing are unverified. No upstream PR has been submitted. Existing
Editorial public GitHub acquisition and v0.5.0 remain unchanged.

Copilot still lacks an established authorized fixed-model route with verified
usage coverage. Do not repeat the previous denial without new access evidence.
Keep upstream submission held: usefulness was not demonstrated and Copilot and
enforced model failures remain incomplete. Preserve the tested implementation,
existing preparation tooling and the owner's scoped “Useful and clear” feedback.
No further model run is justified merely to obtain a favorable comparison.
