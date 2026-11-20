Task: implement internal API token lifecycle utilities in src/api/utils.js.
Status: complete. Added generation, list/get, update/delete, usage logging and last-seen lookup with the three sorted indexes. Authentication accepts utility-generated tokens while retaining legacy settings tokens.
Verification: eslint passed on changed JavaScript files; focused Mocha run passed 7 tests (test/api-tokens.js and authentication API token cases) using temporary local Redis. git diff --check passed.
Constraints observed: local code/tests only; no git history, index baseline, or harness configuration changes.
