# Checkpoint

Task: Fix voice broadcast liveness so it is determined only by `VoiceBroadcastInfoState`, with a centralized mapping utility and stable change events.

Completed: Added and exported `determineVoiceBroadcastLiveness`; playback updates liveness only in `setInfoState`; removed playback state, seek, and chunk-boundary liveness recalculation. Added mapping and playback tests, including unknown and undefined input behavior, initial unset state, live start/first-chunk behavior, and change-only emissions.

Verification: Focused Jest suites passed (2 suites, 47 tests); ESLint, Prettier, and `git diff --check` passed. `yarn lint:types` is blocked by existing `MatrixClient` API type errors in `src/components/structures/MatrixChat.tsx`, `src/utils/device/clientInformation.ts`, and `test/DeviceListener-test.ts`; no changed file appeared in those diagnostics.
