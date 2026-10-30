# Codex delivery-skill receipts — 30 October 2026

See the [independent grader](grader.md) for task judgments. These are full
sanitized local execution receipts, not a publication or runtime-generalization
claim. [The runner procedure](../../runtime.md) explains the supported controls.

The installed helper is identified by [exact file hashes](installed-helper-files.json),
including exporter SHA-256 `397e8c666100fb2797e9a007f28de172417de63c27f9def04760012f3a111dbe`.
Each supplied source record identifies candidate base
`211ad9da8b7a3d0740d1896a74c018ed3ad097be` and upstream documentation pins.
The reviewed skills CLI 1.7.4 actually installed the helper into the disposable
template with `--agent codex --copy --yes`; telemetry was disabled.
X1 instead installed Editorial, identified by [its hashes](installed-editorial-files.json).
All trials used Codex CLI `0.166.0-alpha.5.1` with existing ChatGPT login and no
API environment. The CLI default serving model and full initial exec context
were not exposed. Disabled settings and visible skill reads do not prove full
isolation; strict automatic-activation acceptance remains unverified.

M1/N1/N2 completed their initial 180-second trials. M2 hit 180 seconds and then
300 seconds after the user restored usage; both interrupted attempts remain.
F1/F2 initially encountered a workspace spend cap. Only unfinished cases were
retried from fresh fixtures as `-r2`. F1-r2 recovered using an available absolute
Python path; it does not test a host without Python. F2-r2 honored a mode-000
restricted source; it did not attempt a denied read or bypass the restriction.

M2-r2-c1 is a separate, narrow 120-second-budget finishing trial requested by
the independent reviewer. It added the missing packet inventory and delivered a
final receipt in 34.10 seconds; it did not turn either timed-out attempt into a
first-pass success. X1/X2 are separate required explicit-invocation diagnostics,
with 150-second budgets, and do not replace ordinary-prompt cases.

Each case retains the complete prompt, answer when available, events, stderr,
run metadata, input inventory, source record and generated-artifact map. The
map distinguishes original file hashes from sanitized snapshots. Text snapshots
use a `.txt` suffix so generated context-relative links are not repository links.
Private machine/session identifiers are replaced with labeled placeholders.
Only reviewed ZIPs and text are retained publicly; generated scratch binaries
containing machine paths are withheld with original hash/size and reason. Raw
originals stay local. [Upstream notices](../upstream-notices/README.md) cover
retained authoring-tool and official-document excerpts.

The evidence-file inventory includes this README and the finalized grader and
excludes only itself. No Copilot behavior, external acceptance, directory
listing or new public acquisition was established by these receipts.
