# Checkpoint

Task: Fix `DocCLI.tty_ify(text)` for documented macros, multiple macros, and unsupported parenthesized text.

Implemented:
- Added a `DocCLI` class method covering `I/B/M/U/C`, `L/R`, and `HORIZONTALLINE`.
- The method recognizes complete supported tokens, preserving unknown forms and ordinary words such as `IBM(International Business Machines)`.
- Added focused tests in `test/units/cli/test_doc.py`.

Verification:
- `PYTHONPATH=lib:test pytest -q test/units/cli/test_doc.py test/units/cli/test_cli.py`: 32 passed.
- `git diff --check`: passed.
- Broader `PYTHONPATH=lib:test pytest -q test/units/cli`: 139 passed, with failures/errors in unrelated adhoc and Galaxy tests (including Galaxy CLI context setup and collection output assumptions); the new doc tests passed in that run.
