# Checkpoint

Task: Move MIME suffix workaround to module level and update file selection.
Status: Complete.
Changes: Added `webview.extra_suffixes_workaround` with Qt version gating, exact and wildcard MIME expansion, iterable support, and extra-only suffix output. `WebEnginePage.chooseFiles` unions and deduplicates the original entries and extras before its single superclass fallback call. Updated existing webview tests for the module-level API, version bounds, iterable input, and instance-free invocation.
Validation: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_webview.py` passed (24 tests); `python -m compileall -q` passed; `git diff --check` passed. flake8 is unavailable in the environment.
