# Checkpoint

Task: prevent overlapping topic creation requests from one actor from creating duplicates.

Status: investigating root cause and test path. No code changes yet.

Root cause: `src/controllers/write/topics.js` invokes asynchronous `api.topics.create` directly. No actor-scoped in-flight state exists at this boundary. The API path awaits blacklist/queue/topic persistence, allowing another request to enter before the first finishes. Existing `setupApiRoute` maps controller exceptions to HTTP 400 and `status.code=bad-request`.

Pattern/hypothesis: acquire a synchronous actor key before the first await in create and reply, release it in `finally`. A second overlapping request then throws while a distinct actor remains independent. The isolated controller regression test was executed before the fix and failed: one create remained pending instead of rejecting; a reply was also accepted during an active create.

Implementation: `Topics.lockPosting(req, error)` synchronously reserves `posting<uid-or-sessionID>` in a Set. Create and reply acquire before entering the async API call and release in `finally`, including failures. The route helper maps a thrown lock error to HTTP 400 with `status.code=bad-request`; successful creates retain the 200 `ok` path.

Verification:
- `./node_modules/.bin/mocha --no-config --no-package test/controllers-write-topics-lock.js --reporter spec`: 3 passing, exit 0.
- `./node_modules/.bin/eslint src/controllers/write/topics.js test/controllers-write-topics-lock.js`: exit 0.
- `git diff --check`: exit 0.
- `./node_modules/.bin/mocha --no-config --no-package test/api.js --reporter spec`: blocked in root before hook, `Error: connect ECONNREFUSED 127.0.0.1:6379` (test Redis unavailable); process was stopped after repeated connection errors. HTTP integration behavior and persisted counters remain unverified locally.
- `./node_modules/.bin/mocha --no-config --no-package test/controllers.js --reporter spec`: same before-hook Redis connection error; process was stopped after repeated connection errors.
