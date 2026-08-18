from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[1]
SCRIPT = (
    REPOSITORY
    / "markdown-authoring"
    / "scripts"
    / "count_markdown_blocks.py"
)
SPEC = importlib.util.spec_from_file_location("count_markdown_blocks", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load {SCRIPT}")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CountMarkdownBlocksTests(unittest.TestCase):
    def test_counts_documented_block_types(self) -> None:
        markdown = """---
title: Example
---
# Heading

A paragraph
that spans lines.

- First item
  with a continuation
- Second item

| A | B |
| --- | --- |
| 1 | 2 |

```python
print("internal lines do not add blocks")
```

$$
x = 1
$$

---
"""
        self.assertEqual(MODULE.count_logical_blocks(markdown), 8)

    def test_counts_setext_and_contiguous_text_once(self) -> None:
        markdown = """Setext heading
---

A paragraph
on two lines
"""
        self.assertEqual(MODULE.count_logical_blocks(markdown), 2)

    def test_fence_closer_allows_at_most_three_leading_spaces(self) -> None:
        valid = """```
body
   ```
Paragraph.
"""
        invalid = """```
body
    ```
Paragraph.
"""
        self.assertEqual(MODULE.count_logical_blocks(valid), 2)
        self.assertEqual(MODULE.count_logical_blocks(invalid), 1)

    def test_spaced_thematic_breaks_are_excluded(self) -> None:
        for markdown in ("* * *\n", "- - -\n", "_ _ _\n"):
            with self.subTest(markdown=markdown):
                self.assertEqual(MODULE.count_logical_blocks(markdown), 0)

    def test_counts_indented_code_after_a_list_item(self) -> None:
        markdown = """- Item
    nested code
    continues
- Next item
"""
        self.assertEqual(MODULE.count_logical_blocks(markdown), 3)

    def test_distinguishes_list_continuations_and_nested_items(self) -> None:
        markdown = """- Parent
  continuation
    - Child one
    - Child two
- Sibling
"""
        self.assertEqual(MODULE.count_logical_blocks(markdown), 4)

    def test_counts_blockquoted_list_items(self) -> None:
        markdown = """> - One
> - Two
"""
        self.assertEqual(MODULE.count_logical_blocks(markdown), 2)

    def test_keeps_list_like_indented_code_as_one_block(self) -> None:
        markdown = """    - literal one
    - literal two
"""
        self.assertEqual(MODULE.count_logical_blocks(markdown), 1)

    def test_keeps_blockquoted_fence_as_one_block(self) -> None:
        markdown = """> ```
> - literal one
> - literal two
> ```
"""
        self.assertEqual(MODULE.count_logical_blocks(markdown), 1)

    def test_counts_blank_separated_indented_code(self) -> None:
        markdown = """- Item

    indented code

Paragraph.
"""
        self.assertEqual(MODULE.count_logical_blocks(markdown), 3)

    def test_counts_nested_list_items_after_a_blank_line(self) -> None:
        for markdown in (
            """- Parent

    - Child one
    - Child two
""",
            """> - Parent
>
>     - Child one
>     - Child two
""",
        ):
            with self.subTest(markdown=markdown):
                self.assertEqual(MODULE.count_logical_blocks(markdown), 3)

    def test_cli_reports_over_threshold_without_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "example.md"
            path.write_text("# One\n\nParagraph.\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--threshold", "1", str(path)],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(result.returncode, 0)
        self.assertIn("2 logical blocks", result.stdout)
        self.assertIn("review recommended", result.stdout)

    def test_cli_reports_exact_threshold_for_review(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "example.md"
            path.write_text("# One\n\nParagraph.\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--threshold", "2", str(path)],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(result.returncode, 0)
        self.assertIn("2 logical blocks", result.stdout)
        self.assertIn("review recommended; at threshold", result.stdout)

    def test_cli_rejects_missing_file(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "/definitely/missing/document.md"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cannot read", result.stderr)


if __name__ == "__main__":
    unittest.main()
