# Checkpoint

Implemented token-based invitation verification, storage, email confirmation, group joining, and cleanup. Registration accepts a token without an email and the client form loads the token from the URL.

Verification:
- `node_modules/.bin/mocha test/user.js --grep 'User invites' --reporter dot`: 30 passing, exit 0.
- `node_modules/.bin/eslint src/user/invite.js src/controllers/authentication.js public/src/client/register.js test/user.js && git diff --check`: exit 0.
- `node_modules/.bin/mocha test/user.js --reporter dot`: 177 passing, 1 failing, exit 1. The failure is in `User email confirm should confirm email of user` at test/user.js:2434 (`NaN !== 1`), outside the invitation tests.
- Initial focused test attempt failed with `connect ECONNREFUSED 127.0.0.1:6379`; started the locally installed Redis server with `redis-server --bind 127.0.0.1 --port 6379 --save '' --appendonly no`, then reran verification.
