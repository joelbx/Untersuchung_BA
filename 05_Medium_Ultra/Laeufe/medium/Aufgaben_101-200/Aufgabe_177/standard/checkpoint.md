# Chat allow/deny list checkpoint

Completed implementation: user defaults and safe list parsing/storage; server privacy checks with block precedence and admin/global moderator exemption; direct room creation and invitation checks; account settings controls; 4.3.0 idempotent migration from legacy follow lists; API schema and English strings; relevant tests.

Validation: `mocha test/messaging.js test/user.js --timeout 25000` passed (354 tests). ESLint and `git diff --check` passed. Redis was started locally for tests.
