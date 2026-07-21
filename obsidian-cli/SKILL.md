---
name: obsidian-cli
description: Use the Obsidian CLI when a task depends on Obsidian's indexed notes, links, properties, Bases, or application state; when an approved rename or move should update Obsidian-managed links; or when the user explicitly asks to use `obsidian`. Do not trigger for ordinary filesystem inspection, Markdown or YAML editing, or Git work that does not require Obsidian semantics. Plugin and theme development belongs in a separate skill.
---

# Obsidian CLI

Use the CLI as an adapter to a running Obsidian application when its index or application state is the relevant source of truth.

## Select the interface

- Use filesystem tools for ordinary file inspection and exact Markdown or YAML edits.
- Use the CLI for Obsidian-resolved files, links, backlinks, properties, Bases, search, outline, tasks, or application state.
- Use `move` or `rename` when an approved operation must update Obsidian-managed internal links.
- Do not use this skill for plugin or theme development and debugging.

## Run commands

- Run `obsidian help <command>` before relying on remembered syntax.
- Pass parameters as `key=value`, quote values containing spaces, and pass boolean flags without a value.
- Use `file=<name>` for Obsidian-style name resolution and `path=<vault-relative-path>` for an exact target.
- Put `vault=<name>` first when the intended vault is not unambiguous.
- Resolve mutation targets with read-only commands before changing them.
- Treat `eval` as potentially mutating even when the JavaScript appears observational.

## Verify mutations

- Query the resulting state through Obsidian when indexed behavior matters.
- Inspect the affected files for unexpected filesystem changes.
- Report any application behavior that was not verified in the current environment.
