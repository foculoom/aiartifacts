---
name: test-driven-development
description: Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests.
---

# Test-Driven Development

TDD is the red → green → refactor loop. This skill is the reference that makes that loop produce tests worth keeping: what a good test is, where tests go, the anti-patterns, and the rules of the loop. Every section applies on every cycle: consult them before and during the loop, not after.

When exploring the codebase, read `GLOSSARY.md` (if it exists) so test names and interface vocabulary match the project's domain language, and respect ADRs in the area you're touching.

## What a good test is

Tests verify behavior through public interfaces, not implementation details. Code can change entirely; tests shouldn't. A good test reads like a specification: "user can checkout with valid cart" tells you exactly what capability exists, and it survives refactors because it doesn't care about internal structure.

See [tests.md](tests.md) for examples and [mocking.md](mocking.md) for mocking guidelines.

## Seams: where tests go

A **seam** is the public boundary you test at: the interface where you observe behavior without reaching inside. Tests live at seams, never against internals.

Derive the public boundaries and expected behavior from the current approved
requirements and existing API. Record what each boundary catches and misses.
Existing authorization is sufficient; ask only about a material unresolved
behavior or scope decision, and continue independent approved work.

When the interface itself needs design, keep product rules behind a small
public interface, separate external adapters, and choose observable inputs and
outputs that survive internal restructuring. Respect the repository's existing
architecture rather than adding an abstraction solely to simplify a test.

## Anti-patterns

- **Implementation-coupled**: mocks internal collaborators, tests private methods, or verifies through a side channel (querying the database instead of using the interface). The tell: the test breaks when you refactor but behavior hasn't changed.
- **Tautological**: the assertion recomputes the expected value the way the code does (`expect(add(a, b)).toBe(a + b)`, a snapshot derived by hand the same way, a constant asserted equal to itself), so it passes by construction and can never disagree with the code. Expected values must come from an independent source of truth: a known-good literal, a worked example, the spec.
- **Horizontal slicing**: writing all tests first, then all implementation. Bulk tests verify _imagined_ behavior: you test the _shape_ of things rather than user-facing behavior, the tests go insensitive to real changes, and you commit to test structure before understanding the implementation. Work in **vertical slices** instead: one test → one implementation → repeat, each test a **tracer bullet** that responds to what the last cycle taught you.

## Rules of the loop

- **Red before green.** Write the failing test first, then only enough code to pass it. Don't anticipate future tests or add speculative features.
- **One slice at a time.** One seam, one test, one minimal implementation per cycle.
- **Refactor while green.** After each correction, simplify duplication or structure
  when useful without changing behavior; rerun the focused tests. A no-op refactor
  is valid when there is nothing useful to simplify.
- **Pure refactoring:** first establish passing characterization tests for behavior
  that must remain unchanged. Do not manufacture a red test or preserve a known
  defect as desired behavior. Any behavior correction still needs observed red.
- **Observe the failure.** Run the regression test before correction and confirm
  it fails for the intended missing behavior, not an import/setup error. Preserve
  the command and outcome; run focused tests after each slice and all required
  regression/acceptance checks before completion. Independently derive expectations
  from requirements or worked examples, not the implementation under test.

This method does not replace independent source review or project acceptance.
Read [tests.md](tests.md) and [mocking.md](mocking.md) when selecting assertions
and dependencies. For a requirement about preventing network/file side effects,
observing those system boundaries is legitimate; the warnings about call counts
concern internal implementation coupling.

Adapted from Matt Pocock's MIT-licensed TDD skill; see [LICENSE](LICENSE).
The package [dependency record](../../DEPENDENCIES.md) owns the exact upstream,
local hashes, adaptations and evaluation limits.
