Implemented the `chat:privileged` permission across privilege checks, chat middleware, messaging, and invitations. Chat attempts targeting privileged users now use the shared `messaging.canMessageUser` check and return `[[error:no-privileges]]` when the caller lacks permission. Profile API responses now include `canChat`, documented in OpenAPI.

Added the English admin privilege label and recorded the work in [checkpoint.md](/app/.codex-role-output/checkpoint.md).

**Verification:** ESLint and `git diff --check` passed. The messaging tests could not start because Redis at `127.0.0.1:6379` was unavailable.