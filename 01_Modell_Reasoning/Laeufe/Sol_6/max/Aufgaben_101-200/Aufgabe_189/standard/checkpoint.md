# Checkpoint

- Task: move MIME suffix workaround into `qutebrowser/browser/webengine/webview.py` module scope and use it from `WebEnginePage.chooseFiles`.
- Status: complete. The workaround is a module-level helper, and `chooseFiles` passes a deduplicated union as the third positional argument to one `super().chooseFiles` call site while preserving the external uploader path.
- Verification: `QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/browser/webengine/test_webview.py -q` passed (26 tests); `git diff --check` passed. `flake8` is not installed, so its check could not run.
