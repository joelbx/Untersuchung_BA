# Checkpoint

Task: fix `DocCLI.tty_ify` macro rendering, preserve ordinary parenthesized words, and run tests.
Status: inspecting repository and test layout before writing a failing regression test.
Constraints: no external research or downloads; preserve git history/index and harness configuration.

TDD: Added `test/units/cli/test_doc_tty.py`; first run (`PYTHONPATH=lib:test pytest -q test/units/cli/test_doc_tty.py`) showed 7 expected failures and 1 pass. Implemented `DocCLI.tty_ify` and reran `PYTHONPATH=lib:test pytest -q -o addopts='' test/units/cli/test_doc_tty.py`: 8 passed.
CLI directory run: `PYTHONPATH=lib:test pytest -q -o addopts='' test/units/cli` exited 1: 9 failed, 142 passed, 59 errors, 2 warnings. Galaxy setup errors include `TypeError: join() argument must be str, bytes, or os.PathLike object, not 'NoneType'` in `Galaxy.__init__`; unrelated failures also appeared in adhoc and collection list tests.
Full-suite attempt: `PYTHONPATH=lib:test pytest -q -o addopts=''` collected 3359 items with 18 collection errors (including missing `validate_modules` and an `ansible_test` import mismatch). After 108.26 seconds it was interrupted because unrelated failures and errors were widespread: 98 failed, 440 passed, 14 skipped, 291 errors, 1116 rerun, 2 warnings at interruption. This is not a passing full-suite result.
Final focused verification: `PYTHONPATH=lib:test pytest -q -o addopts='' test/units/cli/test_doc_tty.py test/units/cli/test_cli.py` passed all 35 tests. `git diff --check` passed.
