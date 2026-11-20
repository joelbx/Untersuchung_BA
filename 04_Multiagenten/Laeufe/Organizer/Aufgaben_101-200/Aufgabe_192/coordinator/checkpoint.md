Task: Implement shared calendar event date validation in CalendarUtils.ts.
Status: Complete. Added CalendarEventValidity and checkEventValidity with invalid-date, pre-1970, and ordering precedence. Manual event creation and ICS import call the validator; importer rejects invalid end times instead of correcting them.
Tests: ./node_modules/.bin/tsc --noEmit --incremental false passed; npm run test:app passed (7992 assertions, old style total 8999); git diff --check passed.
Delegation: None.
