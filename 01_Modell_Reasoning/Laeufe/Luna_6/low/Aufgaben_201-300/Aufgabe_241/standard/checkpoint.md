# Checkpoint

Implemented duplicate initiation protection and synchronous disabled UI feedback in `VoiceBroadcastPreRecordingPip`. Initiation remains disabled until a returned promise settles, or through the current event tick for synchronous starts. The microphone line opens the device menu only once while it is open; the existing menu selection passes the selected `MediaDeviceInfo` to the audio selection hook and the hook updates the displayed label.

Verification: the focused existing Jest suite `test/voice-broadcast/components/molecules/VoiceBroadcastPreRecordingPip-test.tsx` passes (6 tests). `yarn lint:types` is blocked by existing MatrixClient typing errors in `MatrixChat.tsx`, `clientInformation.ts`, and `DeviceListener-test.ts`; no reported errors reference the modified component.
