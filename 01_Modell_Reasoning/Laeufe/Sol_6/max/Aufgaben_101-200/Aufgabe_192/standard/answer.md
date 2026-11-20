Added `checkEventValidity` and `CalendarEventValidity` in [CalendarUtils.ts](/app/src/calendar/date/CalendarUtils.ts:52). The validator checks invalid dates first, then pre-1970 starts, then whether the start is strictly before the end.

Manual saves and ICS imports now use that result. Pre-1970 dates are no longer silently changed, and ICS events with equal or reversed times are rejected. Tests cover both paths.

Verification passed: TypeScript checks, `git diff --check`, and the app test suite (8,003 assertions).