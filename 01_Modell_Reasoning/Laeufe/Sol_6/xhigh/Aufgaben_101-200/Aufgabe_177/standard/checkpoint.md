# Checkpoint

Task: implement chat allow/deny lists and disable incoming messages in /app.
Status: implementation and focused test updates complete; final review in progress.
Changes: recipient privacy checks shared by direct chat and room paths, account settings and UI, OpenAPI and English labels, idempotent 4.3.0 migration from local and remote follows, focused tests.
Verification: ESLint, syntax, JSON/YAML parsing, and git diff --check pass. Mocha was attempted but cannot start because configured Redis 127.0.0.1:6379 refuses connections; no harness/config files changed.
