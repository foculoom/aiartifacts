# Optional execution skills

The design plugin has no required third-party skill or runtime dependency. It does not install, vendor, or automatically update upstream instructions.

| Capability | Source | Tested revision | Installation and license |
| --- | --- | --- | --- |
| Frontend implementation | https://github.com/anthropics/skills/tree/main/skills/frontend-design | Not behaviorally tested or installed by this release; source reviewed only | Optional: use Skill Installer with repo anthropics/skills, path skills/frontend-design, and an explicitly reviewed commit via --ref. Inspect that revision's LICENSE.txt before installation or redistribution; do not treat this repository's Apache-2.0 license as covering it. |
| Editorial review | ../editorial, within foculoom/aiartifacts | Editorial 0.1.0; baseline commit 46645ac1af69f9a5e58b7cfed71b3d862215b7e0 | Optional repository marketplace plugin; Apache-2.0. Product voice briefs stay with products. |

Image generation, Figma implementation, and browser/game testing can use skills already available in the host. Their availability is not promised by this plugin. Record the actual skill/source revision in the consuming project's run report. Before adopting an upstream dependency, inspect its license and instructions, test it on a representative brief, and replace the untested marker with the exact tested commit and result. Do not imply inspection alone establishes compatibility.

The optional design-export checker uses Python's standard library only. It does
not install an image renderer or QR decoder. Record the separately available
renderer/decoder and actual final-raster result in the consuming project's
private handoff; the checker does not claim that validation itself.

On **2026-11-10**, the toolkit maintainer confirmed that the optional
`anthropics/skills` source was reachable at
[`2c5958ecac7cee2b583967a2c4981d0f4a75c579`](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/frontend-design).
This is a discovery snapshot, not an accepted or tested version: no revision is
pinned as an active Design dependency, so there is no accepted upstream baseline
from which to claim an update. Reassess authorship, exact included files,
license, environment and representative behavior if a product task actually
needs this optional workflow. The toolkit maintainer reviews this candidate at
that trigger; no recurring install or consumer change is scheduled.
