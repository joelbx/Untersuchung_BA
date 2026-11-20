# Checkpoint

Task: resolve calendar event date validation gaps in `/app`.

Plan:
1. Inspect repository instructions, `CalendarUtils.ts`, and existing validation callers/tests.
2. Add the shared validity enum/function and connect creation/import paths if needed.
3. Run relevant existing tests and summarize the change.

Progress: added prioritized date checks in `CalendarUtils`, wired them into event saves and ICS parsing, and updated calendar utility/parser tests to assert the new rejection behavior.

Verification: `npm run types` and `git diff --check` pass. The full `npm run test:app` suite passes all 7,990 assertions.
