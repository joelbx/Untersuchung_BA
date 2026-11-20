Updated process errors to show the capitalized process name, quoted command, and specific error wording. Non-Windows start failures include the requested hint for missing or non-executable commands. Detached start failures now identify the command, and crash notifications avoid a duplicate generic message.

Updated the affected existing expectations in [test_guiprocess.py](/app/tests/unit/misc/test_guiprocess.py:166).

Verification: `pytest -q tests/unit/misc/test_guiprocess.py` passed (21 tests); `git diff --check` passed.