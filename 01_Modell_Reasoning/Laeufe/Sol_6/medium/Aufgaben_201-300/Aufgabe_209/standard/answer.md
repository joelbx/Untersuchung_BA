Updated [SubscribeCalendarModal](/app/packages/components/containers/calendar/subscribeCalendarModal/SubscribeCalendarModal.tsx) to use `MAX_LENGTHS_API.CALENDAR_URL` for validation. Overlong URLs now disable submission and show “URL is too long,” with extension and Google public link warnings taking priority. Removed the counter and input length attribute.

Moved ResizeObserver test mocks into the calendar, components, and mail Jest setup files and removed inline assignments. Added [modal regression tests](/app/packages/components/containers/calendar/subscribeCalendarModal/SubscribeCalendarModal.spec.tsx) with a default export mock for `useGetCalendarSetup`.

Verification passed: 21 relevant tests, the components TypeScript check, Prettier, and `git diff --check`.