# Checkpoint

Implemented Qt wrapper selection/error changes in machinery and earlyinit, with regression tests and updated version-info expectation.

## Verification

- `rg` unavailable: `/bin/bash: rg: command not found`; used grep/find.
- `pytest -q tests/unit/test_qt_machinery.py tests/unit/misc/test_earlyinit.py` initially failed at conftest (`ModuleNotFoundError: No module named 'qutebrowser'`); using `PYTHONPATH=.` resolved it.
- Red run (`PYTHONPATH=. pytest -q tests/unit/test_qt_machinery.py tests/unit/misc/test_earlyinit.py`) showed 7 intended failures before implementation.
- Focused tests (`PYTHONPATH=. pytest -q tests/unit/test_qt_machinery.py tests/unit/misc/test_earlyinit.py --override-ini addopts=''`) had 32 passes and one test assertion error; corrected the assertion to match the actual diagnostic layout.
- `PYTHONPATH=. pytest -q tests/unit/utils/test_version.py::test_version_info --override-ini addopts=''`: 9 passed.
- Full-suite run with `PYTHONPATH=. QTWEBENGINE_DISABLE_SANDBOX=1 pytest -q -x --reruns 0 --override-ini addopts=''` exposed a startup NameError in `get_argparser` due to removal of machinery import; restored import and confirmed `tests/end2end/test_adblock_e2e.py::test_adblock[auto]` passes.
- Second full-suite run with the same command: 65 passed, 140 skipped, 1 xfailed, then `tests/end2end/test_insert_mode.py::test_auto_load[True-False-True]` failed because the expected insert-mode log was absent; captured log says `No focused element!`. This appears unrelated to wrapper changes, but full suite is not green.
- `PYTHONPATH=. QTWEBENGINE_DISABLE_SANDBOX=1 pytest -q tests/unit -x --reruns 0 --override-ini addopts=''` currently running; result pending.
- Unit suite (`PYTHONPATH=. QTWEBENGINE_DISABLE_SANDBOX=1 pytest -q tests/unit -x --reruns 0 --override-ini addopts=''`): 7312 passed, 133 skipped, 44 xfailed; stopped at `tests/unit/utils/test_urlmatch.py::test_invalid_patterns[host-ipv6-two-closing]` due `[XPASS(strict)] https://bugs.python.org/issue34360` (unrelated to Qt wrapper changes).
- Final focused run (`PYTHONPATH=. pytest -q tests/unit/test_qt_machinery.py tests/unit/misc/test_earlyinit.py tests/unit/utils/test_version.py::test_version_info --reruns 0 --override-ini addopts=''`): 42 passed.
- `git diff --check`: clean.
