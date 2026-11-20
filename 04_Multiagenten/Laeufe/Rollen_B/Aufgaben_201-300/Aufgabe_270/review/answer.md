VERDICT: FIX

**Code defect:** [usePublicSession.tsx](/app/packages/drive-store/store/_api/usePublicSession.tsx:169) no longer returns `isSessionProtonUser`, but [usePublicShare.ts](/app/packages/drive-store/store/_shares/usePublicShare.ts:15) and [index.tsx](/app/packages/drive-store/store/_downloads/index.tsx:55) still call it. The shared Drive type check reports TS2339 at both sites. Restore the method or update both consumers.

**Tests run:**

- `yarn workspace proton-drive test:ci --runTestsByPath src/app/utils/lastActivePersistedUserSession.test.ts src/app/store/_user/useActivePing.test.ts` — passed, 12 tests.
- `yarn workspace @proton/drive-store test:ci --runTestsByPath utils/lastActivePersistedUserSession.test.ts store/_user/useActivePing.test.ts` — passed, 12 tests.
- `yarn workspace @proton/drive-store check-types` — failed: the two TS2339 errors above, plus TS2345.
- `yarn workspace proton-drive check-types` — failed: TS2345.

**TEST_ENVIRONMENT_PROBLEM:** The TS2345 error in [api.ts](/app/packages/crypto/lib/worker/api.ts:579) concerns incompatible `openpgp` types from the root and `pmcrypto` dependency trees. Resolve that dependency type mismatch separately from the provider regression.

I recorded the review in [checkpoint.md](/app/.codex-role-output/checkpoint.md). No project code was changed during review.