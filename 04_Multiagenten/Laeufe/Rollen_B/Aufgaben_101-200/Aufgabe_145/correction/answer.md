Updated both copies of `usePhotosRecovery` to count the union of failed move IDs and photos still present during cleanup. The unrecovered count now reflects photos remaining in the regular or trashed source. Updated the tests for distinct failed and remaining items.

Both recovery suites pass (11/11 each), and `git diff --check` passes.

**TEST_ENVIRONMENT_PROBLEM:** The drive-store type check still fails in `packages/crypto/lib/worker/api.ts:579` because the installed `openpgp` and `pmcrypto` OpenPGP types conflict.