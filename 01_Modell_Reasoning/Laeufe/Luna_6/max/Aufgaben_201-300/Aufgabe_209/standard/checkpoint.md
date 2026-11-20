# Checkpoint

Task: Harden Subscribe to Calendar URL validation and centralize ResizeObserver test setup.

Completed:
- Added `MAX_LENGTHS_API.CALENDAR_URL = 10000` and use it to block empty, malformed, and over-limit URLs in both modal flows.
- Added one prioritized warning helper for extension, Google public link, and URL length warnings. Removed the local maximum, maxLength prop, counter, and length styling; changes remain trimmed before state updates.
- Added one shared `jest.setup.js` ResizeObserver mock and imported it from each application and component Jest setup. Removed per-test and helper overrides.
- Made `useGetCalendarSetup` a default function export and mocked it as an ES module default in the calendar container test.

Verification:
- Calendar: `CalendarSidebar.spec.tsx` and `MainContainer.spec.tsx` passed (4 tests in the latter after the hook mock).
- Components: `SubscribedCalendarsSection.spec.tsx` passed.
- Mail: `useSendVerifications.test.ts` passed (12 tests).
- Prettier check passed; `git diff --check` passed.
