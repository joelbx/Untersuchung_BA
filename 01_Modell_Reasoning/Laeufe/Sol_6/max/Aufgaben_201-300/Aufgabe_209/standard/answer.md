Updated [SubscribeCalendarModal.tsx](/app/packages/components/containers/calendar/subscribeCalendarModal/SubscribeCalendarModal.tsx) to enforce the centralized 10,000 character limit, block invalid submissions, and show one warning in the requested priority order. Removed the counter and input `maxLength`.

Moved ResizeObserver mocking into [shared Jest setup](/app/packages/components/jest.setup.resizeObserver.js) and removed the per-test assignments. Added [modal tests](/app/packages/components/containers/calendar/subscribeCalendarModal/SubscribeCalendarModal.spec.tsx) with a default-export mock for `useGetCalendarSetup`.

**Verification:** 37 relevant tests passed, along with the components type check, ESLint, Prettier, and `git diff --check`.