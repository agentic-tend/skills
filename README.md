# Skills

This repository owns Agentic Tend's reusable skills layer, dogfooded in Codex before publication.

Each top-level skill directory is independently discoverable through its `SKILL.md` entrypoint. The collection follows the open [Agent Skills](https://agentskills.io/home) format: compatible agents discover concise metadata first and load full instructions and bundled resources only when task traits match. Agentic Tend's [agentic tooling model](https://github.com/agentic-tend/.github/blob/main/docs/agentic-tooling.md) owns the primitive ontology, its [context ownership model](https://github.com/agentic-tend/.github/blob/main/docs/context-ownership.md) owns placement and activation boundaries, and this README instantiates the current capability graph. Semantic ownership, activation, and mechanical enforcement remain distinct.

Skills are composable capabilities dispatched from task traits, not mutually exclusive task owners. Modularity encapsulates reusable logic and authority routing; composability exposes ports through which selected capabilities consume the same task data and contribute decisions or evidence.

## Capability topology

Each row describes ports, not an exclusive category.

| Capability | Consumes | Provides | Composition seam | Boundary |
| --- | --- | --- | --- | --- |
| [`bootstrap-project-context`](bootstrap-project-context/SKILL.md) | Repository state and persistence pressure | Context ownership migration | Composes with the affected concern and prose capabilities | Does not own ordinary implementation |
| [`clarifying-contracts`](clarifying-contracts/SKILL.md) | An unresolved user-owned semantic choice | An approved contract | Adds authority resolution to any mixed task | Does not resolve discoverable facts |
| [`software-engineering`](software-engineering/SKILL.md) | Software contract and implementation evidence | Behavior, topology, testing, and delivery decisions | Composes with language and prose capabilities | Does not own host-language syntax |
| [`julia-development`](julia-development/SKILL.md) | Julia project, version, source, and renderer evidence | Julia-specific decisions and host conventions | Composes with software, structure, and Markdown capabilities | Does not own language-independent software topology |
| [`structure-documentation`](structure-documentation/SKILL.md) | Established durable meaning and the reader's task | A language-independent reading path | Composes with artifact-language and host capabilities | Does not decide meaning or syntax |
| [`markdown-authoring`](markdown-authoring/SKILL.md) | A Markdown artifact and renderer facts | Markdown syntax and generic or GitHub rendering realization | Composes with structure and host extensions | Does not own prose semantics or host-specific extensions |
| [`obsidian-cli`](obsidian-cli/SKILL.md) | Obsidian index or runtime state | Runtime-aware Obsidian operations | Composes with Markdown and structure only when content changes | Does not own ordinary filesystem editing |

## Validate

Validate every published skill against the Agent Skills specification:

```bash
python3 -m unittest discover -s tests
gh skill publish --dry-run
```

## Provenance

[`clarifying-contracts`](clarifying-contracts/SKILL.md) adapts Superpowers' brainstorming workflow and Matt Pocock's grilling[^grilling]. [`obsidian-cli`](obsidian-cli/SKILL.md) adapts and narrows Kepano's upstream [Obsidian CLI skill](https://github.com/kepano/obsidian-skills/tree/main/skills/obsidian-cli).

## See also

- The [agentic tooling model](https://github.com/agentic-tend/.github/blob/main/docs/agentic-tooling.md) owns the motivation and layer theory.
- The [development capability model](https://github.com/agentic-tend/.github/blob/main/docs/development.md) illustrates composition without prescribing a fixed reasoning trajectory.
- The [organization roadmap](https://github.com/agentic-tend/.github/blob/main/docs/roadmap.md) tracks evidence and extension work spanning multiple tooling layers.

## License

The repository is available under the [MIT License](LICENSE). Each independently installable skill bundles its complete terms and any required upstream notices.


[^grilling]: Matt Pocock, [*grilling*](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md): one-question-at-a-time clarification of plans and decisions.
