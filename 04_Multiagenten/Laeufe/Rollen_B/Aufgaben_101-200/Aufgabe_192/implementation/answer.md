Added `checkEventValidity` and `CalendarEventValidity` in [CalendarUtils.ts](/app/src/calendar/date/CalendarUtils.ts). The check rejects invalid dates first, then starts before January 1, 1970, then equal or reversed start and end times. The epoch boundary is valid.

Manual creation now uses the shared check. ICS parsing uses it too and rejects invalid end times instead of changing them to a positive duration. Updated the related tests.

Verification: TypeScript checking passed, the full local suite passed (7,990 assertions), and `git diff --check` passed.