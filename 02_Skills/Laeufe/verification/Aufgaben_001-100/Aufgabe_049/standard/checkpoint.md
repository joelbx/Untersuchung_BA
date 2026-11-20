# Email confirmation fix checkpoint

Implemented user-to-code confirmation mapping, explicit expiry, email fallback, ACP status labels, recipient override for pending addresses, an explicit invalid-email error when no address can be found, and confirmation cleanup during user deletion. Added focused tests in `test/user.js`.

Verification:

- `./node_modules/.bin/mocha test/user.js --grep '^User email confirm '` — final rerun: 5 passing, exit 0.
- `./node_modules/.bin/eslint src/user/email.js src/user/create.js src/user/delete.js src/user/profile.js src/emailer.js src/controllers/admin/users.js public/src/admin/manage/users.js test/user.js` — exit 0.
- `node -e "const fs=require('fs'); const b=require('benchpressjs'); b.precompile(fs.readFileSync('src/views/admin/manage/users.tpl','utf8'),{filename:'admin/manage/users.tpl'}).then(()=>console.log('template compile: ok')).catch(e=>{console.error(e);process.exitCode=1})"` — `template compile: ok`, exit 0.
- `./node_modules/.bin/mocha test/user.js` — rerun after final code changes: 173 passing, 1 failing; invitation test `User invites after invites checks should joined the groups from invitation after registration` reports `Error: Not joined to the groups` at `test/user.js:2364`. This lies outside the confirmation section; full `test/user.js` remains unverified as passing.
- Initial `./node_modules/.bin/mocha test/user.js --grep 'email confirm'` failed with `connect ECONNREFUSED 127.0.0.1:6379`; started local Redis and reran focused checks.
- `git diff --check` — exit 0.
