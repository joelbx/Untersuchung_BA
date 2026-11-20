# Checkpoint

Task: resolve the voice broadcast pre-recording control and device-selection behavior in `/app`.

Implemented in `src/voice-broadcast/components/molecules/VoiceBroadcastPreRecordingPip.tsx`:
- Added a synchronous ref guard and rendered disabled state for Go live, held until a promise resolves/rejects or one event tick after a synchronous attempt.
- Made Go live a native button and preserved its pending state when the close control calls cancel.
- Guarded repeated microphone activations, typed device selection as non-null, closed the menu after selection, and passed the selected device to the audio selection hook.

Updated the matching snapshot for the native button.

Verification:
- Focused Jest suite passed: 6 tests and 1 snapshot.
- ESLint and Prettier passed for the changed component.
- `yarn lint:types` reports existing Matrix SDK type mismatches in `MatrixChat.tsx`, `clientInformation.ts`, and `DeviceListener-test.ts`; no error points to the changed component.
- `git diff --check` passed.
