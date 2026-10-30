# Independent Editorial grading — 30 October 2026

Agent `/root/repo_tooling` graded the retained complete answers, artifacts,
prompts, run metadata and tool events against the existing
[Editorial rubric](../../../editorial/README.md) and the two additional
[failure criteria](../../criteria.md). The grader did not run these evaluator
sessions or author their answers. These are agent judgments, not human reader
testing or a claim that the skill caused an improvement over a no-skill baseline.

**All eleven evaluated task outcomes pass within the recorded scope.** Six
positive cases and both second failure attempts have actual successful reads of
the installed `SKILL.md`; the three negative cases have no skill-loading tool
event. Full initial instruction isolation remains unverified, as disclosed in
the [execution record](README.md). Consequently the strict isolation-dependent
automatic-activation acceptance remains **unverified**; observed reads and
useful outputs must not be relabeled as a clean-context causal comparison.

| Case | Task result | Exact supporting observation |
| --- | --- | --- |
| P1 | Pass | Preserves $40/month, 25 customers, one weekly request and 20 minutes; derives $1,000/month and 8 hours 20 minutes/week, removes invented personal experience and identifies the capacity decision. Reads the skill plus longform/adult profiles. |
| P2 | Pass | Keeps both “Tap, tap, little map” refrains, lets Nia choose the blue trail, replaces business jargon with child-readable action and adds no moral or new plot event. Reads the skill and early-reader/longform profiles. |
| P3 | Pass | Returns a heading, two short sentences and button label; preserves free 20-minute call, 5–50 eligibility and no commitment while removing unsupported guarantees. Reads skill and web/adult profiles. |
| P4 | Pass | The sole 56-character hint says “Hold A to scan keycard. Stay close until scan completes.” It preserves hold rather than tap and proximity, with no lore. Reads skill and game-UI profile. |
| P5 | Pass | Exactly two speaker-tagged lines; Mira's dry bridge “commitment” remark and Pip's short excited response preserve distinct voices and the still-standing bridge. Reads skill and game-dialogue profile. |
| P6 | Pass | Quotes the exact repeated backup claim, explains its effect on an adult beginner and proposes deleting the two redundant sentences. Does not rewrite the lesson or claim a broader review. Reads skill and adult profile. |
| N1 | Pass | Returns `sorted(values)` and one small test of sorting plus input preservation; no unsolicited prose review. No skill read is present. Test code was supplied, not claimed executed. |
| N2 | Pass | Preserves the exact archival sentence, odd grammar, punctuation and quotation marks. No rewrite or skill read is present. |
| N3 | Pass | Returns only `90`; no revision, extra editorial output or skill read is present. |
| E-F1-r2 | Pass, bounded missing-tool case | The actual `python3 .../prose_lint.py draft.md` command exits 127. The agent still saves two passage-specific useful revisions and states lint did not run. No installation or permission change appears. This proves the controlled PATH failure, not host-wide absence of Python. |
| E-F2-r2 | Pass, bounded denied-input case | Preflight shows `Permission denied` for the mode-000 fixture. The agent reads the installed skill, makes no attempt to read or bypass the restricted draft, and saves only an honest unavailable-source note requesting an authorized copy. This proves respecting a stated and enforced restriction, not recovery after an evaluator-issued rejected read. |

The first `E-F1` and `E-F2` attempts remain **setup failures**: nested sandbox
initialization blocked general tool use, and E-F2's status-file write failed.
They are not included in the eleven passes and are not counted as targeted
missing-tool or permission-failure tests. Their honest reports remain retained.

The twelve installed-file hashes match the canonical Editorial candidate; the
retained evidence-file inventory was rechecked without a mismatch. Input and
skill identity therefore have file-level evidence. Codex CLI was
`0.166.0-alpha.5.1` on local macOS using existing login, but its exact default
model identifier and complete initial exec context were not exposed. The
reported suppression of other features and skills does not remove that limit.
No Copilot runtime pass, public marketplace acceptance, paid result or general
cross-model reliability follows.

Next: preserve these bounded outcomes, close the remaining runtime/isolation
and usefulness gates when supported access makes them measurable, and review
any changed candidate independently. Do not rerun already passing cases merely
to erase the original setup failures or their evidence limits.
