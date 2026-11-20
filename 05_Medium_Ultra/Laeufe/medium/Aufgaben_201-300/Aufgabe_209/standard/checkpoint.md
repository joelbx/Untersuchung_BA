Task: Harden SubscribeCalendarModal URL validation and centralize ResizeObserver Jest setup.
Status: Complete. Added CALENDAR_URL to MAX_LENGTHS_API; modal uses shared limit, unified submit disabled state and prioritized warning helper; removed counter and maxLength. Centralized ResizeObserver mocks in components, calendar, and mail Jest setup and removed inline test assignments. Added modal regression tests with a default-export useGetCalendarSetup mock.
Verification: Component typecheck and targeted ESLint passed. Modal suite (3 tests), calendar suites (6 tests), and mail useSendVerifications suite (12 tests) passed. Prettier check and git diff --check passed.
Constraints: Local code/tests only; git history, index baseline, and harness configuration untouched.
