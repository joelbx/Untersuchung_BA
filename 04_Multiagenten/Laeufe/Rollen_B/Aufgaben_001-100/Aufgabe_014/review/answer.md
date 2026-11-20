VERDICT: FIX

- **Code defect:** The merge modal’s outer search dropdown uses `w-100`, but [merge.js](/app/public/src/client/topic/merge.js:41) still limits the results list to 400px. Set the results width to match the input.
- **Code defect:** Each notification load adds another `.mark-all-read` handler in [notifications.js](/app/public/src/modules/notifications.js:72). Bind it once or remove the previous handler so one click sends one request.
- **TEST_ENVIRONMENT_PROBLEM:** `timeout 90s ./node_modules/.bin/mocha test/database/hash.js test/notifications.js --reporter spec` was attempted with output filtered to avoid printing configuration. It stopped in the root setup hook: **0 passing, 1 failing**, `ECONNREFUSED 127.0.0.1:6379`. Start the configured test Redis service and rerun it.
- `./node_modules/.bin/eslint public/src/client/header/notifications.js public/src/client/topic/fork.js public/src/client/topic/move.js public/src/modules/notifications.js public/src/modules/search.js src/database/mongo/hash.js src/database/redis/hash.js src/emailer.js src/install.js src/routes/index.js test/database/hash.js` exited 0.

I recorded the review in [checkpoint.md](/app/.codex-role-output/checkpoint.md).