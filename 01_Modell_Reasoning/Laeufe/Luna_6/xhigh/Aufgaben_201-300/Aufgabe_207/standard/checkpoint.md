# Checkpoint

## Objective
Consolidate QtWebEngine `--enable-features` arguments while preserving user features and existing non-QtWebEngine behavior.

## Changes
- QtWebEngine processing now extracts `--enable-features=...` and the `--enable-features VALUE` CLI form, removes those individual arguments, and emits one combined argument when the combined feature list is nonempty.
- `_qtwebengine_enabled_features(feature_flags)` splits supplied feature values and conditionally adds `OverlayScrollbar` using the existing Qt version, platform, and scrolling configuration checks.
- Added coverage for CLI/config merging, multiple existing entries, empty feature values, direct feature splitting, and unchanged QtWebKit arguments.

## Verification
- `python -m pytest -q tests/unit/config/test_qtargs.py -k 'not test_new_chromium'`: 80 passed.
- The excluded `test_new_chromium` crashes in this environment with a segmentation fault in `webenginesettings.init_user_agent`; running the full file stops at that probe.
- `git diff --check`: passed.
- `flake8` is unavailable in the environment (`No module named flake8`).
