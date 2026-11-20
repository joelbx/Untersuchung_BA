VERDICT: ACCEPT

Reviewed `qutebrowser/misc/guiprocess.py` and `tests/unit/misc/test_guiprocess.py`. Both QProcess streams have live handlers with stream-specific severity and replacement keys. Completion reads remaining bytes and publishes nonempty stdout then stderr summaries.

Test: `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/misc/test_guiprocess.py` — 42 passed in 4.43s. `git diff --check` passed. No code defects or test environment problems found.
