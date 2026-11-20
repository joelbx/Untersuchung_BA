# Checkpoint

Task: implement `scrolling.bar=overlay` with QtWebEngine/platform/version gating, update legacy boolean migration, and support version-gated `@js_headers` tests.

Progress: added the `overlay` config value, changed `scrolling.bar=False` migration to `overlay`, added QtWebEngine/Qt 5.11+/non-macOS flag gating, made existing Chromium flag assertions order-insensitive for overlay on/off, added the `@js_headers` Qt compatibility tag to the JS header scenarios, and updated the generated settings help. Tests: config files 159 passed/1 skipped; config data 31 passed; `TestQtArgs` 62 passed; misc end-to-end scenarios collected (74); the `@js_headers` version matrix passed. The complete `test_configinit.py` process exits near completion without pytest's summary in this container, but the modified `TestQtArgs` class passes. Final diff and whitespace checks are complete.

External research is not being used.
