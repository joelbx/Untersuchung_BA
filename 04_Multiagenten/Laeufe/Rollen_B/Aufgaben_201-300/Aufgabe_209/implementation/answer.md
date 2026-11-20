The calendar subscription modal now uses `MAX_LENGTHS_API.CALENDAR_URL` to block URLs over 10,000 characters, including form submissions. It trims input, shows one warning in the requested priority order, and no longer shows a character counter or applies an input `maxLength`.

`ResizeObserver` mocks are defined in the calendar, components, and mail Jest setup files; the inline redefinitions were removed. The new modal test mocks `useGetCalendarSetup` as a default export.

Verification passed: 3 modal tests, 6 calendar tests, 12 mail tests, Prettier, and `git diff --check`.