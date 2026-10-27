# Browser measurement contract

The consumer supplies `run({root, serveRoot, scenario, fixture, exercise})`.
`exercise({page, context, base, measure, nextPaint, frames})` returns named
numeric metrics. Metric names ending in `_bytes` use bytes; others use ms.
`measure(page, action)` includes driver transport, actionability waiting, the
action, and two animation frames. It is action-to-settle duration, not INP or
pure event-handler latency. `frames(page)` reports the maximum of 60 animation
frame intervals; it does not prove GPU presentation or measure memory.

Use explicit assertions after each action. Keep fixtures deterministic and
record their size/version. All external requests are blocked, service workers
are disabled, and the server uses no-store. Service-worker upgrade and offline
acceptance belong in the existing functional suite, not this timing protocol.

Set `PERF_TOOLKIT_ROOT` in the consumer loader and pin its full Git revision in
`tests/performance-toolkit.json`. Set `PLAYWRIGHT_MODULE` only to an existing
Playwright install if the consumer has none. `CHROMIUM_EXECUTABLE` optionally
selects Chromium. `PERF_OUTPUT` must be a new path, normally under an ignored
artifact directory. `PERF_POWER` records a controlled condition such as
`AC; low-power off`; unrecorded power prevents a controlled comparison.
`PERF_INJECT_DELAY_MS=200` adds a labelled synthetic click-handler delay in the
test browser only. It never edits runtime assets. Run baseline, injected, and
recovery measurements using separate paths.

JSON v1 contains source/toolkit revisions, clean-source status, scenario,
fixture, timestamp, environment, conditions, experiment, and metric samples.
Reports include machine type but no hostname, credentials, or user data.
The comparator requires matching environment, conditions, fixture, scenario,
and toolkit. Different application revisions are expected. Missing/invalid
samples return incomplete; no timing signal exits nonzero, but unusable
comparison evidence exits 2. Existing output files are never overwritten.
