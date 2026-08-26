---
name: markdown-authoring
description: Own decisions about Markdown source syntax and generic or GitHub renderer realization when work changes Markdown files, links, headings, tables, footnotes, disclosures, diagrams, mathematics, source formatting, or renderer compatibility. Compose with $structure-documentation for reading-path and prose decisions and with a host capability for renderer extensions such as Documenter.jl. Do not decide prose meaning or operate application runtime state.
license: MIT. See LICENSE.txt for complete terms and notices
---

# Markdown Authoring

Realize an established documentation structure in Markdown while preserving its established meaning owner.

## Establish the artifact contract

1. Inspect repository instructions, the source file, generators, and the documentation build.
2. Identify the actual Markdown renderer and its supported extensions from build and repository evidence.
3. Preserve reading-path and prose structure as a distinct concern when either changes, and preserve host ownership of renderer extensions such as Documenter.jl.
4. Use an application capability when the task depends on application runtime state.

## Author the source

- Preserve the established meaning, navigation, and public/private boundary.
- Choose syntax that realizes its semantic role.
- Use Markdown links for navigation and inline code for literal source tokens.
- Start block structures on their own source lines so that their boundaries remain reviewable.
- Read [GitHub Markdown](references/github.md) when GitHub is the renderer or compatibility target.

## Review logical blocks

Use the bundled counter as a non-failing review signal:

```sh
python3 scripts/count_markdown_blocks.py PATH...
```

Resolve the script path relative to this skill when calling it elsewhere. The default threshold is `100` and can be changed with `--threshold`. At or above it, return pressure to inspect whether semantic or retrieval boundaries have become hard to navigate. Current reader and retrieval pressure determine any subsequent action.

## Verify the rendered artifact

Use the actual build, preview, or renderer when available. Check links, headings, tables, disclosures, diagrams, mathematics, and navigation affected by the change. Report any renderer behavior that could not be verified.
