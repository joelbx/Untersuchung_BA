# Checkpoint

Task: implement the specified chat message edit, send, route, existence, and client behavior in /app. The feature title mentions DirectedGraph, but the concrete requirements and interface all concern chat messaging; investigation will follow those concrete requirements.

Initial state: `git status --short` showed only an existing untracked `appendonly.aof`. `rg` is unavailable (`/bin/bash: rg: command not found`), so local searches use `grep`/`find`.

Root cause: `Chats.messages.edit` is a stub, its PUT route is commented out, the client still calls the socket edit path, and `Messaging.messageExists` is absent. `editMessage` currently reads/writes `message:${mid}` without an existence check. The matching working patterns are `Topics.exists` (`db.exists`) and the v3 `Chats.post` controller using `formatApiResponse`. The socket send path uses `sockets.warnDeprecated`.

Reproduction: Added focused API/existence regression cases in `test/messaging.js`. Initial `./node_modules/.bin/mocha test/messaging.js` failed after 49 passing cases: `TypeError: Messaging.messageExists is not a function` at test/messaging.js:641. A first test attempt could not connect to Redis (`ECONNREFUSED 127.0.0.1:6379`); started the installed local `redis-server` with persistence disabled, then reran. Hypothesis: implementing the missing existence method and wiring the existing edit operation through the controller/route/client will satisfy the cases.

Implementation: added `Messaging.messageExists`, checked it in `editMessage`, implemented the v3 edit controller and PUT route, switched client edits to `api.put`, kept sends on `api.post` with the renamed `message` variable, added the English error string, and deprecated/validated the socket edit path.

Verification: `./node_modules/.bin/mocha test/messaging.js` passed: 74 tests. During verification, a literal translation assertion initially failed because `src/languages.js` reads the ignored `build/public/language/en-GB/error.json`, which was stale relative to the edited source file. Refreshed that local generated copy with `cp public/language/en-GB/error.json build/public/language/en-GB/error.json`, then reran successfully. `git diff --check` passed. `./node_modules/.bin/eslint src/messaging/index.js src/messaging/edit.js public/src/client/chats/messages.js test/messaging.js` passed. Linting all modified JS also reports existing errors in unfinished controller stubs, long preexisting commented routes, and unused imports in socket modules; no new lint finding on changed lines.
