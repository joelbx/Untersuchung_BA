# Checkpoint

Task: Harden Subscribe to Calendar URL validation and centralize ResizeObserver test setup.

Progress: Complete. Centralized calendar URL length validation and prioritized warnings in `SubscribeCalendarModal`; moved ResizeObserver mocks from individual tests/helpers into the components, calendar, and mail Jest setup files; mocked the setup hook as an ES module default in the calendar app test. The focused subscribed-calendar, calendar sidebar/main-container, and mail verification tests passed. Components type checking, Prettier, and `git diff --check` passed. The calendar app tests continue to print unrelated existing React `act(...)` and Router warnings.
