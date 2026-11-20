VERDICT: FIX

The ACP status logic in [src/controllers/admin/users.js](/app/src/controllers/admin/users.js:184) labels a user **Validated** when `email:confirmed` is set even if the user has no email. It can also label the displayed profile email **Validation Pending** when the pending confirmation is for a different address. Derive the status from the displayed email, and require the confirmation email to match before showing Pending.

Tests run:

- `./node_modules/.bin/mocha test/user.js --grep '^User email confirm'` — **6 passing**.
- `./node_modules/.bin/mocha test/user.js` — **173 passing, 1 failing** at [test/user.js](/app/test/user.js:2363), an invitation group membership assertion. The run stopped before the confirmation tests.
- `./node_modules/.bin/mocha test/user.js --grep 'email confirm'` — **0 passing, 1 failing**; the broad filter selected a profile test that needs earlier setup.

**TEST_ENVIRONMENT_PROBLEM:** The first test attempt could not connect to local Redis. I started an ephemeral local Redis instance for the subsequent runs and stopped it afterward. The full test failure remains to be investigated separately. Review notes are in [checkpoint.md](/app/.codex-role-output/checkpoint.md). No project code was changed.