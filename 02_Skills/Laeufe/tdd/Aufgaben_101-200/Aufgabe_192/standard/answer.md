Added `CalendarEventValidity` and `checkEventValidity` in [CalendarUtils.ts](/app/src/calendar/date/CalendarUtils.ts). The function reports invalid dates first, then pre-1970 starts, then start/end ordering errors. Added nine regression tests in [CalendarUtilsTest.ts](/app/test/tests/calendar/CalendarUtilsTest.ts).

`npm test` passed: 7,990 assertions.