# Checkpoint

Task complete: standardized mail metrics helpers and added `@proton/metrics` to the mail manifest and lockfile.

Implemented `getLabelID` and `getPageSizeString` in `applications/mail/src/app/metrics/mailMetricsHelper.ts`, with focused tests. The tests failed first because the helpers were missing, then passed. Added the workspace dependency to `applications/mail/package.json` and its `yarn.lock` workspace entry.

Verification:
- Focused Jest test: 7 passed.
- Full mail Jest suite (`../../node_modules/.bin/jest --runInBand --coverage=false --silent`): 161 suites passed, 1,392 tests passed, 2 skipped, 32 snapshots passed.
- TypeScript (`../../node_modules/.bin/tsc --noEmit -p tsconfig.json`): passed.
- ESLint on the new files: passed.
- Prettier check on the new files: passed.
- `git diff --check`: passed.

`rg` is unavailable, so searches used `find` and `grep`.
