# Checkpoint

Task: Remove stale mail bypass filter entries after optimistic mark-as updates.
Status: Complete.
Changes: Dispatch markAsStatus; type it in OptimisticUpdates; use getElementsToBypassFilter to add or remove bypass IDs according to Unread filter and mark-as status; add helper and reducer regression tests.
Verification: Relevant Jest suites passed (13 tests total), mail TypeScript check passed, targeted ESLint and Prettier checks passed, git diff --check passed.
Constraints observed: Local repository only; git history, index baseline, and harness configuration unchanged.
