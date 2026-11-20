# Checkpoint

Issue: Merge adjacent room search results when their context timelines overlap at a shared event and both results have direct query matches. Pass merged timelines and match indices to the tile so events retain chronological context and matched events remain correctly highlighted.

Progress: Inspected `RoomSearchView`, `SearchResultTile`, the SDK `SearchResult`/`EventContext` model, and their existing tests. Implemented adjacent overlap merging with the required skipped-pivot match-index calculation, changed the tile to take the timeline and direct-match indices, preserved the prior contextual link behavior, and updated the existing tile test fixture for the prop change.

Validation: The existing room search and result tile Jest suites pass (8 tests); the full TypeScript check, ESLint, Prettier, and `git diff --check` pass.

Constraints: Work only from checked-out repository files and existing tests. Do not alter git history, the index baseline, or harness configuration.
