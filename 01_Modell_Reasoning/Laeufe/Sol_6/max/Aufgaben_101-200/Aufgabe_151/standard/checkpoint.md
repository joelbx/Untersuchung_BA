Task: Fix QtWebEngine file picker MIME extension handling in `qutebrowser/browser/webengine/webview.py`.

Status: Completed. Added `extra_suffixes_workaround` with the runtime Qt 6.2.3–6.6.x gate, Python MIME lookups for specific types and wildcards, and exclusion of extensions already accepted. `chooseFiles` now adds the missing suffixes before calling the Qt parent method.

Verification: `QT_QPA_PLATFORM=offscreen QTWEBENGINE_DISABLE_SANDBOX=1 python -m pytest -q tests/unit/browser/webengine/test_webview.py tests/unit/utils/test_qtutils.py::test_version_check tests/unit/utils/test_qtutils.py::test_version_check_compiled_and_exact` passed (31 tests). `git diff --check` passed. flake8 is not installed locally.
