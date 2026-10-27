# Parallel implementation and evidence

Use when the authorized task has independent deliverables. A small, tightly
coupled edit can stay with one agent. This method allocates work; it does not
expand task scope, grant external permissions or create scheduled work.

## Assign lanes before starting writers

Name one coordinator for integration and any production environment. Give each
lane a concrete result, inputs, owned files, excluded files, checks, dependencies
and stopping condition. Reserve shared manifests, version files and final release
records for one owner. If two lanes need the same file, serialize that edit or
have one submit a proposed patch to its owner.

Use a separate checkout/worktree and branch for each writing lane. Disjoint files
alone do not isolate a shared Git index or branch switch. Never reset another
lane's workspace. Read-only review can use an immutable candidate elsewhere.
Assign any shared browser session or provider UI to one operator at a time.

Bound active workers by the available tool capacity, including the coordinator.
Do not recursively spawn workers beyond that capacity. Start only lanes that can
make useful progress without another lane's unfinished output. Queue dependent
work; avoid concurrent load-sensitive benchmarks on the same machine.

## Handoff at an explicit boundary

Use the [handoff template](../assets/parallel-handoff.md) in the owning project's
private work area. For source, supply repository, branch, base and full head SHA,
changed paths, checks and PR. For a package, add the exact inventory/profile and
manifest/archive hashes. A path or a terminal PASS without identity is insufficient.
Do not send credentials, raw provider records or private content to a public toolkit.

A reviewer reads the complete current diff and the candidate named in the handoff.
Record whether the review was independent. Resolve major issues and required
checks before the coordinator merges the exact reviewed head through a PR. A new
commit requires review of the new head. Rebuilt or changed payloads require new
hashes and affected validation; retain earlier results only when their tested
inputs are proven unchanged, and say which evidence was reused.

If blocked, report the exact dependency and continue unaffected authorized work.
No lane bypasses a failed gate or requests broader credentials merely to keep busy.
The coordinator tracks blocked, ready, reviewed and integrated states separately;
completion of one lane does not establish overall readiness.

## Join before release

Integrate dependent changes in order, resolve conflicts in the owning lane, then
validate the combined revision. Freeze the final payload before release handoff.
The final production history refresh, release label, upload, configuration activation and
live verification belong to one deployment owner under the product's release
rules. An uncertain upload is reconciled before retrying; parallel preparation is
not permission for parallel deployment. Use the release-evidence workflow when
available, otherwise the repository's established release procedure.
