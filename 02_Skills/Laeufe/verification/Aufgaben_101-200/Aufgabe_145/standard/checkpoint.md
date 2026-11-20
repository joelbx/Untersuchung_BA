# Photos recovery checkpoint

Implemented in both mirrored recovery hooks and tests:
- Load trash alongside regular children, waiting for both caches to finish decryption.
- Merge regular links with photo entries in the restored share's trash, count the merged targets, and verify both sources before success or share deletion.
- Track pending and failed links when move or cleanup fails; preserve persisted-progress resume behavior.

Verification completed:
- `yarn workspace @proton/drive-store test --runInBand store/_photos/usePhotosRecovery.test.ts`: 11 passed, exit 0.
- `yarn workspace proton-drive test --runInBand src/app/store/_photos/usePhotosRecovery.test.ts`: 11 passed, exit 0.
- `yarn prettier --check packages/drive-store/store/_photos/usePhotosRecovery.ts packages/drive-store/store/_photos/usePhotosRecovery.test.ts applications/drive/src/app/store/_photos/usePhotosRecovery.ts applications/drive/src/app/store/_photos/usePhotosRecovery.test.ts`: exit 0.
- `yarn workspace @proton/drive-store exec eslint store/_photos/usePhotosRecovery.ts store/_photos/usePhotosRecovery.test.ts --quiet`: exit 0.
- `yarn workspace proton-drive exec eslint src/app/store/_photos/usePhotosRecovery.ts src/app/store/_photos/usePhotosRecovery.test.ts --quiet`: exit 0.
- `git diff --check`: exit 0.

Blocked check:
- `yarn workspace @proton/drive-store check-types`: exit 2 with TS2345 at `../crypto/lib/worker/api.ts(579,77)` because `openpgp` and `pmcrypto/node_modules/openpgp` define incompatible `PartialConfig.preferredHashAlgorithm` types. No type-check success is claimed; this error is outside the edited files.

Local tool note: `rg` is unavailable (`/bin/bash: rg: command not found`); used `find` and `grep` for repository search.
