# Foculoom AI Artifacts

Reusable AI workflows from Foculoom live in one repository. A plugin is an installable bundle, a skill is a focused workflow inside a plugin, and an agent is an optional role configuration. Product-specific voice, unpublished writing, and private examples stay with the product that owns them.

## Available artifacts

| Artifact | Purpose | Location |
| --- | --- | --- |
| Editorial plugin | Reviews and revises writing for its audience and medium | [`plugins/editorial/`](plugins/editorial/) |
| Editorial writing skill | Applies the editorial method and the selected writing profile | [`plugins/editorial/skills/editorial-writing/`](plugins/editorial/skills/editorial-writing/) |
| Editorial reviewer agent template | Optional review-only second pass in Codex | [`agents/codex/editorial_reviewer.toml`](agents/codex/editorial_reviewer.toml) |
| Project voice brief | Private project overlay to copy into a product repository | [`templates/project-voice-brief.md`](templates/project-voice-brief.md) |

The editorial method is shared. Voice is chosen for the actual work: long-form nonfiction, children's writing, a website, game interface text, and game dialogue have different reader needs. Audience and medium profiles guide the review; a project's own brief supplies its brand, characters, terminology, and approved examples. No single "human voice" score establishes quality or authorship. An automated review also does not replace a human editor or reader.

## Design plugin

The optional [Design plugin](plugins/design/) includes `product-identity` for brand-family briefs and `experience-review` for evidence-based interface audits. Use the [identity brief template](templates/project-identity-brief.md) beside the project voice brief. Keep completed product briefs and private mockups in their owning repositories. The [dependency register](plugins/design/DEPENDENCIES.md) distinguishes reviewed candidates from tested dependencies; neither skill requires an external design skill. [Behavior cases](evals/design/README.md) cover preservation, audience fit, availability, and evidence limits.

Design starts at 0.1.0; Editorial remains 0.1.0. Repository tag v0.2.0 pins this combined snapshot.

## Use the editorial plugin

The repository's [marketplace catalog](.agents/plugins/marketplace.json) lists the editorial plugin as an optional install. For local testing, add this repository as a marketplace source:

```sh
codex plugin marketplace add ./
```

Then install **Editorial** from that marketplace in the ChatGPT desktop app. For the first tagged release, use `codex plugin marketplace add foculoom/aiartifacts --ref v0.1.0` to follow a versioned snapshot. The catalog is a repository distribution channel; appearing here does not mean the plugin has been published to the universal Plugins Directory.

For a product, copy the [voice brief template](templates/project-voice-brief.md) into that product's repository and fill it with its private context. Cite the exact artifact revision and chosen profile in review records. The [Codex agent template](agents/codex/editorial_reviewer.toml) is an optional separate install: copy it to the product's `.codex/agents/` directory if that role is useful. Installing the plugin does not install that agent automatically.

## Repository layout

```text
.agents/plugins/marketplace.json    Repository plugin catalog
plugins/editorial/                Portable editorial plugin and its skills
agents/codex/                    Opt-in Codex agent templates
evals/                           Public or cleared regression cases
templates/                       Reusable project setup documents
```

Additional skills, agents, or plugins can be added here without creating a repository per artifact. Keep each plugin self-contained and give it its own version. A release tag pins the full catalog snapshot. A consuming project should record the tag or commit SHA it tested, especially when an editorial review must be reproduced later.

## Contributing

Open a focused pull request with the behavior you want to change and a public or cleared example that demonstrates it. Add meaningful positive and negative evaluation cases when a skill's routing or review judgment changes. Do not submit unpublished manuscripts, customer data, credentials, private project briefs, or examples whose publication rights are unclear. Keep prose checks advisory and trace findings to exact passages; do not turn stylistic signals into claims about who wrote the text.

This repository is licensed under [Apache-2.0](LICENSE). See the [changelog](CHANGELOG.md) for release notes.
