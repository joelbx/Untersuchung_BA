Updated [guiprocess.py](/app/qutebrowser/misc/guiprocess.py) to stream both stdout and stderr live, then publish nonempty final summaries in stdout-then-stderr order with informational and error severity respectively.

Updated the focused test to check final summaries. Verification: `pytest -q tests/unit/misc/test_guiprocess.py` passed (40 tests), and `git diff --check` passed.