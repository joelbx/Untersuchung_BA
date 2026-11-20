# Checkpoint

Task: validate admin file uploads against the configured upload directory, returning HTTP 500 with `[[error:invalid-path]]` for missing target directories.

Status: locating route and tests. Assigned TDD workflow applies; regression test will be run red before implementation.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using `find` and `grep`.

Initial red test command: `./node_modules/.bin/mocha test/uploads.js --grep 'target folder does not exist' --no-bail` failed in the root before hook with `connect ECONNREFUSED 127.0.0.1:6379`; route assertion was not reached. Redis server is available locally, so retrying with an ephemeral instance.

Red test reached route after starting ephemeral Redis: `./node_modules/.bin/mocha test/uploads.js --grep 'target folder does not exist' --no-bail` failed as expected with `200 !== 500` at test/uploads.js:411. Green rerun passed (1 passing).

Implementation: admin `uploadFile` now stats `path.join(nconf.get('upload_path'), params.folder)` before saving. Missing paths, non-directory targets, and missing intermediate components produce `[[error:invalid-path]]`; existing route error handling returns HTTP 500. Added HTTP regression asserting status, error, and no directory creation.

Verification:
- `./node_modules/.bin/mocha test/uploads.js --grep 'target folder does not exist' --no-bail`: passed after fix (1 passing).
- `./node_modules/.bin/mocha test/uploads.js`: passed (42 passing).
- `./node_modules/.bin/eslint src/controllers/admin/uploads.js test/uploads.js`: passed.
- `git diff --check`: passed.
- `npm test`: failed after 296 passing at `response status code should match one of the schema defined responses` in test/api.js:528. `GET /api/admin/extend/plugins` returned unexpected HTTP 500 because `https://packages.nodebb.org/api/v1/plugins` fetch failed in this offline environment. The suite uses bail and did not reach later tests; uploads file was run separately as above. A `sendmail-not-found` log also appeared, but was not the reported assertion failure.
