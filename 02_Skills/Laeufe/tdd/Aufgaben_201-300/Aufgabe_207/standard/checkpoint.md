# Checkpoint

Task: consolidate QtWebEngine `--enable-features` arguments from CLI and `config.val.qt.args` with qutebrowser-required features.

Implemented: `qt_args` extracts all existing feature flags for QtWebEngine, removes them from argv, and passes them to `_qtwebengine_args`; `_qtwebengine_enabled_features` strips each prefix and splits comma-separated feature names before appending the configured `OverlayScrollbar` feature. QtWebKit arguments remain unchanged. Added regression tests for CLI/config merging, repeated flags, helper behavior, and QtWebKit preservation.

Verification:
- `pytest -q tests/unit/config/test_qtargs.py -k 'existing_features_from_cli_and_config or multiple_feature_entries_without_overlay or helper_merges_feature_flags'`: 4 passed.
- `pytest -q tests/unit/config/test_qtargs.py -k 'not test_new_chromium'`: 80 passed, 1 deselected.
- `pytest -q tests/unit/config/test_qtargs.py`: exits 1 while running existing `TestDarkMode.test_new_chromium`, without pytest summary. The local PyQt Chromium version appears to differ from that test's fixed allowlist; the cause of abrupt exit is unconfirmed.
- `pytest -q`: started as the full project suite, then interrupted after repeated end-to-end setup errors because local PyQt5 cannot import QtWebKit (`cannot import name 'QtWebKit' from 'PyQt5'`). Full suite result remains unknown.
- `git diff --check`: passed.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep` fallback.
