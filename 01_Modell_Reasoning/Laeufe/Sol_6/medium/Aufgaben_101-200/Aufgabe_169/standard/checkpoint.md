# Checkpoint

Task: Merge adjacent overlapping room search results into one timeline, preserve direct-match indexes and event targets, and run relevant existing tests.
Status: Complete.
Changes: RoomSearchView greedily combines adjacent results at matching event_id boundaries without mutating SearchResult.context timelines. SearchResultTile receives the merged timeline and direct-match indexes, rebuilds call groupers when its timeline changes, and links each matched event to its own event_id. Added regression coverage for a three-result chain and a separate result.
Verification: Focused Jest suites passed (9 tests); TypeScript type check passed; ESLint on changed files passed; git diff --check passed.
