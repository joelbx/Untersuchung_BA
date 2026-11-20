# Checkpoint

Objective: Resolve the process startup error message issue in `/app`.

Completed: Updated `GUIProcess._on_error` to format messages for FailedToStart, Crashed, Timedout, WriteError, and ReadError with a capitalized process name, quoted command, and error detail. Added the specified non-Windows executable hint, including Qt's `execvp:` detail prefix. Crash completion handling avoids a duplicate generic crash message. Updated existing unit and spawn feature expectations.

Verification: `python -m pytest tests/unit/misc/test_guiprocess.py tests/unit/misc/test_editor.py -q` — 69 passed, 4 skipped. `git diff --check` — clean.

Constraints: No external research, downloads, delegation, git history changes, index baseline changes, or harness configuration changes.
