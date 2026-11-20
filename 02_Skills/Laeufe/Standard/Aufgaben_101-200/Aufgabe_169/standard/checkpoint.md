# Search result timeline merge

Status: implementation complete. Adjacent search results whose timeline endpoints share an event ID now render as one timeline. Match indexes account for the skipped pivot; the tile highlights and links each matching event separately.

Verification:
- `./node_modules/.bin/jest --runInBand test/components/structures/RoomSearchView-test.tsx test/components/views/rooms/SearchResultTile-test.tsx --silent` — passed (9 tests).
- `./node_modules/.bin/tsc --noEmit --jsx react` — passed.
- `./node_modules/.bin/eslint src/components/structures/RoomSearchView.tsx src/components/views/rooms/SearchResultTile.tsx test/components/structures/RoomSearchView-test.tsx test/components/views/rooms/SearchResultTile-test.tsx` — passed.
- `./node_modules/.bin/prettier --check src/components/structures/RoomSearchView.tsx src/components/views/rooms/SearchResultTile.tsx test/components/structures/RoomSearchView-test.tsx test/components/views/rooms/SearchResultTile-test.tsx` — passed.
- `git diff --check` — passed.

Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep` for repository inspection.
