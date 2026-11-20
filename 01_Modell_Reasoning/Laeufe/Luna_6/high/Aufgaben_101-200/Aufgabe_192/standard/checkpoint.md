# Checkpoint

Task: Resolve calendar event date validation inconsistencies in `/app`.

Implemented `CalendarEventValidity` and `checkEventValidity` in `src/calendar/date/CalendarUtils.ts`. The validation checks invalid `Date` values first, rejects starts before 1970-01-01 UTC second, and requires start strictly before end third. Added focused tests covering each outcome and precedence in `test/tests/calendar/CalendarUtilsTest.ts`.

Verification: `npm run types` passed. `npm run test:app` passed with all 7,989 assertions. `npm run fasttest` could not run because its configured entry point `api/bootstrapTests-api-fast.ts` is missing. `git diff --check` passed.
