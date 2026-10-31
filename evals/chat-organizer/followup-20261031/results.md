# Follow-up comparison result — October 31, 2026

The [three-pair protocol](cases.md) and [held-out criteria](criteria.md) were
committed and pushed as `8e3563e89f1e0ee06da3c008a583a201f54be27e`
before any model trial. The case author did not inspect the skill, earlier
outputs or original cases. A separate preregistration review checked unique
IDs, counts, section/project references and scoring consistency. Its requested
clarifications were incorporated before that commit. The skill was unchanged:
`SKILL.md` SHA-256
`cd664af43f4b96d6dd31d65f0bdbd88dc2d3f078479872b468f52f177b18be05`.
The input-only cases and held-out criteria have SHA-256 values
`94c4d69f298c254da8e9976431ae57766127d21451eddc455f48b83e83e527a0`
and `390d84072904acba3ced82f6f3fea64dcaa5d735a99825de9cc70ecf3cc0c715`,
respectively. Full traces, randomized arm mapping, first attempts and fictional
state receipts remain outside this repository.

All six final sessions used the existing signed-in Codex CLI
`0.166.0-alpha.5.1`, requested `gpt-6.1-sol` / `medium`, and recorded that
same model and effort in the local runtime. Backend identity was not reported.
Both arms used the same prompt, tool script, starting state and time budget;
only the candidate skill differed. The skill loaded in all three skill arms
and in none of the baselines. The runner's user-level instruction overlay
remained visible despite isolation flags, shared by both arms. A first P1
baseline invocation was denied by the local sandbox before model execution;
that attempt was retained, then the identical run completed in the already
authorized environment. No final run timed out or exited nonzero.

| Pair | Matched prompt SHA-256 | Observed actions and final state |
| --- | --- | --- |
| P1: advice only | `5893e0c557edc0a41083fcde1bb4359157dee81d128144cb452d32fcc86fa686` | Both arms made zero changes and gave ordered cleanup advice. |
| P2: lease restoration | `fa7961c9c285a00ccae48902904e4332d593c3f4a8fde05441161f2922da0d90` | Both arms had six receipts: one section, one restore, three section moves and one rename. The intended three chats ended in Moving; unrelated chats and archive states were preserved. |
| P3: mixed inventory | `c438531580969041ba2e23f0f3589055da42dd6c2303b4515fba637e7f56c682` | Both arms had nine receipts: one section and the same eight fundraiser-chat moves. Other 26 Codex chats, titles, pins, archives and project memberships were unchanged. Both identified the inaccessible ChatGPT work and 13 unseen export rows. |

An independent agent scored randomized A/B answers and state/action records
without knowing skill identity. The mapping was revealed only after its
judgments were fixed. Scores are practical outcome / preservation / user effort
on the predeclared 0–4 scale, followed by the weighted total.

| Pair | Skill | Same assistant without skill | Blinded practical judgment |
| --- | --- | --- | --- |
| P1 | 4 / 4 / 3 = **3.85** | 4 / 4 / 4 = **4.00** | Tie; skill answer added a little avoidable advice, without material loss. |
| P2 | 4 / 4 / 4 = **4.00** | 4 / 4 / 4 = **4.00** | Tie; both verified the same requested state. |
| P3 | 4 / 4 / 4 = **4.00** | 4 / 4 / 3 = **3.85** | Tie; baseline added a broader review list, without material loss. |

No severe failure or material regression was found. There was **no clear
practical improvement in any follow-up pair**, below the required two of
three. The [first comparison](../results-20261031/README.md) remains one skill
improvement and two ties; this supplementary result does not replace it.
Therefore the Chat Organizer candidate remains **held from source merge and
distribution**. Repeating additional comparisons until a favorable split
appears would not establish added value. No behavioral defect was demonstrated
that justifies a narrow fix and rerun of these same cases.

This suite tested fictional Codex organization and honest manual handoff for a
partial ChatGPT export. It did not test direct ChatGPT account compatibility,
friends' or family's installations, or real account organization. As observed
October 31, [draft PR #35](https://github.com/foculoom/aiartifacts/pull/35)
exposes candidate source, while Chat Organizer is absent from the default-branch
catalog and public Plugins Directory. Candidate ZIPs remain private. The
published v0.5.0 toolkit and consumer pins are unchanged. The next decision is
whether the owner wants to change the acceptance target or invest in a
materially different organizer design; no release follows from these tests.
