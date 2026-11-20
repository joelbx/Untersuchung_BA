# Checkpoint

Task: resolve voice broadcast liveness feedback.

Implemented: unified `VoiceBroadcastLiveness` type; playback liveness from playback and info state with change-only events; hook and header propagation; grey badge styling; `VoiceBroadcastChunkEvents.isLast`; updated recording call sites and focused tests/snapshots.

Verification:
- `./node_modules/.bin/jest --runInBand test/voice-broadcast` exited 0: 24 suites, 214 tests, 15 snapshots passed.
- Targeted ESLint on changed TypeScript files exited 0.
- `./node_modules/.bin/stylelint res/css/voice-broadcast/atoms/_LiveBadge.pcss` exited 0.
- `git diff --check` exited 0.
- `./node_modules/.bin/tsc --noEmit --jsx react` exited 2: `src/utils/notifications.ts(79,80): error TS2554: Expected 1-2 arguments, but got 3.` That file was untouched; complete repository type checking remains blocked by this error.
