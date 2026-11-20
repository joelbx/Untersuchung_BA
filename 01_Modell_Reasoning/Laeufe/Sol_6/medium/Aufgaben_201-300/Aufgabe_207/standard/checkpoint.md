# Checkpoint

Task: consolidate QtWebEngine `--enable-features` arguments from CLI, `config.val.qt.args`, and qutebrowser configuration.

Implementation: `qt_args` extracts existing feature arguments for QtWebEngine and passes them to `_qtwebengine_args`; `_qtwebengine_enabled_features` splits comma-separated values and adds `OverlayScrollbar` only under its existing conditions. QtWebKit argument handling is unchanged.

Verification: `pytest -q -o addopts='' tests/unit/config/test_qtargs.py -k 'not test_new_chromium'` passed (83 tests). The full file exits at the pre-existing `test_new_chromium` environment/version check before reporting a result. `git diff --check` passed.
