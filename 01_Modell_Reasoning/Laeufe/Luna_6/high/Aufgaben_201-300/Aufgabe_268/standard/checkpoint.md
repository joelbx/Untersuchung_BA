# Checkpoint: process startup error message

- `_on_error` now formats `FailedToStart`, `Crashed`, `Timedout`, `WriteError`, and `ReadError` with the capitalized process name, quoted command, type specific wording, and QProcess error detail.
- Non-Windows failed starts with `No such file or directory` or `Permission denied` receive the requested executable hint.
- Crash errors are reported by `_on_error`; `_on_finished` keeps command aware crash status in spawn output without emitting a duplicate error notification.
- Updated `tests/unit/misc/test_guiprocess.py` for error types, hints, and crash wording.
- Verification: `pytest -q tests/unit/misc/test_guiprocess.py` passed (28 passed); `git diff --check` passed.
