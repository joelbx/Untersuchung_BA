# Checkpoint

Task: Fix voice broadcast liveness so it is derived only from broadcast info state, with the requested exact mapping and stable liveness events.

Completed:
- Added `determineVoiceBroadcastLiveness` and exported it from the voice broadcast module.
- Changed playback liveness to update only in `setInfoState`, retaining change-only emissions in `setLiveness`.
- Removed liveness changes from playback state, playback position, start, and chunk arrival behavior.
- Updated the existing Resumed playback expectation to Live.

Verification: `yarn test --runInBand test/voice-broadcast/models/VoiceBroadcastPlayback-test.ts` passed (40 tests).
