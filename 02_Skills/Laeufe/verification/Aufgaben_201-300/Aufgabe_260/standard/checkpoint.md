# Checkpoint

Task: restrict request-originated SSE events to other sessions of the same user, propagate a client UUID, and update the broker/queue APIs.

Status: implementation edited. `rg` is unavailable (`/bin/bash: rg: command not found`); using `find` and `grep`.

Changes: request client ID context, header/cookie middleware, UI UUID header, context-aware broker filtering, request/background event contexts, queue rename, and focused tests.

Verification:
- `GOPROXY=off GOFLAGS=-mod=readonly go test ./server/events ./server ./server/subsonic ./scanner ./model/request` exited 0. The taglib C++ dependency emitted a deprecation warning.
- `CI=true npm test -- --watchAll=false --runInBand` in `ui` exited 0: 11 suites, 41 tests.
- `./node_modules/.bin/prettier -c src/clientUniqueId.js src/dataProvider/httpClient.js src/authProvider.js && npm run lint` in `ui` exited 0.
- `git diff --check` exited 0.
