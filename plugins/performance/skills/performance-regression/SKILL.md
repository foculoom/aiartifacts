---
name: performance-regression
description: Measure and investigate runtime regressions with repeated comparable browser scenarios and source-bound evidence. Use for responsiveness, rendering, load, and size changes; not forecast accuracy or release approval.
---

# Performance regression

Start with the user's affected journey and the repository's existing tests.
Preserve functional assertions while measuring real browser work. A reducer
with a mocked clock or renderer cannot establish rendering performance.

## Capture comparable evidence

Keep scenario code, synthetic fixtures, and tested toolkit revision in the
consumer repository. Keep raw reports and traces in ignored local storage.
Use the [browser helper](scripts/browser.cjs) with the consumer's existing
Playwright dependency; it installs nothing and serves only local files. Read
[the measurement contract](references/measurement.md) before integration.

Run on clean committed source, with the same machine, browser, viewport,
fixture, power conditions, and toolkit revision. Close unrelated heavy work.
The helper creates fresh contexts, discards one warm-up, and records five
samples per metric. Repeat interleaved baseline/candidate runs when noise or
thermal drift could change the decision. Do not run timed consumers in parallel.

For a symptom, inspect a browser trace or profile to locate the expensive
operation before optimizing. Verify the same journey after the change. Keep
functional, offline, data-recovery, and accessibility assertions in place.
Native thermal, energy, and memory claims require separate device measurements.

## Compare and decide

Run `python3 scripts/compare.py --baseline BASE.json --candidate CANDIDATE.json
--output NEW_COMPARISON.json` from this skill directory. Missing evidence is
incomplete; changed environments or workloads are incomparable. The comparator
reports median, nearest-rank p95, range and population standard deviation.
Five samples make p95 the maximum; do not describe it as a field percentile.

A wholly slower sample range is an advisory investigation signal, not a
statistical test. Review median changes even when ranges overlap. No universal
millisecond limit, automatic baseline replacement, or release approval follows.
Only add a timing gate after a stable device-specific baseline and an explicit
reviewed threshold change. Preserve a previous baseline for comparison.

Prove the harness catches a deliberately injected slowdown and that removing
it restores the comparison. Label injection in the report. Keep synthetic
results separate from actual defects, field telemetry, and claimed savings.
Attach source revisions and relevant evidence to the owning product's weekly
review. Reuse its release-evidence and recovery workflow rather than replacing it.
