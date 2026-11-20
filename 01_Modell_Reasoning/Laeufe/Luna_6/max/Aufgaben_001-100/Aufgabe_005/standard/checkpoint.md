# Checkpoint

Task: improve early Qt wrapper initialization, availability diagnostics, and SelectionInfo formatting in `/app`.

Completed:
- Added `NoWrapperAvailableError` carrying `SelectionInfo`, and made implicit initialization autoselect, raise this error when all candidates fail, and return the initialized info on success.
- Improved autoselection failure details and implemented the requested short and verbose `SelectionInfo` formats.
- Moved explicit startup initialization into early initialization, passed the returned info to `check_qt_available`, added the Qt info debug log, and padded checker diagnostics with two trailing newlines.
- Updated existing tests for the changed implicit selection and version output behavior.

Verification:
- `tests/unit/test_qt_machinery.py` and `tests/unit/misc/test_earlyinit.py`: 27 passed.
- `tests/unit/test_qutebrowser.py`: 19 passed.
- `tests/unit/utils/test_version.py -k test_version_info`: 9 passed.
- `compileall` and `git diff --check`: passed.
- Broader `test_version.py` runs exited with status 1 mid-run without a traceback in a WebEngine version test; the changed version info cases passed independently.
