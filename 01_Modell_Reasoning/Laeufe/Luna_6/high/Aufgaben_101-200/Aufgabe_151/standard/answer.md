Implemented the Qt version gated suffix workaround in [webview.py](/app/qutebrowser/browser/webengine/webview.py). It expands specific and wildcard MIME types, skips suffixes already supplied, and passes the added suffixes through `chooseFiles`.

Verification: the existing webview unit tests passed (6 tests), and `git diff --check` passed.