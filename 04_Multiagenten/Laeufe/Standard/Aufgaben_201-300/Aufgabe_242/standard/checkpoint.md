Task: Fix voice broadcast playback liveness so it derives only from info state.
Status: Complete. Added determineVoiceBroadcastLiveness mapping and made setInfoState the sole liveness update path. Added mapping and playback regression tests.
Verification: 54 focused Jest tests passed; ESLint, Prettier, and git diff --check passed. Full TypeScript check reports five pre-existing errors in MatrixChat.tsx, clientInformation.ts, and DeviceListener-test.ts unrelated to these changes.
