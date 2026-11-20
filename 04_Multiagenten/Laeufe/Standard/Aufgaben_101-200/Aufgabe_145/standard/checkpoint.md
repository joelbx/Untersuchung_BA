# Recovery issue checkpoint

- Implemented recovery of regular and trashed photo links in `usePhotosRecovery` with a two-source decryption gate.
- Recovery now counts both sources, accounts for rejected and failed moves, checks both sources before deleting restored shares, resets counts on retry, and resumes from persisted `progress` state.
- Added tests for mixed sources, decryption readiness, remaining trashed photos, rejected moves, and trash loading errors. Existing resume and deletion failure tests pass.
- Verification: 12 recovery tests pass; Prettier and `git diff --check` pass. Package type checking reports one pre-existing OpenPGP type conflict in `packages/crypto/lib/worker/api.ts` and no recovery file errors.
