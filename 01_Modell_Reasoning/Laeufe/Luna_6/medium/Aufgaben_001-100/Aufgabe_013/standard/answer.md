Implemented `DocCLI.tty_ify` in [doc.py](/app/lib/ansible/cli/doc.py:74). It renders the requested macros in one pass and leaves unsupported parenthesized text unchanged.

Verification: the requested macro cases passed, and `test/units/cli/test_cli.py` passed (27 tests). `git diff --check` also passed.