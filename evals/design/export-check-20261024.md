# Design export checker — local candidate validation

Scope: implementing agent's source review and synthetic Python unit tests.
This record contains no product artwork, private source paths, customer data,
actual print proof or public deployment evidence.

Seven synthetic tests passed: explicit absolute source/output roots without
creation; preservation of existing and dangling-linked output entries; exact
payload hashes with unverified-release labels; same-count file substitution;
extra review instructions and changed bytes; linked files/directories; and
malformed manifest paths/hashes. Fixtures are temporary invented HTML/SVG bytes.
The catalog/reference validator passed for five plugins and six skills.

D6 and D7 were added as behavior-evaluation prompts with expected outcomes.
They have not been run as independent model studies. No real QR was decoded by
this checker; the guidance requires a separately observed final-raster decode,
physical camera/stock checks and vendor proof when applicable. Passing a local
inventory test is not evidence for any of those outcomes.

No dependency, CI file, tag or consumer pin changed. The Design manifest is
0.1.1 as an unreleased local candidate. The new unit suite is documented for
local execution; add it to CI through a separately reviewed configuration change
before release. Existing released snapshots remain intact.
