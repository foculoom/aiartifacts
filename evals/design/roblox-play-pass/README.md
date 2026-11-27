# roblox-3d-play-pass behavior cases

Synthetic cases for the [roblox-3d-play-pass skill](../../../plugins/design/skills/roblox-3d-play-pass/SKILL.md). Run each in a fresh session with the skill loaded and give the evaluator only the case input. Record the model, skill commit, tools and full output. These cases have not been run yet; no behavioral pass is claimed.

| Case | Input (fictional) | Expected observable behavior |
| --- | --- | --- |
| P1 | A tester with only a Linux machine and the game's source is asked for a full play pass. | Runs static and headless checks only; marks comfort, controls, readability and performance "not run"; does not report PASS for untested rows. |
| P2 | A phone build places a 30 pt jump button over the movement stick, and dragging the camera near it jumps. | Medium for size and jump/camera conflict, citing the 44 pt / 48 dp floors; observed only if seen on a device or Device Simulator at physical size. |
| P3 | A shop shows "LAST CHANCE, ACT NOW" with a 10-minute timer that resets on every join. | High (fake, resetting timer) and Medium (urgent copy); cites Roblox monetization guidance; suggests neutral copy. |
| P4 | An egg bought with gems (gems sold for Robux) shows only rarity names, with no percentages and no PolicyService check. | High: paid random item without numeric odds and without the ArePaidRandomItemsRestricted gate. |
| P5 | Head bob and camera shake are always on; one tester reports FMS 7 at minute 9 and keeps playing. | Medium (no off switch; FMS peak of 5 or more); not High, because no tester stopped. |
| P6 | Everything passes, but the fun rubric totals 8/20. | Reports a Low design concern; verdict stays PASS; does not block on the rubric. |
