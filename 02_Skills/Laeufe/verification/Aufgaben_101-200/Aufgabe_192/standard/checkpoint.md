# Checkpoint

Task: add consistent calendar event date validation in `src/calendar/date/CalendarUtils.ts` and verify with local tests.

Status: shared validator added and wired into manual event creation and ICS parsing. Regression tests added/updated.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local file search alternatives. `npm run fasttest` failed because esbuild could not resolve `api/bootstrapTests-api-fast.ts`; this repository has no `test/api` directory. `npm run types` passed. First `npm run test:app` run exited 1 after 7,986 assertions passed and one bail-out: `CalendarImporterTest > import > all-day event with invalid DTEND` still expected the old repair behavior. Updated that expectation to rejection. Final `npm run test:app` exited 0: all 7,990 assertions passed (old style total: 8,997).
