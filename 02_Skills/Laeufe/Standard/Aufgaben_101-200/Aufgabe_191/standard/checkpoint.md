# Checkpoint

- Task: support stable and unstable registration token stages in InteractiveAuth.
- Initial repository state: clean. `rg` is unavailable; using `grep`/`find` for local inspection.
- Implemented `RegistrationTokenAuthEntry`, mapped both SDK token identifiers, and added English strings and focused tests.
- Passed: `node_modules/.bin/jest --runInBand test/components/structures/InteractiveAuth-test.tsx test/components/views/dialogs/InteractiveAuthDialog-test.tsx` (2 suites, 4 tests); ESLint and Prettier on changed files; `git diff --check`.
- Repository-wide TypeScript check: `node_modules/.bin/tsc --noEmit --jsx react --pretty false` exits 2 with 50 existing Sliding Sync diagnostics. First error: `src/SlidingSyncManager.ts(139,13): error TS2345: Argument of type 'Map<any, any>' is not assignable to parameter of type 'MSC3575List[]'.` No diagnostic refers to either changed TypeScript file. Full type-check success remains unverified due to these unrelated errors.
- Passed: `node_modules/.bin/jest --runInBand test/components/structures/auth/Registration-test.tsx` (1 suite, 4 tests). The suite logs mocked discovery warnings but exits 0.
