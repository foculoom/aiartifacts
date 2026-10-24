# Local runner implementation

Requires macOS, Xcode command-line tools, Python 3.9+, and an existing 1Password CLI/service account. No package installation or provider scope change is performed by these scripts. Official references: [1Password service-account CLI](https://www.1password.dev/service-accounts/use-with-1password-cli) and [Apple Keychain Services](https://developer.apple.com/documentation/security/keychain-services). These are reference dependencies, not vendored code. Recheck provider behavior before extending the implementation.

## Private profile

Create a directory owned by the current user with mode `0700`, and a profile file with mode `0600`. Do not place it in a public checkout. It contains nonsecret stable references, never credential values:

- `version: 1`; `op: {path, sha256}` (resolved real executable path).
- `service_account_id` and exact `vault_ids` allowlist.
- `keychain_helper` absolute output path beside the profile; `keychain_service` and `keychain_account` identifying a dedicated local item.
- `bootstrap_source: {vault_id,item_id,field_id}`: the existing service token's exact concealed field, available to the desktop identity for the one-time bootstrap. This source vault need not be available to the service account.
- `tasks`: fixed names mapping to `authorization`, `source_revision`, absolute `argv`, absolute `cwd`, `reviewed_files` (absolute paths → SHA-256), `credentials`, `timeout_seconds`, and `result_contract`.
- Each credential maps an environment name to `{vault_id,item_id,field_id,pattern}`. Require a single concealed field and an anchored provider-specific shape. IDs remove title ambiguity. The launcher does not inspect unrelated items.
- `result_contract: {directory,target,checks}`: a private `0700` directory, exact target string, and required check names. The task writes exclusively to `LOCAL_RESULT_PATH`, a fresh UUID-named file, with exactly `{run_id: LOCAL_RUN_ID, target: expectedTarget, checks: {requiredName: true}}`. Failed checks are false and cause failure. No source messages, identifiers of customers, response bodies or credentials belong in that file.

The task executable and every absolute file argument must be pinned. Also pin transitively imported code/configuration, and use isolated Python (`-I`) or a reviewed standalone executable. No runtime installer, shell evaluation, writable plugin discovery, broad path search or credential inheritance. The runner cannot discover every dependency for you. Verify external URLs/account/resource identities inside each task before any write, and reject redirects carrying credentials. The service token never reaches the task; only its declared provider secrets do.

## Compile, review, bootstrap

Run `python3 scripts/compile_launcher.py --profile /private/path/profile.json --python /usr/bin/python3` from this skill directory. Review the compiled pins and exact task effects against the user's authorization. The generated Swift configuration contains only paths, hashes, Keychain labels and task names; keep it private. It compiles a launcher that has two operations: `store` accepts the service token through stdin, and `run TASK` launches only the fixed runner/profile/task. There is no generic `read` operation. Never call `store` with a token in an argument or shell history.

Run `python3 scripts/runner.py --profile /private/path/profile.json --bootstrap` once. This reads the existing service item into memory, verifies service identity and exact vault access, then pipes it into Keychain. Core dumps are disabled. The Keychain entry uses the default creating-executable ACL, with synchronization disabled. It is not a globally readable password entry.

Then use `/private/path/launcher run reviewed-task`. The launcher rejects altered pins before retrieving a credential; Keychain reads fail when authentication UI would be required. It passes the service credential only through a private stdin pipe to the pinned runner. The runner revalidates the service account and resolves only task credentials. Provider preflights must distinguish an active credential from verified exact write scope. Task stdout/stderr are suppressed; diagnostic evidence must use the reviewed boolean result contract. A report hash alone is integrity evidence, not a digital signature.

No provider write is included in the generic implementation. Add each concrete workflow separately after scope review and task-specific tests. Do not allow one generic `deploy anything` command.

## Verification and failure codes

Run `python3 -m unittest discover -s tests -v`. Synthetic tests deliberately include a child that prints a credential. Neither stdout/stderr nor the launcher report may expose it. Test actual fresh-process execution and desktop-locked execution locally; synthetic tests cannot establish Keychain ACL compatibility or provider state.

Swift exit codes: `64` invalid operation/task, `65` malformed bootstrap input, `73` existing Keychain item, `74` Keychain/process operation failed, `77` Keychain missing/locked/access unavailable, `78` reviewed file changed. The runner emits sanitized codes for vault access, identity/scope, field shape, task drift and fresh-evidence failures. Expired/revoked/inaccessible provider credentials may have the same status; do not guess which without safe provider evidence. No automatic sign-in, broader credential or mutation retry occurs.

## Rotation and runtime changes

An existing entry is never silently overwritten. After a legitimate rotation, authorize removal of the specific stale local Keychain item through the normal OS recovery flow, then repeat reviewed bootstrap, or use a newly reviewed versioned service/account name and retire the old item. Replacing the helper may change its Keychain trust; validate the replacement with fresh processes and keep failure explicit. Do not change the ACL to allow all applications. Revoking a service account/provider token remains a provider action; deleting the local cache does not revoke it.

Desktop 1Password lock and macOS Keychain lock are distinct. The service-account path should work with the desktop vault locked, while a locked/unavailable Mac or Keychain may require the owner. Do not unlock the Mac or bypass mandatory authentication automatically.
