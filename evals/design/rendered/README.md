# Local rendered Design evaluations

Four original fictional fixtures exercise actual rendered evidence: stateful
actions (R1), production-target judgment (R2), preservation of an intentionally
plain working interface (R3), and stale acceptance across two artifacts (R4).
No product/customer data, copied reference art, external fonts, analytics or
network service is used. The HTML/CSS/JavaScript is original and covered by this
repository's Apache-2.0 license. These interfaces are evaluation material, not
products or release candidates.

## Generate evidence and verify fixture behavior

Use an already installed Node/Playwright/Chromium runtime. This optional local
evaluation adds no required plugin dependency and does not install anything:

```sh
node evals/design/rendered/run.mjs --output /path/to/new-evidence-directory
```

If Playwright is outside Node's normal lookup, set `PLAYWRIGHT_MODULE` to its
installed package directory. If its default browser is unavailable, set
`CHROMIUM_EXECUTABLE` to an already installed compatible browser executable;
do not silently install a browser. Record the actual versions. The runner serves only
the fixture allowlist on loopback, uses a fresh browser context, blocks external
requests, records desktop/narrow PNGs and SHA-256 input/output identities, and
refuses an existing output directory. Node 24 and Playwright 1.x are the intended
runtime; the dated evaluation record owns the exact tested versions.

The assertions verify that the fixture presents the specified behavior,
including deliberate failure examples. A passing run does **not** accept the
fixtures' design quality. The runner is not part of installed skills or a new
hosted CI job. Existing Design export CI remains separate.

## Independent evaluation

Run each case in a fresh evaluator context with the changed skill and only its
section from [prompts.md](prompts.md), raw fixture files and fresh render evidence.
Provide local browser access where available; a bounded fixture-only server can
be started with `python3 -m http.server --bind 127.0.0.1 --directory evals/design/rendered/fixtures PORT`.
The evaluator may use a separate browser automation tool to inspect and exercise
the fixture. Do not expose [assessment.md](assessment.md), runner assertions,
earlier answers or a description of the intended failure before its response.

Retain the complete answer, skill/input revision, generated manifest, viewport,
tool/model identity (unknown when not exposed), observed interactions and gaps.
After the answer is fixed, a separate assessor compares it with the held-out
criteria and records pass/partial/fail with specific evidence. Missing required
interaction is partial coverage, not a pass inferred from a screenshot. Keep
rendered judgment separate from the final independent source-PR review.

Generated evidence stays outside tracked source by default. Only original,
cleared fixture captures may accompany a public evaluation record; never copy
private product captures or local account paths into this repository.
