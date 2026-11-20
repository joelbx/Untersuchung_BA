Implemented the Qt version gated suffix workaround in [webview.py](/app/qutebrowser/browser/webengine/webview.py). `chooseFiles` now adds missing extensions to the accepted types passed to Qt.

Added focused tests in [test_webview.py](/app/tests/unit/browser/webengine/test_webview.py). The relevant test file passed: **9 tests**. `git diff --check` also passed.