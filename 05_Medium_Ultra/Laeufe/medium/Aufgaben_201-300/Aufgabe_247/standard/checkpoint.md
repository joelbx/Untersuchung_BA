# Checkpoint

Resolved `SocketPosts.getUpvoters` exposure. Non-admin callers now require `topics:read` for every category returned by `posts.getCidsByPids` before vote data is read; admins bypass category restrictions. Visible upvoter UIDs are deduplicated for one username lookup while preserving each post's UID order. Responses include cutoff 6, show at most 5 usernames, and include `otherCount`. The tooltip uses the response cutoff and enables HTML.

Added integration coverage for restricted single and mixed-category requests, admin access, truncation, ordering, and deduplicated lookup.

Verification: `test/posts.js` passed (127 passing) with temporary local Redis; ESLint passed on changed JavaScript files; `git diff --check` passed.
