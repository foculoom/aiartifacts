---
name: decision-reporting
description: Turn authorized feedback and website measurement into a private, source-traceable decision report with explicit missing data and minimal retention.
---

# Decision reporting

Use for recurring product feedback and website measurement reviews. Keep project configuration, customer data, and generated reports outside this public plugin.

## Gather before interpreting

Read the project's measurement brief and reporting window. Use authorized read-only connectors or exports. Reuse existing approved access; a reporting request does not authorize credential creation, broader access, replying, deletion, or tracking changes. Record source freshness and full-window coverage. A failed import is unavailable evidence, never zero feedback.

Normalize through the [input contract](references/input-contract.md). Tally is the primary intake; Gmail notifications reference the submission ID and are not additional feedback. Unlinked support threads can be separate cases. Deduplicate by source IDs, not names, email addresses, or text similarity. Supply one normalized record per support case. Explicitly tag known QA and owner tests; do not silently exclude unfavorable feedback. Record optional `usage_context`, edition, and build only when the source supports them. Missing context stays `unknown`; a `paid_used` response is reported use, not purchase verification. Carry unresolved earlier cases to calculate backlog age, and disclose incomplete backlog coverage.

Classify into the project's approved product, contact-type, and theme slugs. Keep free text and identity in their source systems; categories must not encode names, email addresses, or sensitive details. Do not copy subjects, message bodies, referrer URLs, query strings, tokens, or individual identifiers into reports. The script's allowlist is data minimization, not a certification that arbitrary configured labels are anonymous.

## Generate and review

Run `python3 scripts/report.py --input PRIVATE_INPUT.json --output PRIVATE_REPORT.json` from this skill's directory. Python 3.9+ and the standard library suffice. This offline helper implements separate normalized Tally, Gmail, and analytics adapters; it does not authenticate to those services. A source export must be collected and normalized separately. Read [the synthetic fixture](references/synthetic-input.json) for a runnable example.

Inspect `status`, source coverage, observed counts versus complete totals, QA/owner-test/duplicate exclusions, free and paid reported-use counts, unknown experience context, repeated themes, and aging unresolved cases. Recommendations are triage prompts, not inferred demand or conversion gains. Do not convert reported paid use into verified buyers or revenue. Missing analytics dimensions remain null. Normalize page/referral/device breakdowns to the approved categories and document their unit and provider limitations in the private evidence note. Visits are not people. Review source cases before committing to product changes. Record the exact toolkit commit and project measurement brief revision in a private companion evidence record; `skill_revision` pins the helper's plugin version.

## Recurrence and retention

Prove one full source-to-report run before enabling a requested schedule. Use the host's scheduling tool, preserving the user's timezone and notification preference. Compare findings and source failures with the last successful report; notify only on meaningful changes, required decisions, or failures when requested. Do not send automatic customer replies. A successful report with missing sources is operationally generated but remains incomplete evidence.

For a 12-month aggregate retention policy, keep reports in a private directory and remove only generated reports older than 12 calendar months under that approved policy. Do not alter source-system retention. Normalized inputs are temporary; remove them after verification unless a specific private triage requirement needs them. Preserve minimal status/category metadata rather than message copies. Do not infer scheduling or deletion authorization merely from loading this skill.
