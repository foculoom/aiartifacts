# Skill delivery implementation evidence — 30 October 2026

Latest preparation: the [Editorial-only readiness record](../pilot/editorial-readiness-20261030.md)
uses merged `c6fd520`, fresh package manifests and the
[public-source acquisition receipt](editorial-readiness-20261030/acquisition.json).
The remote installer resolved that exact SHA and copied twelve matching files;
this adds acquisition evidence without claiming a listing or runtime pass.
PR #30 and its [post-merge checks](https://github.com/foculoom/aiartifacts/actions/runs/41107455838)
are achieved. Historical experiment outcomes below retain their original scope.

Follow-up owner decision: integrate the tested tooling and documentation while
deferring the extra skill. Current source keeps the exporter in
`scripts/skill-delivery/`, procedures in `docs/skill-delivery/` and the original
entrypoint only as [a non-discoverable fixture](../candidate/README.md).
Engineering's existing manifest/skill set is restored. This applies the
predeclared fallback; it does not change any historical outcomes or hashes.
The reviews and final [CI](https://github.com/foculoom/aiartifacts/actions/runs/41104482894)
at `4592a641d9fc6ea39e055d943a8dc71521442060` are achieved; the path/discovery
follow-up receives its own source checks and review in PR #30.

The implementation is a reviewable source candidate in
[PR #30](https://github.com/foculoom/aiartifacts/pull/30), beginning at
`211ad9da8b7a3d0740d1896a74c018ed3ad097be`. **Defer adopting the extra skill.**
The paired trials favor the helper in only one of three pairs, below the
predeclared two-of-three threshold; full context/model controls also remain
unverified. Retain the exporter, checks, documentation and draft candidate.
Useful local task results do not establish incremental benefit or release readiness.

| Evidence | Result and limit |
| --- | --- |
| [Packaging and installation](packaging-20261030.md) | 148 Python and 10 JavaScript tests pass; upstream lint/schema and dry-run checks pass. Exact 12-file skill and 15-file plugin exports match the isolated installed copies, including modes. Local-source installation does not establish a released remote install or public listing. |
| [Source review](source-review-20261030.md) | Independent exporter/integration review accepts source `211ad9d`; a separate reviewer covers the authored instructions/references in the packaging record. Both hosted Ubuntu runs pass at that SHA. Later evidence and runner changes require their own final-head checks. |
| [Runner review](runner-review-20261030.md) | Three synthetic authentication-guard tests pass without provider calls. The optional development runner uses an existing ChatGPT login and refuses an unverified/API-key login; it does not prove full context isolation. |
| [Editorial execution](codex-editorial-20261030/README.md) and [independent grading](codex-editorial-20261030/grader.md) | Eleven bounded task outcomes pass: six positive, three negative, two safe-failure reruns. Skill reads are observed where appropriate; complete initial instruction isolation and exact model identity remain unverified. Two original sandbox setup failures are retained. |
| [Copilot access](copilot-probe-20261030/README.md) | CLI 1.0.54 installs the local plugin, but a simple unrelated connectivity probe returns a policy denial before skill evaluation. The retry after restored workspace usage has the same provider denial. Copilot behavior remains unverified. |
| [Meta-skill execution](codex-meta-20261030/README.md) and [grading](codex-meta-20261030/grader.md) | Six tasks reach scoped task acceptance after one finishing correction; two explicit invocation diagnostics pass. Original timeouts/resource interruptions remain. The missing-Python case recovered through an available absolute interpreter, so genuine interpreter absence remains untested. |
| [Paired usefulness](codex-pairs-20261030/grader.md) | Baseline/helper correction counts are **1/0, 0/0, 0/1**. Both arms reach the required task quality after corrections. Only one pair favors the helper; formal controlled usefulness remains unmeasured. No adoption recommendation follows. |
| [Final deterministic validation](final-validation-20261030.json) | **152 Python methods and 10 JavaScript tests pass** on the final portability-test working tree. The standalone suite now passes all 23 tests without other repository files; three repository integration tests remain in `evals/`. This is a later test-layout fix, not a rerun or relabeling of the historical 22/25 installed-suite result. |

The portability follow-up moves two Editorial integration checks out of the
installed skill and roots self-export at that skill. A new integration case
copies only the skill into `.agents/skills/skill-delivery` and runs its full
23-test suite. Independent agent review found no blocker; affected checks passed
on Python 3.9 and 3.12. Skill instructions and exporter bytes are unchanged.
Earlier model-trial inventories retain their original test-file identities.

The privacy review withheld scratch binaries containing machine-local paths
from the public evidence snapshots. Their maps retain original hashes, sizes
and omission reasons; candidate payloads were unaffected. Complete public text
and reviewed ZIP-member scans found no remaining machine-path/provider-key
patterns. Those bounded scans do not replace human rights/privacy decisions.
An additional final review found a missed macOS temporary-path alias after the
first evidence push. The [corrective record](../../../docs/skill-delivery-evidence-redaction-20261030.md)
preserves the scope and exact revision: 17 text files were sanitized and their
snapshot inventories updated. The current packet correction does not erase
earlier public copies or repository history; previous broad privacy-clear
wording was incomplete and is superseded by that record.
Four additional offline regression tests cover common host-path aliases,
redaction placeholders, capped compressed members and the retained evidence
tree. These passed after the correction; the earlier 152-test receipt remains
dated evidence for its original source state.

Each receipt distinguishes the original working-tree inputs from later committed
equivalence. Selected-file hashes identify the tested content. Evaluation
inventories cover sanitized records, not a claim that raw sessions were public.
No private company/customer inputs or credentials are intended for this packet.
Pattern screening supplements manual review; it cannot establish publication
rights or absence of sensitive context.

Source approval is agent review, not human rights clearance, runtime acceptance
or permission to submit. The Awesome Copilot packet remains unsent. No release,
listing, account/policy change, paid service or consumer-pin update is performed.
The ordinary branch push reported an existing actor's ref-creation-rule bypass;
no rules changed, and the separate `main` PR/check/review requirements remain.

Public acquisition remains separately dated: v0.5.0 was published October 24,
release metadata was checked October 30, and archive acquisition was last
explicitly verified October 28. The new candidate is publicly reviewable source,
not a new release. No Awesome Copilot listing was created; skills.sh public
indexing/acquisition remains unverified. Telemetry-disabled local installs are
not directory visibility, customer demand or revenue evidence.

The selected tooling/documentation scope is integrated in PR #30; the extra
skill remains a deferred fixture. Next: any further trial should address a concrete gap,
use a pinned observable runtime/model and independent grading, and retain the
original results. An already-authorized Copilot environment is needed to close
that runtime gate. External submission, package release and consumer adoption
remain separately controlled actions.
