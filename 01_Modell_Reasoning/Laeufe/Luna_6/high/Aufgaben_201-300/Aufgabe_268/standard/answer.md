Updated process error messages to include the capitalized process name, quoted command, error type, and QProcess detail. Non-Windows missing-command and permission errors now include the requested hint. Crash notifications also identify the command.

Verification: `pytest -q tests/unit/misc/test_guiprocess.py` passed (28 tests), and `git diff --check` passed.