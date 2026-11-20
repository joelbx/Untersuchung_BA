Task: Fix `ansible-doc` terminal rendering of documentation macros in `DocCLI.tty_ify`.
Status: Implemented `DocCLI.tty_ify` for the requested macros and added regression tests.
Verification: `PYTHONPATH=lib:test python -m pytest -q test/units/cli/test_doc.py test/units/cli/test_cli.py` passed (36 tests); `git diff --check` passed.
