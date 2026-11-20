VERDICT: FIX

Code defect: Existing users API create/delete flows still write `core.api` settings in `src/api/users.js:310-345`; they bypass the new token store and indexes. `src/controllers/admin/settings.js:113-125` also reads settings tokens. A token created through the existing endpoint is absent from `utils.tokens.list()`, and a utility-created token cannot be deleted through that endpoint. Correct by routing create/delete and admin token listing through the new utilities, with any needed migration of legacy settings tokens.

TEST_ENVIRONMENT_PROBLEM: `./node_modules/.bin/mocha test/authentication.js --grep 'api tokens' --timeout 30000` exited 1 before tests ran: `connect ECONNREFUSED 127.0.0.1:6379` (0 passing, 1 failing). A repeat with filtered diagnostics gave the same result. Start the configured test Redis service and rerun. `node --check` on all four modified JavaScript files exited 0; this is syntax verification only.
