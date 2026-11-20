VERDICT: FIX

Code defect: qutebrowser/misc/guiprocess.py:192-194 still reports `Error while spawning testprocess` on a failed detached startup. It omits the command, capitalized process name, error type, detail, and applicable non-Windows hint required for any startup failure. `:spawn --detach` uses this path (qutebrowser/browser/commands.py:1109). tests/unit/misc/test_guiprocess.py:test_start_detached_error still asserts the obsolete message. Correct the detached failure path and its existing test; obtain the QProcess error detail where available.

Tests:
- `pytest -q tests/unit/misc/test_guiprocess.py`: 30 passed.
- `pytest -q tests/end2end/features/test_spawn_bdd.py::test_running_spawn_with_command_that_does_not_exist`: failed before scenario execution because QtWebKit could not be imported (TEST_ENVIRONMENT_PROBLEM).
- `pytest -q --qute-bdd-webengine tests/end2end/features/test_spawn_bdd.py::test_running_spawn_with_command_that_does_not_exist`: failed before scenario execution because Chromium refused root execution without --no-sandbox (TEST_ENVIRONMENT_PROBLEM).
- `QTWEBENGINE_DISABLE_SANDBOX=1 pytest -q --qute-bdd-webengine tests/end2end/features/test_spawn_bdd.py::test_running_spawn_with_command_that_does_not_exist`: 1 passed.

Review only; project code and tests were not changed.
