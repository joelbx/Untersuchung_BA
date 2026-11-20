Implemented the JPG file picker workaround in [webview.py](/app/qutebrowser/browser/webengine/webview.py). For affected Qt versions, it adds missing extensions from accepted MIME types before opening Qt’s picker.

The focused webview tests passed: **11 passed**. `git diff --check` passed.