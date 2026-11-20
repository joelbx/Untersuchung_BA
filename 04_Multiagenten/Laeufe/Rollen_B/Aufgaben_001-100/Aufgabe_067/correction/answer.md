The checked-out patch adds `scrolling.bar=overlay`, gates its Chromium flag to QtWebEngine on non-macOS Qt ≥ 5.11, migrates legacy `False` to `overlay`, and supports the `@js_headers` marker. I also made the Chromium debug and GPU tests independent of the host Qt version.

The reviewer-selected unit tests pass: **132 passed**. `git diff --check` passes.

**TEST_ENVIRONMENT_PROBLEM:** Both reviewer-selected end-to-end header tests still fail because QtWebEngine cannot create an OpenGL context in this environment. Their behavior remains unverified on a working QtWebEngine display.