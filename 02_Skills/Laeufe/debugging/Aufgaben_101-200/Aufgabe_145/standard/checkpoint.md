# Recovery issue checkpoint

Investigating recovery flow and tests. `rg` is unavailable; using local `find`/`grep` equivalents. No changes to application code yet.

Root cause: both duplicated recovery hooks enumerate only root children. Trash listing exists separately by volume and is never loaded or checked. Cleanup checks only regular children. The move helper reports per-link errors via callbacks and can also reject; a rejection currently leaves pending counts unchanged. Resume state is already read on mount but will need verification with the combined flow.

Final implementation: recovery explicitly loads regular children and trash once per volume, waits for both decryption states, merges regular links with photo files from the corresponding restored share's trash, and checks both caches before success. Move errors update remaining/failed counts; residual photos block success. Empty shares are deleted; shares with only unrelated trashed files are left intact. Persisted `progress` resumes through the combined flow.

Checks: focused Jest suites for package and app passed; targeted ESLint and `git diff --check` passed. Full type check command `./node_modules/.bin/tsc --noEmit -p packages/drive-store/tsconfig.json` failed with exit code 2 at `packages/crypto/lib/worker/api.ts(579,77)`: `openpgp` and `pmcrypto/node_modules/openpgp` define incompatible `PartialConfig` types (`preferredHashAlgorithm`, `hash.md5`). This is outside the edited files, so full type correctness remains unverified by that command.
