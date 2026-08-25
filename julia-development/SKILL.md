---
name: julia-development
description: Own Julia-specific decisions about semantics, dispatch, API design, and host conventions for code, comments, docstrings, and Documenter.jl using the target project's contracts and version-compatible official Julia documentation. Use for any Julia implementation, refactor, review, diagnosis, or Documenter.jl realization, and for performance work when requested or when evidence identifies a hot path, allocation, type-instability, benchmark regression, threading issue, or new performance promise. Do not own language-independent software topology or prose organization.
license: MIT. See LICENSE.txt for complete terms and notices
---
# Julia Development

Reconstruct Julia behavior from project evidence and Julia's own semantics. Do not fill uncertainty with habits from Python, MATLAB, or another language that looks similar.

## Establish the local contract

1. Inspect the project's Julia compatibility, source, tests, dependencies, and local agent or contributor contracts.
2. Identify the observable behavior and the evidence that will accept the change before choosing an implementation shape.
3. Prefer current project evidence over generic advice. Report a conflict between project requirements and external guidance rather than silently changing the contract.

## Route semantic questions

Use the official manual as the authority instead of relying on remembered language resemblance:

- For style, API boundaries, and dispatch, consult the [Style Guide](https://docs.julialang.org/en/v1/manual/style-guide/), [Types](https://docs.julialang.org/en/v1/manual/types/), [Methods](https://docs.julialang.org/en/v1/manual/methods/), and [Conversion and Promotion](https://docs.julialang.org/en/v1/manual/conversion-and-promotion/).
- For comments, docstrings, documentation attachment, and Julia-specific authoring conventions, consult [Writing Documentation](https://docs.julialang.org/en/v1/manual/documentation/) and the relevant Style Guide section instead of copying stable language rules into this skill.
- For a migration, a construct that resembles Python or MATLAB, or unresolved cross-language semantics, consult [Noteworthy Differences](https://docs.julialang.org/en/v1/manual/noteworthy-differences/).
- For version-sensitive behavior, replace `/en/v1/` with documentation for the Julia release compatible with the project and verify that page before acting.

Inspect the relevant section rather than treating a page title as an answer. Explain which project fact and official behavior support the implementation decision.

If official documentation cannot be reached, proceed only from project source, tests, and installed-version evidence. State that official verification remains incomplete; do not invent missing Julia semantics.

## Express Julia-native concepts

Prefer [direct Unicode Greek identifiers](https://docs.julialang.org/en/v1/manual/variables/) instead of its transliterated ASCII names (e.g., using β instead of beta).

Represent a concept with the least structure that preserves its semantics.

- verb: Use a generic function when the concept is fundamentally an operation, and variation belongs to the types of its arguments.
- verb with local memory: Use a closure when the concept is still fundamentally an operation, but its behavior depends on local captured context that has no independent domain identity.
- verb with state: Use a callable object when the operation itself has persistent, inspectable state or lifecycle, so that the transformation deserves an identity of its own.
- noun: Use an ordinary data object with external operations when the object represents a domain entity that admits several equally meaningful behaviors; do not arbitrarily elevate one verb into the object's identity.

The official [`!` convention](https://docs.julialang.org/en/v1/manual/style-guide/#bang-convention) identifies argument mutation; it does not determine the return type. Let the software contract decide whether a return edge exists, then realize that decision in Julia. Because a Julia function [returns the value of its last evaluated expression by default](https://docs.julialang.org/en/v1/manual/functions/#The-return-Keyword), end a project-owned command-like mutator with explicit `return nothing` when it has no result so that an internal operation does not accidentally become its public return. Preserve an independent result, an existing public return contract, or the return required by an output-buffer or external generic such as [`LinearAlgebra.mul!`](https://docs.julialang.org/en/v1/stdlib/LinearAlgebra/#LinearAlgebra.mul!).

Julia permits arbitrary objects to be callable, but that mechanism alone does not justify a callable struct. Let the project contract and the object's semantic role choose among these forms; do not impose a rigid checklist or introduce a bespoke container merely to shorten an argument list. See the official [function-like object](https://docs.julialang.org/en/v1/manual/methods/#Function-like-objects) semantics when the distinction matters.

## Compose code prose

When Julia work changes persistent prose, own only Julia attachment and host-specific syntax or conventions. Preserve established software meaning, prose structure, and generic artifact-language realization as distinct concerns, and reconcile official guidance with the target project's active style rather than silently overriding either.

When task data shows that Documenter.jl renders the target, read [Documenter.jl authoring](references/documenter.md) before choosing Julia-specific syntax or validation.

## Select a feedback surface

Read [feedback surfaces](references/feedback-surfaces.md) when implementation behavior is uncertain, an error or test does not identify its cause, performance evidence needs interpretation, platform or backend state may change the result, or a proposed safeguard extends the established contract.

Record the Julia version and relevant platform, dependency, and backend state before interpreting feedback. Choose the smallest official or executable surface that can distinguish the live hypotheses, and preserve the raw result. Treat a passing test, red `@code_warntype` output, requested thread count, or tool result as an observation rather than a Julia rule.

## Escalate performance deliberately

Enter performance diagnosis only when the user requests performance work, the change touches a known hot path, measurements show allocation, type-instability, or regression, or the change makes a new performance promise.

When that pressure exists, consult the official [Performance Tips](https://docs.julialang.org/en/v1/manual/performance-tips/) for the project's Julia version. Establish a valid baseline, locate the cause with available Julia evidence, and validate the selected change against the same measurement. Do not turn performance advice into a universal requirement for ordinary Julia work.

## Keep the skill evidence-gated

Treat external community skills as scenario and failure-mode discovery, not Julia authority. Do not copy their rules into this skill.

Process guidance explicitly chosen by the maintainer may be persisted directly. Add a Julia semantic or performance conclusion only after route-only behavior repeats the same failure in independent scenarios and a minimal candidate, grounded in an official Julia section, fixes a sealed holdout without regressing other suites. A route-only result with no distilled language rule is valid.
