# Checkpoint

Task: move MIME suffix workaround to a module-level `extra_suffixes_workaround` in `qutebrowser/browser/webengine/webview.py`, and have `WebEnginePage.chooseFiles` pass the deduplicated union to `super().chooseFiles` once.

Status: implemented the module-level helper, updated `WebEnginePage.chooseFiles` to pass a deduplicated union to its single Qt superclass fallback, and preserved the external picker path. Updated the existing webview tests for module scope, version boundaries, iterables, and deduplication.

Verification: `QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/browser/webengine/test_webview.py -q` passed (25 tests); `git diff --check` passed.
