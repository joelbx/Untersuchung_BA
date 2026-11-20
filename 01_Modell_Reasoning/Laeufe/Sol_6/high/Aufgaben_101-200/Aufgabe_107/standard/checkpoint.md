Task: Fix stale mail bypass-filter entries when mark-as status matches the active read/unread filter.
Status: Complete. The mark-as dispatch includes status; the reducer uses a helper to add or remove the appropriate message or conversation IDs.
Verification: Jest passed for elementsReducers.test.ts and elementTotal.test.ts (8 tests); TypeScript check passed; Prettier check passed; git diff --check passed.
Constraints: Used local code and tests only; did not change git history, index baseline, or harness configuration.
