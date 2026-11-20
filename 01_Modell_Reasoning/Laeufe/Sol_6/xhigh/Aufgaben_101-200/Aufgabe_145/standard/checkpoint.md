# Photos recovery checkpoint

- Located recovery implementations and tests in `applications/drive/src/app/store/_photos` and `packages/drive-store/store/_photos`.
- Updated both synchronized hooks to load and wait for regular and trashed listings, merge photo trash into recovery targets, account for move failures, and verify that no targets remain before deleting shares.
- Added matching regression tests in both copies. Focused tests and lint passed; the app type check is blocked by an existing `packages/crypto/lib/worker/api.ts` OpenPGP type mismatch.
