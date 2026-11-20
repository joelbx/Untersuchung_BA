# Checkpoint

Implemented consecutive search result merging in RoomSearchView. Overlapping context timelines are combined at their shared event, duplicate pivot events are skipped, and direct match indices are passed to SearchResultTile. The tile renders merged timeline events and highlights only indexed matches. Updated the existing SearchResultTile test for the new props.

Verification: focused Jest test passes; ESLint passes; `tsc --noEmit --jsx react` passes; `git diff --check` passes.
