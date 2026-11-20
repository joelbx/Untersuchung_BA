# Checkpoint

Task: correct GUI process completion messages and SIGTERM handling.
Status: implementation and regression tests complete.

Changes:
- ProcessOutcome recognizes SIGTERM, reports `terminated`, and names crash signals.
- GUIProcess completion messages include the process's own PID; SIGTERM is silent unless verbose.
- Real-process regression tests cover success, failure, SIGSEGV, and SIGTERM messages and states.

Verification:
- `rg -n ...`: unavailable, `/bin/bash: rg: command not found`; used local grep/find.
- `python -m pytest --version`: failed before collection, `ModuleNotFoundError: No module named 'PyQt5'`. Selected installed PyQt6 using `QUTE_QT_WRAPPER=PyQt6`.
- `QUTE_QT_WRAPPER=PyQt6 QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/misc/test_guiprocess.py -k 'start_verbose or exit_unsuccessful or exit_crash or exit_sigterm'`: RED, seven expected failures before implementation.
- `QUTE_QT_WRAPPER=PyQt6 QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/misc/test_guiprocess.py`: 43 passed, but command exited 1 after `XIO: fatal IO error 0 (Success) on X server ":0"` at teardown.
- `QUTE_QT_WRAPPER=PyQt6 QT_QPA_PLATFORM=offscreen python -m pytest -p no:xvfb -q tests/unit/misc/test_guiprocess.py`: setup failed with `RuntimeError: No display and no Xvfb available!`.
- `xvfb-run -a env QUTE_QT_WRAPPER=PyQt6 QT_QPA_PLATFORM=offscreen python -m pytest -p no:xvfb -q tests/unit/misc/test_guiprocess.py`: 43 passed, exit 0.
- `xvfb-run -a env QUTE_QT_WRAPPER=PyQt6 QT_QPA_PLATFORM=offscreen python -m pytest -p no:xvfb -q tests/unit/completion/test_models.py tests/unit/commands/test_userscripts.py tests/unit/browser/test_qutescheme.py`: 121 passed, exit 0.
- `QUTE_QT_WRAPPER=PyQt6 QT_QPA_PLATFORM=offscreen python -m pytest -q`: full suite collected 9805 items, then end-to-end tests failed to start Chromium as root: `Running as root without --no-sandbox is not supported` (tests/end2end/test_adblock_e2e.py and tests/end2end/test_hints_html.py observed). The run was stopped after repeated environment failures; no full-suite pass is claimed.
- Final rerun of GUIProcess tests after formatting: 43 passed, exit 0.
