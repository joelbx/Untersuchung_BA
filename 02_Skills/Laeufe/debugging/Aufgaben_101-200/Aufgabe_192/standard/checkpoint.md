# Debugging checkpoint

Task: implement consistent calendar event date validity checks.

Status: investigating repository code and tests. `rg` is unavailable; using local `find`/`grep`.

Root cause: no shared event validity function exists. The editor checks only `end <= start`; it does not check invalid Date or pre-1970 start. The ICS parser silently changes reversed/equal end times to a valid duration, and has no shared validity result. `isValidDate` only checks `getTime()` for NaN.

Working pattern: `CalendarUtils.ts` already imports `isValidDate`, and `CalendarUtilsTest.ts` uses ospec with `createCalendarEvent()` fixtures. Hypothesis: validate both date objects before comparing milliseconds; compare the start to Unix epoch, then compare start and end to enforce priority.

Reproduction: `npm run test:app` first failed at type checking because `CalendarEventValidity` and `checkEventValidity` did not exist. After adding the shared validator, six parser regression assertions failed as expected because ICS parsing still repaired equal/reversed dates and accepted pre-1970 dates.

Fix: added the enum and shared validator in `CalendarUtils.ts`; the editor now maps its result to a user error, and the ICS parser rejects invalid events with `ParserError` before processing other fields. Updated older parser/importer tests that expected date repair.

Verification: final `npm run test:app` passed (7,990 assertions; exit code 0). Final `git diff --check` passed (exit code 0). No offline tool blockage remained.
