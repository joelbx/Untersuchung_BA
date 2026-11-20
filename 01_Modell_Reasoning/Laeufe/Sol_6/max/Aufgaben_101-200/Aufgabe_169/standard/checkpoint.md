# Checkpoint

- Task: merge adjacent overlapping room search results into a single timeline and preserve direct-match highlighting and event links.
- Initial state: clean working tree; located `RoomSearchView.tsx`, `SearchResultTile.tsx`, and existing tile tests.
- Implemented greedy timeline merging in `RoomSearchView.tsx`, with one tile per overlap chain and exact direct-match indices.
- Updated `SearchResultTile.tsx` to render merged timelines, highlight only direct matches, and link each matched message to its own event ID.
- Updated existing search tests to cover multi-result chains, non-overlapping results, pivot matches, and `m.call.*` overlaps.
- Verification: 11 relevant Jest tests passed; TypeScript, ESLint, Prettier, and `git diff --check` passed.
