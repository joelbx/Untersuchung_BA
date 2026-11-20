# Checkpoint

- Task: prevent overlapping topic creation requests by one actor from creating duplicate topics.
- Applying test-driven development: inspect existing route and tests, add a failing regression, then implement and verify.
- Local search tool `rg` is unavailable (`/bin/bash: rg: command not found`); using `grep`/`find`.
- RED: `./node_modules/.bin/mocha test/topics.js --grep "should accept only one overlapping topic creation" --bail` initially could not connect to local Redis (`connect ECONNREFUSED 127.0.0.1:6379`). Started the installed local Redis server without persistence, reran, and observed the expected failure: 10 successes instead of 1.
- GREEN: the same regression passes after adding an actor posting lock around create/reply. The test checks HTTP status, JSON status code, category topic count and global topic count.
- `./node_modules/.bin/mocha test/topics.js`: 230 passing. The targeted regression was rerun after the final test formatting change and passed.
- `./node_modules/.bin/eslint src/controllers/write/topics.js test/topics.js`: passed. `git diff --check`: passed.
- `npm test`: 1028 passing, 1 failing. Failure: `Admin Controllers` → `should load /admin/extend/plugins` at `test/controllers-admin.js:249`, expected `body.installed` to exist. This is outside the changed route; the full suite therefore did not complete green. Existing plugin warnings and export-profile child process error also appeared in the output.
