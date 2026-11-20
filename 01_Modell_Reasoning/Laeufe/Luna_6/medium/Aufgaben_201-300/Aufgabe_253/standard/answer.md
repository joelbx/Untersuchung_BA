Updated [guiprocess.py](/app/qutebrowser/misc/guiprocess.py) to stream stdout and stderr independently as data arrives. At completion, non-empty streams get separate summaries: stdout as informational, then stderr as an error. Empty streams produce no messages.

Added stderr live-stream coverage and updated summary assertions in [test_guiprocess.py](/app/tests/unit/misc/test_guiprocess.py).

Verification: `pytest -q tests/unit/misc/test_guiprocess.py` passed (41 tests), and `git diff --check` passed.