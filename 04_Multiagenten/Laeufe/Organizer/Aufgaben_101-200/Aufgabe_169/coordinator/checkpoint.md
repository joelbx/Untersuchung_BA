Task: Merge adjacent overlapping room search results into one timeline, preserving direct-match indices and per-event interactions.
Status: Complete. RoomSearchView greedily combines adjacent timelines at matching event IDs and renders only completed chains. SearchResultTile receives timeline plus match indices and links each match to its own event. Regression test covers a three-result chain and a separate result; existing call-event tile test uses the new props.
Verification: Targeted Jest suites passed (9 tests); TypeScript noEmit passed; targeted ESLint, Prettier, and git diff --check passed.
Delegation: None; solved locally.
