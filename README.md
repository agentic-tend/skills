# Skills

This repository is my personal collection of reusable skills, dogfooded in Codex before publication.

Each top-level directory is one independently discoverable skill with a `SKILL.md` entrypoint.
The collection separates meta-level procedures that shape agent work from adapters for a specific capability.

## Agent workflow skills

These meta-level skills govern how an agent reasons about and structures its work across repositories.

- [Clarifying Contracts](clarifying-contracts/SKILL.md) resolves user-owned ambiguity about purpose, observable behavior, constraints, scope, authority, and acceptance evidence before execution.

## Functional skills

These skills guide an agent in using a particular tool or capability safely and consistently.

- [Obsidian CLI](obsidian-cli/SKILL.md) routes work between ordinary filesystem operations and Obsidian's indexed CLI, including verification of application-managed changes.
