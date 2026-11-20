# Checkpoint

Task: Consolidate QtWebEngine `--enable-features` arguments from CLI, configured Qt arguments, and qutebrowser features.

Root cause: `qt_args` appended CLI/config Qt arguments unchanged and `_qtwebengine_args` appended a separate feature argument generated only from overlay scrollbar configuration. No path passed existing feature flags to the helper. A regression test reproduced two or three separate entries before the patch.

Patch: For QtWebEngine only, extract existing `--enable-features=` entries from `argv`, remove them, and pass them to `_qtwebengine_args`. `_qtwebengine_enabled_features` splits their comma-separated values and adds `OverlayScrollbar` when required. The helper emits one consolidated entry only when features exist. Regression tests cover CLI and configured values, non-WebEngine behavior, Qt version, macOS, empty values, and direct helpers.

Verification: `pytest -q -o addopts='' tests/unit/config/test_qtargs.py -k 'not test_new_chromium'` passed (82 passed, 1 deselected). `git diff --check` passed. The full file command `pytest -q -o addopts='' tests/unit/config/test_qtargs.py` exited 1 while running `TestDarkMode::test_new_chromium`. Isolated command `pytest -vv -o addopts='' tests/unit/config/test_qtargs.py::TestDarkMode::test_new_chromium` exited 139 with `Fatal Python error: Segmentation fault`, stack through `qutebrowser/browser/webengine/webenginesettings.py:360 init_user_agent` and `qutebrowser/utils/version.py:403 _chromium_version`. This is an environment/native QtWebEngine crash outside the changed argument assembly, so that one existing version probe remains unverified.

Local search note: `rg` is unavailable; used `grep` and `find`.
