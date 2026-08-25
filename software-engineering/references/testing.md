# Software testing

This reference defines how tests make software design executable at observable responsibility boundaries without fixing the replaceable implementation inside them.

## Observable contract

At the selected responsibility boundary, tests should specify:

- accepted inputs;
- observable outputs;
- invariants;
- error behavior;
- minimal integration paths;
- acceptance thresholds and external oracles when relevant.

Within that boundary, tests should not specify:

- private helper layout;
- incidental intermediate state;
- implementation ordering;
- formatting-only behavior, unless formatting is itself part of the selected boundary's contract.

## Boundary first

Start with the outermost boundary whose inputs and outputs can decide the requested behavior. When failure evidence or a needed judgment creates pressure to descend, treat the next responsibility layer's inputs and outputs as another observable contract.

If a test must inspect behavior hidden inside the current unit, refactor until the real responsibility boundary is explicit. That seam may remain internal to the package; testability does not require exporting it as a user-facing API. Tests and callers depend on the explicit contract while the implementation inside it remains replaceable.

## Design feedback

Establish the contract and its acceptance evidence early enough to constrain implementation. This is a logical dependency, not a fixed test-first chronology: tests, implementation, and refactoring may interleave as feedback changes the design, but work is not complete before evidence closes the relevant contracts.

Tests may expose a missing boundary or pressure to revise a contract. They do not by themselves establish a user-owned objective or the correctness of their oracle.

## Oracle integrity

An implementation must not change expected results, acceptance thresholds, or external oracles merely to make itself pass.

When an oracle is wrong, establish independent evidence and change the contract explicitly rather than treating implementation disagreement as sufficient proof.

When no reliable automated oracle exists, use the proper available validity source, such as human judgment, an authoritative specification, a benchmark, or a controlled probe, and state the automation gap. Do not fabricate an uncalibrated proxy or report a contract as validated without supporting evidence.

A passing test establishes agreement with its oracle, not that the oracle or surrounding claim is correct. Calibrate proxies and automated graders against executable evidence or human judgment, record the scope of the observed result, and add confirmed failures to the regression set.
