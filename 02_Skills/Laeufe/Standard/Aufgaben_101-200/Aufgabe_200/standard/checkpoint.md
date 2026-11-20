# Checkpoint

Task: add unit-aware durations to `:later` via `utils.parse_duration`.

Implemented:
- `parse_duration` accepts ordered h/m/s components (including decimals and whitespace between units), returns integer milliseconds, and keeps bare integers as milliseconds.
- `:later` parses string durations and reports invalid values as command errors.
- Updated command help and added unit and end-to-end test coverage.

Checks:
- `DISPLAY=:0 QT_QPA_PLATFORM=offscreen pytest -p no:xvfb -q tests/unit/misc/test_utilcmds.py tests/unit/utils/test_utils.py`: 190 passed, exit 0.
- `git diff --check`: passed.
- `pytest -q tests/unit/utils/test_utils.py tests/unit/misc/test_utilcmds.py`: 190 passed, but process exit 1 with `The X11 connection broke: I/O error (code 1)` at shutdown. Offscreen rerun above resolves this.
- `DISPLAY=:0 QT_QPA_PLATFORM=offscreen pytest -p no:xvfb -q tests/end2end/features/test_utilcmds_bdd.py -k later_with_units`: setup error; QtWebKit cannot be imported (`cannot import name 'QtWebKit' from 'PyQt5'`).
- `DISPLAY=:0 QT_QPA_PLATFORM=offscreen QTWEBENGINE_DISABLE_SANDBOX=1 pytest -p no:xvfb -q tests/end2end/features/test_utilcmds_bdd.py -k later_with_units --qute-bdd-webengine`: setup error; `Failed to create OpenGL context` while starting the browser. The new end-to-end scenario remains unverified in this environment.

`rg` is unavailable; used local grep/find. No dependencies downloaded.
