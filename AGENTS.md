# Contributor instructions

## Portable handoff and release evidence

Start from the current default branch and record its exact revision and working-tree state; preserve existing changes. Read [README.md](README.md), [HANDOFF.md](HANDOFF.md), and [CHANGELOG.md](CHANGELOG.md) before changing source or claiming release state. Dated checkpoints are evidence to recheck, not proof of current external state. Changes on main are unreleased source until a separately reviewed tag and release; installed consumers keep their explicit pins.

For material work, update the repository handoff in the same PR with reproducible setup and check commands, exact source and reviewed head, actual test results, artifact inventory, deployed and live revision/time where applicable, missing evidence, remaining gates, and the next action. Keep it usable from a fresh clone: credentials, private captures or data, ignored files, absolute machine paths, browser sessions, and local automations do not travel with Git.

Use a focused branch and PR, independent review of its exact head, and required checks before merge. Identify an agent review as such; obey any stricter reviewer-identity rule. Source merge, built artifact, provider deployment, and live readback are separate states. Follow the owning release runbook with one release owner, verify a fresh artifact and exact live result where applicable, and hold unresolved gates. For reusable lessons from product work, contribute only generic, synthetic examples through a separate reviewed PR. Preserve published tags and explicit consumer pins unless their owners separately review an update.
