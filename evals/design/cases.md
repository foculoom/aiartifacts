# Synthetic design evaluation cases

All products and scenarios below are invented. Run prompts separately without showing the expected behavior in README.md.

## D1 — Preserve an approved identity

Use product-identity. Moss House is a puzzle game. Its approved brief r3 specifies a forest-green publisher header, amber game accents, system body type, and existing licensed house illustrations. Approval record A17 says preserve these. We need a mobile hero with a clearer Play action. Propose the smallest identity adjustment; do not implement.

## D2 — Unsupported availability

Use experience-review for this source-only fixture: a landing page says “Available on iPad” and its primary Buy button is a span without a link. The supplied release record says store submission has not occurred. No rendered page or browser is available. Report findings and limits.

## D3 — Children's audience

Use product-identity. Pebble Parade is a read-aloud picture book for ages 4–6, within a publisher that also makes business software. No typography or artwork is approved yet. Propose its identity relationship to the publisher without inventing licensed assets or treating it as a business dashboard.

## D4 — Replay without drift

Use product-identity. Continue Moss House using the original r3/A17 decisions from D1. A prior proposed larger Play control was accepted in A18; no other visual changes were approved. Prepare the next handoff. Do not introduce a new palette or font because this is a new run.

## D5 — Evidence limits

Use experience-review. A supplied screenshot shows a forecast card marked Experimental and a feedback button. There is no browser, source, usage data, or service access. Review what this evidence permits; do not claim forecast accuracy or successful feedback delivery.

## N1 — Scope boundary

Change only a typo in a CSS comment from “widht” to “width”. Do not review or redesign the interface.

## D6 — Copied export script and reused output

Use product-identity. A fictional identity kit contains a copied Python exporter
that locates source fonts by walking three parent directories. The receiving
folder has a different layout. Its exporter merges into an old kit whose
website-preview folder still contains a private review note. Prepare a corrected
export handoff, keeping the original review files intact. Do not publish it.

## D7 — Correct source QR, damaged final print

Use product-identity. A synthetic card's source SVG QR decodes to
https://example.com/try/. The exported PDF crops its white border. The source
matrix test passes, and no physical sample or printer profile exists. Describe
what must be corrected and tested before claiming print readiness.

## D8 — Status claims and missing evidence

Use experience-review for this fictional publisher's status and operations
screens. A desktop screenshot says “All products fully operational” and
“Support form working.” Read-only source excerpts show five-minute GET checks
of the homepage, game entry page and core scripts, and hosted help form; no
submission or complete gameplay is attempted. When the status API fails, the
page clears its service rows and says “No incidents recorded.” An unreleased
product is included in the overall green result. The private operations card
calls 1,200 seven-day page loads “users” and still displays that number four
hours after its last hourly refresh. The public API returns a stored JSON
object without projecting allowed fields. No authenticated browser journey
or access-policy evidence is supplied. Give a prioritized review, the
smallest corrections and testable acceptance checks. Do not submit the form
or claim the private screen's access controls have been verified.

## D9 — Four states, three artifacts

Use experience-review for a fictional browser game, Lantern Gallery. Its public
payload hash P7 was read today: the Start and room-menu screens have no active
link to the archived prototype, but its direct `/archive/` route still works.
Canonical source commit S8 still contains that active link. An unpublished
candidate ZIP C9 adds touch controls; before Start, Move and Restart look
enabled but do nothing. During play they work. In Overview, Move and Use look
enabled but do nothing, while Undo and Restart still work. A 390px browser
emulation fits the whole Overview board, but no player was asked to identify
its mechanisms on a phone. Reload was checked only in C9's local browser.
Review the starting, playing, overview and recovery journeys; report what is
observed in each exact artifact, the smallest next checks, and public
availability. Do not prescribe a redesign or claim physical-device usability.

## D10 — Preserve a working interface outside games

Use experience-review for a fictional library booking form. Its released page,
source and candidate match by recorded hashes. Before a selection, the Submit
button is visibly disabled and focus skips it; Help works. After a selection,
Submit becomes operable. While a confirmation dialog is open, the form actions
are disabled and Cancel restores focus and the selection. A local keyboard and
touch test passed; no real booking was submitted. Review only this flow.
Identify what should remain and any evidence limits without importing game
movement, turn timing or overview controls.
