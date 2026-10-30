# Sources retained in evaluation traces

The complete synthetic evaluation tool traces can include substantial excerpts
of inspected upstream instructions and authoring tools. Preserve these notices
with those records; none of this adds an upstream runtime dependency to the
distributed Foculoom skills.

| Material | Source identity | Terms |
| --- | --- | --- |
| Awesome Copilot instructions, contribution guide and external-plugin form | [github/awesome-copilot](https://github.com/github/awesome-copilot/tree/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd), commit `5269f7ea2d6c3a9bfda5ed878b6726cf509121fd` | [Retained MIT notice](awesome-copilot-LICENSE.txt) |
| skills CLI creation and command documentation | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/92a9a34ac3bf88e695e468b90c7bf32f163d32c8), commit `92a9a34ac3bf88e695e468b90c7bf32f163d32c8` | [Retained MIT notice](skills-cli-LICENSE.txt) |
| Existing OpenAI bundled skill-creator instructions and scripts | Local installed snapshot of [skill-creator](https://github.com/openai/skills/tree/main/skills/.system/skill-creator); exact supplied file hashes are recorded under `existing-authoring/` in each case's input inventory. An upstream commit match was not established. | [Retained Apache-2.0 license](skill-creator-license.txt) |

Both comparison arms received the same source snapshots. The newly evaluated
Foculoom helper was supplied only to the helper arm. Recorded source reads do
not establish upstream endorsement, published-package equivalence or runtime
acceptance. Public text snapshots disclose path redactions through their
artifact maps; original local trial bytes remain separate evidence.
