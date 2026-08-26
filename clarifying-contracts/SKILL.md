---
name: clarifying-contracts
description: Resolve user-authoritative semantic ambiguity after inspection identifies an unresolved choice that could change purpose, direct object, public behavior, constraints, invariants, scope, decision authority, or acceptance evidence, or when the user asks to clarify or stress-test such a contract. Do not use for discoverable facts or agent-owned implementation choices that preserve the contract.
license: MIT. See LICENSE.txt for complete terms and notices
---

# Clarifying Contracts

Establish the observable contract when user judgment is required.

## Contract boundary

A contract may define:

- purpose: why the change is needed;
- direct object and public outcome: what must change, including failure behavior when relevant;
- constraints and invariants: what limits the solution and what must remain true;
- scope and non-goals: what is and is not authorized;
- decision authority: who owns unresolved choices;
- acceptance evidence: how completion can be checked, including thresholds or external oracles when relevant.

Select the fields that affect the current task.

Classify the live uncertainty before asking:

- A discoverable fact belongs to inspection, research, or executable evidence.
- An implementation choice that preserves the established contract belongs to the agent.
- A semantic decision that could change the contract belongs to the user.

Treat a question as semantic only when different answers could change one of these fields. Treat an implementation choice as semantic only when it changes durable meaning, a public interface, or an observable result. Within applicable instructions and the approved contract, the agent owns implementation choices that leave the contract equivalent.

If a purported implementation question changes several independent outcomes or owners, propose smaller task boundaries instead of asking the user to design the implementation.

## Clarification loop

1. Inspect applicable instructions, source files, and current state before asking questions.
2. Apply the classification above: resolve facts from evidence and make contract-equivalent implementation choices directly.
3. Route a blocking fact to exploration or research, then resume from established evidence or an explicit assumption boundary.
4. When two or more user-owned semantic choices constrain one another through decision owners, data or state transitions, branches, failure behavior, or acceptance relations, project `established relations -> one open relation -> downstream effects` with the applicable domain notation.
5. Identify the earliest unresolved decision in the dependency path and ask one question. When alternatives exist, state the relevant options and recommend one with its decisive tradeoff.
6. Incorporate the answer into the affected relation and continue along dependent decisions. A supplied equivalent projection becomes the live contract sketch.

When no user-owned semantic decision remains, continue from the established task data and authority.

## Completion and approval

Stop the loop when no unresolved user-owned decision could change the purpose, direct object, public behavior, constraints, invariants, scope, decision authority, or acceptance evidence. Record non-blocking unknowns outside the dependency path when useful.

Each exact user answer updates the live contract sketch. When the sketch faithfully incorporates those answers and no open relation remains, continue within the requested scope. Pause for confirmation when the agent's synthesis introduces a relation the user did not supply or the user requested pre-execution review.
