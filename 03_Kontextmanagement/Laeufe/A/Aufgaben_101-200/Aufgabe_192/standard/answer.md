Added `checkEventValidity` with distinct results for invalid dates, pre-1970 starts, and starts that are equal to or after the end. Event creation and ICS imports now use the same validation. Updated the affected tests.

Type checking passed, and the application test suite passed with 7,989 assertions.