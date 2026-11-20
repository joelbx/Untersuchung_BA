VERDICT: FIX
Reviewed lib/ansible/cli/doc.py and the checked-out test/units/cli/test_doc.py. The new DocCLI.tty_ify returns the requested separator, but CLI call sites wrap its result with textwrap.fill. In DocCLI.add_fields, a description of 'before HORIZONTALLINE after' becomes '  before  -------------  after', so the CLI output lacks the required newlines. The same pattern appears in main descriptions and notes. Correct the display path so wrapping preserves separator newlines.
Tests: PYTHONPATH=lib:test python -m pytest -q test/units/cli/test_doc.py test/units/cli/test_cli.py -> 31 passed. A direct DocCLI.add_fields reproduction confirmed the defect (contains required separator: False).
TEST_ENVIRONMENT_PROBLEM: none.
