# Checkpoint

Task: Fix GUI process startup error messages to include the process name, exact command, error type/detail, and a non-Windows executable hint for missing or inaccessible commands.

Plan: Inspect implementation and tests; write and verify a failing regression test; implement the minimal fix; run focused and project tests.

Status: Implemented and focused tests passed.

Implementation: `_on_error` now formats the capitalized process name, exact command, error type, and Qt error detail. FailedToStart adds the executable hint on non-Windows when the detail ends with either missing-file or permission-denied text (including Qt's `execvp:` prefix).

TDD: Added regression tests first; the focused run failed on the original generic message. After implementation, `xvfb-run -a -s '-screen 0 1280x1024x24' env QT_QPA_PLATFORM=offscreen python -m pytest -q -p no:xvfb --reruns 0 tests/unit/misc/test_guiprocess.py` exited 0 with 29 passed.

Verification limits: `QT_QPA_PLATFORM=offscreen python -m pytest -q --reruns 0 tests/unit/misc/test_guiprocess.py` reported 29 passed but exited 1 with `XIO: fatal IO error 0 (Success) on X server`, so it is not counted as a clean pass. The controlled-display command above resolved that. A full-project run using `xvfb-run -a -s '-screen 0 1280x1024x24' env QT_QPA_PLATFORM=offscreen python -m pytest -q -p no:xvfb --reruns 0` hit end-to-end setup errors: qutebrowser cannot import QtWebKit in this environment (`cannot import name 'QtWebKit' from 'PyQt5'`). It was interrupted after 61 passed, 9 skipped, and 39 errors. Tests failing during setup included `tests/end2end/features/test_open_bdd.py::test_open_s[http://]`, `tests/end2end/misc/test_runners_e2e.py::test_command_expansion[foo{{url}}bar-foo{url}bar]`, and multiple tests under `tests/end2end/test_adblock_e2e.py`, `tests/end2end/test_dirbrowser.py`, and `tests/end2end/test_hints_html.py`.

Additional verification: `xvfb-run -a -s '-screen 0 1280x1024x24' env QT_QPA_PLATFORM=offscreen python -m pytest -q -p no:xvfb --reruns 0 tests/unit/misc` exited 1 without a pytest failure summary after output reached `tests/unit/misc/test_elf.py .....`; the exact cause is unknown from its output. The focused GUIProcess suite still exited 0 with all 29 tests passing. `git diff --check` exited 0.

Remaining: None for the requested fix; full-suite confidence is limited by the environment's QtWebKit failure and the unexplained unit/misc run exit.
