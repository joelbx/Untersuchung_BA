Task: implement calendar event date validation in src/calendar/date/CalendarUtils.ts and apply it to creation and ICS import.
Status: complete. Added CalendarEventValidity and checkEventValidity; creation/update and ICS parsing reject invalid event times. Updated calendar tests and fixtures.
Verification: npm run types -- --incremental false passed; npm run test:app passed (7,988 assertions); git diff --check passed. fasttest entry point was unavailable in this checkout, so the full app suite was used.
Constraints observed: local code/tests only; no git history, index, or harness changes.
