# Releasing work prepared in parallel

Parallel lanes may prepare source, inspect privacy/discovery, replay isolated
candidates or review changes. Assign one coordinator and one production owner
(the same person/agent may fill both roles). Bound workers by available capacity;
queue dependent checks and reserve shared provider/browser sessions for one owner.
A blocked lane should report its dependency while independent work continues.

Accept a handoff only when it identifies the full source SHA, reviewed PR/head,
exact payload inventory/profile, candidate status, manifest SHA-256, archive hash
if used, commands/results and remaining gaps. Do not infer a valid release from
another lane's local preview or synthetic history. Keep provider details and
completed handoffs in the owning project's private evidence area.

After required reviews/checks and major findings are resolved, the coordinator
merges the exact reviewed heads in dependency order and validates the combined
revision. Source or artifact changes require updated identities and affected
review/verification. Unchanged-input evidence may be retained with its basis
recorded; a prior review never silently covers a new head.

Reserve the production window from fresh history through final readback to one
owner. That owner prepares the final label and artifact, changes authorized
configuration, uploads once, reconciles the provider outcome and verifies the
public bytes and experience. Other lanes may review evidence but must not upload,
activate collection, migrate production or roll back concurrently. Coordinate
existing automation and human operators too; a local lock is not a global lock.

If ownership or the outcome is uncertain, stop dependent mutations and inspect
history/live state before retrying. Approval, source merge, upload success and
public verification remain distinct gates. Record activation only after the
product's required checks pass; preserve rollback and unresolved limitations.

The final receipt should identify the integrated source, actual deployed artifact
hash, deployment ID, completion/activation times, readback scope, reused evidence
and remaining limitations. A static helper cannot prove this coordination or grant
permissions; use the owning project's release process and existing authorization.
