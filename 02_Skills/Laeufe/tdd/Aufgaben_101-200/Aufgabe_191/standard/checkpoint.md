Task: Add stable and unstable registration token support to InteractiveAuth.

Plan: inspect local flow and tests; add a failing behavioral test; implement the stage; run focused and full existing tests.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); use `find` and `grep` for local searches.

Focused tests: `./node_modules/.bin/jest test/components/views/auth/InteractiveAuthEntryComponents-test.tsx --runInBand --silent` passed (7 tests). The first run failed because the registration token component was missing; after implementation a detached Enzyme mount prevented focus and was fixed by attaching the test mount to the document.

Type check: `./node_modules/.bin/tsc --noEmit --jsx react` failed with existing SlidingSync API type mismatches in `src/SlidingSyncManager.ts`, `src/components/views/rooms/RoomSublist.tsx`, `src/hooks/useSlidingSyncRoomSearch.ts`, `src/stores/room-list/SlidingRoomListStore.ts` and related tests. No diagnostics point to the changed auth files.

Full suite: `./node_modules/.bin/jest --runInBand --silent` completed with 367 passing suites and 6 failing suites (3443 passing tests, 16 failing). Failing suites: `test/SlidingSyncManager-test.ts` (`lists.map is not a function`), `test/components/views/messages/MLocationBody-test.tsx`, `test/stores/widgets/StopGapWidget-test.ts` (`No iframe supplied`), `test/components/views/location/SmartMarker-test.tsx`, `test/components/views/location/LocationViewDialog-test.tsx`, and `test/components/views/location/ZoomButtons-test.tsx`. The four location suites fail snapshots with an extra `Symbol(shapeMode): false`. Auth tests passed in the full suite.

Static checks: ESLint on changed TSX files, Prettier check on changed files, and `git diff --check` passed.
