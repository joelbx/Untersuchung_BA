# Checkpoint

Task: combine adjacent overlapping room search results into one timeline and preserve match highlighting and event links.
Status: complete.
Changes: RoomSearchView greedily merges adjacent contexts at matching event IDs, skips the shared pivot, and records each direct-match index. SearchResultTile renders the merged timeline, highlights only direct matches, links each event to its own ID, and refreshes call groupers when the timeline changes. Existing tests were updated and new tests cover three-result chains, separate results, and call-event overlap.
Validation: 10 focused tests passed; TypeScript, ESLint, Prettier, and git diff --check passed.
