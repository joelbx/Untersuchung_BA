# Checkpoint

- Task: validate calendar event dates consistently for creation and import.
- Added `CalendarEventValidity` and `checkEventValidity` with invalid-date, pre-1970, and ordering precedence.
- Manual creation and ICS parsing call the shared validator. ICS parser no longer repairs reversed/equal end dates.
- Updated existing calendar tests for rejection and added boundary/precedence coverage.
- Verification: `npm run test:app` passed (7,995 assertions); `npm run types` and `npx tsc -p test/tsconfig.json --noEmit` passed.
