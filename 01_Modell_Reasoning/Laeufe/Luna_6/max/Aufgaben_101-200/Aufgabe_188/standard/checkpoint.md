# Checkpoint

Task: centralize storage unit definitions and usages under `@proton/shared/lib/helpers/size`.

Completed:
- Added `packages/shared/lib/helpers/size.ts` as the canonical source for `BASE_SIZE`, `sizeUnits`, and `SizeUnits`.
- Moved `humanSize` to use the shared unit object; updated member provisioning/editing, CSV import, organization setup, bonus storage, offer/referral copy, Drive limits, preview limits, and logo upload calculations.
- Migrated calendar, contacts, and CSV file-size limits to import `BASE_SIZE` from the helper.
- Replaced remaining GIGA and inline gigabyte arithmetic in source and existing tests.

Verification:
- Components CSV Jest suite passed: 64 tests, 5 snapshots.
- Shared Karma bundle compiled; browser tests could not launch because the configured Playwright Chromium binary is missing.
- Targeted ESLint passed for changed component and shared files.
- Shared and components type checks were blocked by the existing `packages/crypto/lib/worker/api.ts` `openpgp` type mismatch; no changed-file errors were reported.
- `git diff --check` passed; no remaining `GIGA` or inline 1024^3 calculations in source.
