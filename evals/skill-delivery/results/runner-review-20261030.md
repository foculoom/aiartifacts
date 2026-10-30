# Independent development-runner review — 30 October 2026

Agent `/root/repo_tooling` reviewed the development-only case runner, its three
synthetic subprocess tests and their addition to the existing CI step. The
reviewer did not author those changes. **No blocking finding was identified in
this scope.** This review does not approve publication, authorize inference or
claim complete runtime isolation.

| Reviewed file | SHA-256 |
| --- | --- |
| `evals/skill-delivery/run_codex_case.py` | `5c87c4a91a3da0de98f0d3aa728df0b2618c6715b14a5333600df1e9c88772a4` |
| `evals/skill-delivery/test_runtime_runner.py` | `44a68cf5a976ff8ebf421b88c4b9ba948ff7a7f1833b8b74e0eab07fc495c5f7` |
| `.github/workflows/validate.yml` | `0bfc2a3bcf48d0899e633c689457c6472d576cbd2ca48fc82ce0eca67ceaa479` |

These are follow-up working-tree bytes after source commit
`211ad9da8b7a3d0740d1896a74c018ed3ad097be`; that commit does not contain the new
runner. A later commit must be matched to these hashes or receive review of its
changed scope. Readback after the interrupted session matched all three hashes;
the earlier tests were retained, not relabeled as a new execution.

Later source readback on 30 October matched all three reviewed files byte for
byte to commit `f5061ad33fcb553e623ca87b31759d6eb9d77282`. This binds this scoped
review to the committed runner/test/CI changes without claiming a repeated
test run or extending review to other changes in that commit.

The runner requires a successful existing ChatGPT login-status check before
starting inference and refuses an API-key login or unavailable authentication.
The subprocess environment uses a small allowlist: API keys, provider endpoint
overrides, parent session variables and `CODEX_HOME` are omitted. The preserved
ordinary `HOME` determines both the child login state and the host-skill search
root; no credentials are copied. Process-only flags ignore user configuration
and disable the named integration features. Their actual runtime coverage and
the complete initial context remain explicitly unverified.

New output paths preserve earlier attempts. Timeout handling signals the
child's process group and records the timeout/exit status. The runner retains
the prompt, full events, stderr, version and input-inventory identity for later
sanitization and independent grading. It does not install skills, acquire
credentials, grade answers or publish evidence automatically. Raw results must
remain private until the documented human/agent review and sanitization.

Independent validation used Python 3.12.14:

```sh
python3 -m unittest discover -s evals/skill-delivery -p 'test_*.py' -v
git diff --check
```

All **three synthetic tests passed**: API-key login refuses inference,
unavailable authentication refuses inference, and ChatGPT status permits only
the test stub. Whitespace checks passed. No real login, provider or live model
was called by these tests. CI adds only this standard-library test command to
the existing job; it changes neither permissions nor dependencies.

Next: preserve these results, independently grade the real case receipts, and
review the final evidence/source revision. Synthetic guard tests do not turn
missing live behavior, provider access or instruction isolation into a pass.
