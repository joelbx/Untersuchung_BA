Implemented `DocCLI.tty_ify` in [doc.py](/app/lib/ansible/cli/doc.py:74) to render the requested macros, process multiple tokens on a line, and preserve ordinary parenthesized text. Removed the old base `CLI.tty_ify` implementation.

Verification: all 27 existing CLI unit tests passed, targeted macro checks passed, and `git diff --check` was clean.