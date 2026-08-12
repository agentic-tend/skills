---
name: bootstrap-project-context
description: Derive, audit, or migrate persistent repository agent context from durable local evidence, then apply the minimum sufficient result, including a valid zero-file result. Use for repository agent rules, decisions, local skills, mechanical enforcement, generators, or retirement of generic agent scaffolding. Do not use for ordinary implementation or transient planning.
license: MIT. See LICENSE.txt for complete terms and notices
---

# Bootstrap Project Context

Apply this rule throughout the workflow:

> observed need -> minimal persistent structure

Interpret minimal as the smallest sufficient structure that preserves every non-inferable preference, authority boundary, rationale, source, and local contract needed for future work. It does not mean the fewest files or shortest prose.

Treat audit and classification as inputs to the change, not as the final output. Apply the justified repository-local increment unless the request is read-only.

## 1. Inspect actual state

Read the prompt and active instructions, then inspect the repository before proposing structure:

- check Git status and preserve unrelated work;
- locate manifests, languages, toolchains, source topology, and public entry points;
- locate tests, validation commands, CI, hooks, and release machinery;
- read existing `AGENTS.md`, repository skills, decisions, and relevant documentation;
- inspect representative instances before a broad semantic migration;
- distinguish repository facts, inherited preferences, user-owned choices, and one-time prompt constraints.

Do not ask the user for facts that the repository can answer. Treat frequent legacy usage as evidence, not as authority.

## 2. Establish persistence pressure

Persist a candidate only when it is:

- likely to matter in future work;
- non-obvious from nearby code, active instructions, or standard tooling;
- able to change a decision, behavior, constraint, validation step, reader action, or future judgment;
- preserving a non-inferable preference, authority boundary, rationale, assumption, source, or local contract;
- stable enough to remain correct beyond the current task.

Keep one-time prompt constraints transient. Treat a zero-file result as valid. Do not create empty directories, placeholder decisions, generic policy copies, or a standard context skeleton without evidence.

## 3. Classify the semantic layer

Classify meaning before choosing the mechanism that activates or enforces it:

The following classification is the self-contained executable projection of Agentic Tend's public [context ownership model](https://github.com/agentic-tend/.github/blob/main/docs/context-ownership.md). Use the public document for rationale and this projection for the migration decision.

| Semantic layer | Content | Canonical context |
| --- | --- | --- |
| Model capability | General intelligence the model can already supply | Do not encode it as policy |
| L0 cross-domain epistemology | Unconditional reasoning preferences plus the smallest authority and routing appendix | User-level `AGENTS.md` |
| L1 conditional realization | Domain taste, reusable workflows, or expertise | User-level skills |
| L2 repository truth | Repository-specific facts, constraints, public contracts, local workflows, and evidence-backed rationale | Repository `AGENTS.md`, repository skills, or `decisions/` according to activation and retrieval need |
| Current task only | Temporary instructions, exploration notes, and unconfirmed ideas | Transient task state |

Use one canonical owner for each decision and link downstream consumers instead of restating it.

## 4. Choose activation and enforcement

Keep activation and enforcement orthogonal to the semantic layers:

| Mechanism | Use when |
| --- | --- |
| `AGENTS.md` | The owned context must load ambiently at its applicable user or repository scope |
| Skill | A reusable workflow or domain realization has a distinct trigger |
| Human document or decision | Motivation or durable rationale should be retrieved for its question rather than loaded ambiently |
| Test, hook, or CI | A mechanically observable part of a canonical contract has a reliable oracle |
| Generator | Repeated deterministic materialization is safer than direct maintenance |

Tests, hooks, and CI are mechanical projections or oracles for an owned contract, not parallel prose owners. A generator materializes owned structure; it does not own the policy that justifies its output.

## 5. Diagnose inconsistency at the owner

Classify a conflict before correcting it:

- authority conflict: multiple sources claim the same decision;
- abstraction gap: no owner preserves a repeated decision;
- instance drift: one clear owner exists, but an instance violates it.

For an authority conflict, retain one owner and replace copies with navigation. For an abstraction gap, change the nearest justified owner only when the gap blocks work or recurs. For instance drift, correct the instance without broadening the policy.

Separate meaning-preserving mechanical edits from changes to user-owned semantics. Use `$clarifying-contracts` only when an unresolved choice would materially change ownership, public behavior, scope, constraints, authority, migration, or acceptance evidence.

## 6. Pressure-test the migration

For every candidate, test each applicable operation independently:

- add: what future failure, ambiguity, or repeated work occurs if the context remains absent?
- retain: which distinction or decision would be lost if the current content disappeared?
- move: is the content useful but owned or activated at the wrong boundary?
- compress: do all behavior-changing distinctions, rationale, and sources survive the shorter form?
- delete: is the content inferable, duplicated by its canonical owner, obsolete, or unable to affect future judgment?

Deletion requires evidence that no non-inferable preference, authority, rationale, source, or local contract is lost. Preserve structured rationale and external citations when their detail prevents semantic drift.

## 7. Apply the minimal sufficient increment

- Keep repository `AGENTS.md` executable and limited to actual local pressure.
- Create a decision only for durable rationale spanning multiple changes or surfaces.
- Create a repository skill only for a repeatable local workflow with a distinct trigger and outcome.
- Add a hook or CI check only when the condition is mechanically observable and false positives are acceptably low.
- Add a generator only when repeated materialization is safer than direct maintenance.
- Use `$structure-documentation` for every persistent prose edit, including `AGENTS.md`, decisions, comments, and docstrings.

When migrating context, move each useful item to its canonical owner once, update navigation, and remove stale copies. Do not preserve generic scaffolding for compatibility unless a real consumer contract requires it.

## 8. Verify and report

Run validation appropriate to the changed boundary. At minimum:

- check instruction and documentation links;
- confirm referenced commands exist and remain accurate;
- inspect the final diff for duplicated, compressed-away, or misplaced context;
- run repository checks affected by hooks, skills, or generators.

Report what stayed, moved, was created, compressed, or deleted; the pressure and possible loss considered for each owner; validation performed; and any remaining intentional duplication or unresolved boundary.
