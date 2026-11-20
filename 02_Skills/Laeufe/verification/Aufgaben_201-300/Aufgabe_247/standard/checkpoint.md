# Checkpoint

Issue: restrict SocketPosts.getUpvoters by read privilege for every associated category, deduplicate UIDs, return cutoff-based display data, and update frontend tooltip.

Initial inspection: `rg` is unavailable (`/bin/bash: rg: command not found`); using grep/find locally. No tests run yet.

Existing test attempt: `./node_modules/.bin/mocha test/posts.js --grep 'should get upvoters' --reporter spec` failed in the root before-all hook with `Error: connect ECONNREFUSED 127.0.0.1:6379` (0 passing, 1 failing). The Redis-backed integration suite remains unverified. Proceeding with isolated local tests.

Final local verification:
- `./node_modules/.bin/mocha test/socket-posts-upvoters.js --reporter spec`: 3 passing, exit 0.
- `./node_modules/.bin/eslint src/socket.io/posts/votes.js public/src/client/topic/votes.js test/socket-posts-upvoters.js`: exit 0.
- `git diff --check && node --check src/socket.io/posts/votes.js && node --check public/src/client/topic/votes.js && node --check test/socket-posts-upvoters.js`: exit 0.

Redis-backed integration test remains unverified due to unavailable local Redis service. The isolated test uses stubbed dependencies, so it does not prove real database integration.
