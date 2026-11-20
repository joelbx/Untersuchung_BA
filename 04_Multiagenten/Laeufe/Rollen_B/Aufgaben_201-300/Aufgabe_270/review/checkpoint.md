VERDICT: FIX
CODE_DEFECT: packages/drive-store/store/_api/usePublicSession.tsx removes isSessionProtonUser from the provider return (lines 169-176), but packages/drive-store/store/_shares/usePublicShare.ts:15-17 and store/_downloads/index.tsx:55-56 still call it. @proton/drive-store type check reports TS2339 at both call sites. Restore the method or update both consumers consistently.
TEST_ENVIRONMENT_PROBLEM: Both package type checks also fail at packages/crypto/lib/worker/api.ts:579 due to incompatible openpgp and pmcrypto nested openpgp types. This is separate from the patch defect.
TESTS: yarn workspace proton-drive test:ci --runTestsByPath src/app/utils/lastActivePersistedUserSession.test.ts src/app/store/_user/useActivePing.test.ts: PASS, 2 suites/12 tests. yarn workspace @proton/drive-store test:ci --runTestsByPath utils/lastActivePersistedUserSession.test.ts store/_user/useActivePing.test.ts: PASS, 2 suites/12 tests.
TYPE CHECKS: yarn workspace @proton/drive-store check-types: FAIL (TS2339 x2 plus crypto TS2345). yarn workspace proton-drive check-types: FAIL (crypto TS2345).
No project code changed during review.
