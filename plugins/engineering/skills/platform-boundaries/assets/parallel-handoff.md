# Parallel work handoff

Keep the completed record with the owning project. Fill only applicable fields;
mark unperformed checks and unavailable evidence explicitly. Do not include secrets.

## Assignment

- Lane / owner / coordinator:
- Intended result and acceptance criteria:
- Owned paths; excluded/shared paths and their owner:
- Dependencies; allowed independent work if blocked:
- Workspace / branch / base SHA:
- State: working, blocked, ready-for-review, reviewed, or integrated

## Immutable result

- Repository / full head SHA / changed paths / PR:
- Candidate path and status: local QA, release candidate, or deployed:
- Inventory/profile; manifest SHA-256; archive SHA-256 if applicable:
- Canonical content/source pins and permitted transformations:
- Commands and results; evidence paths; tested environment:
- Untested behavior / mocks / remaining issues:

## Review and integration

- Reviewer / independent or self-review / reviewed full SHA:
- Major findings and disposition; required checks/reviews:
- Reused evidence and proof its inputs are unchanged:
- Coordinator's next action; exact dependency or approval still required:
- Merge SHA, if integrated; release remains a separate gate:

Invalidate this handoff's readiness when its source, inventory, payload or target
changes. Replace the identities and review affected evidence before proceeding.
