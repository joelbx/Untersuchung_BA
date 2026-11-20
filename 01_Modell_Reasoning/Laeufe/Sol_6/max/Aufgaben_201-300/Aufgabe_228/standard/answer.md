Added [utils.parse_version](/app/qutebrowser/utils/utils.py:93) to return a normalized `QVersionNumber`. The Qt checks now use `QLibraryInfo.version()` and Qt-native comparisons; distribution versions and the crash dialog’s update note use the shared parser.

Verification: **425 passed, 4 skipped** in the relevant test files. `git diff --check` passed.