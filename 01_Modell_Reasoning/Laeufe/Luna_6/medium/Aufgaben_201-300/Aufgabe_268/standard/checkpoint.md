# Checkpoint

Task complete: `GUIProcess._on_error` now formats errors with the capitalized process name, quoted command, code-specific wording, and error detail. Failed starts on non-Windows append the requested hint when the detail exactly matches `No such file or directory` or `Permission denied`.

Updated the existing missing-command test to verify the new message. Validation: `pytest -q tests/unit/misc/test_guiprocess.py` — 21 passed.
