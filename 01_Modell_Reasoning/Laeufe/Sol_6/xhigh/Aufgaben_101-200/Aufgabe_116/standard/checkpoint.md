# Checkpoint

Task: add a global `chat:privileged` gate for initiating chats with privileged users, expose `canChat` on the profile API, update OpenAPI and i18n, and run relevant existing tests.

Status: implemented and verified.

- Added `chat:privileged` to global privilege sets and the English admin label.
- Global privilege checks now accept strings and arrays; chat middleware, messaging, room loading, editing, invitation, controller, and render checks use the array result.
- Starting a chat or inviting a privileged target requires `chat:privileged` and returns `[[error:no-privileges]]` without it.
- Profile data exposes a boolean `canChat` derived from `messaging.canMessageUser`; OpenAPI documents it.
- Added messaging and API coverage for admins, moderators, invitation, profile data, and return types; updated middleware privilege-set assertion.

Verification: `test/messaging.js` (79 passing), `test/middleware.js` (12 passing), ESLint (passing), OpenAPI read/write validation (passing), `git diff --check` (passing). Tests used a temporary local Redis server, which was stopped afterward.
