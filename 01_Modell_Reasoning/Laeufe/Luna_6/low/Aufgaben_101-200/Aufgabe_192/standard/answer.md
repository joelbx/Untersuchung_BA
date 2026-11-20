Implemented shared calendar date validation in [CalendarUtils.ts](/app/src/calendar/date/CalendarUtils.ts). It checks invalid dates first, then pre-1970 start dates, then start/end ordering; January 1, 1970 is accepted.

Manual saves now reject invalid events before saving or sending notifications. ICS imports reject invalid event dates instead of silently correcting equal or reversed end times. Updated the affected tests.

Verification: TypeScript passed, `git diff --check` passed, and the calendar test run passed all 7,986 assertions.