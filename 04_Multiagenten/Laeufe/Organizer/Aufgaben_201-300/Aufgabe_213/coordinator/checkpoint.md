Task: Resolve locked or soft-deleted share navigation in Drive.
Status: Complete.
Changes: useDefaultShare exposes isShareAvailable(signal, shareId), forwarding to getShare and checking lock/soft-delete flags. FolderContainer checks availability before setting an explicit folder and redirects unavailable shares to root. Hook tests cover normal, locked, and soft-deleted metadata while retaining default-share creation assertions.
Verification: Drive-scoped Jest useDefaultShare.test.tsx passed (6 tests). Drive TypeScript check passed. ESLint on changed files and git diff --check passed.
Delegation: None.
