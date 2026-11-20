Added `utils.parse_version` using normalized `QVersionNumber` values and updated the requested Qt, WebKit, distribution, and crash dialog comparisons. The Qt runtime checks now use `QLibraryInfo.version()`.

The affected tests passed: **421 passed, 4 skipped**. One QtWebEngine runtime test was deselected because it exits the test process in this environment.