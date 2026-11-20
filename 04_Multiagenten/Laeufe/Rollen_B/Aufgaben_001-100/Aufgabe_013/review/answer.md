VERDICT: FIX

The patch passes the selected tests, but **CLI output still loses the horizontal rule’s required newlines**. [DocCLI.add_fields](/app/lib/ansible/cli/doc.py:560) passes the result of `tty_ify` through `textwrap.fill`; a description of `before HORIZONTALLINE after` displays as `before  -------------  after`. The main description and notes use the same pattern. Preserve the separator newlines when wrapping CLI text.

Tests: `PYTHONPATH=lib:test python -m pytest -q test/units/cli/test_doc.py test/units/cli/test_cli.py` — **31 passed**. A direct `DocCLI.add_fields` check reproduced the output defect. **TEST_ENVIRONMENT_PROBLEM:** none.