# Skills

This repository owns Agentic Tend's reusable skills layer, dogfooded in Codex before publication.

Each top-level skill directory is independently discoverable through its `SKILL.md` entrypoint.
The collection follows the open [Agent Skills](https://agentskills.io/home) format: compatible agents discover concise metadata first and load full instructions and bundled resources only when a task calls for them.
[Agentic Tend&#39;s context ownership model](https://github.com/agentic-tend/.github/blob/main/docs/context-ownership.md) places these on-demand workflows within a semantic layer while keeping activation and enforcement mechanisms orthogonal.

Below separates reusable workflows, domain realizations, and adapters for a specific capability. All are preference instead of scaffold.

## Validate

Validate every published skill against the Agent Skills specification:

```bash
python -m unittest discover -s tests
gh skill publish --dry-run
```

## Workflow skills

These skills provide reusable procedures with a distinct task outcome.

- [Bootstrap Project Context](bootstrap-project-context/SKILL.md) derives or migrates persistent repository agent context from durable local evidence, including a valid zero-file result.
- [Clarifying Contracts](clarifying-contracts/SKILL.md) resolves user-owned ambiguity about purpose, observable behavior, constraints, scope, authority, and acceptance evidence before execution. It adapts Superpowers' brainstorming workflow and Matt Pocock's grilling[^grilling], focusing on the intrinsically complex entries of HITL (human-in-the-loop).

## Domain skills

These skills realize cross-domain epistemic preferences for a particular kind of work.

- [Software Engineering](software-engineering/SKILL.md) applies the user's preferred method when software behavior, structure, acceptance evidence, or delivery is the task's direct object.
- [Structure Documentation](structure-documentation/SKILL.md) structures durable, intentionally authored natural language for human, agent, or mixed semantic readers.

## Functional skills

These skills guide an agent in using a particular tool or capability safely and consistently.

- [Obsidian CLI](obsidian-cli/SKILL.md) adapts and narrows Kepano's upstream [Obsidian CLI skill](https://github.com/kepano/obsidian-skills/tree/main/skills/obsidian-cli), using Obsidian only when its index or running application state is the relevant source of truth.

## See also

- The [agentic tooling model](https://github.com/agentic-tend/.github/blob/main/docs/agentic-tooling.md) owns the motivation and layer theory.
- The [development routing model](https://github.com/agentic-tend/.github/blob/main/docs/development.md) connects semantic clarification to planning and execution.
- The [organization roadmap](https://github.com/agentic-tend/.github/blob/main/docs/roadmap.md) tracks evidence and extension work spanning multiple tooling layers.

## License

The repository is available under the [MIT License](LICENSE). Each independently installable skill bundles its complete terms and any required upstream notices.


[^grilling]: Matt Pocock, [*grilling*](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md): one-question-at-a-time clarification of plans and decisions.
