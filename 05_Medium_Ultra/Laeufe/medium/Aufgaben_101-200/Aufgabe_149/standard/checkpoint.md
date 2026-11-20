Task: Add support for --disable-features in QtWebEngine argument building.
Status: Complete. QtWebEngine argument building merges enable flags and preserves disable flags from both command line and configuration. Added source combination coverage.
Verification: pytest -q tests/unit/config/test_qtargs.py (86 passed); git diff --check passed.
Constraints: Use local repository and existing tests; preserve git history, index, and harness configuration.
