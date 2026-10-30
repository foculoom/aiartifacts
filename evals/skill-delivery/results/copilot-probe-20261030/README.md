# Copilot access probe — 30 October 2026

GitHub Copilot CLI 1.0.54 was executable. A bounded connectivity probe using
existing GitHub CLI authentication reached the provider but returned exit 1 in
3.88 seconds: `Access denied by policy settings`. The retained JSONL also has a
separate organization-policy warning about third-party MCP servers. The response
does not identify which subscription or policy condition caused the denial.
No skill test ran and no runtime-compatibility pass is claimed.

Prompt: `Return the number 437 only.` No `--model` was supplied; the provider
denied access before a selected model identity or answer was reported.

```sh
copilot --no-auto-update --no-custom-instructions --disable-builtin-mcps \
  --no-remote --no-ask-user --output-format json \
  --available-tools=view,glob,grep,skill \
  --allow-tool=view --allow-tool=glob --allow-tool=grep --allow-tool=skill \
  -C '<empty-disposable-project>' -p 'Return the number 437 only.'
```

Fresh `COPILOT_HOME` and `COPILOT_CACHE_HOME` isolated configuration/history.
Test-only settings disabled memory, hooks, auto-update and IDE auto-connect.
The child retained only ordinary existing process environment values; API keys,
GitHub token variables and custom-provider overrides were omitted. Credentials
were neither printed nor copied; the CLI's supported GitHub CLI fallback used
existing authentication. No account, policy, login or global setting was changed.

The [complete stdout](copilot-probe.jsonl) and [stderr](copilot-probe.stderr)
retain the denial. A later evaluation requires an already-authorized runtime
where Copilot access is available; do not retry this unchanged condition or
alter account policy as part of skill packaging. Installer success is a separate
claim from provider access and useful skill behavior.

## Retry after restored usage

After the owner reported restored workspace usage on October 30, one bounded
connectivity check was retried. The sandboxed attempt could not access existing
authentication and returned no authentication information; it is a host-access
result, not evidence of invalid credentials. The same 437-only probe with access
to the existing supported sign-in returned the original provider policy denial
in 3.08 seconds. No skill, account change, login flow or policy modification was
performed. The sandbox attempt and the existing-auth retry are retained in
`restored-sandbox/` and `restored-existing-auth/`; only temporary paths and session
identifiers are redacted. The restored workspace usage did not resolve this
separate Copilot access gate. Further unchanged retries are not indicated.
