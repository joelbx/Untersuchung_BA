# Checkpoint

Task: implement `/.well-known/webfinger` in `/app`.

Status: investigation. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

Constraints: no external research/downloads; do not alter git history, index baseline, or harness configuration.

Investigation: main router composes core routes in `src/routes/index.js`; no WebFinger mount or controller exists. User slugs resolve through `user.getUidByUserslug`; `privileges.global.can('view:users', 0)` maps UID 0 to the Guest group, whose persisted privilege key is `groups:view:users`. Profile URLs use `/uid/:uid` and `/user/:userslug`.

Hypothesis: missing route/controller is the cause of the 404. The minimal test `node_modules/.bin/mocha test/well-known.js --reporter spec` failed as expected before implementation with `ENOENT: /app/src/controllers/well-known.js` (exit 1). This test covers route wiring, validation, Guest/authenticated authorization, lookup, and response structure.

Implementation: added dedicated WebFinger controller and route module; registered both in the core composition. The handler validates a single `acct:<slug>@<configured hostname>` resource, checks `view:users` with UID 0 for absent `req.uid`, resolves the slug, and returns JRD JSON with UID and slug aliases and an HTML profile link.

Verification: `node_modules/.bin/mocha test/well-known.js --reporter spec` passed (5 tests, exit 0). `node_modules/.bin/eslint src/controllers/well-known.js src/controllers/index.js src/routes/well-known.js src/routes/index.js test/well-known.js` passed (exit 0). `git diff --check` passed (exit 0).

Existing database backed controller tests were not run: `test/mocks/databasemock.js` reads and logs `config.json`, which may contain credentials; accessing those is prohibited. The isolated WebFinger suite covers route registration and handler behavior without that fixture. Full application startup was not exercised, so integration with the production middleware stack remains unverified.
