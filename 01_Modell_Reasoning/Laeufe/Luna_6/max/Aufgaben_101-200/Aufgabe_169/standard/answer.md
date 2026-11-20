Implemented greedy merging for adjacent search results with matching overlap pivots. The merged tile receives the full timeline and adjusted match indexes; only direct matches are highlighted, and each match links to its own event ID.

Updated the existing tile test for the new props.

- Focused suites: **2 passed, 8 tests passed**
- `yarn lint:types`: **passed**
- Prettier and `git diff --check`: **passed**

Changed [RoomSearchView.tsx](/app/src/components/structures/RoomSearchView.tsx:215), [SearchResultTile.tsx](/app/src/components/views/rooms/SearchResultTile.tsx:31), and its existing test.