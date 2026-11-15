# Engineering dependencies

## Pinned TDD adaptation

Maintainer: Foculoom Engineering toolkit maintainer. Source inspected November
14, 2026 Pacific; next review December 7 within the existing maintenance review,
or sooner for a relevant upstream correction or observed behavior failure.
[Maintenance procedure](../../docs/skill-delivery/upstream-maintenance.md).

Upstream: [Matt Pocock skills/engineering/tdd](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/tdd),
revision `5863806dd4e15c63174bee4e7515a4256792ecfa`. Adopt only three Markdown
files plus the root MIT license. No executable dependency or cross-skill runtime
is needed. The package remains Apache-2.0 for original material; the retained
MIT notice covers this adapted skill and upstream examples. No endorsement is
implied. The manifest declares both licenses.

Local bundle: `skills/test-driven-development/`. Adaptations: rename for catalog
clarity; retain refactoring inside the cycle; derive boundaries from approved
requirements without repeated confirmation; allow passing characterization tests
for pure refactoring; replace unavailable design/review skill calls with local
guidance; make observed-red, focused/full checks and boundary assertions explicit.
`tests.md`, `mocking.md` and MIT notice remain byte-identical to upstream.

| Included file | Upstream SHA-256 | Adapted SHA-256 |
| --- | --- | --- |
| SKILL.md | `5505d25bbaa8fc14a79e4d20163936958992a2995b7f1dd1d6197edc9ed722e0` | `836ce8c24d9015a9568d055b4b42fe2c996aff0bb742fb9782be0291df3b4f02` |
| tests.md | `859f9e592c188fda4fc7277dd180e4ce9c7a2e13f6efe1f6f29eccc9d28c106a` | `859f9e592c188fda4fc7277dd180e4ce9c7a2e13f6efe1f6f29eccc9d28c106a` |
| mocking.md | `3ceb807fdf4a47d6a93d4d9a891e5ba6d362a6247bd08adc451feebfc17361ef` | `3ceb807fdf4a47d6a93d4d9a891e5ba6d362a6247bd08adc451feebfc17361ef` |
| LICENSE | `0e7ac423bf2c6e223b7c5b156f8cf72da49d748e56a1641402c31f22ad07dbb5` | `0e7ac423bf2c6e223b7c5b156f8cf72da49d748e56a1641402c31f22ad07dbb5` |

Disposition: source adaptation under evaluation; the owning
[requirements](../../docs/tdd-adoption.md) and subsequent handoff/evaluation
receipt distinguish reviewed source, explicit runtime loading and publication.
No global install, package publication or existing consumer adoption is implied.

## Existing parser

The optional platform-boundary parser retains its own
[Acorn provenance and accepted pin](skills/platform-boundaries/references/import-graph-adoption.md).
