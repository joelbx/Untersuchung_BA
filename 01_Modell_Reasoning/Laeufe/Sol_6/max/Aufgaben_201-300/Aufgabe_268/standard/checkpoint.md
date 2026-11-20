# Checkpoint

- Task: Include the command and process error type in GUI process startup errors.
- Repository state: clean at start.
- Implemented error messages for all QProcess error types with the process name,
  quoted command, and error detail. Added the executable hint for matching
  startup errors on non-Windows platforms, including Qt's `execvp:` detail.
- Detached startup failures use the same formatter. Crash exits avoid duplicate
  messages and still report a crash if no error signal arrives.
- Updated `tests/unit/misc/test_guiprocess.py`; relevant suite result:
  `DISPLAY=:0 QT_QPA_PLATFORM=offscreen pytest -q --no-xvfb
  tests/unit/misc/test_guiprocess.py tests/unit/misc/test_editor.py`:
  84 passed, 4 skipped.
