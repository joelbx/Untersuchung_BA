# Checkpoint

Implemented guarded Go live activation with immediate disabled feedback and reset on promise resolution or rejection (or after one event tick for synchronous starts). Device menu opening is guarded against duplicate activation; selecting a non-null audio device closes the menu and delegates the selected `MediaDeviceInfo` to the audio selection hook, which refreshes the header label.

Added a regression test for repeated Go live activation while `start()` is pending.

Validation completed:
- `yarn test test/voice-broadcast/components/molecules/VoiceBroadcastPreRecordingPip-test.tsx --runInBand` — passed (7 tests).
- ESLint on the component and its test — passed.
