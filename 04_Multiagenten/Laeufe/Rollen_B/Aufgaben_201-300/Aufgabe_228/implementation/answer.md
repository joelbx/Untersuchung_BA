Implemented Qt-native version handling across the affected modules. `utils.parse_version` now returns a normalized `QVersionNumber`; runtime checks use `QLibraryInfo.version()`, and distribution and crash dialog comparisons use the shared parser. Updated the relevant tests.

Verification: 422 passed, 4 skipped, and 1 unrelated QtWebEngine initialization test deselected. `git diff --check` passed.