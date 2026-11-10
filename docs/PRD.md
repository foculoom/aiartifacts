# AI Artifacts requirements

This is the authoritative requirements entry point for this repository. It
consolidates the existing toolkit contract; the linked documents retain their
detailed requirements. [HANDOFF.md](../HANDOFF.md) owns dated implementation and
evaluation status, and [CHANGELOG.md](../CHANGELOG.md) owns release history.

## Purpose and users

Provide reusable AI workflows that contributors can maintain and consuming
projects can deliberately select, review and reproduce. Users are toolkit
contributors, maintainers and people or agents applying a specific artifact to
an authorized project task.

## Approved scope and constraints

- Keep skills, installable plugins, optional agent configurations, templates,
  helpers and evaluations in this single repository. Keep each artifact focused
  and usable under its documented delivery contract; do not duplicate its
  instructions across artifact types.
- Keep plugins self-contained and independently versioned. A repository tag
  pins a catalog snapshot; source changes, published packages, installed
  artifacts and consumer adoption are separate states.
- Keep reusable methods public and project-specific briefs, configuration,
  customer evidence, credentials and reports in the owning project. Examples
  and evaluations must be synthetic or explicitly cleared for publication.
- Preserve exact source and dependency identities, applicable licenses and
  attribution. Inspect suitable maintained methods for a material workflow gap
  before creating a local equivalent; use the existing maintenance process for
  assessment and deliberate adoption. Do not silently update consumers.

## Observable acceptance

| Intended task | Acceptance and owning contract |
| --- | --- |
| Select an artifact for a project | The [README](../README.md) and [catalog](../.agents/plugins/marketplace.json) identify its purpose and delivery route; its entry point states relevant inputs, outputs and limits. An optional agent template is distinct from plugin installation. |
| Contribute or change a method | A focused PR identifies the intended user task and governing requirement. [Contribution rules](../CONTRIBUTING.md) and [toolkit acceptance](../AGENTS.md#toolkit-production-quality-acceptance) require proportional evidence and positive/negative cases when routing or judgment changes. |
| Prepare a distribution payload | The [packaging guide](skill-delivery/packaging.md) requires an explicit file inventory, identities, licenses, dependencies and review. Package integrity establishes only the checked file properties. |
| Assess behavior or usefulness | [Evaluation guidance](../evals/skill-delivery/README.md) separates structural checks, loading, behavior and comparative usefulness. Retain actual attempts and limitations; blocked, contaminated or tied comparisons supply no demonstrated benefit. Use the relevant artifact's cases and acceptance contract. |
| Maintain an adopted source | The [maintenance procedure](skill-delivery/upstream-maintenance.md) records the accepted revision, candidate, provenance, task evidence and disposition without replacing accepted files during discovery. Each consumer owns adoption or deferral. |
| Resume or release work | The [handoff and release rules](../AGENTS.md#portable-handoff-and-release-evidence) require reproducible evidence, independent review of the exact head and required checks. A source merge does not authorize a package release or establish consumer acceptance. |

## Exclusions and decision ownership

The toolkit is not a repository for private product operations or customer
records. It does not grant deployment, financial, messaging or broader access
authority, install or schedule itself, or certify quality from structural
validation. Product rules and stronger acceptance or release gates remain with
the consuming project.

The toolkit maintainer owns proposed scope, artifact maintenance and release
decisions through the reviewed PR workflow. A consuming project maintainer owns
its configuration, runtime acceptance and pin changes. Unresolved scope or
release decisions must name that responsible owner in the existing handoff or
relevant PR; do not invent requirements or acceptance results to close them.
The existing handoff and evaluation records retain deferred candidates and
unmet runtime/usefulness gates. This PRD does not reopen those experiments or
authorize their submission, installation or publication.

## Requirements before implementation

Before implementation, identify the governing requirement and reconcile newer
documented owner decisions. If requirements are missing, stale or contradictory,
repair and review them before continuing implementation in this repository.
Read-only investigation and requirements repair remain available. Scope changes
need reviewed requirements first; fixes to accepted behavior reference the
existing acceptance criteria. Keep approved direction, proposals, implementation
and achieved outcomes distinct. Update this entry point only when its umbrella
contract changes; keep detailed requirements and dated evidence in their owning
documents.
