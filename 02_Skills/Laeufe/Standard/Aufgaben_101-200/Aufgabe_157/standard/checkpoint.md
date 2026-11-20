# Checkpoint

Issue: standardize mail metrics label IDs and page sizes, and add `@proton/metrics` to the mail dependency manifest and lockfile.

Status: inspecting local repository. `rg` is unavailable; using `find` and `grep`.

Implemented: added `@proton/metrics` to the mail manifest and its workspace lockfile entry. Added `mailMetricsHelper.ts` and focused tests for system/custom labels and page size values/defaults.

Checks: `./node_modules/.bin/jest --config applications/mail/jest.config.js --runInBand --coverage=false applications/mail/src/app/metrics/mailMetricsHelper.test.ts` passed (5 tests). `git diff --check` passed. App type check and existing label tests are running.

Existing check: `./node_modules/.bin/jest --config applications/mail/jest.config.js --runInBand --coverage=false applications/mail/src/app/helpers/labels.test.ts` passed (24 tests). Prettier check passed. First `./node_modules/.bin/tsc --noEmit -p applications/mail/tsconfig.json` found TS2352 in the intentional invalid-value test fixture; fixed the cast and reran type check. Focused tests passed again (5 tests).

Final checks: `./node_modules/.bin/tsc --noEmit -p applications/mail/tsconfig.json` passed after the fixture correction. `git diff --check` passed. No dependencies downloaded.
