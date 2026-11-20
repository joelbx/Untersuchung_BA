# Photos recovery checkpoint

- Completed mirrored changes in `packages/drive-store/store/_photos` and `applications/drive/src/app/store/_photos`.
- Recovery loads regular children and trash, waits for both to decrypt, moves regular links plus photo entries from each restored share's trash, checks both caches before deleting, tracks pending and failed moves, and resumes persisted progress.
- Both focused Jest suites passed: 13 tests each.
- ESLint, Prettier, and `git diff --check` passed. Both TypeScript workspace checks report only the existing OpenPGP type mismatch in `packages/crypto/lib/worker/api.ts:579`.
