Updated [guiprocess.py](/app/qutebrowser/misc/guiprocess.py) to stream stdout and stderr independently. Live stderr uses error severity; completion summaries appear in stdout-then-stderr order, and empty streams are skipped.

Added coverage in [test_guiprocess.py](/app/tests/unit/misc/test_guiprocess.py), including a check that stderr appears before the process exits.

Verification: `pytest -q tests/unit/misc/test_guiprocess.py` — 41 passed. `git diff --check` passed.