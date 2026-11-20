Task: Improve Qt wrapper error handling and early initialization.
Status: Complete. Moved explicit machinery initialization into early_init, added availability checks and NoWrapperAvailableError with SelectionInfo, improved implicit autoselection and logging, and updated related tests.
Verification: python -m pytest -q tests/unit/test_qutebrowser.py tests/unit/test_qt_machinery.py tests/unit/misc/test_earlyinit.py (53 passed); git diff --check passed.
Constraints observed: Local repository only; no git history/index/harness changes.
