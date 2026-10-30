# Editorial-writing contribution review packet

Prepared 2026-10-30. **Ready for owner review; not ready for submission.**

The review candidate is under [candidate/skills/editorial-writing](candidate/skills/editorial-writing). It contains 12 intended files, retains Apache-2.0, and adds only a resource-discovery paragraph to `SKILL.md`. No licensing decision, PR, issue, release, installation or publication has been made. All supplied inputs, including `source/`, match their supplied hashes.

The current awesome-copilot [repository license](https://github.com/github/awesome-copilot/blob/main/LICENSE) is MIT. Its [contribution terms](https://github.com/github/awesome-copilot/blob/main/CONTRIBUTING.md#license) require contributions under MIT; the supplied candidate declares Apache-2.0 in its license, skill metadata and provenance. Direct inclusion needs a rights-holder decision and agreement on the resulting notices. This packet preserves the existing terms rather than assuming permission to change them. An external-plugin issue is a documented alternative that can retain Apache-2.0, subject to owner choice and upstream review.

- [Review findings and requirements](review.md): licensing, scope, source provenance, upstream rules and pending decisions.
- [Intended file manifest](file-manifest.json): source and candidate SHA-256 hashes, target paths, exclusions and changes.
- [Candidate adaptation](candidate-adaptation.patch): the entire content change from the supplied skill.
- [Validation report](validation.md): successful checks, retained failures and unperformed checks.
- [Draft PR](draft-pr.md): direct-inclusion proposal, conditional on licensing resolution.
- [Draft external-plugin issue](draft-external-plugin-issue.md): alternative route using the existing plugin metadata; no listing JSON is proposed.
- [Behavioral test plan](behavioral-test-plan.md): synthetic Copilot scenarios and acceptance criteria, not completed host tests.
- [Evidence](evidence): copied official requirements, source records, browser observations, command logs and integrity checks. Internal provenance files are review material, not upstream contribution files.

Local results: supplied quick validator passes; all 27 checker tests pass with a canonical temporary directory; five tests fail with this Mac's default symlinked temporary-directory path. Advisory prose lint checks nine documents with no findings. Upstream npm validation/build, generated documentation, Copilot behavior, and installation remain unverified.

To reproduce local evidence from the workspace root with already available Python and PyYAML:

```sh
python3 -B output/validate_packet.py
```

Only the candidate subtree maps to proposed upstream source paths. Generated README changes must be produced in an authorized awesome-copilot checkout later. Do not upload this entire packet as a contribution. No external action is authorized by these drafts.

Copied official documents preserve their original relative links; those links refer to their upstream repositories, whose surrounding files are not bundled here.
