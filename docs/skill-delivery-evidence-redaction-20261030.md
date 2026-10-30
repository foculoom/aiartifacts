# Skill delivery evidence redaction — 30 October 2026

Owner: the AI Artifacts implementation/review workflow. Affected channel: public
draft PR #30, evidence commit `e746a5097361333a149beeae53c4067340efddc1`.
The expected boundary was public-safe evaluation evidence before the branch
update. A final reviewer found machine-generated macOS temporary paths after
that update had already been pushed.

## Observed scope and sequence

The independent readback found **36 occurrences in 17 text files**, representing
21 distinct temporary-path strings from one host temporary-root family. They
appeared in evaluator command/test logs and snapshots. No credential values,
user-home paths, private company/customer content or affected ZIP payloads were
found within the reviewed scope. This is a bounded inspection, not proof that
every possible sensitive pattern was detectable.

1. Initial retention scans and reviews checked homes, selected temporary-root
   forms, keys and archived payloads. An earlier scratch binary was withheld.
2. The root agent pushed the evidence commit while the final privacy review
   was still outstanding. Earlier scan results were treated too broadly.
3. That reviewer identified the unhandled `/var/folders` form. The sanitizer
   covered the corresponding `/private/var` form but missed this alias.
4. All 17 affected files were redacted from their retained originals. Eight
   artifact maps kept original paths, sizes and hashes while updating snapshot
   hashes/transforms; two evidence indexes were regenerated. No skill source,
   candidate package, runtime answer judgment or test outcome was rewritten.
5. Independent readback verified the exact substitutions, all 907 evidence
   entries, and 18 ZIPs containing 229 members. Expanded path/key checks found
   no remaining flagged content in the corrected packet.

## Containment and limits

The corrective branch update supplies a clean current packet for the observed
patterns. **It does not recall earlier public copies or erase GitHub history.**
The earlier commit remains a historical exposure; no deletion, cache purge or
third-party acquisition result is claimed. No account/permission change,
credential rotation or history rewrite was performed. The owner can separately
decide whether any historical-removal action is warranted; this record does
not authorize contacting a provider or changing repository visibility.

Distributable Editorial packages and the skill instructions/exporter were
unchanged and independently checked. No new release, ecosystem submission or
consumer update occurred. Published v0.5.0 remains the achieved release
(metadata checked October 30; archive acquisition last verified October 28).
The experiment's adoption hold still follows its usefulness/runtime evidence,
not an inference that this issue invalidated every earlier test or package.

## Prevention and closure

- The runtime evidence owner expanded redaction to both macOS temporary-root
  forms and preserved original-vs-snapshot identities. Independent substitution
  and inventory checks verified this correction.
- The source owner added a narrow offline regression for common machine paths
  in retained public text and ZIP members. It supplements manual review; it is
  not a comprehensive privacy or secret scanner.
- The integration owner must wait for the explicit privacy review of the exact
  staged revision before another public evidence push. A source-code approval
  or an earlier pattern scan is insufficient. This is a workflow correction;
  no claim of universal agent enforcement follows.

The verified causes are the omitted path alias and publication before the final
privacy result. No additional causal chain or customer impact is inferred.
Current-packet verification and historical-public-copy uncertainty remain
separate closure states.
