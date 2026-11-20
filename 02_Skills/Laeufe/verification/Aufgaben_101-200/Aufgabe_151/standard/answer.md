Updated [webview.py](/app/qutebrowser/browser/webengine/webview.py) so Qt 6.2.3 through 6.6.x file pickers receive missing extensions for accepted MIME types, including JPG. Existing extensions are not added twice.

Verification: the focused WebEngine tests passed (12/12), including a check against the local JPEG MIME mapping. `git diff --check` and Python compilation also passed.