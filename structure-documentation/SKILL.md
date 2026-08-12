---
name: structure-documentation
description: Structure durable, intentionally authored natural language. Use when creating or editing project prose, including documentation and natural-language spans inside code or interfaces. Do not apply directly to formal code or data, generated content, transient chat, or verbatim quotations.
license: MIT. See LICENSE.txt for complete terms and notices
---

# Structure Documentation

Build the smallest complete reading path first, then add only the structure that exposes its semantic dependencies.

## 1. Organize semantic blocks

A semantic block is the smallest coherent reader move: a claim, reason, contract, example, evidence item, caveat, or action with one logical role.

Start with the smallest complete main reading path. Introduce headings and other hierarchy only when groups of semantic blocks expose a real dependency or retrieval boundary. Split an object only when its blocks differ in owner, audience, lifecycle, primary question, or reader action.

## 2. Write only useful prose

- Retain a block when it changes interpretation, decision, behavior, constraint, or reader action, or preserves a non-inferable preference, authority boundary, rationale, assumption, source, or local contract.
- Delete a block only when none of those pressures applies.
- Lead with the need, constraint, or obstruction before a non-obvious abstraction.
- State facts, decisions, assumptions, recommendations, and unresolved questions distinctly.
- Keep comments and docstrings focused on non-obvious intent, invariants, public behavior, or hazards. Do not narrate code that is already clear.
- Keep API docs, CLI help, error messages, and user-facing copy aligned with observable behavior and the reader's next action.

## 3. Use ASCII punctuation and spacing

Use ASCII half-width punctuation in both Chinese and English project prose.

- Use no space before `, . : ; ! ?`.
- Use one space after those marks unless the mark is at the end of a line or immediately before a closing delimiter.
- Use one space outside parentheses or brackets when they are surrounded by prose.
- Use no space immediately inside parentheses, brackets, or quotation marks.

Exempt code, identifiers, URLs, paths, commands, Markdown syntax, math, exact quotations, generated content, and language-mandated syntax. This is an artifact rule, not a requirement for transient chat replies.

Examples:

```text
Correct: 这是一个 contract, 它约束 future changes.
Correct: Use the public API (not the private helper) for validation.
Wrong: 这是一个 contract，it changes behavior。
Wrong: Use the public API( not the private helper )for validation.
```

## 4. Apply artifact conventions

Read [documentation conventions](references/documentation.md) for file contracts, navigation syntax, physical-line behavior, disclosures, public/private promotion, and the Markdown logical-block counter.

## 5. Verify the artifact

Review by semantic block and reading path rather than isolated physical lines. Check the applicable links, hierarchy, examples, public wording, and repository-specific validation. Confirm that mixed-task prose follows the same rules as standalone prose and that exempt material was not rewritten.
