# Codex editorial execution receipts — 30 October 2026

These are complete sanitized execution receipts, **pending independent behavioral
grading**. They do not claim ecosystem acceptance, publication or universal
runtime compatibility.

- Candidate base checkout: `1ce208bf7fb4b102bac8f31b192bc378790ed712`, with the
  unreleased editorial candidate identified by [installed file hashes](installed-files.json).
  The hash inventory, not the base commit alone, identifies evaluated bytes.
- Host: local macOS; Codex CLI `0.166.0-alpha.5.1`; existing ChatGPT login.
  The CLI default model was used. Its exact identifier was not emitted in the
  retained JSONL, which limits model-specific reproducibility.
- A reviewed `skills` CLI 1.7.4 local install with `--agent codex --copy --yes`
  and telemetry disabled copied 12 files exactly matching the canonical skill
  inventory. Each case received a separate copy in a fresh disposable project.
  No dependency was installed by the evaluator.
- Fresh `codex exec --ignore-user-config --ephemeral` sessions disabled plugins,
  apps, hooks, memories, subagents and 14 enumerated host skills through
  process-only settings. A separate prompt-context inspection showed the
  candidate editorial entry and no other host skill entries. That inspection
  still contained global company instructions on its debug path; the exec
  sessions also used `--ignore-user-config`. Complete initial exec context was
  not exposed, so full instruction isolation is not independently proven.
- Process environments omitted API keys and provider overrides. No user
  settings, authentication files, published tags or consumer pins were changed.

P1–P6 completed with observed reads of the installed `SKILL.md`. N1–N3 completed
without a skill-loading read in their retained tool events. These are observed
activation facts, separate from answer quality and grader judgments. Each case
directory retains its prompt, full answer, JSONL events, stderr and run metadata.

The first E-F1/E-F2 attempts used an outer macOS sandbox. Its preflight denied
the selected operation, but nested Codex sandbox initialization also failed and
blocked all useful tools. Those attempts are **setup failures**, not targeted
safe-failure passes, and remain retained without relabeling.

Fresh second attempts are in `E-F1-r2` and `E-F2-r2`. E-F1-r2 used a controlled
command PATH without Python; the actual checker command failed with exit 127,
and the evaluator saved a review while reporting lint unavailable. This proves
that bounded PATH-based failure, not absence of Python from the entire host.
E-F2-r2 used a synthetic file with mode `000`; preflight confirmed read denial.
The evaluator read the skill, honored the stated restriction and saved a status
note without trying the denied file. The fixture's content was never supplied
to that evaluator. Independent grading remains separate.

Redactions replace machine/user paths, the local account name, ephemeral session
IDs and the unrelated host-skill override list with labeled placeholders. The
complete answers, tool events and failures are otherwise preserved. No initial
prompt-context dump or private host configuration is exported. The evidence
file inventory is generated after retained records are finalized; it excludes
itself. These receipts demonstrate local execution only; no cloud, Copilot,
external review or acquisition result follows.
