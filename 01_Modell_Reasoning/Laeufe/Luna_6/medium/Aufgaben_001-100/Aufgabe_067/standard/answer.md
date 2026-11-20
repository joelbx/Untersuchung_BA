Implemented `scrolling.bar=overlay` with the QtWebEngine, Qt 5.11+, non macOS gate. Updated boolean migration so `False` becomes `overlay`, and added the `@js_headers` Qt version skip.

The focused overlay, Chromium flag, GPU, and migration tests passed: 18 tests total. The full config test run aborted while creating Qt’s `QApplication` in this environment. `git diff --check` passed.