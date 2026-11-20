Added `utils.parse_version` using normalized `QVersionNumber` values and updated the Qt, distribution, and crash dialog version checks to use Qt-native comparisons. Runtime Qt checks now use `QLibraryInfo.version()`.

Updated the affected test expectations. Verification: 140 targeted tests passed, and `git diff --check` passed.