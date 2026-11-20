# Checkpoint

Task: Harden Subscribe to Calendar URL validation and centralize ResizeObserver test setup.

Completed:
- Added `MAX_LENGTHS_API.CALENDAR_URL = 10000` and removed the modal's duplicate length constant, counter, and input maxLength.
- Trimmed URL input; blocked empty, malformed, and overlong URLs in the submit button and form handler. Added one warning function with extension, Google public link, then length priority.
- Moved ResizeObserver mocks into Calendar, Mail, and Components Jest setup files; removed assignments from individual tests and Mail's test helper.
- Added focused modal tests with a default-export mock for `useGetCalendarSetup`.

Verification:
- `yarn jest --runInBand --coverage=false containers/calendar/subscribeCalendarModal/SubscribeCalendarModal.spec.tsx --silent` (packages/components): 4 passed.
- `yarn jest --runInBand --coverage=false containers/calendar/settings/SubscribedCalendarsSection.spec.tsx` (packages/components): 1 passed.
- `yarn jest --runInBand --coverage=false src/app/containers/calendar/CalendarSidebar.spec.tsx src/app/containers/calendar/MainContainer.spec.tsx --silent` (applications/calendar): 6 passed.
- `yarn jest --runInBand --coverage=false src/app/hooks/composer/useSendVerifications.test.ts --silent` (applications/mail): 12 passed.
- `yarn check-types --pretty false` (packages/components): passed.
- `git diff --check`: passed.

Tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`), so repository searches used `git grep`.
