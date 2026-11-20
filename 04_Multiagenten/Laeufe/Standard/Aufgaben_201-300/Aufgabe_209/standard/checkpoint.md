Task: Harden SubscribeCalendarModal URL validation and centralize ResizeObserver test setup.
Status: Complete.
Changes: Added MAX_LENGTHS_API.CALENDAR_URL = 10000; unified modal submit validation and warning priority; removed URL counter and input maxLength; trimmed input; moved ResizeObserver mocks into components, calendar, and mail Jest setup; removed inline redefinitions; added focused modal tests with a default-export mock for useGetCalendarSetup.
Verification: Focused modal tests passed (2); components calendar settings tests passed (1); calendar integration tests passed (6); mail composer tests passed (12). Prettier check and git diff --check passed. Existing calendar integration tests emit React act and Router warnings while passing.
