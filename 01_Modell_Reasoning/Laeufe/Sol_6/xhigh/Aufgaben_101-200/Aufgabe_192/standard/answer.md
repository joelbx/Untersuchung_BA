Added `checkEventValidity` with distinct results for invalid dates, pre-1970 starts, and start times at or after the end time. Manual creation and ICS parsing now use it; imports reject invalid ranges instead of changing them.

Verification passed: `npm run test:app` (7,995 assertions), source and test TypeScript checks, and `git diff --check`.