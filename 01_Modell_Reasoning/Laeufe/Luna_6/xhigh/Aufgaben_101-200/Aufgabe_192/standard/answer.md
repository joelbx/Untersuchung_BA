Implemented shared event date validation in [CalendarUtils.ts](/app/src/calendar/date/CalendarUtils.ts:52), prioritizing invalid dates, pre-1970 starts, then non-increasing start and end times.

Manual saves now reject invalid events, and ICS imports reject invalid dates instead of repairing equal or reversed end times. Updated the corresponding calendar tests.

Verification: `npm run types` and `git diff --check` pass; `npm run test:app` passes all 7,990 assertions.