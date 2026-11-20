VERDICT: FIX

**Code defect:** The existing token creation and deletion routes still use `core.api` settings in [src/api/users.js](/app/src/api/users.js:310). Tokens created there are absent from `utils.tokens.list()`, and tokens created by the new utility cannot be deleted through the existing route. [Admin token settings](/app/src/controllers/admin/settings.js:113) also reads the old store. Route these operations through the new utilities and account for existing settings tokens.

**TEST_ENVIRONMENT_PROBLEM:** `./node_modules/.bin/mocha test/authentication.js --grep 'api tokens' --timeout 30000` exited 1 before tests ran: Redis refused the connection at `127.0.0.1:6379` (0 passing, 1 failing). Start the configured test Redis service and rerun it. `node --check` passed for all four modified JavaScript files; that verifies syntax only.

No project code was changed during this review.