# Checkpoint

Issue: consolidate QtWebEngine `--enable-features=` arguments from CLI, `qt.args`, and qutebrowser configuration.

Current findings: `qt_args` appends all incoming Qt arguments before `_qtwebengine_args`; the latter currently emits its own feature argument. The existing tests cover overlay scrollbar but not merging.

Completed: QtWebEngine now extracts existing feature flags from the assembled Qt argv and emits a single consolidated flag through the existing helpers. CLI `--qt-arg enable-features VALUE` is supported; other backends retain their argument layout. Regression cases cover merging, overlay scrollbar, empty flags, helper parsing, and QtWebKit preservation.

Verification: `pytest -q tests/unit/config/test_qtargs.py -k 'not test_new_chromium'` passed (81 tests). `git diff --check` passed. The excluded existing Chromium version test segfaults in this environment when run alone or in the full module.
