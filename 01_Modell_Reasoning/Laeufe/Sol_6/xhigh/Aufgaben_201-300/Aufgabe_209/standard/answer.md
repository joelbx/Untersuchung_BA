The calendar subscription modal now uses `MAX_LENGTHS_API.CALENDAR_URL` to block URLs over 10,000 characters. It trims input, uses one disabled state for both modal flows, and shows a single warning in the requested priority order. I removed the counter and input length cap.

ResizeObserver mocks now live in the components, calendar, and mail Jest setup files; the inline test mocks are removed. The calendar setup hook has the correct default-export mock in the new modal test, so the real hook does not run there.

Verification passed: 20 relevant tests, targeted ESLint, Prettier, and `git diff --check`.