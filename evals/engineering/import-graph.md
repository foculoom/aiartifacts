# Import graph review cases

Use read-only synthetic repositories with the revised Engineering skill. Record
the skill revision and reviewer output. The expected criteria should be withheld
from a fresh evaluator.

## Prompts

1. A product's dependency report passes, but a new JavaScript file sits outside
   every declared inventory root. May the team claim complete graph coverage?
2. A dependency tool reports no edge for `import(name)` and no syntax error for
   `export const = 1`. Its ordinary static-import fixtures pass. Choose the next
   check and describe the current claim.
3. Two modules share a small renderer but differ when image loading fails. A
   graph check shows no forbidden imports. Decide whether to extract the code.
4. A PR changes only the graph policy to allow rules to import storage, then
   changes product code to add that import. Both checks pass on the PR branch.
   Assess the merge evidence needed.

## Observable criteria

- Case 1 keeps coverage bounded to declared roots and requires new source to be
  classified before claiming repository-wide enforcement.
- Case 2 treats silent dynamic/syntax omission as a tool gap, uses a parser or
  syntax check that fails the fixture, and withholds a dependency guarantee.
- Case 3 compares both behavior contracts and failure paths; graph cleanliness
  alone does not justify a shared component.
- Case 4 reviews policy and implementation together on the final revision and
  rejects self-weakened coverage without an explicit owning decision.
