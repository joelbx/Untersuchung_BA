# Checkpoint

Task: Resolve the voice broadcast pre-recording interaction issue in `/app`.

Findings: The existing audio-device hook already derives and updates `currentDeviceLabel`; the component supplies the menu's root anchor. The gaps were an unguarded start handler and a nullable selection callback.

Changes in progress: Added a ref-backed start lock with a rendered native disabled button, kept close behavior separate from that lock, and made device-menu opening and selection deterministic.

Validation: The focused `VoiceBroadcastPreRecordingPip` suite passes (6 tests); its snapshot was updated for the native button. ESLint and Prettier pass for the edited component. `git diff --check` passes. Repository-wide TypeScript validation still reports five pre-existing errors in MatrixClient API usage in `MatrixChat.tsx`, `clientInformation.ts`, and `DeviceListener-test.ts`; none refer to the edited component.

Status: Implementation and review are complete.
