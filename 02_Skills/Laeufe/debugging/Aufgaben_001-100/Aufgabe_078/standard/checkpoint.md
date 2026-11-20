# Checkpoint

Issue: voice broadcast liveness feedback.

Status: investigating existing playback, info, UI, and tests before editing implementation.

Root cause: `useVoiceBroadcastPlayback` computes a boolean solely from info state; `VoiceBroadcastHeader` renders the same red badge for all truthy values. `VoiceBroadcastPlayback` has no liveness value/event, so buffering, pause and stop transitions cannot update the badge. Existing playback events already suppress unchanged state/duration values.

Hypothesis: deriving a three-valued liveness from info and playback state, then emitting only on derived-value changes, will synchronize the badge through buffering/play/pause/stop and info transitions. Existing `setState`/`setInfoState` methods provide the appropriate update points.

Reproduction: focused Jest tests failed before implementation with `getLiveness is not a function` and `isLast is not a function` (exit 1). After implementation, model and utility tests pass; old playback-body snapshots fail because they mock playback state but use the real liveness getter. Aligning those fixtures with the mocked state.

Type check: `node_modules/.bin/tsc --noEmit --jsx react --pretty false` exited 2 with `src/utils/notifications.ts(79,80): error TS2554: Expected 1-2 arguments, but got 3.` This file is unchanged by this patch, so full type-check success is unavailable. No dependencies were downloaded.

Implemented: shared liveness union, badge grey style and header mapping, playback-derived liveness and change event, hook subscription, final-chunk check, boolean recording call-site mapping. Playback-body snapshots now reflect grey buffering/paused and no badge when stopped.

Verification: `node_modules/.bin/jest --runInBand --silent test/voice-broadcast` passed (24 suites, 215 tests, 15 snapshots). A final info pause/resume regression was then added and `node_modules/.bin/jest --runInBand --silent test/voice-broadcast/models/VoiceBroadcastPlayback-test.ts` passed (39 tests). Targeted ESLint, stylelint, and `git diff --check` passed. The full type check remains limited by the unrelated error above.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find`/`grep`.
