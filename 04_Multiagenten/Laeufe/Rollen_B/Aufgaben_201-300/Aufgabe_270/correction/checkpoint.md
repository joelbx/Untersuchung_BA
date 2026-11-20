Correction round complete: restored `isSessionProtonUser` to the shared Drive public session provider, preserving the existing consumer contract in `usePublicShare` and `PublicDownloadsProvider`.

Verification: both reviewer-listed test commands passed (12 tests each); `git diff --check` passed. Both reviewer-listed type checks now fail solely at `packages/crypto/lib/worker/api.ts:579` with TS2345 from incompatible root and pmcrypto `openpgp` dependency types. TEST_ENVIRONMENT_PROBLEM: prepared dependency mismatch, separate from this correction. No downloads or dependency changes made.
