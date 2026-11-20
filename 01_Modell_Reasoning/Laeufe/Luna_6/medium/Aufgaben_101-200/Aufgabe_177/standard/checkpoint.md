# Chat Allow/Deny List

- Inspect existing user settings, chat permission checks, upgrade conventions, and relevant tests.
- Implement explicit incoming-chat disable, allow list, and deny list with required precedence and moderator exceptions.
- Add repeat-safe 4.3.0 migration and update naming references.
- Run relevant existing tests and record results.

## Progress

- Replaced `restrictChat` runtime settings with `disableIncomingMessages`, `chatAllowList`, and `chatDenyList`; list values are parsed defensively and saved as JSON-encoded string UID arrays.
- Updated the shared sender permission gate and API settings schema. Added an idempotent 4.3.0 migration that seeds absent allow lists from each legacy-restricted user's follows.
- Updated existing messaging/user tests and the admin default setting label/key.
- Static syntax checks and `git diff --check` passed; ESLint passed after correcting one line-length issue.
- The messaging test command was attempted, but test startup failed because Redis at 127.0.0.1:6379 is unavailable.
