# Checkpoint

Task: Add `scrolling.bar=overlay`, gate the QtWebEngine Chromium feature flag by Qt/platform, update boolean migration behavior, and support the `js_headers` test marker.

Implemented: added the `overlay` accepted config value; `False` migration now maps to `overlay` (`True` remains `always`); QtWebEngine emits `--enable-features=OverlayScrollbar` only for overlay on Qt >= 5.11 outside macOS; end-to-end `js_headers` marker skips Qt < 5.11; added gate and migration tests and adjusted Chromium/GPU assertions to tolerate independent flags.

Verification: `git diff --check` passes. Focused existing tests report 19 passed. This environment's pytest/X11 teardown emits `XIO: fatal IO error` and exits with status 1 after the passing summary; larger relevant config suite likewise completes test progress without reported assertion failures but exits abnormally. `QT_QPA_PLATFORM=offscreen` was used because the initial run without it aborted creating QApplication.
