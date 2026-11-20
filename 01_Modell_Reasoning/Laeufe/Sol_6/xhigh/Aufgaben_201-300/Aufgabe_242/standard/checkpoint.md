# Voice broadcast liveness fix

Status: complete.

- Added `determineVoiceBroadcastLiveness` with Started/Resumed → live, Paused → grey, and all other states → not-live.
- `VoiceBroadcastPlayback.setInfoState` now owns liveness updates. Playback state, position, start, and chunk arrival no longer update it independently.
- Added utility and playback regression tests for state mapping, initial state, playback actions, first chunk, and stable event emissions.
- Verification: all 29 voice broadcast suites passed (278 tests, 35 snapshots); ESLint, Prettier, and `git diff --check` passed.
- Repository-wide TypeScript check still reports five errors in unrelated existing files: `MatrixChat.tsx`, `clientInformation.ts`, and `DeviceListener-test.ts`.
