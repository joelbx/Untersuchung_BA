# Checkpoint

Task: add `scrolling.bar=overlay` with QtWebEngine/Qt/platform gating, migrate legacy `False`, and support `@js_headers` test marking.

Status: implementation complete. Added the overlay config value, gated its Chromium flag by backend/runtime Qt/platform, updated boolean migration, and added dynamic-header marker handling.

Verification: 320 config tests passed, 1 skipped, 1 deselected (`test_new_chromium` exits in this headless environment); 10 marker tests passed; strict BDD collection selected both `@js_headers` scenarios; `git diff --check` passed.
