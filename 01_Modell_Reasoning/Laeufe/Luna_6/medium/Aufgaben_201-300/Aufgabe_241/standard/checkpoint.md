# Checkpoint

Implemented in `VoiceBroadcastPreRecordingPip.tsx`:
- guarded live initiation with a synchronous ref lock and rendered disabled state through Promise completion/rejection (or one event tick for sync start)
- ignored repeated device-line activation while the selection menu is open
- closed the menu on selection and passed only a selected non-null `MediaDeviceInfo` into the audio selection hook
- preserved header cancellation callback behavior

Verification: `yarn test test/voice-broadcast/components/molecules/VoiceBroadcastPreRecordingPip-test.tsx --runInBand` passed (1 suite, 6 tests). Prettier formatting was applied after its check reported differences.
