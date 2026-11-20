Added the global `chat:privileged` permission and enforced it when a user starts a chat with, or invites, an administrator or moderator. Chat middleware and messaging now use array based privilege checks; denied requests return `[[error:no-privileges]]`. Profile responses expose `canChat`, and the privilege appears in the admin UI and OpenAPI schema.

**Verification:** 80 messaging tests passed, OpenAPI validation passed, and ESLint and `git diff --check` passed. A broader run reached 455 passing tests before an unrelated controller data export test failed in its profile export child process.

No delegation was used.