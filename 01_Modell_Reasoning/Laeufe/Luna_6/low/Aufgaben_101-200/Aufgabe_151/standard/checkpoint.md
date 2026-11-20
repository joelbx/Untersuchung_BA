# Checkpoint

Task: Fix Qt WebEngine file picker suffix handling for Qt >= 6.2.3 and < 6.7.0.

Implemented `extra_suffixes_workaround` in `qutebrowser/browser/webengine/webview.py`. It uses Python `mimetypes` mappings for specific and wildcard MIME types, excludes extensions already supplied, and is guarded by runtime Qt version checks with `compiled=False`. The default file picker now merges computed suffixes into accepted filters.

Validation in progress: running existing WebEngine `test_webview.py` tests.
