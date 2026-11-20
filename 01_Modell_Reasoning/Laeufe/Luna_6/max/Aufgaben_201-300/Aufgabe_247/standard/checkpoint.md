# Checkpoint

Task: enforce category read access in `SocketPosts.getUpvoters`, deduplicate user lookups, return a server cutoff, and update tooltip behavior.

Implemented:
- Non-admin callers are checked against every distinct category from `posts.getCidsByPids` using the bulk `topics:read` category filter; any unreadable category throws `[[error:no-privileges]]` before vote data is fetched.
- Upvoter UIDs are truncated to five per post, deduplicated across posts, resolved in one batch, and mapped back in original per-post order. Each result includes `cutoff: 6` and the remaining count.
- The frontend reads `cutoff` from each result and creates an HTML-enabled tooltip.

Verification:
- ESLint passed for both changed JavaScript files.
- `git diff --check` passed.
- `npm test -- --grep 'should get upvoters'` could not reach test execution because the test setup requires Redis at `127.0.0.1:6379`; the connection was refused.

Current changes are in `src/socket.io/posts/votes.js` and `public/src/client/topic/votes.js`.
