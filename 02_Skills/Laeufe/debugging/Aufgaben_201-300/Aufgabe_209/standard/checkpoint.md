# Checkpoint

Root cause: the modal used a local 10,000 character constant and an input maxLength, while submit validation checked only nonempty and URL format. The shared MAX_LENGTHS_API had no CALENDAR_URL entry. ResizeObserver was assigned in individual calendar and mail tests in addition to test setup. The test for the shared constant failed before implementation with `Expected: 10000; Received: undefined`.

Added CALENDAR_URL to the shared limit object, centralized submit validation and warning priority, and removed the counter and maxLength. Moved test ResizeObserver mocks to the components, calendar application, and mail application Jest setup files. Removed individual test and helper assignments. Added modal regression tests with a default-export mock for useGetCalendarSetup.

Checks completed successfully:
- Components modal regression test: 4 passed.
- Components subscribed calendar section suite: 1 passed.
- Calendar application CalendarSidebar and MainContainer suites: 6 passed (existing React warnings).
- Mail useSendVerifications suite: 12 passed.
- `./node_modules/.bin/tsc --noEmit -p packages/components/tsconfig.json` passed.
- Targeted ESLint, Prettier check, and `git diff --check` passed.
