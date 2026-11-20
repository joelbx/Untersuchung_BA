Implemented photo recovery across regular and trashed sources in both mirrored hooks. Recovery waits for both sources to finish decrypting, adds only photo entries from trash, tracks failed and unrecovered items, and succeeds only when the sources are clear. Failures are persisted, and retry resets the counts.

Both existing recovery suites pass: **7/7 tests** in each workspace. ESLint and `git diff --check` pass. Workspace type checks stop on an unrelated OpenPGP type mismatch in [api.ts](/app/packages/crypto/lib/worker/api.ts:579).

Changes are in [the Drive recovery hook](/app/applications/drive/src/app/store/_photos/usePhotosRecovery.ts:95) and its [drive-store copy](/app/packages/drive-store/store/_photos/usePhotosRecovery.ts:95), with corresponding test fixture updates.