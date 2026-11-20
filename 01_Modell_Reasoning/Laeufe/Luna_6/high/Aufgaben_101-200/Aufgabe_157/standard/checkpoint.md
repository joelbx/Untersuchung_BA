# Checkpoint

Task: standardize mail metrics helper functions in `/app`.

Completed:
- Added `@proton/metrics` as a mail application dependency and updated only the mail workspace entry in `yarn.lock`.
- Added `applications/mail/src/app/metrics/mailMetricsHelper.ts` with `getLabelID` and `getPageSizeString`.
- Validation passed: `yarn workspace proton-mail check-types --pretty false`; `yarn workspace proton-mail test --runInBand src/app/helpers/labels.test.ts`; `git diff --check`.
