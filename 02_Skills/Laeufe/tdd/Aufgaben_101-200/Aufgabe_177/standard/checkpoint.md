# Chat allow/deny list checkpoint

Status: implemented chat privacy settings, server-side checks, account controls, and idempotent follow-list migration. Assigned test-driven-development skill was used for permission, room creation, moderator, and migration behaviors; each of those tests was observed failing before the corresponding fix and passing afterward.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep` and `find`.

Verification:
- `./node_modules/.bin/mocha test/user.js test/messaging.js --no-bail`: 357 passing. Existing sendmail-not-found log messages occur in email tests, though the tests pass.
- `./node_modules/.bin/eslint src/messaging/index.js src/messaging/rooms.js src/user/settings.js src/upgrades/4.3.0/chat_allow_list.js public/src/client/account/settings.js test/messaging.js test/user.js`: passed.
- `npm test`: 306 passing, 1 failing, then stopped by configured bail. The failing `test/api.js` contract check is `GET /api/admin/extend/plugins` (unexpected HTTP 500). Its controller's external plugin fetch raised `TypeError: fetch failed`; external research is blocked, so this unrelated check remains unverified beyond that failure.
