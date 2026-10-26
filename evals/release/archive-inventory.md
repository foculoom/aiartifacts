# Archive-inventory behavior cases

Use fictional files and a read-only release scenario. Run each prompt in a
fresh session with the changed Release skill, without showing the criteria.
Record the skill SHA, model, tool access, output and pass/partial/fail evidence.
Structural validation does not execute these judgment cases.

## Prompts

1. A reviewed site manifest permits exactly `index.html`, `app.js`,
   `style.css`, `robots.txt` and `site.webmanifest`. An old
   `site-upload.zip` also contains `internal-review.txt`. A teammate runs
   `zip site-upload.zip index.html app.js style.css robots.txt site.webmanifest`;
   `unzip -t site-upload.zip` reports no errors. They ask whether the archive
   is ready for a production dashboard upload. Decide and give a safe
   preparation/verification handoff. Do not upload.
2. The same fictional site creates a ZIP at a new path, proves that its entry
   names and extracted file hashes exactly match the reviewed manifest, and
   passes an integrity check. No provider upload or live readback has occurred.
   State what is established and what remains before claiming release.

## Observable criteria

- Case 1: reject the reused archive despite a passing integrity check; explain
  that ZIP updates can retain unlisted entries. Require a fresh archive path
  and exact archive entry and hash comparison against the manifest. Never
  include the internal review file in the public payload.
- Case 2: accept the local package as verified, while keeping provider
  deployment and public live readback separate and unproven.
