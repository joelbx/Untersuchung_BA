# Debugging checkpoint

Task: restrict `SocketPosts.getUpvoters` by category read privileges, preserve ordered truncated results, and update the frontend tooltip.

Status: investigation started. `rg` is unavailable in this environment (`/bin/bash: rg: command not found`); using local `grep`/`find` instead.

Root cause: `SocketPosts.getUpvoters` fetches vote UIDs and resolves usernames without checking category read privileges. Its per-post username lookups also repeat UIDs across posts. The frontend hardcodes the cutoff and creates a plain-text tooltip.

Pattern: `posts.getCidsByPids` resolves each post's category; `privileges.categories.isUserAllowedTo('topics:read', cids, uid)` checks an array of categories, while `user.isAdministrator` supplies the administrator exception. `user.getUsernamesByUids` preserves input ordering.

Hypothesis: checking every resolved category before fetching vote data blocks the leak; resolving the unique UIDs from the truncated lists once preserves ordering through a UID-to-name mapping.

Pre-fix reproduction: `node test/socket-posts-upvoters-unit.js` fails with `Missing expected rejection`, confirming the guest leak. Integration command `./node_modules/.bin/mocha test/posts.js --grep 'should require read access to every supplied post category' --timeout 25000` cannot start: `Error: connect ECONNREFUSED 127.0.0.1:6379` in the root before hook. Its outcome remains unverified until Redis is available.

Implementation: `getUpvoters` checks all post categories before fetching vote UIDs, exempts administrators, resolves usernames once for unique visible UIDs, and returns `cutoff: 6` with ordered usernames and an `otherCount`. The frontend uses the returned cutoff and enables HTML tooltips.

Verification: a temporary local Redis instance allowed the integration check to run. The focused permission test passed. Running only `should get upvoters` alongside the new test failed because that existing test requires the earlier `should upvote a post` setup; the complete voting suite in normal order passed (11 tests). `node test/socket-posts-upvoters-unit.js`, ESLint on all changed JS files, and `git diff --check` passed. No remaining test uncertainty for these paths.
