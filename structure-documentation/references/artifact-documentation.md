# Project documentation artifacts

Use this reference for standalone project documentation whose file structure, navigation, renderer, or public/private boundary affects how readers retrieve it.

## File ownership and navigation

- State each file's essence in its first non-heading sentence.
- Keep content in a file only when that file's ownership and retrieval boundary explain why it belongs there.
- Add navigation where a real reader path requires it. Do not impose a fixed `See also` section.

## Authoring workflow

- Introduce headings when groups of blocks expose a nontrivial Markdown topology or retrieval path.
- Prefer pseudo-code to prose in planning when it clarifies language-independent design before implementation.
- Order explanation from motivation or obstruction through contract and structure to mechanism, evidence, and limits.
- Use footnotes for provenance or optional qualifications that would interrupt the main path.
- Use renderer-supported disclosures for secondary derivations, examples, or evidence only when the main path remains complete without them.
- Keep the thesis, executable contract, safety caveat, and next action in the primary reading path.

## Renderer routing

- Identify the actual renderer from the target, build configuration, resolved toolchain, and active project instructions before adopting renderer-specific syntax.
- Do not transfer syntax between renderers merely because the intended semantics or rendered appearance is similar.
- For repository Markdown with no downstream generator and GitHub as its primary rendered surface, use `$...$` for inline mathematics and `$$...$$` blocks for display mathematics. See [GitHub's mathematical-expression syntax](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
- For content rendered by Documenter.jl, read [Documenter.jl authoring](render-Documenter.md) before choosing syntax or validation.
- Validate renderer-specific content with the real build or render path and inspect the resulting artifact. Source-level resemblance is not acceptance evidence.

## Formatting

- Use inline code only for literal code, identifiers, commands, paths, or other verbatim machine-facing text. Do not use it as a visual substitute for mathematics or emphasis.
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

- each heading, paragraph, list item, and Markdown table row as one logical block;
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
