Updated process errors to include the capitalized process name, quoted command, specific error wording, and error detail. Failed starts on non-Windows systems now include the executable hint, including when Qt prefixes the detail with `execvp:`. Crash errors show once without a duplicate completion message.

Updated the unit and spawn feature expectations in [test_guiprocess.py](/app/tests/unit/misc/test_guiprocess.py) and [spawn.feature](/app/tests/end2end/features/spawn.feature). The checkpoint is recorded in `.codex-role-output/checkpoint.md`.

Verification: `python -m pytest tests/unit/misc/test_guiprocess.py tests/unit/misc/test_editor.py -q` — **69 passed, 4 skipped**. `git diff --check` passed.