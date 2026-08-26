# Software implementation

This reference defines how implementation topology evolves from an established contract into working semantics without unnecessary expansion.

## Topology evolution

Use two orthogonal views of implementation:

- Vertical design establishes the overall data and logic topology across responsibility levels: the public contract, subsystem and data ownership, interfaces, and control flow. Build only the coherent skeleton the task changes. At a lifecycle boundary whose contract is not inferable from surrounding code, preserve its inputs, mutations or outputs, and ordering invariants with the minimum suitable contract prose.
- Horizontal realization refines one selected topology unit through the "make it work, make it right, make it fast" sequence[^three-m]:
  1. write the smallest plain-code implementation that satisfies the contract;
  2. simplify the working code and align its units with the declared topology;
  3. optimize only against explicit performance evidence and a relevant benchmark.

The views may interleave as feedback changes either the topology or the selected unit. They describe software design and realization, not a global task taxonomy or a fixed authoring sequence.

During horizontal realization, add motivation comments only at non-obvious state transitions where removing the comment would create a logical gap. Explain why the transition is necessary without narrating the code. Software engineering owns this semantic decision; prose and language capabilities own expression and host syntax once the need is established.

Correct behavior supplies the observable baseline for later simplification and optimization.

## Return edges

A return value establishes a caller-visible data-flow and API edge; exposing a value already available inside the implementation is not contract-free.

- Establish that edge only for an independently meaningful result, an intentional composition or output-buffer contract, an external protocol, or an existing public contract.
- When the caller already holds the mutation target and the operation has only an effect, do not manufacture a target-alias return without one of those contracts.
- Preserve an existing public return contract unless the approved task includes its API migration.

## Complexity boundary

- Follow the KISS principle[^kiss]: prefer the smallest conceptual diff that satisfies the contract.
  - If the requested scope is over-designed, surface the simpler route before implementation.
- Add an abstraction only when a repeated concrete use, an explicit contract boundary, or demonstrated pressure requires it.
- State the difficulty an abstraction removes and the assumption, cost, or trade-off it introduces.
- Treat defensive checks, fallback behavior, conversions, new exception guarantees, and theoretically safer arithmetic as behavior, not free robustness. Add them only when the active contract, a reachable failure, or measured pressure requires them.

## Redesign gate

When implementation friction appears, produce the smallest failing evidence before proposing a broader redesign.

A broader redesign must identify which existing boundary fails and why a local correction is insufficient.

[^three-m]: Emre Demircan, ["Make It Work, Make It Right, Make It Fast: The Three Steps to Quality Code"](https://medium.com/@edemircan/make-it-work-make-it-right-make-it-fast-the-three-steps-to-quality-code-e452160595c9), Medium, February 13, 2025.
[^kiss]: ["KISS principle"](https://en.wikipedia.org/wiki/KISS_principle), Wikipedia.
