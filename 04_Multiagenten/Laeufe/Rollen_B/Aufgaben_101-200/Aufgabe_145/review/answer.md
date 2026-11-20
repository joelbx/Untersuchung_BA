VERDICT: FIX

**Code defect:** Cleanup combines move failures and photos still in the cache with `Math.max`. If they are different items, the failed count is too low; the unrecovered count also stays at zero despite photos remaining. Track failed link IDs and reconcile them with the remaining IDs in [usePhotosRecovery.ts](/app/packages/drive-store/store/_photos/usePhotosRecovery.ts:219) and its [application copy](/app/applications/drive/src/app/store/_photos/usePhotosRecovery.ts:219).

**Existing tests run:** Both recovery suites passed, 11/11 tests each.

- `yarn workspace proton-drive test --runInBand --coverage=false --watch=false src/app/store/_photos/usePhotosRecovery.test.ts`
- `yarn workspace @proton/drive-store test --runInBand --coverage=false --watch=false store/_photos/usePhotosRecovery.test.ts`

**TEST_ENVIRONMENT_PROBLEM:** `yarn workspace @proton/drive-store check-types` failed in [packages/crypto/lib/worker/api.ts](/app/packages/crypto/lib/worker/api.ts:579) because the installed `openpgp` and `pmcrypto` OpenPGP types conflict. Align those dependency types and rerun the check.