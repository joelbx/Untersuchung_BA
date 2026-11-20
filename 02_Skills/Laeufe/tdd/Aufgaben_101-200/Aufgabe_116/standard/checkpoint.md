# Checkpoint

Implemented privileged chat gate across global privileges, middleware, messaging, chat API, profile response, i18n, and OpenAPI.

## Verification

- `./node_modules/.bin/mocha test/messaging.js --grep 'global privilege arrays|chatting with an administrator|reports canChat|low-reputation user targeting'`: 5 passing after observing expected red failures.
- `./node_modules/.bin/eslint src/privileges/global.js src/messaging/index.js src/messaging/rooms.js src/messaging/edit.js src/middleware/user.js src/controllers/accounts/chats.js src/controllers/accounts/helpers.js src/api/chats.js test/messaging.js`: passed before final ordering patch; rerun pending.
- `git diff --check`: passed before final ordering patch; rerun pending.

## Offline / existing test obstacles

- Initial `./node_modules/.bin/mocha test/messaging.js --grep 'global privilege arrays|chatting with an administrator|reports canChat'` failed during setup: `connect ECONNREFUSED 127.0.0.1:6379`. Started locally installed Redis for subsequent tests, with no download.
- `npm test`: 194 passing, 1 failing. `response status code should match one of the schema defined responses` failed because `GET /api/admin/extend/plugins` returned HTTP 500 after `https://packages.nodebb.org/api/v1/plugins` failed with `tunneling socket could not be established, statusCode=403`. Full suite beyond that point remains unverified because Mocha is configured to bail.
- `./node_modules/.bin/mocha test/messaging.js`: 8 passing, 1 failing. Existing `should not allow messaging room if user is muted` expects `[[error:no-room]]` but receives `[[error:user-muted-for-hours, 2]]` after its database field deletion; the failure also occurs when run alone.
- `./node_modules/.bin/mocha test/messaging.js --no-bail`: 76 passing, 3 failing. The mute test above, `should return true if user is dnd` (false result), and `should fail if user can not view toMid` (mute error instead of privilege error; likely downstream from stale mute state).
- `./node_modules/.bin/mocha test/messaging.js --no-bail --grep 'should not allow messaging room if user is muted' --invert`: 77 passing, 1 failing: `should return true if user is dnd` (false result).

Final focused verification after preserving the single-string helper path: `./node_modules/.bin/mocha test/messaging.js --grep 'global privilege arrays|chatting with an administrator|reports canChat|low-reputation user targeting'` passed (5 tests). Final ESLint and `git diff --check` passed. OpenAPI YAML and English privilege JSON parsed successfully with local Node modules.
