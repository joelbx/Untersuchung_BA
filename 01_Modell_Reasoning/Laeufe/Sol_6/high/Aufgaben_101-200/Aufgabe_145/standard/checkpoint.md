# Recovery issue checkpoint

- Updated both synchronized recovery hooks to load regular and trashed links, wait for both decryption sources, merge regular links with photo entries from the matching share's trash, and require empty sources before success.
- Pending work becomes failed on core errors; individual move callbacks update progress. Persisted `progress` state still resumes automatically.
- Updated mirrored recovery tests for mixed sources, decryption readiness, residual photos, load and move failures, and resume.
- Both focused recovery suites pass: 11 tests each. Prettier and `git diff --check` pass.
- Both workspace type checks stop on an existing OpenPGP type mismatch in `packages/crypto/lib/worker/api.ts:579`, outside the edited files.
- Final lint check is running.
- Targeted ESLint check passed for all four edited files.
