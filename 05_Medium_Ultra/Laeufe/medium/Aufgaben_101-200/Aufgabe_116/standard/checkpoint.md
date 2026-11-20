# Checkpoint

Implemented global `chat:privileged` permission, array support in `privileges.global.can`, consistent chat gates, privileged-target rejection in `messaging.canMessageUser`, profile API `canChat`, OpenAPI schema, and English privilege label.

Verification: `./node_modules/.bin/mocha test/messaging.js` (79 passing); ESLint on changed JavaScript files; `git diff --check`.
