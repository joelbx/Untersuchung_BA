# Checkpoint

Task: Fix `SocketPosts.getUpvoters` read-permission enforcement, user-ID deduplication and ordering, server-defined cutoff handling, and frontend tooltip HTML support.

Implemented:
- Resolve all category IDs from the requested post IDs and bulk-check `topics:read` for non-administrators; reject the full request with `[[error:no-privileges]]` if any category is unreadable.
- Deduplicate UIDs across the response before username resolution and preserve each post's UID appearance order when constructing its list.
- Return `cutoff: 6`, show at most five usernames, and report the rest as `otherCount`.
- Have the frontend use the returned cutoff and enable HTML tooltip content.

Verification:
- ESLint passed for the changed backend and frontend JavaScript files.
- `mocha test/posts.js` could not run because Redis was unavailable at `127.0.0.1:6379` (suite failed in its before-all hook).
