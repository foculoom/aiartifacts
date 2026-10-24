# Release evidence evaluation — 2026-10-23

Revision: release plugin 0.1.0 in repository v0.3.0.

- Five deterministic tests cover payload changes, symlink rejection, unsafe origins/paths, index URL mapping, content mismatch, and HTTP failure reporting.
- Anonymous HTTPS integration readback matched all 33 files in a previously authorized static deployment. No credentials or publishing operation were used by the verifier.
- The first integration trial returned HTTP 403 with Python’s default user agent. A standard curl user agent matched the established readback client; failures now record HTTP status without response bodies.
- All 27 existing editorial tests and the catalog validator pass.

These are author-run checks. Browser interaction, concurrent deployments, and host content rewriting are procedural review cases, not automated end-to-end coverage. A byte mismatch must remain incomplete until independently explained; the helper does not waive host rewrites. Hash equality does not certify accessibility or visual quality.
