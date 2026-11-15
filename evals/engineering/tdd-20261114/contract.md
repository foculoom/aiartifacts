# Accepted verifier behavior

Preserve the existing manifest(root), verify(record, origin) and command-line
interfaces and their valid outputs. Manifest JSON must reject duplicate object
members instead of silently discarding them. A record must be an object with
integer version 1 (not bool/float), and a nonempty files object. Every inventory
path must be a nonempty relative canonical POSIX file path without empty, dot,
parent or backslash components; each digest must be exactly 64 lowercase hex
characters. Validate the entire inventory before constructing a network client,
issuing a request or creating a report, including invalid entries after valid
ones. Invalid CLI input must not create output. Valid distinct inventory entries
must all survive parsing and verification. Existing HTTPS/index-route, HTTP
failure and output-preservation behavior must remain.

Implement only in this history-free workspace. Python 3.9.6 and the standard
library suffice. Run python3 -B -m unittest -v test_verify_static. Do not read
outside this workspace or seek historical fixes/tests. Retain a concise complete
work log and phase evidence so another reviewer can inspect actual outcomes.
