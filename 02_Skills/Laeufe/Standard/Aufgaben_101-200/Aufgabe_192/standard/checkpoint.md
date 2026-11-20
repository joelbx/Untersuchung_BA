# Checkpoint

Task: Add shared calendar event date validation in `src/calendar/date/CalendarUtils.ts` and verify relevant workflows/tests.

Initial search: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

Implementation: Added `CalendarEventValidity` and `checkEventValidity` with invalid-date, pre-1970, then ordering precedence. Manual save and ICS parsing now use it; ICS parsing preserves seconds. Added utility and parser/importer test coverage.

Checks so far:
- `npm run types`: passed.
- First `npm run test:app`: build failed because the test used unsupported ospec `hasLength`; fixed.
- Second `npm run test:app`: 7985 assertions passed, but two tests failed: epoch boundary exposed seconds being discarded by ICS parsing, and an importer test expected legacy repair of invalid `DTEND`; fixed both and rerunning.
- Final `npm run test:app`: passed; 7,990 assertions (old style total: 8,997).
- Final `git diff --check`: passed.

Result: Both manual event saving and ICS parsing reject invalid date objects, pre-epoch starts, and non-increasing date ranges using the shared enum. ICS seconds are retained so one-second events remain valid.
