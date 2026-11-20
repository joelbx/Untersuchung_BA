# Chat allow/deny list work

- Implemented typed chat settings parsing and persistence, centralized allow/deny/disable enforcement, room creation/add-user checks, and the 4.3.0 follow-to-allow-list migration.
- Updated the account settings controller/client handling, API schema, admin default setting, and messaging/user tests.
- Focused tests were attempted, but the suite could not start because Redis at 127.0.0.1:6379 is unavailable. ESLint passed on the edited JavaScript files; `git diff --check` passed.
