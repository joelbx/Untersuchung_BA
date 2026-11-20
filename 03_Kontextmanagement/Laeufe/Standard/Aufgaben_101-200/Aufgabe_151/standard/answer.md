Updated [webview.py](/app/qutebrowser/browser/webengine/webview.py) so the file picker adds missing MIME suffixes on affected Qt versions, including JPG extensions for image filters. Added coverage in [test_webview.py](/app/tests/unit/browser/webengine/test_webview.py).

Verification: 11 focused tests passed; `git diff --check` passed.