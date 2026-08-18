---
name: clarifying-contracts
description: Resolve user-authoritative semantic ambiguity after inspection identifies an unresolved choice that could change purpose, direct object, public behavior, constraints, invariants, scope, decision authority, or acceptance evidence, or when the user asks to clarify or stress-test such a contract. Do not use for discoverable facts or agent-owned implementation choices that preserve the contract.
license: MIT. See LICENSE.txt for complete terms and notices
---

# Clarifying Contracts

Reduce essential ambiguity without turning ordinary work into a clarification ceremony. Establish why and the observable contract when user judgment is required, while leaving facts to inspection and equivalent implementation choices to the agent.

## Contract boundary

A contract may define:

- purpose: why the change is needed;
- direct object and public outcome: what must change, including failure behavior when relevant;
- constraints and invariants: what limits the solution and what must remain true;
- scope and non-goals: what is and is not authorized;
- decision authority: who owns unresolved choices;
- acceptance evidence: how completion can be checked, including thresholds or external oracles when relevant.

Include only fields that affect the task. Do not turn this list into a mandatory template.

Classify the live uncertainty before asking:

- A discoverable fact belongs to inspection, research, or executable evidence.
- An implementation choice that preserves the established contract belongs to the agent.
- A semantic decision that could change the contract belongs to the user.

Treat a question as semantic only when different answers could change one of these fields. Treat an implementation choice as semantic only when it changes durable meaning, a public interface, or an observable result. Within applicable instructions and the approved contract, the agent owns implementation choices that leave the contract equivalent.

If a purported implementation question changes several independent outcomes or owners, propose smaller task boundaries instead of asking the user to design the implementation.

## Clarification loop

1. Inspect applicable instructions, source files, and current state before asking questions.
2. Apply the classification above: resolve facts from evidence and make contract-equivalent implementation choices directly.
3. If a blocking fact lacks evidence, route it to exploration or research. Resume clarification only after the fact is established or explicitly bounded as an assumption.
4. Identify the unresolved decision with the greatest effect on the contract or on later decisions.
5. Ask one question. When alternatives exist, state the relevant options and recommend one with its decisive tradeoff.
6. Incorporate the answer and continue along dependent decisions.

If the audit finds no unresolved user-owned semantic decision, state that no clarification is needed when the skill was explicitly invoked, then leave it. Do not manufacture a design ceremony.

## Completion and approval

Stop the loop when no unresolved user-owned decision could change the purpose, direct object, public behavior, constraints, invariants, scope, decision authority, or acceptance evidence. Record non-blocking unknowns when useful; do not prolong clarification to resolve branches that cannot change the contract.

If clarification created or changed the semantic contract, present it once in precise, reviewable language and request approval. An exact user-provided contract already carries that approval.

After approval, leave this skill. Subject to applicable instructions, recording the contract, deriving any required plan, executing it, verifying the result, and reviewing the diff form one continuous workflow and do not create another semantic approval gate when they preserve the approved meaning.

Request approval again only when later work introduces a new semantic decision, expands scope, changes a target or invariant, adds an unapproved destructive action, or reveals a conflict that cannot be resolved mechanically.
