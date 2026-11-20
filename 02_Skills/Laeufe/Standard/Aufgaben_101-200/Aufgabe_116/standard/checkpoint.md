# Checkpoint

Task: Add and enforce global `chat:privileged` permission, expose `canChat`, update i18n/OpenAPI, and run relevant local tests.

Status: Implemented and verified. The first test attempt, `./node_modules/.bin/mocha test/messaging.js --reporter dot --timeout 25000 --exit`, failed in global setup with `connect ECONNREFUSED 127.0.0.1:6379` because local Redis was not running; no assertions executed. Started a temporary local Redis instance and reran the suite. Final result: 77 passing. ESLint on changed JavaScript files, `git diff --check`, and local YAML/JSON parsing also passed.

Implementation: Global `chat:privileged` appears in privilege lists and English UI translations. `global.can` preserves boolean return for a string and returns booleans for an array. Chat middleware and messaging use the array check. `canMessageUser` requires `chat:privileged` for administrator or moderator targets and returns `[[error:no-privileges]]` when missing. The invitation path already calls `canMessageUser` for every UID. Profile data exposes `canChat`, documented in OpenAPI. Focused tests cover denial, grant, API invitation, and profile signal.
