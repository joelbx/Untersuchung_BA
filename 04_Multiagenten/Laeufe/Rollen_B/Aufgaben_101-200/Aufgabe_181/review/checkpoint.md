VERDICT: FIX
Reviewed qutebrowser/misc/guiprocess.py and tests/unit/misc/test_guiprocess.py. No production code defect found in the changed outcome/message paths. Two new tests fail under PyQt6.

Tests:
- `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/misc/test_guiprocess.py` exited 4: PyQt5 is absent; repository defaults to PyQt5. TEST_ENVIRONMENT_PROBLEM resolved for rerun by selecting installed PyQt6.
- `QUTE_QT_WRAPPER=PyQt6 QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/misc/test_guiprocess.py` exited 1: 43 passed, 2 failed, 6 reruns.

Test defects:
- tests/unit/misc/test_guiprocess.py:436: test_exit_unsuccessful[True] calls message_mock.getmsg(error), which asserts there is exactly one total message. Verbose mode also emits the expected Executing info message. Select the error message by level without assuming total count one.
- tests/unit/misc/test_guiprocess.py:457: test_exit_uses_own_pid emits the expected error message but does not allow its ERROR log; the test harness raises from fail_on_logging. Wrap the failing-process wait in caplog.at_level(logging.ERROR), as adjacent tests do.

No project code or test files changed during this review.
