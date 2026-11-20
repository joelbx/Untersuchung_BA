# Checkpoint

Task: standardize mail metrics helper functions and add `@proton/metrics` to the mail app manifest and lockfile.

Implementation complete:
- Added `applications/mail/src/app/metrics/mailMetricsHelper.ts` with `getLabelID` (built-in IDs preserved, custom IDs normalized) and `getPageSizeString` (recognized page sizes mapped to standard strings; missing or invalid values default to `50`).
- Declared `@proton/metrics: workspace:^` in `applications/mail/package.json` and updated the matching `proton-mail` dependency entry in `yarn.lock`.

Verification:
- `yarn workspace proton-mail check-types` — passed.
- Existing `labels.test.ts` and `paging.test.ts` — passed (2 suites, 37 tests).
- `git diff --check` — passed.
