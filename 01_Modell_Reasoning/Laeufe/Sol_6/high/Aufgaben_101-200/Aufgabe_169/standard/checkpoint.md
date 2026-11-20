Task: Merge overlapping adjacent room search result timelines, tracking each direct match for highlighting.
Status: Complete. RoomSearchView accumulates adjacent timelines at a shared event ID and renders one SearchResultTile per chain. SearchResultTile uses merged timeline and match indices, preserving per-event links and call grouping.
Verification: 10 focused Jest tests passed; TypeScript type check, ESLint, Prettier, and git diff --check passed.
