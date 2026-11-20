# Checkpoint

Task: normalize mail metric labels and page-size strings; add `@proton/metrics` to the mail manifest and lockfile.

Changes:
- Added `applications/mail/src/app/metrics/mailMetricsHelper.ts` with `getLabelID` and `getPageSizeString`.
- Added focused tests covering all built-in mailbox IDs, custom IDs, supported sizes, and fallback behavior.
- Added `@proton/metrics` as a mail workspace dependency in `applications/mail/package.json` and `yarn.lock`.

Verification:
- `cd applications/mail && yarn jest src/app/metrics/mailMetricsHelper.test.ts --runInBand --coverage=false --forceExit`: passed (5 tests).
- `cd applications/mail && yarn check-types`: passed (exit 0).
- `cd applications/mail && yarn eslint src/app/metrics/mailMetricsHelper.ts src/app/metrics/mailMetricsHelper.test.ts --no-cache`: passed (exit 0, rerun after final changes).
- `cd applications/mail && yarn prettier --check src/app/metrics/mailMetricsHelper.ts src/app/metrics/mailMetricsHelper.test.ts`: passed (exit 0, rerun after final changes).

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); used `find` and `grep` for local inspection. No dependencies were downloaded.
- `git diff --check`: passed (exit 0).
- Local manifest/lockfile consistency check: passed (exit 0).
