Task: Restrict SocketPosts.getUpvoters by category read privileges, preserve ordered truncated usernames, and update the frontend tooltip and cutoff handling.

Progress: Implemented bulk category read checks with administrator bypass, shared username lookup with stable post order, cutoff response metadata, and HTML tooltips. Added integration tests for restricted categories, administrator access, deduplication, ordering, and the cutoff boundary. Verification: ESLint and git diff --check pass; test/posts.js passes (127 tests). Temporary local Redis was stopped after testing.
