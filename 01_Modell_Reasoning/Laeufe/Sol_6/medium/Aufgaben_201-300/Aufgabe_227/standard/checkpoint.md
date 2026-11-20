# Checkpoint

- Task: gate MIME suffix workaround on runtime Qt only.
- Status: implementation and regression tests complete.
- Changes: both bounds call version_check with compiled=False; utility documents compiled and raises RuntimeError for compiled=True with exact=True.
- Verification: 13 version_check tests passed; full webview file passed (24 tests) with QT_QPA_PLATFORM=offscreen; git diff --check passed.
