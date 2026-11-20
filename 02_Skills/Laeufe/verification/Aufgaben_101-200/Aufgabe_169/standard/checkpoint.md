# Checkpoint

Task: merge adjacent overlapping room search results into one timeline.

Implemented in RoomSearchView and SearchResultTile. Adjacent results with matching boundary event IDs are merged greedily; the shared pivot is skipped, direct match indices are tracked, and each event links to its own event ID. The tile builds legacy call groupers from the merged timeline. Added a regression test for a three-result chain plus a separate result and updated the call-event tile test for the new props.

Verification (final run):
- `./node_modules/.bin/jest --runInBand test/components/structures/RoomSearchView-test.tsx test/components/views/rooms/SearchResultTile-test.tsx --silent`: exit 0, 2 suites and 9 tests passed.
- `./node_modules/.bin/tsc --noEmit --jsx react --pretty false`: exit 0.
- ESLint on four changed files, Prettier check on four changed files, and `git diff --check`: exit 0.

Initial test runs found fixture assertion and type errors; those were corrected before the final successful checks.
