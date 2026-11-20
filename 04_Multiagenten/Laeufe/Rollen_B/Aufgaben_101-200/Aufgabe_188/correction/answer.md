The checked-out storage constants patch is consistent with the requested `sizeUnits` definitions. I found no code defect and made no project code changes in this correction round.

The reviewer’s component command passed again: 68 tests and 5 snapshots. `git diff --check` also passed.

**TEST_ENVIRONMENT_PROBLEM:** The shared `humanSize` test could not start because the prepared Playwright Chromium binary is missing. The shared type check still fails at [api.ts](/app/packages/crypto/lib/worker/api.ts:579) because the installed root and `pmcrypto` copies of `openpgp` have incompatible types. I left those dependencies unchanged under the no-download constraint.