# Checkpoint

Task: Fix QtWebEngine file picker suffix handling for accepted MIME types in `/app`.

Implementation: Added a MIME suffix workaround in `webview.py`, gated to Qt runtime versions >= 6.2.3 and < 6.7.0. Specific MIME types use `mimetypes.guess_all_extensions`; wildcard patterns use `mimetypes.types_map`. `chooseFiles` now appends sorted missing suffixes before calling the parent implementation.

Verification: `python -m pytest tests/unit/browser/webengine/test_webview.py` passed (6 tests). `git diff --check` passed.
