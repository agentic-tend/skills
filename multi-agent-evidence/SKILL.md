---
name: multi-agent-evidence
description: Use multiple agent contexts when independent evidence, held-out checks, or posterior falsification can reduce correlated failure or human review load. Expose a plan before delegation and a provenance-aware delivery. Do not use for agent count, importance, task size, latency-only parallelism, repeated opinions, stylistic review, or majority voting.
license: MIT. See LICENSE.txt for complete terms and notices
---

# Multi-Agent Evidence

Use evidence-separated agent contexts without prescribing their internal orchestration. The public [multi-agent evidence model](https://github.com/agentic-tend/.github/blob/main/docs/multi-agent.md) owns the effective-theory rationale; this skill realizes its conditional port contract.

## Establish the evidence boundary

Activate this skill only when another context can:

- form a claim from a distinct validity source or method without inheriting another conclusion;
- keep applicable evidence held out from a proposed implementation;
- seek a discriminating failure without receiving the success narrative it should challenge.

A request for more agents, task importance, size, nontriviality, context volume, or latency-only parallelism does not establish this boundary. Repeating the same prompt, sources, and method creates more output, not independent evidence. When no evidence can be usefully decoupled, continue with one agent.

Treat each agent context as a black box. Specify only the motivation, inputs, outputs, withheld information, provenance obligation, and feedback edges that change observable task behavior. Leave agent count, prompts, private reasoning, local decomposition, message order, and contract-equivalent execution choices to the active model and runtime.

## Show the plan before delegation

Once the skill activates, the coordinating agent presents a human-visible plan before delegating. Expose the motivation and observable outcome, the ports that current evidence requires, their input and output boundaries, intentionally withheld information, feedback and stopping evidence, authority, and unvalidated claims.

This visibility is not an approval gate. Continue within the current contract and authority; pause only for a user-owned semantic choice, expanded authority, destructive action, or another boundary that already requires human input.

Establish the minimum observable port topology before filling local execution detail: motivation, contract, port boundaries, and applicable validity sources must constrain each port's realization. This is a logical dependency, not a fixed runtime sequence; structure, execution, and feedback may interleave after the boundary is coherent.

## Derive conditional ports

Derive the minimum port graph from current task data. These ports describe effective interfaces, not persistent roles or mandatory stages.

- **Coordinator bridge:** consumes the request, established contract, task data, authority, and returned evidence. It exposes the plan and delivery, bounds port interfaces, maintains feedback edges, and applies the stopping contract. It does not own truth or resolve disagreement by preference or vote.
- **Prior-evidence port:** appears only when valid evidence can be formed independently and implementation exposure could contaminate it. Give it motivation, contract, current facts, and applicable validity sources, but withhold the proposed implementation when independence matters. It returns supported mechanical predicates, judgment-changing findings, and explicit unvalidated boundaries.
- **Worker port:** consumes a bounded objective, contract, authoritative facts, allowed actions, and applicable capabilities. It returns an artifact or claim, observations, evidence, provenance, and unresolved boundaries. Its internal trajectory remains unspecified.
- **Posterior-review port:** appears when an independent attempt can expose a plausible failure or compress review. Give it the resulting artifact, contract, evidence, and needed environment without an unnecessary success narrative. It returns a counterexample, disagreement, evidence gap, or bounded support with provenance.

The coordinator is the stable human ingress and egress once multi-agent execution is active. Prior-evidence and posterior-review ports are conditional. Add, combine, repeat, or retire ports as observations update task data; do not preserve a port merely because it existed earlier.

## Preserve oracle and capability ownership

A mechanical predicate belongs in prior evidence only when an available oracle can decide it and the contract makes the check useful. An interpretation is useful only when it traces a result to motivation, contract, evidence, or human authority; an agent's satisfaction judgment remains a claim. If no validity source can decide a claim, mark it unvalidated instead of fabricating a test or evaluator.

When software work activates `$software-engineering`, let that capability own implementation topology and realization, testing, oracle integrity, and delivery semantics. This skill decides only whether those judgments benefit from separate contexts; it does not redefine them or change any other capability's semantic owner.

## Route recursive feedback

Transport observations with the input or condition, expected contract behavior, observed result, validity source, and provenance. Pass interpretations only when the next reader needs them to judge a live alternative.

Posterior review may recurse like a limited cache hierarchy: a cheaper local layer absorbs routine detail, while a failure, disagreement, or audit gap escalates. Do not fix the number of layers. Add another layer only when its independent evidence can change judgment, and forward only judgment-changing distinctions while preserving pointers to accessible artifacts.

Agreement establishes current consistency, not correctness. Shared models, specifications, sources, and tools remain possible common-mode failures. Route disagreement to the cheapest discriminating source or probe. Return user-owned semantics to the user, and retain unresolved claims as unvalidated.

Stop when the established contract has sufficient evidence from its proper validity sources and no material unresolved conflict remains within the authorized scope. Passing generated tests or obtaining agent agreement is not a universal stopping rule.

## Deliver the effective result

Present motivation and observable outcome before agreement, disagreement, evidence, and unvalidated claims. Keep design, implementation, checks, falsification attempts, and provenance reachable through available files, tool outputs, and lane evidence without concatenating agent transcripts.

If the runtime cannot expose an underlying transcript or artifact, identify that audit gap rather than claiming complete traceability or creating a transcript store. Follow the active authority boundary for any external action.
