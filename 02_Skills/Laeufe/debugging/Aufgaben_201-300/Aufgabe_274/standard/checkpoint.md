# Checkpoint

Task: Add version-aware modes for `qt.workarounds.disable_accelerated_2d_canvas`.

Status: Investigating root cause and current tests. `rg` is unavailable locally; using `grep`/`find` for repository searches.

Root cause: `qtargs._qtwebengine_args` receives `versions`, `namespace`, and `special_flags`, but calls `_qtwebengine_settings_args()` without them. The settings map uses Boolean keys, and `configdata.yml` declares the option as `Bool` with default `true`. Thus automatic version selection cannot be expressed or resolved. Existing enum settings in `configdata.yml` use `String` with `valid_values`; Qt runtime detection uses `machinery.IS_QT6`; the version table maps Qt 6.5 to Chromium 108 and Qt 6.6 to Chromium 112.

Hypothesis: Propagating the three context values to settings resolution, resolving callable map values to enum keys, and migrating the schema/map will produce the requested version boundary behavior.

Baseline check: `python -m pytest -q tests/unit/config/test_qtargs.py -k 'settings_exist or test_webengine_args'` exited 134 before any test ran. Pytest-qt aborted while creating its QApplication, consistent with no display in this environment. Will try `QT_QPA_PLATFORM=offscreen` for test execution.

Implementation: Changed the option to a `String` enum (`always`, `auto`, `never`) with default `auto`. `_qtwebengine_args` now passes version/namespace/special flags into `_qtwebengine_settings_args`, which resolves callable map entries through the returned enum key. The auto resolver enables the flag only with Qt 6 and a nonzero Chromium major below 111. Added integration tests for Qt 5.15.2, Qt 6.5.3 and Qt 6.6.0, plus direct tests for unknown, zero, 110 and 111 Chromium majors.

Verification: `QT_QPA_PLATFORM=offscreen python -m pytest -q --tb=short --reruns 0 tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py` exited 0: 144 passed. `git diff --check` exited 0. `python -m compileall -q qutebrowser/config/qtargs.py tests/unit/config/test_qtargs.py` exited 0.

Tooling note: `QT_QPA_PLATFORM=offscreen python -m pytest -q -p no:rerunfailures tests/unit/config/test_qtargs.py -k accelerated_2d_canvas` exited 4 with `ERROR: Missing required plugins: pytest-rerunfailures` because this repository requires the plugin. Reran the checks with the plugin enabled and `--reruns 0`, which passed. No remaining uncertainty from that error.
