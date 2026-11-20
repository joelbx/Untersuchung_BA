Task: Fix `DocCLI.tty_ify` output for documentation macros and preserve ordinary parenthesized words.

Status: Implemented `DocCLI.tty_ify` in `lib/ansible/cli/doc.py` and added focused tests in `test/units/cli/test_doc.py`.

Verification: `PYTHONPATH=lib:test pytest -q test/units/cli/test_doc.py test/units/cli/test_cli.py && git diff --check` exited 0; 31 tests passed.
