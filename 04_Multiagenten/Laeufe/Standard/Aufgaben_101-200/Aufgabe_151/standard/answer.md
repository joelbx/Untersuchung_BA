Updated [webview.py](/app/qutebrowser/browser/webengine/webview.py) so Qt 6.2.3 through 6.6.x adds missing file extensions for accepted MIME types, including `image/*`, before opening the file picker. Existing extensions are excluded from the additions.

Added coverage in [test_webview.py](/app/tests/unit/browser/webengine/test_webview.py). The relevant test file passes: **11 tests**.