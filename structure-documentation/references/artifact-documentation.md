# Project documentation artifacts

Use this reference for standalone project documentation whose file ownership, navigation, reader path, or public/private boundary affects retrieval. Artifact syntax and renderer extensions remain outside this reference's ownership.

## File ownership and navigation

- State each file's essence in its first non-heading sentence.
- Keep a semantic block in a file only when that artifact's retrieval boundary explains why it belongs there. A mixed artifact may carry decisions from several owners; do not split it solely to manufacture one owner per file.
- Add navigation where a real reader path requires it. Do not impose a fixed `See also` section.
- Prefer one canonical explanation with downstream navigation over synchronized copies.

## Build the reading path

- Introduce hierarchy when groups of semantic blocks expose a real semantic topology or retrieval path.
- Order explanation from motivation or obstruction through contract and structure to mechanism, evidence, and limits.

## Select a structure

- Use a list for peers, steps, or checks.
- Use a table for repeated fields, exact mappings, or comparisons.
- Use a diagram for a non-trivial topology, ownership relation, or state flow.
- Use a footnote for provenance or a qualification that would interrupt the main path.
- Use a disclosure for a secondary derivation, example, or evidence only when the main path remains complete without it.
- Keep the thesis, executable contract, safety caveat, and next action in the primary reading path.

## Compose artifact realization

- Identify the artifact language and actual renderer from the target, build configuration, resolved toolchain, and active project instructions.
- Preserve artifact-language ownership of source realization and host ownership of renderer extensions.
- Do not transfer syntax between renderers merely because the intended semantics or appearance is similar.
- Validate renderer-dependent content with the real build or render path. Source-level resemblance is not acceptance evidence.

## Public/private boundary

- Committed documentation must not depend on a specific private or uncommitted file.
- Ask whether private material would guide a future diff. If it would, promote the minimum sufficient context to its durable public owner.
- If one sentence cannot preserve the needed distinction, reconsider the ownership boundary instead of over-compressing it.
- Keep personal reminders private when they do not constrain public behavior, and create no public dependency on them.
