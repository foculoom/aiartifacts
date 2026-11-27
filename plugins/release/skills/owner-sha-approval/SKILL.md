---
name: owner-sha-approval
description: Require an explicit owner yes on the exact 40-character commit SHA before merging or deploying a release candidate. Use at publication time; not for ordinary review comments or for approving a different revision.
---

# Owner SHA approval

A review of an earlier commit, a yes on a branch name, or a yes on a pull request number is not approval of a later head. Production merge and deploy wait for the owner to accept the exact 40-character SHA that will ship.

## The rule

1. Name the full SHA, the product, and the action ("merge and deploy this revision," not "looks good").
2. The SHA on the usefulness report, the visual sign-off, and the release artifact must be the same full SHA.
3. The owner's yes must cite that same full SHA. A shortened SHA, a branch, or "the latest build" is not enough.
4. If the branch moves, the previous yes is stale. Prepare a fresh preview and ask again.
5. Record the yes in the project's ordinary approval channel, with the SHA, the date, and a pointer to the reviews. Do not invent an approval or treat a reviewer's PASS as an owner yes.

The optional helper `scripts/check_owner_yes.py --commit SHA --owner-yes-sha SHA` only checks that the two values are the same full SHA. It does not prove the owner said yes; the recorded approval still has to exist.

This skill grants no deployment authority. Combine it with [usefulness review](../usefulness-review/SKILL.md) and [release evidence](../release-evidence/SKILL.md) when those apply. Keep account identifiers and private approval URLs out of public artifacts.
