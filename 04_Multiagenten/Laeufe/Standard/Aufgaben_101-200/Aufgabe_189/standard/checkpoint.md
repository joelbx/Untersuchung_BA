# Checkpoint

Task: Move MIME suffix workaround to module scope in webview.py; update chooseFiles and run relevant existing tests.

Status: Complete. Module-level helper added; chooseFiles deduplicates merged suffixes; tests updated.
Validation: QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_webview.py (24 passed); git diff --check passed.
