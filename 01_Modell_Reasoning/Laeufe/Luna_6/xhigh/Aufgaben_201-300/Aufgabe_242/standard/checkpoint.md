# Checkpoint

Issue: Voice broadcast liveness must be derived solely from broadcast info state.

Completed:
- Added `determineVoiceBroadcastLiveness` with Started/Resumed → live, Paused → grey, and Stopped/unknown/undefined → not-live.
- Exported the utility and changed `VoiceBroadcastPlayback` so only `setInfoState` derives and sets liveness. Playback state, position, start, and chunk receipt no longer update it directly.
- Preserved deterministic initial `not-live` liveness and changed the stale resumed-broadcast expectation to `live`.

Verification:
- `jest --runInBand test/voice-broadcast/models/VoiceBroadcastPlayback-test.ts`: passed (40 tests).
- ESLint on changed source and test files: passed.
- `tsc --noEmit --jsx react`: reports five unrelated MatrixClient typing errors in `MatrixChat.tsx`, `clientInformation.ts`, and `DeviceListener-test.ts`; none are in changed files.
