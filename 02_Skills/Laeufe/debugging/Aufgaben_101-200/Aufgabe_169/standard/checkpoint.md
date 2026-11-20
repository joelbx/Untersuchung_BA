# Search result merge checkpoint

Status: investigating root cause. The assigned systematic-debugging process requires a failing reproduction before the fix.

Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

Root cause: `RoomSearchView` loops through each SDK SearchResult and renders a separate tile. `SearchResultTile` reads one `context.getOurEventIndex()`, so it cannot distinguish multiple direct matches in a combined timeline. SDK `SearchResult.fromJson` provides timelines and direct-match indices; adjacent search results are displayed in chronological order by reversing the results array.

Hypothesis: accumulate adjacent timelines when the previous last event ID equals the next first event ID, append from index 1, and track each direct-match index with the adjusted offset. Render one tile per chain and derive per-event links in the tile.

Implementation: the view accumulates chronological result timelines while their boundary event IDs overlap, skips the duplicate pivot, and records direct-match indices with `offset + (nextOurEventIndex - 1)`. It flushes the chain at a gap or hidden result. The tile accepts the merged timeline and match indices, builds call event groupers from that timeline, highlights only direct matches, and links each direct match to its own event ID.

Verification: the new regression test failed before the fix with 4 result tiles instead of 2. After the fix, `./node_modules/.bin/jest test/components/structures/RoomSearchView-test.tsx test/components/views/rooms/SearchResultTile-test.tsx --runInBand --silent` passed (9 tests). `./node_modules/.bin/tsc --noEmit --jsx react`, targeted ESLint, and targeted Prettier checks passed. No dependencies were downloaded.
