Implemented shared date validation and applied it to manual event creation and ICS parsing. Pre-1970 dates are rejected instead of shifted, and equal or reversed end times are rejected instead of repaired.

Updated existing tests for the new import behavior. `npm run types` passed, and `npm run test:app` passed with 7,981 assertions. The separate `npm run fasttest` script could not start because its configured entry point is missing from this checkout.

Key changes: [CalendarUtils.ts](/app/src/calendar/date/CalendarUtils.ts:52), [CalendarEventViewModel.ts](/app/src/calendar/date/CalendarEventViewModel.ts:1183), [CalendarParser.ts](/app/src/calendar/export/CalendarParser.ts:464).