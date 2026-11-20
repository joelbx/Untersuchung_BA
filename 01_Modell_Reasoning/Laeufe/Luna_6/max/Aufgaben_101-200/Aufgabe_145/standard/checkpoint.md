# Recovery issue checkpoint

- Objective: fix photo recovery to include regular and trashed items, gate on both decryptions, track progress/failures, fail consistently on core action errors, and resume persisted in-progress work.
- Constraints: used local repository code and existing tests only; did not alter git history, index baseline, or harness configuration.
- Implementation: synchronized the duplicated Drive app and shared store recovery hooks. Recovery now starts regular and trash enumeration together when trash inclusion is explicitly enabled, waits for both caches to finish decrypting, merges regular links with image/video trash links by source share, and checks the remaining source contents before reporting success. Per-item move errors remain counted as unrecovered; loading, moving, and delete-share errors persist FAILED. Persisted `progress` still starts recovery on initialization.
- Verification: both focused test files pass (11 tests each); ESLint and Prettier pass. Full type checks are blocked by an existing OpenPGP type mismatch in `packages/crypto/lib/worker/api.ts:579`.
