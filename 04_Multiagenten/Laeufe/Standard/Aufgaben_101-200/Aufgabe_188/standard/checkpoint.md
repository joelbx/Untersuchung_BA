Task: centralize storage size constants in packages/shared/lib/helpers/size.ts and update affected consumers.
Status: implemented and verified. CSV import Jest suite passed (64 tests, 5 snapshots); Prettier and git diff --check passed. Shared and components type checks both encounter the existing OpenPGP type mismatch in packages/crypto/lib/worker/api.ts:579. Existing worktree was clean at start.
