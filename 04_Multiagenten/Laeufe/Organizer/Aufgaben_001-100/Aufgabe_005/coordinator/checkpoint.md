Task: Improve Qt wrapper error handling and early initialization.
Status: Implemented and verified. Explicit startup now initializes machinery inside early_init and passes the returned SelectionInfo to check_qt_available. Implicit initialization autoselects an importable wrapper or raises NoWrapperAvailableError with import outcomes. SelectionInfo formatting, diagnostic spacing, and debug output updated.
Tests: PYTHONPATH=. python -m pytest -q tests/unit/test_qt_machinery.py tests/unit/misc/test_earlyinit.py tests/unit/test_qutebrowser.py (50 passed). git diff --check passed.
Delegation: None.
