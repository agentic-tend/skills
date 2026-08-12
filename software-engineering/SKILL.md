---
name: software-engineering
description: Apply the user's preferred engineering method when a task changes, evaluates, or delivers software behavior, structure, or acceptance evidence. Use for implementation, debugging, refactoring, testing, architecture, optimization, review, or software delivery. Do not use for non-software reasoning or prose-only work that makes no software-engineering decision.
license: MIT. See LICENSE.txt for complete terms and notices
---

# Software Engineering

Let software structure grow from the established contract and concrete pressure.

## 1. Establish the boundary

- Inspect the relevant implementation, tests, documentation, and repository state before changing behavior.
- Use `$clarifying-contracts` when an unresolved user-owned choice could change purpose, public behavior, scope, constraints, authority, or acceptance evidence.
- Preserve active public contracts and repository invariants unless the approved task changes them.

## 2. Select the method

Read [implementation](references/implementation.md) when creating or changing topology, introducing an abstraction, refactoring, redesigning, or optimizing. Let structure grow only from the contract and concrete pressure.

Read [testing](references/testing.md) when behavior or acceptance evidence changes, or when reviewing test quality. Test observable contracts rather than private implementation shape.

Read [delivery](references/delivery.md) before handing completed work back or preparing requested delivery prose. Keep local technical evidence separate from authority for external action.

## 3. Compose with other skills

- Load and follow `$structure-documentation` whenever the task changes persistent natural-language content, including prose spans inside code or interfaces.
- Return to `$clarifying-contracts` if execution exposes new semantic ambiguity.

## 4. Verify and report

Run validation at the observable boundary when the execution context permits, and never claim a check passed without evidence. Follow the delivery reference for the completion report and any unvalidated boundary.
