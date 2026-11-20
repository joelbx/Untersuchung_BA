VERDICT: FIX

**Code defect:** [getLastPersistedLocalID](/app/applications/drive/src/app/utils/lastActivePersistedUserSession.ts:37) accepts `{}` or `[]` under a numeric session key and returns that ID. For example, `ps-2` containing `{}` yields `2` instead of `null`, causing the [bookmark hook](/app/applications/drive/src/app/store/_views/useBookmarksPublicView.ts:41) to attempt resuming an unusable session. Validate the required persisted session fields before selecting an ID, and update the minimal fixtures in the existing tests.

**Tests:** `../../node_modules/.bin/jest --config jest.config.js --runInBand --coverage=false src/app/utils/lastActivePersistedUserSession.test.ts src/app/store/_views/useBookmarksPublicView.test.ts` — 2 suites passed, 18 tests passed.

**TEST_ENVIRONMENT_PROBLEM:** None. No project code or tests were changed during this review.