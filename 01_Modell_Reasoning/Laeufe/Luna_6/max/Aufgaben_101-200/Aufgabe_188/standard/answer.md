Centralized storage units in [size.ts](/app/packages/shared/lib/helpers/size.ts), with `BASE_SIZE`, `sizeUnits`, and `SizeUnits`. Updated `humanSize`, member allocation and editing, CSV imports, organization setup, bonus storage, and other storage limits to use the shared definitions. Removed `GIGA` and inline gigabyte calculations.

**Verification**

- CSV Jest suite passed: 64 tests and 5 snapshots.
- Targeted ESLint and `git diff --check` passed.
- Shared Karma bundle compiled, but browser tests could not launch because Playwright’s Chromium binary is missing.
- Both package type checks hit an existing `openpgp` type mismatch in `packages/crypto/lib/worker/api.ts`; no errors were reported in changed files.