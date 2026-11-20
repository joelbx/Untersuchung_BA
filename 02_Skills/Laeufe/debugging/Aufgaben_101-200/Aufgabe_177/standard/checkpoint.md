# Chat privacy issue checkpoint

Root cause: `Messaging.canMessageUser` used a single `restrictChat` flag and the recipient's live follow relationship. Account settings only loaded and saved that flag, and the installed account template displayed it. HTTP chat creation and invitations called this check, while the lower level room helpers and federated message creation could bypass it.

Reproduction: added a focused permission test before the fix. `./node_modules/.bin/mocha test/messaging.js --grep 'honors deny, allow' --exit` first failed with `ECONNREFUSED 127.0.0.1:6379` because local Redis was stopped. After starting local Redis, it failed at `test/messaging.js:87` with `[[error:chat-restricted]]`, where an explicitly allowed sender was still rejected by the old follow rule.

Patch: settings now parse and store allow and deny lists as JSON arrays of string UIDs, with invalid inputs loading as empty arrays. The server checks explicit blocks before disabled incoming, deny, and allow rules, while admins and global moderators retain their exemption from the latter rules. Room creation and adding users check recipient privacy before mutation, including federation paths. Account settings expose the three new controls. The upgrade seeds allow lists from local and remote follows, handles the old global default, preserves closed access for legacy users with no follows, and skips already migrated accounts on repeat runs.

Verification: `./node_modules/.bin/eslint src/user/settings.js src/messaging/index.js src/messaging/rooms.js src/upgrades/4.3.0/chat_allow_list.js public/src/client/account/settings.js test/messaging.js test/user.js` exited 0. `./node_modules/.bin/mocha test/messaging.js test/user.js --exit` exited 0 with 358 passing. The test run logged missing `sendmail` in unrelated email tests but did not fail. `git diff --check` exited 0.

Final test assertion also covers an explicitly blocked administrator. After adding it, `./node_modules/.bin/mocha test/messaging.js --grep 'explicit block' --exit` passed (1 passing), and `./node_modules/.bin/eslint test/messaging.js && git diff --check` exited 0.

Tooling note: `rg` is unavailable, so searches used `grep` and `find`. No dependencies were downloaded.
