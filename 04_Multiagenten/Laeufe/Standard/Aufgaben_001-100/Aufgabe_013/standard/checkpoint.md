Task: Fix ansible-doc CLI documentation macro rendering through DocCLI.tty_ify.
Status: Complete. DocCLI.tty_ify now renders I/B/M/U/C, L/R, and HORIZONTALLINE in one pass while preserving unsupported text and parenthesized phrases inside words.
Files: lib/ansible/cli/doc.py; test/units/cli/test_doc.py.
Verification: PYTHONPATH=lib:test python -m pytest -q test/units/cli/test_doc.py test/units/cli/test_cli.py (30 passed); git diff --check passed.
Constraints observed: Local repository only; no git history, index, or harness configuration changes.
