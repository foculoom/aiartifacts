---
name: audio-pr-proof-of-work
description: Run and record loudness, true-peak, loop-wrap, and second-opinion checks on pull requests that change game or product audio. Use before opening or updating such a PR; not for generating new audio or for importing a model's output into the build.
---

# Audio PR proof of work

Run this on every pull request that adds or changes audio. Paste the results into the PR body under **Audio checks**, and keep them short.

## Checklist

1. **Clips under review.** Render or capture each changed cue or loop to WAV, at speed 1 and in the scene it plays in. List the files.
2. **Scripted checks**, for example ffmpeg `ebur128` for integrated LUFS and true peak, plus a seam check at loop joins:
   - Integrated loudness (LUFS) and true peak per clip, against the project's own targets. Broadcast programmes often use EBU R 128 (−23 LUFS, true peak not above −1 dBTP); games and short UI cues may use a different target. Write the project's target next to the measurement. Do not treat a broadcast number as a product target if the project has not adopted it.
   - Clipping: report any samples at or above 0 dBFS, and the true-peak margin.
   - Loop wraps: for each loop, measure the jump and the correlation across a short window (about 80 ms) at the join. Report pass or fail. A negative correlation or an audible step is a click.
3. **Second opinion.** Using only the project's designated audio-understanding account and model, ask for the mood, whether the clip fits the scene (give a one-line scene and emotional beat), and any artifacts. A public example of such an endpoint is [fal.ai audio-understanding](https://fal.ai/models/fal-ai/audio-understanding). This skill does not require that vendor. Paste a one- or two-line summary per clip, plus the estimated cost.
   - It is a second opinion, not the verdict. It may raise at most a Medium, and a person decides.
   - Nothing the model generates is imported into the build without the owner's explicit yes. Already approved code-generated audio stays approved.
   - Do not put API keys or vendor account names in the PR.
4. **Usual proof.** Include the local test commands and results, plus the audio size budget (bytes used against the limit).

## PR body template

```markdown
### Audio checks
| Clip | LUFS-I | True peak | Clipping | Loop wrap | Second-opinion mood / fit |
|---|---|---|---|---|---|
| ... | ... | ... | none | pass | ... |
Second-opinion flags: none / Medium: ...
Budget: N B of M B
```

See [sources](references/sources.md) for the loudness recommendations. Keep raw recordings and paid-account receipts in the owning project.
