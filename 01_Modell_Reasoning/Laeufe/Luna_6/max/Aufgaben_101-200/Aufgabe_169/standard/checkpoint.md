# Checkpoint

Task: merge adjacent room search results whose timelines overlap at the same event and whose results each contain a direct query match.

Implemented: `RoomSearchView` now greedily accumulates adjacent overlapping result timelines, skips each duplicate pivot, adjusts each direct-match index, and renders one tile for each chain. `SearchResultTile` now consumes the merged `MatrixEvent[]` and match indexes, groups call events across the full timeline, and highlights/links only direct matches using each event's own ID. Updated the existing tile test to the new props.

Verification: focused RoomSearchView and SearchResultTile suites passed (8 tests); `yarn lint:types` passed. Formatting and whitespace checks are clean.
