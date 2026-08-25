---
name: scientific-claim-audit
description: Evaluate whether a specific scientific claim or scientific-validity objection is supported by controlling derivation, data, code, figure, manuscript context, or cited-source evidence, and return its support status, scope, and unresolved gaps. Use for claim-validity review, citation-support checks, and claim-level inconsistencies across scientific artifacts. Do not use merely because content is scientific, or for explanation, copyediting, style or notation review, literature discovery, response drafting, or faithful format transfer.
license: MIT. Adapted from texra-ai; see LICENSE.txt.
---
# Scientific Claim Audit

Determine what the evidence supports before prose or delivery choices obscure the scientific boundary.

## Establish the claim boundary

1. Identify the exact claim or scientific objection, its current artifact and version, and the requested validity judgment.
2. Derive only the evidence closure needed to distinguish the live alternatives:

   ```text
   claim -> scope and conditions -> controlling evidence -> support status -> support boundary
   ```
3. Inspect controlling evidence rather than trusting summaries, nearby citations, successful builds, or prior reviewer agreement. Do not require a full-artifact pass when a smaller closure decides the claim, and do not stop locally when a definition, appendix, generated artifact, or cited source controls validity.

## Select the evidence port

- For a derivation, proof, or analytic argument, read [formal evidence](references/formal-evidence.md).
- For a numerical result, benchmark, convergence statement, or figure backed by data or code, read [computational evidence](references/computational-evidence.md).
- For a supplied citation, inspect the primary source that contains the relevant result. When finding, comparing, or synthesizing a literature corpus is itself required, compose `$scientific-literature-evidence` rather than expanding this audit into a general search workflow.

## Judge support

- Classify the claim as verified, contradicted, inference, proposal, unresolved, or dependent on author confirmation according to its actual validity source.
- Preserve every scope condition that could change the judgment. Depending on the field, this may include definitions and assumptions, system or sample, protocol, parameter regime, observable or endpoint, uncertainty, finite-size or convergence limits, and the alternatives actually compared.
- Separate a missing explanation from a scientific error, local evidence from extrapolation, and absence of evidence from evidence of absence.
- Controlling evidence determines what is supportable. The author owns unresolved interpretation or scope choices; confidence and consensus do not replace that authority.

## Return the support boundary

- Lead with the smallest set of judgment-changing findings. For each, give an exact pointer, support status, why it matters, and the strongest supportable claim or unresolved gap.
- When no material problem is found, state what was checked and what remains untested.
- Return scientific meaning, not final prose or artifact syntax. Compose `$structure-documentation` when durable wording is requested. For comments, LaTeX, figures, presentations, compilation, or rendering, follow the repository's build instructions and use the current artifact tools; those mechanics remain outside this audit.
- An audit-only request does not authorize edits or new calculations. Stop when each claim in scope is supported, bounded, contradicted, or explicitly unresolved. A passing build, converged optimizer, or agent agreement validates only the predicate it directly tests.
