Implemented `extra_suffixes_workaround` in [webview.py](/app/qutebrowser/browser/webengine/webview.py). It resolves specific and wildcard MIME types for Qt 6.2.3 through 6.6.x, skips suffixes already supplied, and adds missing suffixes to the accepted types passed to Qt.

Verification: `python -m pytest tests/unit/browser/webengine/test_webview.py` passed (6 tests); `git diff --check` passed.