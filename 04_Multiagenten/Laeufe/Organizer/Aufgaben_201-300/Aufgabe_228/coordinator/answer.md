Added `utils.parse_version` using a normalized `QVersionNumber` and updated the specified Qt checks, distribution version, startup minimum check, and crash dialog comparison to use Qt-native versions. Updated the relevant tests.

**Verification:** 343 focused tests passed; `git diff --check` passed. I completed the work directly, with no delegation or adoption.