# Checkpoint

Task: Add the `chat:privileged` gate and profile `canChat` field.

Root cause: `privileges.global.can` accepted only a string; array input was passed to `helpers.isAllowedTo` with a CID array, triggering `[[error:invalid-data]]`. `messaging.canMessageUser` checked only the general `chat` privilege, so privileged targets had no dedicated gate. The profile data builder did not compute chat permission.

Patch: Register `chat:privileged`, support string and array results in `global.can`, use array-based chat checks in middleware and messaging, deny privileged targets without the new privilege, compute `canChat` through `messaging.canMessageUser`, and document/translate the field and privilege. Existing invitation code already checks each UID through `canMessageUser`.

Verification: The focused test failed before the patch with `[[error:invalid-data]]` from `helpers.isAllowedTo`. Initial test command `./node_modules/.bin/mocha test/messaging.js --grep 'requires chat:privileged' --exit` could not connect to local Redis (`ECONNREFUSED 127.0.0.1:6379`); an available local Redis server was started with `redis-server --bind 127.0.0.1 --port 6379 --save '' --appendonly no --daemonize yes`. After the patch, the focused test passed. Final `./node_modules/.bin/mocha test/messaging.js --exit`: 78 passing, exit 0. Targeted ESLint, `git diff --check`, and JSON parse checks: exit 0.
