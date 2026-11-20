# Mail metrics helper checkpoint

Task completed: `@proton/metrics` added to the mail application dependencies and its yarn lockfile workspace entry. Added `applications/mail/src/app/metrics/mailMetricsHelper.ts` with `getLabelID` and `getPageSizeString`.

Behavior: built-in mailbox IDs are preserved; custom labels and folders map to `custom`. Page size 100 and 200 map to their strings; 50, missing settings, and unexpected values map to `50`.

Verification: existing mail label and paging tests passed (37 tests); mail TypeScript check passed; ESLint and Prettier checks passed; `git diff --check` passed.
