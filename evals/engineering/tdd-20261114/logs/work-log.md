# Replay work log

## Scope and sources
Read AGENTS.md, contract.md, plugins/engineering/skills/test-driven-development/SKILL.md, tests.md and mocking.md, verify_static.py and test_verify_static.py. `rg --files` listed the workspace; no GLOSSARY.md or ADR was present. No external resources, history or delegation used.

## Boundaries and independent expectations
- verify(record, origin): contract requires ValueError on invalid record/inventory, before constructing any network client. Observe the external network factory and request boundary. Does not exercise live HTTPS.
- CLI main via argv and real local files: duplicate JSON members rejected, invalid input creates no output, distinct entries retained. Exercises actual parser/output creation; transport stub prevents network.
- manifest(root): existing tests characterize content changes and symlink rejection; add literal output characterization for valid payload.
- Expected hashes use published SHA-256 empty-byte and abc literals, not verifier digest for new assertions. Expected path and schema invalidity come directly from contract.

## Command recording
All suite phase logs capture command, Python version, stdout/stderr and exit code. Required command: python3 -B -m unittest -v test_verify_static. Existing five tests are retained byte-for-byte; original snapshot saved here.

## Cycle 1: record shape
Independent expectation: non-object records, non-integer-1 version (including True and 1.0), and missing/empty/non-object inventories raise ValueError without constructing a client. Added one public verify test with contract-derived cases.
Observed red (cycle-1-red.log, exit 1): five non-object cases produced AttributeError; True and 1.0 were accepted. These are intended contract defects, not setup failures. Correction: guard dict type and exact int version before accessing inventory.
Green: 6 tests passed, exit 0. Refactor: wrap long schema condition for readability, no behavior change.
Refactor result: 6 passed, exit 0.

## Cycle 2: canonical file paths
Independent expectation: empty, dot, parent, absolute, repeated/trailing separator, backslash and non-string paths are invalid. Each must fail before network construction, also when preceded by a valid entry. One verify test covers these equivalent contract cases.
Observed red: 20 failures and 4 errors, exit 1; client construction happened for invalid paths, dot path accepted, non-string paths raised TypeError. Late-invalid cases had already issued requests. Full output retained in cycle-2-red.log (tool display was truncated). Correction: validate all path components before creating the client.
Green: 7 tests passed, exit 0. Refactor: remove now-unused PurePosixPath import.
Refactor: 7 passed, exit 0.

## Cycle 3: digest preflight
Independent expectation: digest must be a string of exactly 64 lowercase hex characters. Invalid type, length, uppercase, non-hex or newline must reject before client construction even after a valid entry.
Observed red: all 20 digest cases constructed a client; late cases made a request before rejection (exit 1). Full output retained despite truncated display. Correction: move existing digest validation into the inventory preflight loop.
Green: 8 tests passed, exit 0. Refactor: wrap digest condition for readability.
Refactor: 8 passed, exit 0.

## Cycle 4: duplicate JSON object members
Independent expectation: CLI must reject duplicates at root, inventory and nested object levels, including equal values, differing values and escaped equivalent keys. No client or output file. Tests use literal JSON text so no encoder can erase duplicate evidence.
Initial red run (cycle-4-red.log) exited 1 with six TypeErrors while serializing an unconfigured response mock. This proves processing proceeded but is not the intended regression assertion; corrected test transport to raise OSError, then reran before any production change.
Confirmed red: six assertion failures, ValueError not raised (cycle-4-red-confirmed.log, exit 1). Correction: json object_pairs_hook constructs objects while detecting repeated decoded member names.
Green: 9 passed, exit 0. Refactor: expand manifest/readback selection to readable branches; preserve behavior.
Refactor: 9 passed, exit 0.

## Acceptance characterization
Added only tests (no behavior change): valid multi-entry CLI retains four distinct files and exact literal reports/routes; invalid shape/path/digest CLI creates no output; existing output and payload boundary preserved; manifest CLI outputs the independent SHA-256 abc literal. Expectations written before execution. These characterize required preservation and integrate prior corrected behaviors; no artificial red expected.
Acceptance: all 13 tests passed with required command on Python 3.9.6, exit 0. Final source review confirmed preflight completes before client/report creation and duplicate hook retains all distinct members. The original five-test class is byte-for-byte unchanged (final-review.log).

## Limits and outcomes
No live network, repository history, external resources or Git commands were used. Only this workspace was read/edited; Python standard-library runtime and original tempfile tests necessarily use system installation/temp facilities. New temporary fixtures are within this workspace. CLI tests invoke real main with argv and real files in-process; they do not launch a shell subprocess or verify live server behavior. Network construction/open are mocked only at the external transport boundary. Existing five tests remain; 8 contract/acceptance tests added. No report is created for tested invalid CLI inputs. Each code change followed intended observed red; the cycle-4 setup failure and corrected red are both preserved. Command logs include full outputs, including output truncated in tool display. No unresolved test failures.
