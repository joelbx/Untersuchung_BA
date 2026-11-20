Calendar subscription URLs now use `MAX_LENGTHS_API.CALENDAR_URL` (10,000). The modal trims input, blocks empty, malformed, and oversized URLs in both submit flows, and shows one warning at a time in the requested priority. I removed the character counter and input `maxLength`.

ResizeObserver test mocks now live in the relevant Jest setup files; inline redefinitions were removed. A new [modal test](/app/packages/components/containers/calendar/subscribeCalendarModal/SubscribeCalendarModal.spec.tsx) covers the length boundary, warning priority, and disabled states, with a default export mock for `useGetCalendarSetup`.

Verification: 22 affected tests pass, along with the components typecheck, Prettier check, and `git diff --check`.