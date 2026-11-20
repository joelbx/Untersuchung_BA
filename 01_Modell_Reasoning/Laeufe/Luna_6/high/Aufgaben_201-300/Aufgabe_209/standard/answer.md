Implemented calendar URL validation with the centralized 10,000 character limit, a unified submit disabled state, and one prioritized warning at a time. Removed the URL counter and `maxLength` prop.

Moved `ResizeObserver` mocks to the components and calendar Jest setup files, removed individual test reassignments, and added a default-export hook mock to the calendar integration test.

Verification passed: calendar test suites (6 tests), MainContainer rerun after the hook mock (4 tests), Prettier check, and `git diff --check`. Updated [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).