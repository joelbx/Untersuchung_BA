# Checkpoint

Issue resolved: calendar events now share date validation across manual creation and ICS parsing/import.

Implementation:
- Added `CalendarEventValidity` and `checkEventValidity` in `src/calendar/date/CalendarUtils.ts`.
- Validation checks invalid Date values first, then start times before the Unix epoch, then start/end ordering (including equal times).
- Manual event construction rejects each invalid result; date selection no longer silently shifts pre-1970 dates.
- ICS parsing rejects invalid results instead of repairing equal/reversed end times.
- Updated existing parser/importer tests whose expectations covered the previous repair behavior.

Verification:
- `npm run types` passed.
- `npm run test:app` passed: 7,981 assertions.
- `npm run fasttest` could not start because its configured `test/api/bootstrapTests-api-fast.ts` entry point is absent in this checkout; the regular app test runner built and ran the existing suite.
