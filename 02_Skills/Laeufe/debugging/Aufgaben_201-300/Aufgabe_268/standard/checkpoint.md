# Checkpoint

Task: Fix GUIProcess startup error messages in `qutebrowser/misc/guiprocess.py`.

Status: Investigating root cause. Current `_on_error` emits a generic `Error while spawning <what>: <detail>` message, omitting `self.cmd` and the QProcess error code. `rg` is unavailable (`/bin/bash: rg: command not found`), so searches use `grep`/`find`.

Root cause confirmed: `_pre_start` stores the command, but `_on_error` formats only `_what` and `errorString()`. The failing reproduction tests cover the actual missing command and all five requested error codes. On this Linux Qt build, a missing executable returns `execvp: No such file or directory`, so the hint must recognize the error phrase within that detail. Existing crash behavior suppresses `_on_error` on non-Windows because `_on_finished` already reports it; that avoids duplicate messages.

Fix: `_on_error` now maps the five QProcess errors to distinct descriptions, includes the capitalized process name and quoted `self.cmd`, and appends the POSIX hint for missing-file or permission-denied startup details. Updated unit and spawn feature expectations.

Checks:
- `pytest -q -o addopts='' tests/unit/misc/test_guiprocess.py` — exit 0, 28 passed, 1 rerun.
- `pytest -q -o addopts='' tests/end2end/features/test_spawn_bdd.py -k 'command_that_does_not_exist'` — exit 1 before scenario assertion: browser fixture cannot start with QtWebKit backend (`cannot import name 'QtWebKit' from 'PyQt5'`). This leaves the end-to-end assertion unverified in this environment. No dependencies downloaded.
