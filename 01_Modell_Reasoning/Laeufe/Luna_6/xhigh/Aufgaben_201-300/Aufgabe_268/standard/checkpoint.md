# Checkpoint

Task: Fix process startup error messages in `qutebrowser/misc/guiprocess.py` so they include the capitalized process name, quoted command, specific error wording and details, and the requested non-Windows hint for missing or non-executable commands.

Progress: `_on_error` maps the requested `QProcess` error codes to specific wording, names the capitalized process and quoted command, and appends the requested non-Windows hint for missing or non-executable commands. Crash errors use that specific message without a duplicate generic notification from `_on_finished`; detached start failures also identify the process and command. Updated the existing affected expectations. Verification: `pytest -q tests/unit/misc/test_guiprocess.py` passed (21 tests), and `git diff --check` passed.
