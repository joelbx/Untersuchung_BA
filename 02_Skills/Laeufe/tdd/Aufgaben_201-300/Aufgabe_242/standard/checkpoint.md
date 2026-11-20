# Checkpoint

Issue: derive voice broadcast playback liveness from broadcast info state.

Progress: added state-to-liveness utility; playback now updates liveness only in `setInfoState`. Added mapping and playback regression tests. `rg` is unavailable; used local `find`.

Verification:
- `./node_modules/.bin/jest --runInBand test/voice-broadcast/models/VoiceBroadcastPlayback-test.ts test/voice-broadcast/utils/determineVoiceBroadcastLiveness-test.ts`: 48 tests passed. Before implementation, playback tests failed with expected `live`, received `grey`; utility test failed because module was absent.
- `./node_modules/.bin/prettier --check src/voice-broadcast/models/VoiceBroadcastPlayback.ts src/voice-broadcast/utils/determineVoiceBroadcastLiveness.ts test/voice-broadcast/models/VoiceBroadcastPlayback-test.ts test/voice-broadcast/utils/determineVoiceBroadcastLiveness-test.ts`: passed.
- `./node_modules/.bin/jest --runInBand --silent`: aborted before a suite summary with `TypeError: Cannot read properties of null (reading 'createEvent')` in `react-dom/cjs/react-dom.development.js:3905` while processing `@matrix-org/matrix-wysiwyg`. Whether all remaining suites pass is unknown.
- `./node_modules/.bin/tsc --noEmit --jsx react`: failed on existing MatrixClient type mismatches in `src/components/structures/MatrixChat.tsx`, `src/utils/device/clientInformation.ts`, and `test/DeviceListener-test.ts`; no errors reported in changed files.
- `./node_modules/.bin/jest --runInBand test/voice-broadcast`: 29 suites, 258 tests, and 35 snapshots passed. The run printed existing Browserslist, deprecation, listener, and console warnings.
- `./node_modules/.bin/eslint --max-warnings 0 src/voice-broadcast/models/VoiceBroadcastPlayback.ts src/voice-broadcast/utils/determineVoiceBroadcastLiveness.ts test/voice-broadcast/models/VoiceBroadcastPlayback-test.ts test/voice-broadcast/utils/determineVoiceBroadcastLiveness-test.ts`: passed.
- `git diff --check`: passed.
