# Checkpoint

Updated photo recovery to load and wait for regular and trashed links, merge trashed photo entries into the recovery set, verify both sources during cleanup, and account for pending links on failure. Added coverage for trash recovery, trash load failure, remaining trash, and move failure counts.

Checks:
- `../../node_modules/.bin/jest store/_photos/usePhotosRecovery.test.ts --runInBand --silent` from `/app/packages/drive-store`: passed (10 tests) after final formatting.
- `../../node_modules/.bin/tsc --noEmit --pretty false` from `/app/packages/drive-store`: failed in unrelated `../crypto/lib/worker/api.ts:579` with TS2345. The installed `openpgp` and `pmcrypto/node_modules/openpgp` `PartialConfig`/`enums.hash` types are incompatible. Full package type correctness remains unverified because of this existing dependency type conflict.
- `git diff --check`: passed after final formatting.
