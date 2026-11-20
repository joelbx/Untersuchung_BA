# Checkpoint

Implemented default adjacent search-result merging in `RoomSearchView.tsx`. Adjacent result timelines merge only when each has a direct match and the earlier timeline's last event ID equals the next timeline's first event ID. The shared pivot is skipped, and each direct match is recorded with `offset + (nextOurEventIndex - 1)`. Merged chains render as one tile; non-overlapping groups remain individual tiles.

`SearchResultTile.tsx` now receives `timeline: MatrixEvent[]` and `ourEventsIndexes: number[]`, initializes legacy call event groupers from the supplied timeline, treats only indexed events as matches, and makes each matching event's highlight link target its own event ID.

Validation: targeted Jest suites pass (2 suites, 9 tests); `yarn lint:types`, targeted ESLint, Prettier check, and `git diff --check` pass.
