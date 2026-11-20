# Progress

- Located the checked-out qutebrowser repository; working tree starts clean.
- Added `content.javascript.log_message.levels` (with migration from the old
  setting) and `content.javascript.log_message.excludes`.
- Added `_js_log_to_ui` and kept the standard logger fallback for messages not
  shown in the UI. Regenerated the settings reference and added focused tests.
- Verification: 47 targeted tests passed with Qt offscreen; `git diff --check`
  passed.
