VERDICT: FIX

**Code review:** I found no defect in the applied admin action lock in [UserInfo.tsx](/app/src/components/views/right_panel/UserInfo.tsx). It shares the pending state across Kick, Ban, and Mute, blocks repeat activation before the disabled state renders, and releases the lock after cancellation or failure. I made no project code changes.

**Checks:** `./node_modules/.bin/jest --runInBand test/components/views/right_panel/UserInfo-test.tsx` passed (70 tests, 6 snapshots). ESLint and Prettier passed for both changed files.

**TEST_ENVIRONMENT_PROBLEM:** `./node_modules/.bin/tsc --noEmit --jsx react` failed with missing dependency declarations and SDK API mismatches outside the changed files. Align the installed dependencies with the repository lockfile, then rerun the TypeScript check. The failed check requires a FIX verdict.