# Local Automation 0.1.0

The [local-credential-runner skill](skills/local-credential-runner/SKILL.md) turns repeated credential handoffs into explicitly reviewed local tasks. It includes a macOS Keychain launcher, a 1Password service-account resolver, synthetic tests and a private-profile runbook. It does not provision credentials, deploy a product or schedule itself.

The runner has no generic secret-export or arbitrary-command operation. Its tested boundary is accidental task/configuration drift and scoped secret delivery to trusted reviewed programs. It is not an OS sandbox against same-user malicious code. Consumer account references and execution evidence stay private.

Run the synthetic suite with `python3 -m unittest discover -s plugins/automation/skills/local-credential-runner/tests -v`. Compile and validate Keychain/provider access on the actual Mac before claiming unattended execution. Credential availability never replaces a release decision, agreement, financial authorization or required human review.
