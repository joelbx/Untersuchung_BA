Updated [SubscribeCalendarModal.tsx](/app/packages/components/containers/calendar/subscribeCalendarModal/SubscribeCalendarModal.tsx) to use the shared 10,000 character URL limit, block invalid or oversized submissions, trim input, and show one warning in the requested priority order. Removed the counter and input length attribute.

Moved ResizeObserver mocks into the components, calendar, and mail Jest setup files and removed the test-local redefinitions. Added [modal tests](/app/packages/components/containers/calendar/subscribeCalendarModal/SubscribeCalendarModal.spec.tsx) with a default-export mock for `useGetCalendarSetup`.

Verification passed: 21 relevant tests, Prettier, and `git diff --check`.