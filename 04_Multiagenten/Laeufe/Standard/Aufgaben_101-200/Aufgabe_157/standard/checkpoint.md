# Checkpoint

Task: Add Mail metrics normalization helpers and declare `@proton/metrics` in the Mail package and lockfile.

Status: Complete. Added `getLabelID` and `getPageSizeString` in `applications/mail/src/app/metrics/mailMetricsHelper.ts`, focused tests, and the Mail workspace dependency in `package.json` and `yarn.lock`.

Verification: Mail helper and existing label Jest suites passed (44 tests); Mail TypeScript check passed; focused ESLint and Prettier checks passed.
