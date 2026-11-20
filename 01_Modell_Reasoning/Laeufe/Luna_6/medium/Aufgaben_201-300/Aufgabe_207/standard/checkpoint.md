# Checkpoint

Implemented QtWebEngine feature argument consolidation in `qutebrowser/config/qtargs.py`.

The QtWebEngine path now extracts both `--enable-features=value` and `--enable-features value` forms from generated argv (including `qt.args` and `--qt-arg`), removes those entries, and sends all feature strings to `_qtwebengine_args`. `_qtwebengine_enabled_features` splits each value on commas and adds the configured OverlayScrollbar feature subject to existing Qt/macOS/config conditions. Other backends retain the previous argv path.

Validation: `pytest -q tests/unit/config/test_qtargs.py` completed successfully (77 tests); `git diff --check` passed.
