# GitHub Markdown

Use this reference when GitHub renders the Markdown artifact. It owns GitHub-specific realization while prose meaning and reading path retain their established owners.

## Realize the selected structure

- Realize a selected comparison or mapping with a GitHub Flavored Markdown table.
- Realize a selected diagram with a fenced Mermaid block.
- Realize a selected provenance note or qualification with GitHub footnote syntax.
- Realize a selected disclosure with a `<details>` element and a `<summary>` label.
- Realize mathematics with GitHub's supported delimiters only when the repository contract permits them.

Follow GitHub's official syntax for [basic writing and footnotes](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting), [tables](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables), [collapsed sections](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections), [Mermaid diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-mermaid-diagrams), and [mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).

## Preserve source semantics

- Use `$...$` and `$$...$$` only when the GitHub renderer and repository contract support the intended mathematics.
- Use Markdown links for reader navigation and inline code for literal paths, commands, symbols, and identifiers.
- Leave a dangling link only when the target is part of the same planned, committed change.
- Repeat a link when each occurrence is independently useful; do not make readers search upward for the only route.
- Put block constructs on their own source lines and keep surrounding blank lines when GitHub parsing requires them.
