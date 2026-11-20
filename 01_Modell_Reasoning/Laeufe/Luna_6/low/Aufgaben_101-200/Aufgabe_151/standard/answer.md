Implemented the MIME suffix workaround in [webview.py](/app/qutebrowser/browser/webengine/webview.py). It applies only to Qt 6.2.3 through 6.6.x, handles specific and wildcard MIME types, and adds missing suffixes to the default picker’s accepted filters.

The existing WebEngine tests passed: **6 passed**. `git diff --check` also passed.