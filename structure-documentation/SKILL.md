---
name: structure-documentation
description: Organize and express durable, intentionally authored natural language independently of artifact syntax. Use when persistent prose is the direct task object or another capability has established prose to write, including documentation and natural-language spans inside code or interfaces. Do not decide whether software prose is needed, what semantic contract it owns, or which artifact or host-language syntax is valid; do not apply directly to formal code or data, generated content, transient chat, or verbatim quotations.
license: MIT. See LICENSE.txt for complete terms and notices
---

# Structure Documentation

Build the smallest complete reading path from actual reader pressure, then add only the structure that exposes its semantic dependencies.

## 1. Organize semantic blocks

A semantic block is the smallest coherent reader move: a claim, reason, contract, example, evidence item, caveat, or action with one logical role and a current reason to exist.

Start with the smallest result that lets the reader make the current judgment, then descend through the distinctions, evidence, mechanisms, and details on which it depends. Apply the same ordering recursively inside a deeper block. Introduce headings and other hierarchy when groups of semantic blocks expose a real dependency or retrieval boundary. Split a mixed artifact when blocks need independent retrieval because their audience, lifecycle, primary question, or reader action differs.

When prose is embedded in another artifact, accept whether it is needed and what durable meaning it must preserve from the capability that owns that decision. Own the prose structure and expression. Let the artifact-language and host capabilities own serialization, attachment, syntax, and renderer-specific conventions.

## 2. Write from reader pressure

- Retain a sentence or block only when it answers the reader's current question; supplies context, a result, a relation, evidence, a boundary, or an action that the remaining path needs; or preserves a non-inferable preference, authority boundary, rationale, assumption, source, or local contract.
- Delete a sentence or block when removing it loses none of those functions.
- Lead with the need, constraint, or obstruction before a non-obvious abstraction.
- Within each layer, introduce a prerequisite, definition, or distinction before a statement that depends on it. Start from available context, add the next needed relation, and leave the context required by the following sentence.
- Use the plainest domain-appropriate language that preserves the meaning. Each retained abstraction names the object and relation that create reader pressure.
- State facts, decisions, assumptions, recommendations, and unresolved questions distinctly.
- Keep API docs, CLI help, error messages, and user-facing copy aligned with observable behavior and the reader's next action.

## 3. Use ASCII punctuation and spacing

Use ASCII half-width punctuation in both Chinese and English project prose.

- Use no space before `, . : ; ! ?`.
- Use one space after those marks unless the mark is at the end of a line or immediately before a closing delimiter.
- Use one space outside parentheses or brackets when they are surrounded by prose.
- Use no space immediately inside parentheses, brackets, or quotation marks.

Exempt code, identifiers, URLs, paths, commands, artifact syntax, math, exact quotations, generated content, and language-mandated syntax. This is an artifact rule, not a requirement for transient chat replies.

Examples:

```text
Correct: 这是一个 contract, 它约束 future changes.
Correct: Use the public API (not the private helper) for validation.
Wrong: 这是一个 contract，it changes behavior。
Wrong: Use the public API( not the private helper )for validation.
```

## 4. Specialize by artifact

Apply the universal rules above before artifact-specific conventions. When the target is standalone project documentation, read [documentation artifact conventions](references/artifact-documentation.md). Preserve artifact-language ownership of serialization and host ownership of renderer extensions. Do not apply an artifact reference outside that artifact boundary.

## 5. Verify the prose

Review by semantic block and reading path rather than isolated physical lines. Check why each block exists, whether the first layer gives the smallest sufficient result, whether each layer descends by dependency, and whether any sentence needs later prose to become intelligible. When an artifact reference applies, run its validation. Confirm that mixed-task prose follows the same rules as standalone prose and that exempt material was not rewritten.
