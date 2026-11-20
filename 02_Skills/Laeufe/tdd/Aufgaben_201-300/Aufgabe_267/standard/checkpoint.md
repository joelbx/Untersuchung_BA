# Checkpoint

Task: repair RoomView initial load signaling, widget room options, and initial event focus.
Approach: follow assigned TDD workflow; add a focused failing test before implementation, then run relevant and full existing tests.
Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); using `find` and `grep`.

Implemented: `Action.RoomLoaded`, dispatch from `RoomView.onRoomLoaded`, store handler `setViewRoomOpts`, and nullish initial-event fallback. Focused regressions were observed failing before the patch and passing afterward. Relevant suites: `./node_modules/.bin/jest --runInBand test/stores/RoomViewStore-test.ts test/components/structures/RoomView-test.tsx --silent --forceExit` passed (65 tests). Full Jest suite and TypeScript check are running.

Verification obstacle: `./node_modules/.bin/tsc --noEmit --jsx react` reached Node's default ~2 GB heap and emitted `FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory`; type correctness remains unverified by that command. Full Jest run so far shows failures in `test/Lifecycle-test.ts` (OIDC native-flow tokenRefreshFunction expected but undefined) and `test/components/views/rooms/wysiwyg_composer/components/WysiwygComposer-test.tsx` (disabled contentEditable test exceeded 5000 ms). Neither file was edited.

Full suite result: `./node_modules/.bin/jest --runInBand --silent --forceExit` finished with 511 passed / 10 failed suites, 5148 passed / 18 failed tests, 625 passed / 1 failed snapshots. Failing suites: `test/Lifecycle-test.ts`, `test/components/views/rooms/wysiwyg_composer/components/WysiwygComposer-test.tsx`, `test/utils/AutoDiscoveryUtils-test.tsx`, `test/utils/DateUtils-test.ts`, `test/components/views/dialogs/ServerPickerDialog-test.tsx`, `test/stores/widgets/StopGapWidget-test.ts`, `test/components/structures/ThreadView-test.tsx`, `test/utils/oidc/registerClient-test.ts`, `test/utils/oidc/TokenRefresher-test.ts`, `test/components/views/elements/SpellCheckLanguagesDropdown-test.tsx`. The two edited suites passed within that run. Changed-file ESLint, Prettier, and `git diff --check` passed. A 4 GB heap TypeScript run is in progress.

Final TypeScript check: `NODE_OPTIONS=--max-old-space-size=4096 ./node_modules/.bin/tsc --noEmit --jsx react` completed with exit code 2 and 19 errors outside edited files, primarily matrix-js-sdk/OIDC API mismatches, plus existing TabbedView implicit-any errors. No errors were reported in the edited files; the repository type check remains failing.
