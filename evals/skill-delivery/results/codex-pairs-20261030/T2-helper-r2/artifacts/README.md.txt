# Editorial writing contribution review packet

Prepared **2026-10-30**. Local preparation is complete; external submission is not authorized. Start with [licensing and requirements](licensing-and-requirements.md), then [intended files](intended-files.md), [validation](validation.md), and [decisions](decisions.md).

The supplied skill declares Apache-2.0 in `SKILL.md`, includes the full Apache-2.0 `LICENSE`, and records Foculoom provenance in `DEPENDENCIES.md`. The supplied existing `editorial` plugin version 0.1.1 also declares Apache-2.0. Awesome Copilot's supplied contribution policy requires MIT for direct repository contributions. The unchanged standalone candidate is therefore **held for a rights/licensing decision**, not ready to submit under MIT.

The existing external-plugin issue route is a plausible alternative that retains Apache-2.0. It still requires public-source verification, quality gates, owner authorization and human maintainer acceptance. This packet does not choose a new license or attest those stages.

| Artifact | Purpose |
| --- | --- |
| [Direct PR draft](drafts/direct-pr.md) | Conditional draft targeting upstream `main`; explicit licensing hold |
| [External-plugin issue draft](drafts/external-plugin-issue.md) | Existing plugin metadata and candidate immutable SHA; unchecked attestations |
| `skill-candidate/` | 12 unchanged allowlisted files, exact manifest and ZIP |
| `plugin-candidate/` | 14-file reconstructed local plugin, unchanged manifest and notices, exact manifest and ZIP |
| `evidence/` | Actual command logs, input/source hashes, package hashes and tool environment |
| `behavior-cases/` | Synthetic input-only cases and separate reviewer rubric; not executed |
| `prepare.py` | Local evidence-generation script; fresh candidate directories required to rerun exports |

Source identity: supplied `foculoom/aiartifacts` revision `211ad9da8b7a3d0740d1896a74c018ed3ad097be`, canonical path `plugins/editorial/skills/editorial-writing`. All 14 supplied skill-file hashes match `source-record.json`; all 15 files under `source/` are unchanged. This workspace has no Git checkout, so the revision is supplied provenance rather than independently verified Git ancestry. Remote plugin bytes have not been compared to the reconstructed local package.

No dependencies were installed. No licensing, source files, global configuration, PRs, issues, releases or public listings were changed. As observed on 2026-10-30, this run establishes local review-package availability only; current customer acquisition through the remote plugin or Awesome Copilot was not verified. No acceptance, listing, installation or customer receipt is claimed.
