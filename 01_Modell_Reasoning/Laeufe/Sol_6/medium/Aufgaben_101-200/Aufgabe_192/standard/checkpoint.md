Task: Resolve calendar event date validation in /app.
Implemented: CalendarEventValidity and checkEventValidity in CalendarUtils; manual event creation and ICS parser use shared validation. Parser rejects equal/reversed end times instead of repairing them. Updated utility, parser, and importer tests.
Verification: TypeScript check passed; npm run test:app passed (7,991 assertions). git diff --check passed.
Constraints respected: local repository and existing tests only; no git history, index baseline, or harness configuration changes.
