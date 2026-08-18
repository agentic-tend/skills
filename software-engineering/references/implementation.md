# Software implementation

This reference defines how implementation topology evolves from an established contract into working semantics without unnecessary expansion.

## Topology evolution

Treat structure and behavior as coupled axes:

- Vertical evolution establishes the smallest coherent skeleton and public topology when a task creates or changes that topology. At a lifecycle boundary whose contract is not inferable from the surrounding code, decide whether a concise contract docstring is needed to preserve inputs, mutations or outputs, and ordering invariants. Establish these boundaries early enough to guide the implementation, but interleave topology, local semantics, prose, and evidence when the task benefits; do not require empty scaffolding or a fixed authoring sequence for a local correction.
- Horizontal evolution follows the "make it work, make it right, make it fast" sequence[^three-m]:
  1. write the smallest plain-code implementation that satisfies the contract;
  2. simplify the working code and align its units with the declared topology;
  3. optimize only against explicit performance evidence and a relevant benchmark.

During horizontal evolution, add motivation comments only at non-obvious state transitions where removing the comment would create a logical gap. Explain why the transition is necessary without narrating the code. Software engineering owns this semantic decision; prose and language capabilities own expression and host syntax once the need is established.

Correct behavior supplies the observable baseline for later simplification and optimization.

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
