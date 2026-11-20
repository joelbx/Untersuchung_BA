# Checkpoint

Task: Include the command and process error type in startup failure messages.
Status: implemented and verified.

Changes:
- Map FailedToStart, Crashed, Timedout, WriteError, and ReadError to distinct messages in GUIProcess._on_error.
- Include the capitalized process label, quoted command, and Qt error detail.
- Add the executable hint for common non-Windows startup errors, including Qt execvp prefixes.
- Route detached startup failures through the same formatter.
- Update unit coverage and the spawn feature expectation.

Verification:
- pytest -q tests/unit/misc/test_guiprocess.py: 36 passed.
- QTWEBENGINE_DISABLE_SANDBOX=1 pytest -q --qute-bdd-webengine tests/end2end/features/test_spawn_bdd.py::test_running_spawn_with_command_that_does_not_exist: 1 passed.
- git diff --check: passed.
