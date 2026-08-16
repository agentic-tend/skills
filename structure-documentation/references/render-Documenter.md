# Documenter.jl authoring

Use this reference only for content rendered by Documenter.jl, including manual pages and docstrings included in a Documenter site.

## Resolve the configured site

1. Read active project instructions for project-specific syntax and validation preferences.
2. Inspect `docs/Project.toml` and the active manifest when present to identify the Documenter version and extensions.
3. Inspect `docs/make.jl` for navigation, modules, plugins, output formats, warning policy, and the repository's build entry point.

Active project instructions own project preferences. Upstream behavior establishes capability and compatibility; it does not override a deliberate local choice.

## Author for the configured site

- In Markdown manual pages, default to Documenter's double-backtick syntax for inline mathematics and `math` fences for display mathematics. Documenter currently accepts `$...$` and `$$...$$`, but documents them as deprecated.
- Use Documenter directives such as `@ref`, `@docs`, `@autodocs`, and `@meta` only where their evaluation and resolution context is understood. Add public pages to the configured navigation.
- Use DocumenterCitations syntax only when the documentation environment and `makedocs` pipeline configure it.
- Introduce Literate.jl input and generated pages only when the repository defines their source ownership, generation command, and navigation path.

See the official [Documenter syntax](https://documenter.juliadocs.org/stable/man/syntax/) and [LaTeX syntax](https://documenter.juliadocs.org/stable/man/latex/) for renderer behavior. Prefer the documentation matching the resolved major version when it differs from stable.

## Validate rendered behavior

- Run the configured build command in its documentation environment.
- Compare warnings with the known baseline; do not let `warnonly` or unrelated missing-docstring warnings hide new cross-reference, citation, directive, or page errors.
- Inspect the generated site where syntax or navigation changed. Confirm that mathematics is rendered as mathematics rather than code or literal delimiters, links and citations resolve, and the intended page appears in navigation.
- If the real build or output cannot be inspected, report that renderer compatibility remains unverified instead of inferring success from Markdown source alone.
