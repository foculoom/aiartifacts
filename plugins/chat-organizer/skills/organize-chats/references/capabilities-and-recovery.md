# Capability and recovery guidance

The skill supplies decisions and workflow. The recipient's host supplies data,
authentication, authorization, and mutations. Discover tools by purpose rather
than assuming names or parity between Codex and ChatGPT accounts.

| Capability | Use when available | If unavailable |
| --- | --- | --- |
| List and read chats, including archived pages | Inventory by stable ID and inspect turns | Use an authorized export or user-supplied inventory; state coverage |
| Rename, pin, archive, or group chats | Apply only the approved organization | Provide exact manual actions; do not claim application |
| Read project instructions, sources, sharing, and memory mode | Check both source and destination before moving | Defer membership changes; continue independent organization |
| Inspect existing automations | Preserve target IDs, schedules, state, and notifications | Avoid changes that depend on unknown automation targets; mark the gap |
| Supported browser control | Use current visible UI for a missing dedicated operation | Leave that operation pending; do not assume a hidden API |

For browser fallback, obtain fresh UI state after each action and verify the
resulting chat ID and state. A flow observed in one account is not a contract for
another. Do not ship recorded selectors, session handles, IDs, or account URLs.
In particular, some hosts may require restore → move → rearchive for an archived
chat, while others may support direct moves or prohibit them. Determine the
actual supported path before acting.

An ambiguous timeout, navigation, or error does not establish failure. Read the
current state by ID before another mutation. For temporary unarchiving, record
the restoration obligation before the first action. On interruption, first
reconcile project membership and archive state, then rearchive an originally
archived chat. Do not repeat a completed move or leave a chat active merely
because the subsequent move failed.

Project memory mode, sharing, and access can make a destination incompatible.
Do not change sharing or memory settings just to complete a move. Report the
specific limitation and preserve the chat's current membership. If inventory
pages overlap, deduplicate by ID; if a page is missing, say how many were
observed and which totals remain unverified. Store migration records privately
in the recipient's own workspace, subject to their retention preferences.
