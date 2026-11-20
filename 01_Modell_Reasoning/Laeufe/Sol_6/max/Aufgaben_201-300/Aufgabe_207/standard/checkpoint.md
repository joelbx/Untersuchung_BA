# Checkpoint

- Task: consolidate QtWebEngine `--enable-features` arguments while preserving user features.
- Current state: QtWebEngine feature arguments are consolidated across CLI and `qt.args`; WebKit output keeps its original argument form.
- Verification: `test_qtargs.py` passed all 91 tests with `xvfb-run`, `QTWEBENGINE_DISABLE_SANDBOX=1`, and the repository Xvfb plugin disabled. `git diff --check` passed.
- Remaining: none; the checked-out implementation and regression tests are ready for export.
