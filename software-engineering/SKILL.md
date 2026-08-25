---
name: software-engineering
description: Own software-engineering decisions about behavior, topology, implementation, testing, feedback, refactoring, performance, review, delivery, and whether embedded prose must preserve non-inferable software meaning. Use for any task with these software traits, including mixed tasks. Do not use for prose-only expression or host-language attachment that makes no software decision.
license: MIT. See LICENSE.txt for complete terms and notices
---

# Software Engineering

Let software structure grow from the established contract and concrete pressure.

## 1. Establish the boundary

- Inspect the relevant implementation, tests, documentation, and repository state before changing behavior.
- Return an unresolved user-owned choice that could change purpose, public behavior, scope, constraints, authority, or acceptance evidence to task data rather than resolving it as an engineering choice.
- Preserve active public contracts and repository invariants unless the approved task changes them.

## 2. Select the method

Read [implementation](references/implementation.md) when creating or changing topology, introducing an abstraction, refactoring, redesigning, or optimizing. Let structure grow only from the contract and concrete pressure.

Read [testing](references/testing.md) when behavior or acceptance evidence changes, or when reviewing test quality. Treat tests as executable design language at observable responsibility boundaries: establish acceptance evidence early enough to constrain implementation, and leave each boundary's replaceable internals unspecified.

Read [delivery](references/delivery.md) before handing completed work back or preparing requested delivery prose. Keep local technical evidence separate from authority for external action.

Read [feedback](references/feedback.md) when a result is surprising, the cause or oracle is uncertain, the work needs iterative diagnosis or measurement, or a proposed guardrail extends beyond the established contract. Use feedback to discriminate among hypotheses, not to justify additional behavior by default.

## 3. Preserve composition boundaries

- Decide whether a comment, docstring, error message, or other embedded prose is justified and which public contract, invariant, rationale, or hazard it must preserve. Do not add prose that only narrates obvious implementation.
- Establish only the software meaning of persistent prose. Preserve prose-structure, artifact-language, and host-language ownership for expression, source realization, syntax, and renderer extensions.
- Return semantic ambiguity exposed during execution to task data for trait re-derivation.

## 4. Verify and report

Run validation at the observable boundary when the execution context permits, and never claim a check passed without evidence. Follow the delivery reference for the completion report and any unvalidated boundary.
