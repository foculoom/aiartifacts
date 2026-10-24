---
name: local-credential-runner
description: Prepare and validate narrowly scoped local automation using an existing 1Password service account and macOS Keychain. Use when repeated credential prompts block reviewed tasks. Do not use this to authorize releases, payments, agreements, new provider scopes, or a cloud runner.
---

# Local credential runner

## Establish scope first

1. Identify the concrete task, its existing authorization, exact provider account/resources, and intended read or write operations. Credential availability grants no additional authority.
2. Inventory only authorized vault metadata. Resolve only task-specific items by stable IDs. Diagnose missing, duplicate, expired, malformed or inaccessible entries without revealing values. Do not dump a vault, print credentials, use clipboard transport, or put secrets in command arguments.
3. Reuse an existing service account only after verifying its identity, active state and exact accessible vault set. A desktop CLI failure may be an execution-environment problem; test the actual environment before concluding no account is configured. Never evade an approval rejection.

## Prepare and review

Use the [implementation runbook](references/runbook.md) and optional [runner](scripts/runner.py). Keep project configuration private. The compiled [Keychain launcher](scripts/keychain.swift) accepts only a fixed task list, pins the profile/runner/interpreter hashes and has no credential-export operation. Each task pins its wrapper, imported helpers and configuration inputs. Prefer self-contained standard-library Python with `-I`; review dependencies and environment side effects explicitly.

Before bootstrap, test synthetic missing, expired/revoked, malformed, wrong-scope and inaccessible credentials; changed task files; unapproved tasks; secret-printing children; and absent/incorrect result evidence. Get an independent code review for credential handling and the concrete task policy. Do not treat nonempty `authorization` prose as proof of user authorization: compare the fixed task's effects with the actual request.

The optional implementation is an operational guardrail for trusted reviewed code, **not a sandbox against software running as the same OS user**. The owner and same-user processes may modify code or read process memory. Pinning catches accidental drift; it does not provide tamper resistance against an active local adversary.

## Bootstrap and validate

Bootstrap once using already-authorized desktop access or a separately reviewed secret-entry flow. Tokens move only in memory to Keychain. Do not grant broader access to make a check pass. Run a fresh process twice and, where supported, with desktop 1Password locked. Verify provider identity/scope and read-only workflow preflights before allowing a task to mutate state. A locked Keychain, unavailable Mac, expired credential, required MFA or required human action remains a dependency; do not fall back to broader credentials or repeated interactive prompts.

Require a fresh task report bound to its invocation and expected target. Count a provider check as verified only if that report's required checks passed. Record source/file hashes, scope, runtime, timestamp and limits. Keep reports and credential references private. Do not claim all workflows are automated from one successful task.

## Maintain

- Recompile/review deliberately after code, profile or runtime updates; never silently accept changed hashes.
- Rotation is an explicit maintenance event. Revoke/replace credentials through the authorized provider flow. Existing Keychain entries are never overwritten automatically. See the recovery procedure in the runbook.
- Keep scheduling separate. Reuse an existing authorized local automation instead of adding a duplicate. Never add CI secrets or a cloud runner without an explicit decision.
- Publish methods and synthetic tests only. Keep product artifacts, account IDs, vault references and reports in their owner repositories or ignored private local state.

## Return

Report implemented tasks, exact verification evidence, observed access limits, unresolved human steps and next deliverable. Never equate a merged change with deployment or an executed command with a passed release gate.
