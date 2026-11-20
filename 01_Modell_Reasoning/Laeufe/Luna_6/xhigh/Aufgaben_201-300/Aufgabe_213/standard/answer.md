Implemented share availability checking in [useDefaultShare.ts](/app/applications/drive/src/app/store/_shares/useDefaultShare.ts). Folder routes now return to the root when a share is locked or soft deleted, while default share loading and creation remain unchanged.

The targeted test suite passed: **3 tests**. `git diff --check` passed.