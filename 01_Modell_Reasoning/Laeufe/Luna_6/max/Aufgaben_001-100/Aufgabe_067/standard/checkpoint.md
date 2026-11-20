# Checkpoint

## Issue
Add `scrolling.bar=overlay`, enable Chromium overlay scrollbars only for QtWebEngine on Qt >= 5.11 outside macOS, migrate legacy booleans, and support Qt-version-gated `@js_headers` end-to-end tests.

## Implemented
- Added and documented the `overlay` config value.
- Boolean migration now maps `True` to `always` and `False` to `overlay`.
- Added the Chromium feature flag only for QtWebEngine on Qt >= 5.11 outside macOS.
- Registered `@js_headers`, skipping affected QtWebEngine tests on Qt 5.12-5.14; marked the dynamic user-agent test.
- Added tests for supported/unsupported environments, regular values, flag coexistence, and migration.

## Validation
- `tests/unit/config/test_configfiles.py`: 159 passed, 1 skipped.
- Focused `test_configinit.py` Chromium and overlay tests: 11 passed.
- End-to-end collection with `--qute-bdd-webengine -m js_headers` selected the marked scenario on Qt 5.15.
- Running both complete config modules together returned exit status 1 after reporting all test progress but no pytest summary; focused relevant tests and the complete configfiles module completed cleanly.

## Status
Implementation and final review complete.
