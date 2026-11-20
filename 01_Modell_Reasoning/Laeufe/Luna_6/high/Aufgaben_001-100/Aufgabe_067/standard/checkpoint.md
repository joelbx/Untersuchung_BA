# Checkpoint

Implemented `scrolling.bar=overlay` in the config schema and help, gated the QtWebEngine Chromium flag to Qt >= 5.11 on non-macOS, mapped migrated `False` values to `overlay`, and added the `js_headers` skip marker handling for QtWebEngine versions below 5.11. Added coverage for supported and fallback flag cases (including QtWebKit), coexistence with other Chromium flags, and the boolean migration.

Validation:
- Config and migration suite: 293 passed, 1 skipped.
- Config schema tests: 31 passed.
- Final focused regression tests after the final test update: 17 passed.
- `git diff --check` passed.

Qt tests require `QT_QPA_PLATFORM=offscreen QTWEBENGINE_DISABLE_SANDBOX=1` in this environment; running without the offscreen setting aborts during Qt application startup.
