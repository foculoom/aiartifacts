# TDD replay acceptance — November 14, 2026 Pacific

This is an offline replay of completed [PR29](https://github.com/foculoom/aiartifacts/pull/29),
merged October 30 as `1ce208bf7fb4b102bac8f31b192bc378790ed712`.
It does not reopen the production fix or replace its implementation.

Requirements were independently reviewed before implementation at
`418cd05f559348d3a4ab0638aa891c847ad4bff6` by the `requirements_review`
agent. Candidate method source is `b84e461d140d62a9dd0eed8271c7e1fc0be59cab`;
upstream and adapted bundle identities are in the
[Engineering dependency record](../../../plugins/engineering/DEPENDENCIES.md).

## Isolation and loading

A fresh Codex collaboration agent (`fork_turns=none`, default inherited model;
exact model ID not exposed) received a disposable history-free directory with
only [baseline verifier/tests](baseline), [repository-local instructions](AGENTS.md),
[accepted behavior contract](contract.md) and the candidate skill bundle.
It was told to implement the contract, explicitly read the skill/examples,
work only within that directory, use no network/history/delegation, and retain
all phase results. The directory contained no Git history or historical fix or
added tests. Baseline files are exact copies from
`8b7d4fd92c361cb0ba8697322e50a5b7878efffa` under
`plugins/release/skills/release-evidence/scripts/`.

The [complete work log](logs/work-log.md) records explicit local loading and
sources read. This demonstrates supplied repository-local invocation in this
runtime, not automatic discovery, global installation or cross-provider use.
The archived AGENTS/contract are input fixtures, not repository instructions.
Only the minimal replay files were supplied, not the complete baseline tree.

## Observed behavior

| Phase | Actual result |
| --- | --- |
| Baseline | Five original tests passed |
| Record-shape cycle | Intended red, then 6 green and 6 refactor tests passed |
| Complete-path cycle | Intended red, then 7 green and 7 refactor tests passed |
| Digest-preflight cycle | Intended red, then 8 green and 8 refactor tests passed |
| Duplicate-member cycle | Initial mock-setup failure retained; corrected test observed six missing-ValueError failures before implementation; 9 green and 9 refactor tests passed |
| Preservation/acceptance | 13 passed; original five-test class preserved byte-for-byte |
| Independent held-out probes | Baseline failed (16 failed subcases, 9 error subcases); replay passed all 5 probe methods |

Full [phase logs](logs) preserve stdout/stderr, command, Python version and exit
status, including the failed setup attempt. Local workspace prefixes alone are
replaced with `<replay>`, `<baseline>` or `<evaluation>`; original log hashes
are retained in [original-log-hashes.json](original-log-hashes.json).
Tests derive new expected values from the contract and literal known hashes,
not the verifier. Four bounded behavior corrections each precede a refactor
check; later passing characterization tests verify preservation without fake red.

The parent evaluator wrote [heldout_verify.py](heldout_verify.py) independently
before seeing the completed implementation and withheld it from the agent.
It checks duplicate root/inventory members, strict version/shape, invalid later
paths/digests, direct-call preflight, no client/report side effects, and exact
valid-entry/routes/report preservation. Its [baseline](logs/heldout-baseline.log)
and [candidate](logs/heldout-candidate.log) results are retained separately.
No historical implementation was used as a behavioral oracle.

## Reproduce checked outcomes

From this directory on Python 3.9+ (observed 3.9.6, macOS, standard library):

```sh
(cd baseline && python3 -B -m unittest -v test_verify_static)
(cd replay && python3 -B -m unittest -v test_verify_static)
python3 -B heldout_verify.py baseline  # expected nonzero: old defect
python3 -B heldout_verify.py replay    # expected pass
```

For a new behavioral replay, copy only baseline's two files, AGENTS.md,
contract.md and the exact skill bundle into an empty directory with the skill
at the path named in AGENTS.md. Withhold this README, replay outputs, logs and
heldout probes. Do not substitute a successful fresh run for the original logs.
Intermediate source snapshots were not retained; per-cycle outcomes are logged,
while final deterministic results are reproducible from the archived code.
Verify archived file identities from repository root with
`shasum -a 256 -c evals/engineering/tdd-20261114/evidence.sha256`.

## Scope and limits

No live HTTPS, production deployment, provider check or customer receipt was
performed. CLI exercised real main/argv and local files in process; transport
was mocked at the system boundary. This is one bounded successful engineering
replay, without a no-skill control or productivity measurement. Pure-refactor
permission is source-reviewed; no separate pure-refactor agent experiment was
run. Organizational methods are evaluated in their private owning repository,
not with private evidence copied here. Source review and required CI are still
separate from method behavior and package release.
