# Checkpoint

Task: Resolve the photo recovery flow issue in `/app`.

Initial state: Working tree was clean. No `AGENTS.md` files were found in the repository. `rg` is unavailable, so repository searches use `find` and `grep`.

Plan: Locate recovery implementation and existing tests; inspect relevant behavior; edit the flow to include regular and trashed photo items, gate on both decryptions, preserve accurate state/counts, and resume in-progress recovery; run relevant existing tests.

Progress: Located the recovery hook in both the Drive app and its `drive-store` duplicate. Recovery now enumerates trashed links alongside regular links, waits for both caches to finish decrypting, filters trash to photo metadata, includes both sources in progress counts, verifies the caches before success/share deletion, and marks operation errors as failed. Existing test mocks were updated for the trash listing API. Relevant Jest suites are next.

Verification: Both existing recovery hook suites pass (7/7 each) in `drive-store` and the Drive app. ESLint passes for the changed `drive-store` recovery files. Workspace type checks stop on an existing unrelated OpenPGP type mismatch in `packages/crypto/lib/worker/api.ts:579`; no diagnostics point to the recovery changes. Final mirrored source and test files match, and `git diff --check` is clean.
