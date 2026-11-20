# Pill refactor checkpoint

Completed the functional Pill refactor, public usePermalink hook, named Pill exports and caller updates. Added focused Pill tests.

Verification: 3 relevant Jest suites passed (12 tests). ESLint passed on all changed source and test files. Full TypeScript check still reports existing SDK mismatch errors in LoginWithQR, Notifications, and VectorPushRulesDefinitions; it reports no errors in changed files. git diff --check passed.
