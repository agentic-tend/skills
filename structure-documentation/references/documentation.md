# Documentation conventions

This reference defines conventions for documentations in natural language.

## File and directory contracts

- State each file's essence in its first non-heading sentence.
- Treat an existing `README.md` as the contract for its directory. Do not create a README merely because a directory exists.
- Let child files specialize the directory contract instead of restating it.
- Keep content in a file only when that file's ownership and retrieval boundary explain why it belongs there.
- Add navigation where a real reader path requires it. Do not impose a fixed `See also` section.

## Authoring workflow

- Introduce headings when groups of blocks expose a nontrivial Markdown topology or retrieval path.
- Prefer pseudo-code to prose in planning when it clarifies language-independent design before implementation.
- Order explanation from motivation or obstruction through contract and structure to mechanism, evidence, and limits.
- Use footnotes for provenance or optional qualifications that would interrupt the main path.
- Use renderer-supported disclosures for secondary derivations, examples, or evidence only when the main path remains complete without them.
- Keep the thesis, executable contract, safety caveat, and next action in the primary reading path.

## Formatting

- Do not manually reflow code only for visual alignment.
- Do not hard-wrap Markdown, comments, commit prose, or docstrings merely to satisfy a visual line length.
- Start a new physical line when it begins a new semantic Markdown block or when code, math, table, list, callout, or blockquote syntax requires it.
- Separate prose paragraphs with a blank line; a soft line break does not create a semantic boundary.

## Markdown file references

- Use Markdown links, `[name](path)`, for repository files that function as documentation nodes.
- Use inline code for a literal filename, directory, command, glob, identifier, or path fragment that is not a navigational edge.
- Allow a dangling link only for a planned committed file where the link intentionally records a documentation node that must be created.
- Repeat a link when the later reference still has independent navigational value.
- Prefer one canonical explanation with downstream links over synchronized copies.

## Logical-block review

The Markdown logical-block count is a syntax-level proxy for review load. It does not identify semantic blocks and is not a CommonMark conformance oracle.

Treat 100 logical blocks as a review trigger, not as a validity limit. Count:

- each heading, paragraph, list item, and Markdo table row as one logical block;
- each fenced or indented code block, or display-math block, as one logical block regardless of internal lines.

Exclude YAML frontmatter, blank lines, fence and math delimiters, table separators, and thematic breaks.

Run:

```bash
python scripts/count_markdown_blocks.py PATH...
```

Resolve the script path relative to the skill directory when invoking it elsewhere. The script reports counts and exits successfully above the threshold because the result requests review rather than automatic rejection.

When review is triggered:

1. prune stale, repeated, or non-actionable blocks only when no needed distinction, preference, authority, rationale, assumption, source, or local contract is lost;
2. split only along a real ownership or retrieval boundary;
3. compress repetition without weakening the contract or reading path;
4. keep the document intact when it remains the clearest coherent object.

## Public/private boundary

- Committed documentation must not depend on a specific private or uncommitted file.
- Ask whether private material would guide a future diff. If it would, promote the minimum sufficient context to its durable public owner.
- If one sentence cannot preserve the needed distinction, reconsider the ownership boundary instead of over-compressing it.
- Keep personal reminders private when they do not constrain public behavior, and create no public dependency on them.
