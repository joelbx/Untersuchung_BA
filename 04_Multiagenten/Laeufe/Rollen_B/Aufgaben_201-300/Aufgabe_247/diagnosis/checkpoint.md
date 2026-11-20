# Fault localization checkpoint

Located `SocketPosts.getUpvoters` in `src/socket.io/posts/votes.js`. It fetches vote UIDs before any authorization, does one username lookup per post, and truncates only when count is greater than 6. The tooltip in `public/src/client/topic/votes.js` hardcodes 6 and omits `html: true`.

`posts.getCidsByPids` resolves post category IDs. `privileges.categories.isUserAllowedTo('topics:read', cids, uid)` returns an array for bulk checks; the caller must require every result true. `user.isAdministrator(uid)` is the existing admin bypass helper. Existing `test/posts.js` covers an authorized single post only. Source and tests unchanged.
