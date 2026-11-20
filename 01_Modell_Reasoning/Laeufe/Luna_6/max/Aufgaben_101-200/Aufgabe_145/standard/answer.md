Implemented recovery across both synchronized copies: [Drive recovery hook](/app/applications/drive/src/app/store/_photos/usePhotosRecovery.ts) and [shared store hook](/app/packages/drive-store/store/_photos/usePhotosRecovery.ts).

Recovery now enumerates regular and trashed sources together, waits for both to finish decrypting, and merges regular links with trashed image and video links by source share. Failed moves remain counted as unrecovered, core action errors persist `FAILED`, and recovery reports `SUCCEED` only when no targeted items remain. Persisted in-progress recovery still resumes on initialization.

Both focused test suites pass: **11 tests each**. ESLint and Prettier pass. Full type checks stop at an unrelated OpenPGP type mismatch in `packages/crypto/lib/worker/api.ts:579`.