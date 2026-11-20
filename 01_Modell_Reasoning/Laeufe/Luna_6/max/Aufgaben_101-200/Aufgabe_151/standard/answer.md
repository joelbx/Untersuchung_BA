Implemented the workaround in [webview.py](/app/qutebrowser/browser/webengine/webview.py): it checks the Qt version, expands wildcard and specific MIME types, and passes the extra suffixes to the parent file picker without adding duplicates.

The focused WebEngine view tests passed: **6 passed**. `git diff --check` also passed.

One detail: this environment’s Python MIME database returns additional aliases for the examples, including `.jpeg`, `.jfif`, and `.mp4`; the helper includes all suffixes returned by `mimetypes.guess_all_extensions()`.