# Reuse decisions across products and platforms

Use this only when an audit or change proposes extraction across callers. The
product's architecture map and release record still govern its actual scope.

## Decide what belongs together

For each candidate, name the two callers and compare observable inputs, outputs,
error behavior, persistence format and release cadence. Trace the duplicate to
source and tests. Extract shared code when the behavior is the same and both
callers can adopt an explicit contract without new coupling. Keep the entrypoint
small enough that a caller can understand it without importing another product's
UI, provider SDK, brand, secrets or release policy. Use parameters for actual
variation, not a growing set of product-name branches.

When platform behavior differs, share schemas, fixtures or test expectations
instead. When only static page chrome repeats, first enforce parity with a test;
an offline renderer can follow once its generated inventory, source ownership and
rollback are demonstrated. Generated output has one source of truth. Avoid a
runtime dependency solely to remove copied markup from a static site.

A silent fallback is not a reusable storage adapter. Its contract should expose
readable, writable, corrupt and unsupported states so the UI can tell the user
when progress will be session-only. Preserve unknown bytes on failed migration;
never write candidate data to production keys during testing. Ownership/receipt
checks remain provider adapters, separate from local save state.

## Change without drifting callers

Characterize current behavior for each caller, including one failure path. Add
contract tests that run the same scenarios through both adapters or implementations
where a common rule is claimed. Record version and migration effects, and compare
the packaged artifacts that users will actually run. If a live or owner-accepted
artifact is frozen, introduce the shared seam in an unpublished candidate first;
keep the frozen bytes and their passing evidence. Promote only after affected
regressions, owner decisions and channel checks are complete.

A successful extraction has a smaller maintenance surface and a clear owner.
Report which duplication remains intentionally separate, which checks passed,
and which platform or release claims are still unverified. Do not turn lexical
coverage or a clean refactor into proof of native behavior or public release.
