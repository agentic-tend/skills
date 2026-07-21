# Skills

This repository is my personal collection of reusable skills, dogfooded in Codex before publication.

Each top-level directory is one independently discoverable skill with a `SKILL.md` entrypoint.
The collection follows the open [Agent Skills](https://agentskills.io/home) format: compatible agents discover concise metadata first and load full instructions and bundled resources only when a task calls for them.

Below separates meta-level procedures that shape agent work from adapters for a specific capability.

## Agent workflow skills

These meta-level skills govern how an agent reasons about and structures its work across repositories.

- [Clarifying Contracts](clarifying-contracts/SKILL.md) resolves user-owned ambiguity about purpose, observable behavior, constraints, scope, authority, and acceptance evidence before execution. It adapts Superpowers' brainstorming workflow and Matt Pocock's grilling[^superpowers][^grilling], focusing on the intrinsically complex entries of HITL (human-in-the-loop).

## Functional skills

These skills guide an agent in using a particular tool or capability safely and consistently.

- [Obsidian CLI](obsidian-cli/SKILL.md) adapts and narrows Kepano's upstream [Obsidian CLI skill](https://github.com/kepano/obsidian-skills/tree/main/skills/obsidian-cli), distinguishing non-CLI versus CLI processes and non-DEV versus DEV tasks.

[^superpowers]: obra, [*Superpowers*](https://github.com/obra/superpowers): composable, enforceable workflows for agentic software development.
[^grilling]: Matt Pocock, [*grilling*](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md): one-question-at-a-time clarification of plans and decisions.
