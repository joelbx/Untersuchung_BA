Updated [SubscribeCalendarModal.tsx](/app/packages/components/containers/calendar/subscribeCalendarModal/SubscribeCalendarModal.tsx) to use `MAX_LENGTHS_API.CALENDAR_URL` for validation. Overlong URLs now show a single warning according to the requested priority and cannot be submitted. The character counter and input length cap are removed.

Moved ResizeObserver test mocks into the shared calendar, components, and mail Jest setup files and removed the inline assignments.

**Verification:** All 19 relevant tests passed across four suites; `git diff --check` passed.