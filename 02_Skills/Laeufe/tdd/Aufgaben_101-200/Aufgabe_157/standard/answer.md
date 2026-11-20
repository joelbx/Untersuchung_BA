Added [mailMetricsHelper.ts](/app/applications/mail/src/app/metrics/mailMetricsHelper.ts) with `getLabelID` and `getPageSizeString`, and added `@proton/metrics` to the [mail manifest](/app/applications/mail/package.json) and [lockfile](/app/yarn.lock).

Verification passed: the full mail suite (161 suites, 1,392 tests passed, 2 skipped), TypeScript, ESLint, Prettier, and `git diff --check`.