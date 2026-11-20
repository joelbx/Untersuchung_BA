# Checkpoint

Task: add `scrolling.bar=overlay` with platform/Qt gating, update boolean migration, and support `js_headers` test gating.

Initial search: `rg -n "scrolling\.bar|OverlayScrollbar|js_headers|enable-features" . --glob '!*.pyc'` could not run because `rg` is unavailable (`/bin/bash: rg: command not found`). Using local grep/find instead.

Implementation: added the `overlay` config value; enabled Chromium's OverlayScrollbar flag only for QtWebEngine with runtime Qt >= 5.11 outside macOS; changed legacy `False` migration to `overlay`; registered/gated `js_headers` for the QtWebEngine 5.12-5.14 dynamic-header bug; marked relevant BDD scenarios; added argument matrix tests.

Checks:
- `xvfb-run -a env QT_QPA_PLATFORM=offscreen pytest -q --no-xvfb --reruns 0 tests/unit/config/test_configinit.py -k 'overlay_scrollbar or chromium_debug or disable_gpu'`: 38 passed.
- `xvfb-run -a env QT_QPA_PLATFORM=offscreen pytest -q --no-xvfb --reruns 0 tests/unit/config/test_configfiles.py`: 160 passed, 1 skipped.
- `xvfb-run -a env QT_QPA_PLATFORM=offscreen pytest --collect-only -q --no-xvfb tests/end2end/features/test_misc_bdd.py`: 74 collected.
- `git diff --check`: passed.

Environment/remaining uncertainty:
- `pytest -q tests/unit/config/test_configinit.py tests/unit/config/test_configfiles.py` aborted at Qt QApplication setup because no display was available.
- `QT_QPA_PLATFORM=offscreen pytest -q -p no:xvfb ...` failed because tests/conftest.py requires the `--no-xvfb` option from the xvfb plugin.
- `QT_QPA_PLATFORM=offscreen pytest -q --no-xvfb ...` failed because tests/conftest.py requires DISPLAY on Linux.
- Under xvfb-run, the entire test_configinit.py run exits with code 1 at existing `TestDarkMode::test_new_chromium`, without a pytest summary; focused changed tests and all configfiles tests pass. This leaves that unrelated full-module test unresolved in this environment.
- `xvfb-run -a env QT_QPA_PLATFORM=offscreen pytest -q --no-xvfb --reruns 0 tests/unit/config/test_configinit.py -k 'not test_new_chromium'`: 161 passed, 1 deselected. The excluded existing test is the one where the full module exits without summary in this environment.
- `xvfb-run -a env QT_QPA_PLATFORM=offscreen pytest --collect-only -q --no-xvfb -m js_headers tests/end2end/features/test_misc_bdd.py`: both marked header scenarios selected.
