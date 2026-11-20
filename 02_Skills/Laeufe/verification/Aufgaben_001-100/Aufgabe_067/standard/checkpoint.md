# Checkpoint

Task: add `scrolling.bar=overlay` with QtWebEngine, Qt version, and platform gating; update boolean migration and tests, including `js_headers` handling.

Status: inspecting repository. `rg` is unavailable (`/bin/bash: rg: command not found`), so searches use `grep`/`find`.

Initial check: `python -m pytest -q tests/unit/config/test_configinit.py tests/unit/config/test_configfiles.py` aborted with exit 134 while creating pytest-qt's `qapp`; `xdpyinfo was not found, X start can not be checked`. Retrying with `QT_QPA_PLATFORM=offscreen` to run without an X display.

Implemented: configuration value and migration, gated QtWebEngine flag, order-independent flag tests, and `js_headers` marker handling for the Qt 5.12-5.14 dynamic-header bug.

Verification: `DISPLAY=:1 QT_QPA_PLATFORM=offscreen python -m pytest --no-xvfb -o addopts='' -q tests/unit/config/test_configinit.py tests/unit/config/test_configfiles.py -k 'not test_new_chromium'` exited 0: 320 passed, 1 skipped, 1 deselected. The focused overlay/debug/GPU/migration selection exited 0: 47 passed. `DISPLAY=:1 QT_QPA_PLATFORM=offscreen python -m pytest --no-xvfb --qute-bdd-webengine -o addopts='' --collect-only -q -m js_headers tests/end2end/features/test_misc_bdd.py` exited 0 and selected both tagged scenarios. `git diff --check` and `python -m compileall -q qutebrowser/config/configinit.py qutebrowser/config/configfiles.py tests/end2end/conftest.py tests/unit/config/test_configinit.py` exited 0.

Environment-limited checks: The full config suite with the same offscreen settings exits 1 while running `TestDarkMode.test_new_chromium`; isolated command `DISPLAY=:1 QT_QPA_PLATFORM=offscreen python -m pytest --no-xvfb -o addopts='' -q tests/unit/config/test_configinit.py -k test_new_chromium` reports `Fatal Python error: Segmentation fault` in `webenginesettings.init_user_agent` / `version._chromium_version`. This unrelated QtWebEngine runtime probe remains unverified here. `python -m flake8 qutebrowser/config/configinit.py qutebrowser/config/configfiles.py tests/end2end/conftest.py tests/unit/config/test_configinit.py tests/unit/config/test_configfiles.py` exits 1 with `/usr/local/bin/python: No module named flake8`.
