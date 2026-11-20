Implemented the chat edit flow: the v3 controller validates content, checks edit permissions, saves the change, and returns the updated message. Added `messageExists` and invalid ID handling, enabled the PUT route, updated localization and client requests, and added socket deprecation logging and input validation.

**Verification:** Syntax, JSON parsing, diff checks, and focused ESLint checks passed. The messaging tests could not start because Redis at `127.0.0.1:6379` refused the connection. Broader linting still reports existing unused parameters/imports and long commented-out routes.

The required progress notes are in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).