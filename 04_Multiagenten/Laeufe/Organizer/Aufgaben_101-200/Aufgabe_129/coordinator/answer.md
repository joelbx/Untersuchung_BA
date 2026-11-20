Added a kebab menu to the Current session header with localized, accessible sign-out actions. It stays visible but disabled during loading, when no current device exists, or while signing out. The bulk action passes only other-session IDs. Menu interactions close it and return focus to the trigger.

The focused Jest suites pass: **56 tests and 9 snapshots**. ESLint, Stylelint, and `git diff --check` pass. The repository-wide TypeScript check still reports existing errors in unrelated SDK integration files; it reports none in the changed files.

No delegation was used.