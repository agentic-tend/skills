# Software testing

This reference defines how tests express public boundaries without mirroring private implementation.

## Observable contract

Tests should specify:

- accepted inputs;
- observable outputs;
- invariants;
- error behavior;
- minimal integration paths;
- acceptance thresholds and external oracles when relevant.

Tests should not specify:

- private helper layout;
- incidental intermediate state;
- implementation ordering;
- formatting-only behavior, unless formatting is itself part of the public contract.

## Boundary first

Write tests against the public boundary before relying on internals. If a test must depend on hidden implementation details, refactor until the real boundary is explicit.

## Oracle integrity

An implementation must not change expected results, acceptance thresholds, or external oracles merely to make itself pass.

When an oracle is wrong, establish independent evidence and change the contract explicitly rather than treating implementation disagreement as sufficient proof.
