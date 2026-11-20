Updated photo recovery in both [Drive](/app/applications/drive/src/app/store/_photos/usePhotosRecovery.ts) and [drive-store](/app/packages/drive-store/store/_photos/usePhotosRecovery.ts). It now loads regular and trashed items, waits for both to decrypt, recovers photo entries from trash, tracks move failures, and marks recovery successful only after targeted items are processed and no photos remain. Persisted in-progress recovery resumes automatically.

Both focused test suites pass (11 tests each), and ESLint passes. The package type check is blocked by an unrelated `openpgp`/`pmcrypto` type mismatch in `packages/crypto/lib/worker/api.ts`.

No delegation was used.