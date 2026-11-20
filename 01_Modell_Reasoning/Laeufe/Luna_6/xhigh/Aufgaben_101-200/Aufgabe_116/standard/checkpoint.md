# Checkpoint

Implemented `chat:privileged` across global privilege registration, chat middleware, messaging permission checks, and the admin privilege labels. `privileges.global.can` now returns a boolean for one privilege and a boolean array for an array of privileges.

`messaging.canMessageUser` requires the regular `chat` permission and additionally requires `chat:privileged` when the target is an administrator, global moderator, or category moderator. Existing direct chat creation and per-invitee validation use this check.

Profile responses from the legacy API, v3 users API, and account profile helpers now include `canChat`, computed by calling `messaging.canMessageUser`. Documented this field in the OpenAPI user schemas.

Validation:
- `npx eslint` on changed JavaScript: passed.
- `git diff --check`: passed.
- `npx mocha test/messaging.js test/middleware.js`: 87 passing.
- `npx mocha test/controllers.js --grep 'should load user by uid'`: 1 passing.
- Broader `npx mocha test/messaging.js test/middleware.js test/controllers.js`: 227 passing, 1 unrelated failure in the existing user posts export route (`test/controllers.js:1692`, `assert(body)`); export worker also logged an uncaught error.
