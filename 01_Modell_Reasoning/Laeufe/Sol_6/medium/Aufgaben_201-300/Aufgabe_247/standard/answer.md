Fixed `SocketPosts.getUpvoters` to check `topics:read` across every category associated with the supplied post IDs before returning data. Administrators bypass category restrictions. The method now resolves deduplicated upvoter IDs in one lookup, preserves display order, and returns `cutoff: 6`.

The [frontend tooltip](/app/public/src/client/topic/votes.js) uses the server’s cutoff and supports HTML content. Added [tests](/app/test/posts.js) for mixed-category denial, administrator access, truncation, ordering, and deduplication.

Verification: all 12 voting tests pass; ESLint and `git diff --check` pass.