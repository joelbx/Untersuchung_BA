# Checkpoint

Implemented CalendarEventValidity and checkEventValidity with invalid-date, pre-1970, and ordering precedence. Manual creation maps results to UserError; ICS parsing rejects invalid events with ParserError and no longer repairs equal/reversed end times. Updated calendar tests. Verification: npm run types -- --incremental false passed; npm run test:app passed (7,989 assertions).
