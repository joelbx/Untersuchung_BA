# Checkpoint

Task: Resolve voice broadcast liveness mapping and playback update paths.

Status: Root cause confirmed by failing regression test. `updateLiveness()` combines info state with playback state and chunk position; `start()` buffering sets `grey` for a Resumed broadcast. It is also called from chunk arrival, seeking, and playback state changes. Existing `setLiveness()` already suppresses duplicate events.

Baseline regression: `node_modules/.bin/jest test/voice-broadcast/models/VoiceBroadcastPlayback-test.ts --runInBand --silent` exited 1: expected `live`, received `grey` in two new assertions (39 other tests passed).

`rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

Patch: Added `determineVoiceBroadcastLiveness` with Started/Resumed → live, Paused → grey, all other values → not-live. `VoiceBroadcastPlayback.setInfoState()` is now the sole liveness update path. Removed playback-state, seek, and chunk-triggered liveness updates. Added regression tests for mapping, unset initialization, lifecycle transitions, playback independence, and stable event emissions.

Verification:
- `node_modules/.bin/jest test/voice-broadcast/models/VoiceBroadcastPlayback-test.ts test/voice-broadcast/utils/determineVoiceBroadcastLiveness-test.ts --runInBand --silent`: exited 0; 2 suites, 50 tests passed.
- `node_modules/.bin/eslint src/voice-broadcast/models/VoiceBroadcastPlayback.ts src/voice-broadcast/utils/determineVoiceBroadcastLiveness.ts test/voice-broadcast/models/VoiceBroadcastPlayback-test.ts test/voice-broadcast/utils/determineVoiceBroadcastLiveness-test.ts && node_modules/.bin/prettier --check src/voice-broadcast/models/VoiceBroadcastPlayback.ts src/voice-broadcast/utils/determineVoiceBroadcastLiveness.ts test/voice-broadcast/models/VoiceBroadcastPlayback-test.ts test/voice-broadcast/utils/determineVoiceBroadcastLiveness-test.ts`: exited 0.
- `git diff --check`: exited 0.
- `node_modules/.bin/jest test/voice-broadcast --runInBand --silent`: stopped with Ctrl-C (exit 130) after becoming unusually slow. Completed suites shown in output passed; full directory result is unknown.
- `node_modules/.bin/tsc --noEmit --jsx react`: stopped with Ctrl-C (exit 130) after prolonged silence. Full project type-check result is unknown.
