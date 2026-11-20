Implemented chat privacy settings, server-side enforcement, room checks, and the idempotent 4.3.0 migration. Account settings now expose the disable toggle and allow/deny UID lists; the API schema and relevant tests were updated.

ESLint and `git diff --check` passed. The focused tests could not start because Redis at `127.0.0.1:6379` is unavailable.

The migration reads the legacy `restrictChat` field to identify accounts that need conversion.