# Checkpoint

- Task: merge adjacent room search results whose context timelines overlap at a matching event ID, preserving each direct match for highlighting and navigation.
- Repository: `/app`; working tree initially clean.
- Implemented greedy overlap merging in `RoomSearchView`, skipping the shared boundary event and recording every direct-match index.
- `SearchResultTile` now receives the merged timeline and match indices, builds call groupers from that timeline, and links each matched event to its own event ID.
- Added coverage for a three-result chain, a separate result, and a call event at an overlap boundary; updated the existing tile test for the new props.
- Verification: 10 search tests passed; TypeScript, ESLint, Prettier, and `git diff --check` passed.
