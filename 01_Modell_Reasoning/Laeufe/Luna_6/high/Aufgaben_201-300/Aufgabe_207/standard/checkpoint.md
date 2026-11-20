# Checkpoint

Implemented QtWebEngine feature argument consolidation in `qutebrowser/config/qtargs.py`.

- QtWebEngine argument assembly extracts both `--enable-features=...` and `--enable-features VALUE` user forms from CLI and `qt.args`, removes the original entries, and emits one combined feature argument when features exist.
- Feature extraction splits comma-separated values and combines them with the existing OverlayScrollbar condition.
- Other backends retain their existing argument path.

Added focused coverage in `tests/unit/config/test_qtargs.py` for CLI/config inputs, combining both sources, overlay feature combination, backend preservation, and splitting.

Validation: `pytest -q tests/unit/config/test_qtargs.py::TestQtArgs` passed (58 passed); `git diff --check` passed. Running the full test file exits during `TestDarkMode` after 13 dots with exit code 1 and no pytest failure summary; the relevant `TestQtArgs` subset passes.
