# Expert-source maintenance

Use this procedure during the existing Monday 09:00 Pacific engineering review
when a source check is due, or after a relevant security report, broken method,
consumer request, or material upstream correction. The proposed toolkit check
is due on the first Monday of each month; the last actual source inspection
was **2026-11-10** and the next review date is **2026-12-07**. This is a written procedure and completed bounded
inspection, not a configured automation. The toolkit maintainer owns discovery
for toolkit dependencies; each product maintainer decides adoption for that
product. Routine contributions do not require a live upstream lookup.

## Classify before checking

Read the current repository instructions, package dependency records, lockfiles,
scripts, evaluation records and adoption evidence. Mark each mentioned method
as active contribution dependency, optional workflow, historical artifact
method, evaluated candidate, or original local method. A link, installed folder
or recommendation alone does not establish use. Preserve unknown provenance;
select a verified baseline for future work without inventing historical use.

For a material workflow gap, inspect relevant maintained methods already known
to the organization at their original repositories and first-party documents.
Review task fit, authorship, maintenance, evaluations, limitations, tool/model
and interaction requirements, license, redistribution and maintenance cost.
Choose direct reuse, a small adapter, a documented fork, or rejection with a
brief reason. Keep upstream identity and any Foculoom adaptation identity
separate. Do not import a collection to resolve a single dependency.

The maintained [skills CLI](https://github.com/vercel-labs/skills/blob/26dc8e4755a11fea22ed788256c3db50001b013d/docs/commands.md)
was source-inspected on **2026-11-10**. Its documented `skills check` discovers
updates to installed standalone skills, and `skills update` installs them.
The [GitHub skill CLI](https://cli.github.com/manual/gh_skill) is another
documented discovery/install route. Those interfaces do not document a
three-way comparison of an accepted upstream bundle, a candidate and a local
adapter across arbitrary references and scripts. The small read-only helper
below fills that specific review gap; it does not replace their installers or
claim runtime acceptance. The earlier distribution-route review is in
[ecosystems.md](ecosystems.md).

## Check without adopting

1. Record the accepted full source revision, canonical URL/path, bundle content
   identity, required files and dependencies, local location and modifications,
   license, intended tasks/environments, acceptance evidence and known limits in
   the owning existing dependency record. Include the responsible maintenance
   role, last check, disposition and next trigger. For an unresolved historical
   source, record the uncertainty and verify a prospective baseline.
2. Fetch the exact accepted and candidate source into separate disposable
   directories from immutable Git trees or an equivalently verified package
   manifest, excluding untracked/generated files. Do not run tests inside
   comparison snapshots; use separate working copies. Check the origin and
   revisions. Inspect the full required bundle
   and its dependencies, including scripts, templates, permissions, network use,
   outputs and licensing; the entry `SKILL.md` alone is insufficient. A failed
   lookup means **upstream unavailable**, not current. Use `git diff` over the
   relevant source paths and check package lockfiles independently.
3. For local copies or adapters, compare accepted upstream, candidate upstream
   and accepted local content. The standard-library comparison helper reads
   explicit directories and required paths, emits per-file hashes, normalized
   executable modes (`0644` or `0755`) and conflicts,
   and makes no network request or installation:

   ```sh
   python3 scripts/skill-delivery/check_upstream.py \
     --accepted "$ACCEPTED_BUNDLE" --candidate "$CANDIDATE_BUNDLE" \
     --local "$LOCAL_ACCEPTED_BUNDLE" \
     --required references/required.md --required scripts/required.py
   ```

   Supply the actual dependency set. Its `upstream_content_identical` result
   means only that the supplied accepted and candidate upstream trees match;
   local adaptations are still listed separately. Assess whether the paths
   cover the method. `change_for_assessment` reports any changed file even when the wrapper
   is unchanged. `conflicts` flags a file changed by both upstream and the local
   adaptation. `upstream_unavailable` and `required_dependency_missing` block
   an update and leave the accepted copy untouched. Generated caches also block
   comparison, since they would make results depend on test order. The helper
   does not judge relevance, provenance, rights, security, model behavior or
   runtime loading.
4. Record one of: no relevant change found, update available and awaiting
   assessment, candidate under evaluation, adopted and verified, intentionally
   retained, or upstream unavailable/provenance unresolved. A failed check is
   not a no-change result. Save the accepted version for recovery. A credible
   security problem uses the existing security process rather than executing an
   unsafe pin.

## Assess and propagate

Use a focused update branch and the normal independent review/CI path. Compare
representative tasks and relevant failures with the accepted version when the
change affects behavior or compatibility. Verify actual skill loading and
invocation, required dependency resolution, outputs and product constraints in
each supported runtime; keep deterministic file/test checks distinct from agent
behavior. Scale checks to the change. A wording correction needs less evidence
than new code, permissions or decision behavior. Do not replace accepted files
during discovery or silently update an active workspace.

List affected products. Record separate adoption, deferral or incompatibility
for each; updating this public toolkit alone does not update a product pin.
When a correction could invalidate prior work, do a targeted impact review
without rewriting accepted product decisions. Paused products and archives
retain their existing restrictions. A product transfer package must carry the
reviewed required bundle or an exact tested retrieval path without seller-only
access, and a fresh contributor must verify that the intended version loads.

## 2026-11-10 exercise and limits

The real [Release skill](../../plugins/release/skills/release-evidence/SKILL.md)
source changed between `de1426ff254658b920856f5b0d2b2a4ef2655d58`
and `67e6e0d3f4dd833f2f768a2351932136af3dc394`. The complete skill tree
identity changed from Git tree `74bfd4f2368bb088406acaec29aeb8895da74784`
to `95e4974703c49975187f19e173f270ac7c6b9a90` while `SKILL.md` stayed
byte-identical. The helper detected changes to `scripts/verify_static.py` and
`scripts/test_verify_static.py`. The October 30 commits add duplicate manifest
member rejection and inventory/path validation before network readback. This is
**update available and awaiting consumer assessment**, not an installed update
or a cross-provider behavior test. Check affected consumer pins and manifests
before deciding whether the correction changes earlier evidence.

The local, clearly synthetic comparison tests in
`scripts/skill-delivery/tests/test_check_upstream.py` exercise an unchanged
wrapper with a changed dependency, an upstream/local edit conflict, an
unavailable source and missing required file, and separate accepted-local
identity. Additional guard cases check generated caches, unchanged upstream
with a local adaptation, permissions and size limits. They assert that no
candidate replaces the accepted files. These
deterministic tests do not show agent loading. A separate no-history agent check
on **2026-11-10** in an authorized private consumer checkout read the repository
instructions, explicitly opened its accepted repository-local `SKILL.md`,
matched the file to that product's recorded baseline, and applied the procedure
to a fictional prose sentence. No global skill was invoked in that check. The
exact source identity and task receipt remain in the owning private repository.
This demonstrates one explicit local load and use, not automatic skill discovery,
same-name global precedence, another provider, or real-product acceptance. A
separate Codex CLI attempt stopped before agent initialization because its
configuration directory was not writable; it supplies no runtime result. No
simulated update is described as a real upstream event.
