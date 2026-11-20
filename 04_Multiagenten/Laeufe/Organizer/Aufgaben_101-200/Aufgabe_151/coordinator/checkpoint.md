# Checkpoint

Issue: JPG files are missing from QtWebEngine file pickers when image MIME types are accepted.

Plan: inspect `webview.py` and existing tests, implement a runtime Qt version gated suffix workaround using Python `mimetypes`, integrate it into `chooseFiles`, then run relevant local tests.

Status: implemented the runtime Qt 6.2.3–6.6.x gate, MIME and wildcard suffix resolution, and `chooseFiles` integration. Added unit coverage for version boundaries and suffix handling. `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_webview.py` passed (12 tests); `git diff --check` passed. No delegation used.
