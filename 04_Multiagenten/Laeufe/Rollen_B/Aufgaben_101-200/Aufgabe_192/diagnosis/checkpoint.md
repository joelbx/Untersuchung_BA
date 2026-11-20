# Fault localization progress

- The requested `checkEventValidity` function and `CalendarEventValidity` enum do not exist in the checked out source or tests.
- Likely implementation home: `src/calendar/date/CalendarUtils.ts`; it already imports `isValidDate`, but uses it only in an unrelated private assertion near line 554. `isValidDate` in `packages/tutanota-utils/lib/DateUtils.ts` calls `date.getTime()` and recognizes `NaN` Date instances.
- Manual creation: `CalendarEventViewModel._initializeNewEvent` (near line 1151) builds dates and rejects `end <= start` near line 1191; it does not check pre-1970 or invalid Date values. `CalendarModel._doCreate` (near line 253) assigns an ID and saves without shared validation.
- ICS import: `CalendarParser.parseCalendarEvents` (near line 431) builds events; an equal/reversed `DTEND` is normalized to a one-day or one-second duration near line 451, so downstream validation would no longer see that input. `parseTime` checks Luxon validity, but date validity is not checked across entry points.
- Import save: `CalendarImporterDialog.importEvents` (near line 42) maps parsed events directly to `assignEventId` and `saveImportedCalendarEvents`; no common validation. `CalendarFacade._saveCalendarEvents` explicitly says it performs no event checks.
- Existing `CalendarImporterTest` around line 715 expects the current normalization of equal all-day `DTEND`; this test would need changed behavior if malformed ICS is to be rejected at parse time.
- Recommended behavioral checks: valid 1970-01-01T00:00:00.000Z boundary; pre-1970 start; invalid start/end Date; equal and reversed times; precedence invalid > pre-1970 > ordering; both manual and import paths. Runtime non-Date fields need explicit handling if included in the intended invalid-date contract, because `isValidDate` calls `getTime()`.
- Scope constraint: no project source or test files changed. No tests run because this is a read-only diagnosis.
