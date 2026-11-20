# Checkpoint

Task: Align version parsing and comparison with Qt-native `QVersionNumber` in the requested qutebrowser modules.

Completed:
- Added `utils.parse_version`, using `QVersionNumber.fromString()` and returning a normalized Qt version number.
- Updated Qt runtime checks to use `QLibraryInfo.version()` and shared parsing for compiled Qt/PyQt strings; retained equality/greater-or-equal behavior and the conflicting-flags `ValueError`.
- Updated early initialization minimum checks and Qt version reporting to use the Qt library version API.
- Changed distribution version metadata and crash dialog comparisons to use the shared Qt-native parser.
- Updated existing unit expectations and runtime mocks for the new API.

Verification:
- Relevant utility/dialog modules: 318 passed; pytest then exited nonzero due to an X server `XIO: fatal IO error` during shutdown.
- Version module excluding its QtWebEngine `test_unpatched`: 93 passed, 4 skipped, 1 deselected; same X server shutdown error after the test summary.
- Distribution/sandbox version cases: 19 passed with exit status 0.
- `git diff --check` passed.
