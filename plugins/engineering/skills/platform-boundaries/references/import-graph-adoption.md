# Optional JavaScript import graph guard

Use this only after the product has a passing `architecture-inventory.json` and
real boundary rules. It parses covered `.js`, `.mjs` and `.cjs` files with pinned
Acorn 8.18.0 (MIT); it does not run their code. Python, TypeScript, JSX, Swift and
generated bundler imports require separately named checks or review gaps. The
inventory checker is still required to find new unowned files in declared roots.

From this `scripts/js-import-graph` directory, run `npm ci --ignore-scripts`,
`npm test`, then `node check.mjs --root PRODUCT_ROOT`. The product owns a reviewed
`architecture-imports.json` beside its inventory. For example, with inventory
areas `rules` and `storage`:

```json
{
  "version": 1,
  "review_gaps": ["Native modules are checked by the native build."],
  "forbidden": [{"from": "rules", "to": "storage"}],
  "forbid_external_in": ["rules"],
  "excluded_extensions": [".json"]
}
```

The guard rejects malformed covered JavaScript, nonliteral `import()` and
`require()`, `import.meta` loaders, unresolved or ambiguous relative imports,
imports of unowned files, forbidden area edges, external imports in named areas,
and cycles. It reports exact excluded source files. An exception or new area
must be reviewed in the owning product; do not weaken a policy to make a PR pass.

It does not interpret dependency injection, `eval`, custom `module.require`
wrappers, runtime-generated specifiers, bundler aliases, or framework templates.
List any of those used by the product as a gap and test their behavior directly.
Do not claim TypeScript/JSX coverage by adding their extensions to
`excluded_extensions`; their import direction remains unverified.

## Tool choice and adoption evidence

Dependency-cruiser 18.5.0 (MIT, Node `^22 || ^24 || >=26`) was evaluated with a
synthetic ES module graph. With `--validate`, it rejected forbidden edges,
cycles, unresolved imports and literal dynamic imports. In that evaluation it
reported both `import(name)` and malformed `export const = 1` as modules with no
dependencies or diagnostics. It installed 43 packages. The optional Acorn guard
uses one pinned parser and fails those cases; its ten synthetic tests pass.
This is a bounded tool choice, not a claim that every JavaScript loader is known.

Before product adoption, record the owning inventory/policy, covered roots,
runtime, clean-install command, positive and negative fixtures, behavior tests,
tool revision/hash, CI result and final independent review. Check the product's
actual imports and packaged runtime. Installing a checker or merging source does
not publish a product or update a consumer's existing plugin pin.
