Moved `extra_suffixes_workaround` to module scope, with the Qt version gate before MIME processing and wildcard expansion through `mimetypes.types_map`. `chooseFiles` now merges and deduplicates suffixes before its superclass fallback call, without using instance state. Updated the tests for the module-level API and `None` as `self`.

Validation: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_webview.py` — **20 passed**.

Changed: [webview.py](/app/qutebrowser/browser/webengine/webview.py:22), [test_webview.py](/app/tests/unit/browser/webengine/test_webview.py:113).