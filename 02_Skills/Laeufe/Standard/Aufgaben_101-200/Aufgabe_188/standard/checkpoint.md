# Checkpoint

Task: centralize storage size units in `packages/shared/lib/helpers/size.ts`.

Implemented: `BASE_SIZE`, `sizeUnits`, and `SizeUnits` are defined in the new size helper. Removed duplicate `BASE_SIZE` and `GIGA` from shared constants. Updated humanSize, member provisioning/editing, CSV import, organization setup, bonus storage, calendar/contacts import limits, offer/referral displays, shared Drive/preview limits, and Drive file-size consumers. Drive plans now initialize with `sizeUnits.TB`.

Checks:
- `yarn workspace @proton/components test --runInBand --watch=false containers/members/multipleUserCreation/csv.test.ts`: passed (64 tests).
- `yarn prettier --check` for all modified source files: passed after formatting.
- `yarn workspace @proton/components eslint` for modified component files and `yarn workspace @proton/shared eslint` for modified shared files: passed.
- `git diff --check`: passed.
- `yarn workspace @proton/components check-types`: failed at `../crypto/lib/worker/api.ts(579,77)` with TS2345; installed `openpgp` and `pmcrypto/node_modules/openpgp` define incompatible `PartialConfig`/`enums.hash` types (`hash.md5` not assignable). No errors in changed files were reported before this failure, but a full type-check pass is unverified.
- `yarn workspace @proton/shared check-types`: failed with the same TS2345 error at `../crypto/lib/worker/api.ts(579,77)`; full type-check pass remains unverified.

Tool note: `rg` is unavailable (`/bin/bash: rg: command not found`); used `git grep`.
