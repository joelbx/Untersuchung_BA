# Checkpoint

Issue: `SocketPosts.getUpvoters` needs category read authorization across every supplied post, deduplicated username resolution, six-person cutoff response, and frontend response-driven tooltip formatting with HTML enabled.

Initial inspection: implementation in `src/socket.io/posts/votes.js`; frontend in `public/src/client/topic/votes.js`; integration tests in `test/posts.js`. Existing implementation has no read check, performs per-post username lookups, and frontend hardcodes six.

Plan: add failing integration coverage for unreadable categories and cutoff/ordering; implement the minimal backend and frontend changes; run focused and project tests. No external research or downloads.

Implementation: `getUpvoters` resolves all category IDs, rejects non-admin callers if bulk `topics:read` filtering excludes any category, then fetches votes. It displays at most five names per post, resolves distinct displayed UIDs in one lookup, preserves per-post UID order, and returns `cutoff: 6` plus `otherCount`. Tooltip uses response cutoff and enables HTML.

Verification:
- RED: `./node_modules/.bin/mocha test/posts.js --grep 'should upvote a post|should get upvoters|upvoters when any|administrators to see upvoters|five ordered usernames|resolves each displayed' --no-bail` failed on missing denial, cutoff, and repeated username lookups; existing admin case passed.
- RED: `./node_modules/.bin/mocha test/topic-votes-tooltip.js --no-bail` failed with title `translated` rather than `A, B, C, D, E` when response cutoff is 8.
- GREEN: focused posts and tooltip run: 7 passing.
- `./node_modules/.bin/mocha test/posts.js test/topic-votes-tooltip.js`: 130 passing, exit 0. Existing deprecation and unsupported test image warnings appeared.
- `./node_modules/.bin/eslint src/socket.io/posts/votes.js public/src/client/topic/votes.js test/posts.js test/topic-votes-tooltip.js`: exit 0.
- `git diff --check`: exit 0.
- `npm test`: exit 1, 194 passing, 1 failing. Failure: `response status code should match one of the schema defined responses` in `test/api.js` at line 529; `GET /api/admin/extend/plugins` returned 500 after a proxy tunnel failed with HTTP 403. Full-suite completion remains uncertain due to this external dependency; no download attempted.

Environment: Initial focused test command failed before tests with `connect ECONNREFUSED 127.0.0.1:6379`. Started locally available Redis with `redis-server --port 6379 --save '' --appendonly no --daemonize yes`; focused checks then ran.
