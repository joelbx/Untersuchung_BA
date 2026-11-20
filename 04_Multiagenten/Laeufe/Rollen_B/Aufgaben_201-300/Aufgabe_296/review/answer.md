VERDICT: ACCEPT

I reviewed the invitation patch and found no correctness regression in the changed registration and invitation paths. The form passes the URL token through its hidden field; registration uses token metadata for email confirmation, group membership, and invitation cleanup. No project code was changed.

Tests executed:

- `./node_modules/.bin/mocha test/user.js --grep 'invites'` — 31 passing.
- `./node_modules/.bin/mocha test/authentication.js` — 30 passing.
- `./node_modules/.bin/eslint public/src/client/register.js src/controllers/authentication.js src/user/invite.js test/user.js` — exit 0.

**TEST_ENVIRONMENT_PROBLEM:** The first invitation test attempt could not start because local Redis was down (`ECONNREFUSED 127.0.0.1:6379`). I started the installed Redis server, reran the tests successfully, and stopped it afterward.