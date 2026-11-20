# Checkpoint

Task: align voice broadcast playback liveness with broadcast info state.
Status: patch complete.

Changes:
- Added `determineVoiceBroadcastLiveness` with Started/Resumed → live, Paused → grey, and Stopped/unknown/undefined → not-live.
- `VoiceBroadcastPlayback.setInfoState` now provides the only liveness update. Playback state, position, and chunk arrival no longer update it.
- Updated playback tests and added mapping and event-emission coverage.

Checks:
- PASS: `./node_modules/.bin/jest --runInBand test/voice-broadcast/models/VoiceBroadcastPlayback-test.ts test/voice-broadcast/utils/determineVoiceBroadcastLiveness-test.ts` (52 tests).
- PASS: `./node_modules/.bin/eslint src/voice-broadcast/models/VoiceBroadcastPlayback.ts src/voice-broadcast/utils/determineVoiceBroadcastLiveness.ts test/voice-broadcast/models/VoiceBroadcastPlayback-test.ts test/voice-broadcast/utils/determineVoiceBroadcastLiveness-test.ts`.
- PASS: `./node_modules/.bin/prettier --check src/voice-broadcast/models/VoiceBroadcastPlayback.ts src/voice-broadcast/utils/determineVoiceBroadcastLiveness.ts test/voice-broadcast/models/VoiceBroadcastPlayback-test.ts test/voice-broadcast/utils/determineVoiceBroadcastLiveness-test.ts`.
- PASS: `git diff --check`.
- FAIL (unrelated files): `./node_modules/.bin/tsc --noEmit --jsx react` exited 2. Errors: `src/components/structures/MatrixChat.tsx:371` missing `MatrixClient.userHasCrossSigningKeys`; `src/utils/device/clientInformation.ts:80` missing `MatrixClient.deleteAccountData`; `test/DeviceListener-test.ts:99,192,201` reference missing `deleteAccountData`. No errors were reported in the changed files. Repository-wide typecheck remains uncertain until these SDK typing mismatches are resolved.

Tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`); local `find`/`grep` were used. No dependencies downloaded.
