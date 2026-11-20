# Checkpoint

Issue: `SocketPosts.getUpvoters` exposes upvoter data without category read access.

Starting state: repository at `/app`; `git status --short` returned no changes. `rg` is unavailable, so local inspection uses `grep` and `find`.

Plan: inspect socket handler, privilege helpers, frontend caller, and tests; patch access checks and cutoff behavior; run relevant existing tests.

Implemented:
- `getUpvoters` resolves categories with `posts.getCidsByPids`, bulk-checks `topics:read` for non-administrators, rejects any unreadable or missing category before fetching votes, and allows administrators.
- The handler uses cutoff 6, resolves distinct visible UIDs in one lookup, preserves each post's UID order, and returns cutoff with each result.
- The frontend reads the server cutoff and enables HTML tooltips.
- Added isolated tests for mixed-category denial, missing category, administrator access, UID deduplication, truncation, and ordering.

Verification:
- `./node_modules/.bin/mocha test/posts-get-upvoters.js --no-config --reporter spec`: 4 passing.
- `./node_modules/.bin/eslint src/socket.io/posts/votes.js public/src/client/topic/votes.js test/posts-get-upvoters.js`: passed.
- `git diff --check` and `node --check` on the three changed JS files: passed.

The broader `test/posts.js` integration suite was not run: its database mock reads and prints `config.json`, which could expose credentials. This limits verification to the isolated handler suite and static checks.
