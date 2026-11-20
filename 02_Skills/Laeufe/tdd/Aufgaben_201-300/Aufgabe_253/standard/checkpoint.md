# Checkpoint

Task: Fix GUIProcess live stderr and per-stream completion reporting.

Implemented: listen to both QProcess output signals; show nonempty live stderr as errors; avoid empty stdout live notifications; drain and summarize stdout before stderr on completion. Added a real subprocess regression test for stderr before exit and updated per-stream final message expectations.

Verification:
- `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/misc/test_guiprocess.py`: 41 passed.
- `git diff --check`: passed.
- `QT_QPA_PLATFORM=offscreen pytest -q`: full suite could not complete; end-to-end setup in `tests/end2end/features/test_open_bdd.py::test_open_s[http://]` failed because QtWebKit could not be imported from PyQt5. The run was stopped after repeated backend failures. Remaining full-suite status is unknown.
- `QT_QPA_PLATFORM=offscreen pytest -q tests/unit --maxfail=1`: exited 1 after reaching `tests/unit/browser/test_caret.py`, without a failure summary; cause unknown.
- `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/misc --maxfail=1`: 99 passed, 7 skipped, then `tests/unit/misc/test_elf.py::test_result` failed: `ImportError: QtWebEngineWidgets must be imported before a QCoreApplication instance is created`. Remaining misc-suite status is unknown.
- `QT_QPA_PLATFORM=offscreen pytest -q -p no:rerunfailures tests/unit/misc/test_guiprocess.py`: cannot start because pytest.ini requires `pytest-rerunfailures`.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used grep/find.
