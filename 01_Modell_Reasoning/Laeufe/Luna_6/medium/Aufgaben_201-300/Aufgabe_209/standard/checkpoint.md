# Checkpoint

Task: Harden Subscribe Calendar URL validation and centralize ResizeObserver test setup.

Completed: Added MAX_LENGTHS_API.CALENDAR_URL (10000); consolidated URL length, validity, warning precedence, and submit disabling in SubscribeCalendarModal; removed inline ResizeObserver assignments from calendar/mail test files and configured shared Jest setups.

Verification: CalendarSidebar.spec.tsx and MainContainer.spec.tsx passed (2 suites, 6 tests). An attempted components modal test path does not exist in the repository.
