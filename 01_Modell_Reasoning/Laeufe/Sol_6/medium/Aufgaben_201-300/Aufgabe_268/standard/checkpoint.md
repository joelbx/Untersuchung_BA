Task: Fix process startup error messages in qutebrowser/misc/guiprocess.py.
Plan: Inspect current handler and existing tests, update error-specific messages and startup hint, then run relevant existing tests.
Status: Implemented error-code-specific messages with command names and non-Windows startup hints. Updated unit and end-to-end expectations. The guiprocess unit module passes (28 tests); git diff --check passes. The targeted end-to-end scenario is blocked by browser startup (QtWebKit unavailable in this environment), before the spawn assertion runs.
