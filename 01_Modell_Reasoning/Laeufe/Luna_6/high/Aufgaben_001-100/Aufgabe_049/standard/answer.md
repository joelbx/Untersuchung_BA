Implemented the confirmation key refactor, email fallback and expiry checks, ACP email status labels, and confirmation cleanup on user deletion.

ESLint and `git diff --check` pass. The user and admin test suites could not start because Redis at `127.0.0.1:6379` refused the connection.