Task: Fix ansible-doc terminal rendering of documentation macros.

Status: Implemented DocCLI.tty_ify in lib/ansible/cli/doc.py. It renders I, B, M, U, C, L, R, and HORIZONTALLINE and preserves unsupported parenthesized words. Added focused unit coverage in test/units/cli/test_doc.py.

Validation: `PYTHONPATH=lib:test/units python -m pytest -q test/units/cli/test_doc.py test/units/cli/test_cli.py` passed (30 tests). `git diff --check` passed. `rg` is unavailable; local inspection used grep/find instead.
