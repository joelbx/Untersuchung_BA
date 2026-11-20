# Checkpoint

Task: migrate `qt.workarounds.disable_accelerated_2d_canvas` to always/auto/never and make auto depend on Qt and Chromium versions.

Initial search: `rg` is unavailable (`/bin/bash: rg: command not found`); using local grep/find fallback.

Status: inspecting repository; implementation and verification pending.

Verification attempt: `python -m pytest -q tests/unit/config/test_qtargs.py` exited 134 with `Fatal Python error: Aborted` in `pytestqt/plugin.py` while creating the Qt application. Retrying with `QT_QPA_PLATFORM=offscreen`.

Implementation: schema now exposes `always`, `auto`, `never` with `auto` default; QtWebEngine setting resolution receives versions, namespace, and special flags. Auto enables the canvas flag only on Qt 6 with Chromium major 1–110. Added boundary and mode tests.

Final verification: `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py tests/unit/config/test_configinit.py tests/unit/config/test_qtargs_locale_workaround.py` exited 0: 573 passed, 1 xfailed. `python -m py_compile qutebrowser/config/qtargs.py tests/unit/config/test_qtargs.py` exited 0. `git diff --check` exited 0.

Unavailable check: `python -m flake8 qutebrowser/config/qtargs.py tests/unit/config/test_qtargs.py` exited 1 with `/usr/local/bin/python: No module named flake8`. Lint status remains unverified; dependencies were not downloaded.
