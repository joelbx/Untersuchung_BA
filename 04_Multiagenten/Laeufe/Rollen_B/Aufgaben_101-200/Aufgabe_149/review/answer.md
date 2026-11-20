VERDICT: ACCEPT

The patch meets the stated QtWebEngine argument requirements. It merges enabled features into one flag, preserves each disable flag as a separate, unmodified argument, and handles flags from both command line and configuration. I found no code defect.

`python -m pytest -q tests/unit/config/test_qtargs.py` — **84 passed**. `git diff --check` — **passed**. No test environment problem.