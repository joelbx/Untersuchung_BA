Implemented the current-session kebab menu with accessible trigger state, localized sign-out actions, bulk sign-out of other sessions, and destructive styling. Updated the affected snapshots.

Verification: both focused test suites pass (43 tests), ESLint passes, and `git diff --check` passes. The full type check remains blocked by existing Matrix SDK type errors elsewhere in the repository.