# Checkpoint

Implemented shared `checkEventValidity` and `CalendarEventValidity` in `src/calendar/date/CalendarUtils.ts`. Manual event creation now checks the result and shows existing date errors. ICS parsing rejects invalid dates, pre-1970 starts, and equal or reversed event times instead of repairing invalid end times. Updated calendar utility, parser, and importer tests.

Verification: `npm run types` passed; `npm run test:app` passed (7,989 assertions); `git diff --check` passed.
