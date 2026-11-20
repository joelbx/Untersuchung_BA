# Checkpoint

Task completed: `DocCLI.tty_ify(text)` now handles I/B/M/U/R/C/L and `HORIZONTALLINE` in a single pass, preserves unsupported parenthesized text, and avoids interpreting macro-like substrings within words. Added focused unit coverage in `test/units/cli/test_doc.py`.

Verification: `PYTHONPATH=lib python3 -m pytest -q test/units/cli/test_doc.py` passed (3 tests); `git diff --check` passed. `ansible-test units test/units/cli/test_doc.py` could not run because its Python 3.8 environment lacks pytest; the repository test file passed with the available Python 3.9 pytest.
