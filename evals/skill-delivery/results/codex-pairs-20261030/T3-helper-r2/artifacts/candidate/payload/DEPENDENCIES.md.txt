# Dependencies and provenance

| Component | Requirement | Provenance and limits |
| --- | --- | --- |
| Skill instructions and profiles | A runtime that discovers Agent Skills and can read this folder | Foculoom AI Artifacts; Apache-2.0. Record the exact tested source commit and installed-file hashes. Format support is not behavioral acceptance. |
| `scripts/prose_lint.py` | Optional Python 3.9+; standard library only | Foculoom-authored advisory checker; does not rewrite, establish facts or identify authorship. No package installation or network required. |
| `tests/test_prose_lint.py` | Development only: Python `unittest` | Synthetic fixtures; no customer text or account access. Tests do not grade writing quality. |
| Project voice, facts and source prose | Supplied by the user with appropriate access | Consumer-owned inputs, never bundled automatically. Respect read/write permission and retain private material in the consuming project. |

No external skill, MCP server, SDK, model provider, credential, browser, macOS
service or unrelated Foculoom product is required. A host may use its ordinary
model subscription and filesystem tools. Do not install missing tools or obtain
broader access merely to claim completion; report unperformed optional lint or
unreadable source explicitly.

This folder includes the [Apache-2.0 license](LICENSE). The profiles, synthetic
examples and helper originate in `foculoom/aiartifacts`; no third-party prose or
code is vendored by this distribution change. Preserve applicable notices when
adding material. A license label alone is not proof of rights to new content.

Distribution tools are separate development dependencies. Review and pin their
versions, licenses and sources before use. Their supported-agent lists do not
certify this skill, and installer telemetry is not user demand or revenue.
