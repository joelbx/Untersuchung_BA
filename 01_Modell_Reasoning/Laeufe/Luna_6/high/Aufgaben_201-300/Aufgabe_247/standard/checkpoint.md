# Checkpoint

Implemented `SocketPosts.getUpvoters` category read checks for all distinct post categories (administrators bypass the check), rejects unreadable requests with `[[error:no-privileges]]`, batches username resolution over deduplicated voter UIDs, and preserves voter order while returning five explicit usernames plus `otherCount` and `cutoff: 6`.

Updated the topic vote tooltip to use the cutoff supplied in the response and enable HTML content.

Validation: ESLint passed for both changed JavaScript files; `git diff --check` passed. The existing `npx mocha test/posts.js` suite could not start because Redis was unavailable at `127.0.0.1:6379` (`ECONNREFUSED`).
