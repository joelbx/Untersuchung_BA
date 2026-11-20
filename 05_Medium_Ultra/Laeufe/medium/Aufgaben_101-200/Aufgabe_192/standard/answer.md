Added shared event date validation and applied it to manual creation and ICS imports. Events with invalid dates, a start before January 1, 1970, or a start at or after the end are now rejected in the required priority order. ICS imports no longer repair invalid end times.

Verification passed: `npm run types`, `npm run test:app` (7,989 assertions), and `git diff --check`.