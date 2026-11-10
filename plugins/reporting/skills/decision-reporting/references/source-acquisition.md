# Source acquisition for a decision report

Use this reference when collecting a reporting window. The project brief supplies the expected accounts, form/site identifiers, approved categories, QA ledger, timezone, and any separately authorized aggregate sources. Keep those values, provider responses, customer data, and the resulting evidence note private. The public reporting helper cannot sign in or establish access.

## Establish a window and source receipt

Compute local-midnight UTC bounds with `scripts/weekly_window.py`; record the timezone, cutoff date, exact start-inclusive/end-exclusive instants, and observation time. Daylight-saving transitions can make a local week 167 or 169 hours. Do not substitute a rolling seven-day dashboard view for an exact local week.

For each source, record privately: expected and observed account/site identity, acquisition method, provider filter and timestamp bounds, observation time, pages or cursor completion, record/metric units, precision or rounding, excluded QA, and unavailable dimensions. Mark a source `ok` in the normalized input only when identity and full-window coverage are established. Missing access, an unexhausted cursor, a rounded boundary, or an unverified host filter makes the affected source incomplete; never represent it as zero. Preserve the original provider records in their existing system and retain only minimized triage metadata and aggregates locally.

## Feedback sources

- **Tally:** verify the signed-in owner and the intended form before reading submissions. Read the complete paginated interval, including an empty final page or explicit exhausted-cursor indication. Tally submissions are authoritative for form feedback. Use the project's QA/owner ledger and optional experience answers as recorded; absence of an answer is `unknown`. Do not turn anonymous submissions into unique people.
- **Gmail:** before searching, verify the connected profile equals the project mailbox. If it does not, stop that source without reading another mailbox. Use exact epoch-second bounds for the project's timezone window; date strings can be interpreted in the provider's default timezone. Exhaust pagination. Normalize one direct support case per thread, while linked form notifications refer to the Tally submission ID and are excluded from case counts. Read older unresolved cases only when needed for backlog age, and state whether that backlog read is complete.

## Website analytics and separate aggregates

- **Website analytics:** verify the intended provider site/tag, hostname, bot setting, and exact custom range. Record the provider's displayed timezone and precision. Keep a rounded or differently bounded figure separate from an exact-window total. Page views, visits, referrer counts, device counts, and performance samples have different units; do not sum them or infer customers. Mark unavailable performance dimensions null. Label deployment and controlled-test traffic as a limitation.
- **Other aggregates:** keep opt-in product events, store transactions, and operating evidence outside the feedback helper's three-source schema unless it is deliberately extended and privacy-reviewed. Query only approved aggregate fields; do not export event identifiers or join event rows to feedback or buyer identity. Report the observation date, coverage and limitations in a separate private companion section.

## Generate, compare, and stop

Normalize only approved category slugs into the [input contract](input-contract.md), run `scripts/report.py`, and check that its source states agree with the acquisition receipt. Compare the current report with the prior accepted report before notifying. Keep a generated incomplete report as evidence of a failed collection, but do not describe its absent source as zero. If an account is unavailable or a provider requires new authentication, report that exact limitation and continue independent authorized sources. A skill does not keep a session active, guarantee a schedule, or authorize replies, releases, permission changes, or purchases.
