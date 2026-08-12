#!/usr/bin/env python3
"""Report review-oriented logical block counts for Markdown files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Sequence

ATX_HEADING = re.compile(r"^ {0,3}#{1,6}(?:\s+|$)")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
FENCE_CLOSE = re.compile(r"^ {0,3}(`{3,}|~{3,})\s*$")
LIST_ITEM = re.compile(r"^ {0,3}(?:[-+*]|\d+[.)])\s+")
NESTED_LIST_ITEM = re.compile(r"^(?: {4,}|\t+)(?:[-+*]|\d+[.)])\s+")
INDENTED_CODE = re.compile(r"^(?: {4}|\t)")
SETEXT_UNDERLINE = re.compile(r"^ {0,3}(?:=+|-+)\s*$")
THEMATIC_BREAK = re.compile(
    r"^ {0,3}(?:(?:\*\s*){3,}|(?:-\s*){3,}|(?:_\s*){3,})$"
)
TABLE_SEPARATOR_CELL = re.compile(r"^:?-{3,}:?$")


def _content_start(lines: list[str]) -> int:
    """Return the first content line, excluding complete initial frontmatter."""
    if not lines or lines[0].strip() != "---":
        return 0
    for index in range(1, len(lines)):
        if lines[index].strip() in {"---", "..."}:
            return index + 1
    return 0


def _strip_blockquote_prefixes(line: str) -> str:
    """Return content after explicit leading Markdown blockquote markers."""
    content = line
    marker = re.compile(r"^ {0,3}>[ \t]?")
    while match := marker.match(content):
        content = content[match.end() :]
    return content


def _is_table_separator(line: str) -> bool:
    stripped = line.strip().strip("|")
    if not stripped:
        return False
    cells = [cell.strip() for cell in stripped.split("|")]
    return bool(cells) and all(TABLE_SEPARATOR_CELL.fullmatch(cell) for cell in cells)


def _is_table_row(line: str) -> bool:
    return "|" in line and bool(line.strip())


def count_logical_blocks(text: str) -> int:
    """Count Markdown logical blocks using the skill's review semantics."""
    lines = text.splitlines()
    index = _content_start(lines)
    count = 0
    paragraph_open = False
    list_item_open = False

    def close_paragraph() -> None:
        nonlocal count, paragraph_open
        if paragraph_open:
            count += 1
            paragraph_open = False

    while index < len(lines):
        line = _strip_blockquote_prefixes(lines[index])
        stripped = line.strip()

        if not stripped:
            close_paragraph()
            index += 1
            continue

        fence_match = FENCE.match(line)
        if fence_match:
            close_paragraph()
            count += 1
            marker = fence_match.group(1)
            marker_character = marker[0]
            marker_length = len(marker)
            index += 1
            while index < len(lines):
                closing_line = _strip_blockquote_prefixes(lines[index])
                closing_match = FENCE_CLOSE.match(closing_line)
                if closing_match:
                    closing_marker = closing_match.group(1)
                    if (
                        closing_marker[0] == marker_character
                        and len(closing_marker) >= marker_length
                    ):
                        index += 1
                        break
                index += 1
            list_item_open = False
            continue

        if stripped.startswith("$$") or stripped == r"\[":
            close_paragraph()
            count += 1
            if stripped.startswith("$$"):
                closed_inline = len(stripped) > 4 and stripped.endswith("$$")
                closing_token = "$$"
            else:
                closed_inline = False
                closing_token = r"\]"
            index += 1
            while not closed_inline and index < len(lines):
                math_line = _strip_blockquote_prefixes(lines[index])
                if closing_token in math_line:
                    index += 1
                    break
                index += 1
            list_item_open = False
            continue

        if index + 1 < len(lines) and _is_table_row(line) and _is_table_separator(
            _strip_blockquote_prefixes(lines[index + 1])
        ):
            close_paragraph()
            count += 1
            index += 2
            while index < len(lines) and _is_table_row(
                _strip_blockquote_prefixes(lines[index])
            ):
                count += 1
                index += 1
            list_item_open = False
            continue

        if ATX_HEADING.match(line):
            close_paragraph()
            count += 1
            list_item_open = False
            index += 1
            continue

        if THEMATIC_BREAK.match(line):
            close_paragraph()
            list_item_open = False
            index += 1
            continue

        if LIST_ITEM.match(line) or (
            list_item_open and NESTED_LIST_ITEM.match(line)
        ):
            close_paragraph()
            count += 1
            list_item_open = True
            index += 1
            continue

        if INDENTED_CODE.match(line):
            close_paragraph()
            count += 1
            index += 1
            while index < len(lines):
                code_line = _strip_blockquote_prefixes(lines[index])
                if not code_line.strip():
                    index += 1
                    continue
                if not INDENTED_CODE.match(code_line):
                    break
                index += 1
            list_item_open = False
            continue

        if list_item_open and (line.startswith("  ") or line.startswith("\t")):
            index += 1
            continue

        if SETEXT_UNDERLINE.match(line) and paragraph_open:
            close_paragraph()
            index += 1
            continue

        list_item_open = False
        paragraph_open = True
        index += 1

    close_paragraph()
    return count


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Report Markdown logical blocks for structure review."
    )
    parser.add_argument("paths", nargs="+", type=Path, metavar="PATH")
    parser.add_argument(
        "--threshold",
        type=int,
        default=100,
        help="review threshold to report (default: 100)",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.threshold < 1:
        print("error: --threshold must be positive", file=sys.stderr)
        return 2

    reports: list[tuple[Path, int]] = []
    for path in args.paths:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            print(f"error: cannot read {path}: {error}", file=sys.stderr)
            return 2
        reports.append((path, count_logical_blocks(text)))

    for path, blocks in reports:
        if blocks > args.threshold:
            status = f"review recommended; {blocks - args.threshold} over threshold"
        else:
            status = "within review threshold"
        print(
            f"{path}: {blocks} logical blocks; "
            f"threshold {args.threshold} ({status})"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
