# Voice broadcast liveness fix

- Goal: derive playback liveness from `VoiceBroadcastInfoState` with one mapping utility and update it only through `setInfoState`.
- Repository inspected: `/app`; working tree initially clean. Existing playback model and tests are under `src/voice-broadcast` and `test/voice-broadcast`.
- Implemented `determineVoiceBroadcastLiveness` with Started/Resumed → live, Paused → grey, and Stopped/unknown/undefined → not-live. Playback now sets liveness only in `setInfoState`; unknown info events reach that mapping. Info state listeners observe the updated liveness.
- Added regression coverage for initial liveness, start and first chunk behavior, info state transitions, unknown and missing states, and stable liveness event emissions.
- Verification: all 29 `test/voice-broadcast` Jest suites passed (282 tests, 35 snapshots). ESLint and Prettier passed on changed code. Repository-wide `tsc --noEmit --jsx react` still reports five unrelated MatrixClient method errors in `MatrixChat.tsx`, `clientInformation.ts`, and `DeviceListener-test.ts`.
