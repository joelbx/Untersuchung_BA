# Checkpoint

Task: merge consecutive room search results when their timelines overlap at a shared event and both contain a direct match; preserve event-level match highlighting and contextual rendering.

Progress: RoomSearchView now greedily combines adjacent results whose timelines overlap at the shared event. SearchResultTile renders the merged MatrixEvent timeline, highlights only the direct-match indices, initializes call groupers from the whole timeline, and links each match to its own event ID. Existing tile fixture updated for the changed props.

Verification: focused Jest suites passed (2 suites, 8 tests); TypeScript check passed. Prettier, ESLint, and diff whitespace checks are running/being finalized.
