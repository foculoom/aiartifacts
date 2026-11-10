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

## Parser provenance and update check

The active parser dependency is [Acorn](https://github.com/acornjs/acorn/tree/d788421b242ddccb28040f1431438ee5cf474208/acorn), source path `acorn/`,
maintained by the authors named in its `package.json`. The accepted npm package
is `acorn@8.18.0` from `https://registry.npmjs.org/acorn/-/acorn-8.18.0.tgz`.
The adjacent `package-lock.json` pins integrity
`sha512-lGq+9yr1/GuAWaVYIHRjvvySG5/4VfKIvC8EWxStPdcDh/Ka7FG3twP6v4d5BkravUilhIAsG4Qj83t02LWUPQ==`;
its SHA-256 in the accepted toolkit source is
`774d5a473e375c8a4984fd6a4c04482521b14d07ab25bbe91c2092be5e7469fc`.
The parser is MIT licensed. There are no local modifications to Acorn; the
Foculoom-authored `check.mjs` is the adapter and must be assessed separately.
Its accepted SHA-256 is
`e1060596dc227631c6878c39b41f2819682f87b4753676812d74a99e4898c222`.
The lockfile, `package.json`, checker and tests form the required local tool
bundle; use `npm ci --ignore-scripts` with Node 22, 24 or 26+ before the checker.
The earlier ten synthetic cases establish bounded parser/checker behavior, not
coverage of every loader or product runtime.

On **2026-11-10**, the toolkit maintainer checked the original Git repository,
its `acorn/` source and changelog, and npm's package metadata. The latest npm
release was `8.19.0`, upstream commit
[`0e0ece7cc7202624d4aca531be4b515b0114b5d0`](https://github.com/acornjs/acorn/tree/0e0ece7cc7202624d4aca531be4b515b0114b5d0/acorn).
Compared with the accepted `8.18.0` source commit
`d788421b242ddccb28040f1431438ee5cf474208`, it changes parser expression
and parse utilities, generated Unicode tables, package metadata and the
changelog. The release adds Unicode 18 support and three parser bug fixes.
**Disposition: update available and awaiting assessment.** Keep the accepted
lockfile and consumer pins while testing the candidate against the ten synthetic
cases, malformed-import failures and a representative product import graph.
Review the candidate's npm integrity, license, scripts, permissions and runtime
requirements before installation in a disposable branch. Record any changed
parse decisions and independent review before an adoption PR. Recheck at the
next toolkit maintenance review on **2026-12-07**, or earlier for a credible
security issue, a parser failure, or a consumer request. The toolkit maintainer
owns discovery; each product maintainer owns its own adoption decision.
