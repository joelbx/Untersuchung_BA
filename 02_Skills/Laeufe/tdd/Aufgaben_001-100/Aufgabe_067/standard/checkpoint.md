# Checkpoint

Implemented and tested `scrolling.bar=overlay`, QtWebEngine Chromium flag gating, boolean migration (`False` → `overlay`), and `@js_headers` gating for the Qt 5.12–5.14 dynamic-header bug. Added platform/backend/version tests and order-independent debug/GPU flag assertions.

TDD: the overlay validation test failed with `ValidationError: Invalid value 'overlay'`; the `@js_headers` test failed for Qt 5.12 before implementation. The 42-test focused run passed after the configuration/flag patch; a later 83-test marker/arguments run passed but reported an import warning, which was removed by changing the test import.

Environment/check limits:
- `rg` is unavailable (`/bin/bash: rg: command not found`); used `grep`/`find`.
- Plain `pytest` aborted while creating QApplication because no display was configured. `QT_QPA_PLATFORM=offscreen pytest -p no:xvfb` failed because repository fixtures require the plugin's `--no-xvfb` option. `QT_QPA_PLATFORM=offscreen pytest --no-xvfb` failed with `No display and no Xvfb available!`. Test runs use `DISPLAY=:1001 QT_QPA_PLATFORM=offscreen pytest --no-xvfb`.
- The expanded config run `DISPLAY=:1001 QT_QPA_PLATFORM=offscreen pytest --no-xvfb -q tests/end2end/test_marker_gating.py tests/unit/config/test_configinit.py tests/unit/config/test_configdata.py tests/unit/config/test_configfiles.py` exited 1 after `TestDarkMode::test_new_chromium` started, without a pytest summary. Its cause is not yet identified; the focused tests passed.
- A full-suite run is in progress. Its first collection pass reported `StopIteration` in the new marker test due to relative versus absolute paths; the test has been corrected and passed in isolation. End-to-end startup logs also show QtWebKit cannot be imported (`cannot import name 'QtWebKit' from 'PyQt5'`).

Final verification:
- `DISPLAY=:1001 QT_QPA_PLATFORM=offscreen pytest --no-xvfb -q tests/end2end/test_marker_gating.py tests/unit/config/test_configinit.py tests/unit/config/test_configdata.py tests/unit/config/test_configfiles.py -k 'not test_new_chromium'`: 357 passed, 1 skipped, 1 deselected.
- `DISPLAY=:1001 QT_QPA_PLATFORM=offscreen pytest --no-xvfb --collect-only -q`: successful full-suite collection (6 existing skips).
- `git diff --check`: passed.
- `DISPLAY=:1001 QT_QPA_PLATFORM=offscreen timeout 120s pytest --no-xvfb -q`: exited 124 after 120 seconds. The run repeatedly errored in end-to-end tests including `tests/end2end/features/test_open_bdd.py`, `test_prompts_bdd.py`, `tests/end2end/fixtures/test_quteprocess.py`, and `tests/end2end/misc/test_runners_e2e.py` because the test subprocess forced QtWebKit, which cannot be imported from installed PyQt5. This run began before the marker-test collection fix and also reported `StopIteration` there; subsequent full collection succeeded. No full-suite pass is claimed.
- The broad config run including `tests/unit/config/test_configinit.py::TestDarkMode::test_new_chromium` exits 1 without a pytest summary when that test starts. It initializes the QtWebEngine user agent; exact failure cause remains uncertain. The final focused run deselected only this test.
