# Checkpoint

Task: Fix voice broadcast liveness state, events, and badge rendering.
Status: implementation complete; targeted tests pass; repository-wide checks have unrelated failures listed below.
Constraints: local repository only; no downloads; no history/index/harness changes.

Implementation: liveness type, model state and change event, hook subscription, badge styling and callers, final-chunk helper. Focused tests passed. Voice broadcast suite initially failed only due playback body snapshots using mocked states without matching liveness; fixtures and snapshots updated.
Type check attempted: `./node_modules/.bin/tsc --noEmit --jsx react` exited 2 with `src/utils/notifications.ts(79,80): error TS2554: Expected 1-2 arguments, but got 3.` This is outside changed files; type-check status remains uncertain for the repository.

Final verification:
- `./node_modules/.bin/jest --runInBand test/voice-broadcast --silent`: 24 suites, 218 tests, 15 snapshots passed (before two additional model assertions). `./node_modules/.bin/jest --runInBand test/voice-broadcast/models/VoiceBroadcastPlayback-test.ts --silent`: 44 tests passed after those assertions.
- Final `./node_modules/.bin/jest --runInBand test/voice-broadcast --silent`: 24 suites, 220 tests, 15 snapshots passed.
- ESLint on changed TS/TSX files, Stylelint on the badge CSS, and `git diff --check` passed.
- `./node_modules/.bin/jest --runInBand --silent`: 8 suites failed, 322 passed, 1 skipped; 10 tests failed, 2971 passed, 39 skipped, 2 todo. Failed suites: RoomView-test.tsx (video room unread chat panel), BeaconMarker-test.tsx (snapshot), MLocationBody-test.tsx (snapshot), LocationViewDialog-test.tsx (snapshot), ZoomButtons-test.tsx (snapshot), StopGapWidget-test.ts (two tests, `No iframe supplied`), BeaconStatus-test.tsx (snapshot), SmartMarker-test.tsx (two snapshots). Seven snapshot failures show added Symbol(shapeMode) in unrelated map/beacon objects. `--onlyFailures` rerun reproduced all 8 suites and 10 failures. No voice-broadcast suite failed.
