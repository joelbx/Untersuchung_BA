# Checkpoint

Task: Resolve repeated Go live activation and device selection state in VoiceBroadcastPreRecordingPip.

Phase 1: Root cause. The component passes `voiceBroadcastPreRecording.start` directly to `AccessibleButton`; no pending guard or disabled prop exists. `AccessibleButton` defaults to a div and only forwards `disabled` when supplied. Repeated activation can therefore call `start` more than once. The menu already receives the root ref and maps device items to their `MediaDeviceInfo`; the hook's `setDevice` updates its state and `currentDeviceLabel`. The component accepts a nullable device even though the menu emits non-null devices. Current tests cover only single interactions.

Phase 2: Pattern. `VoiceBroadcastRecordingPip` uses the same device hook/menu. The menu's callback is typed `(device: MediaDeviceInfo) => void`; `useAudioDeviceSelection.setDevice` requires `MediaDeviceInfo`. The pre-recording component differs by accepting null and has no initiation state.

Phase 3 hypothesis: A synchronous ref guard plus rendered disabled state over the lifetime of `start()` will prevent repeat calls, including events before React rerenders. A non-null selection callback and menu-open guard will preserve a single menu and hook-driven label updates.

Phase 3 result: A failing test demonstrated two `start()` calls for two rapid clicks before the patch. The guarded handler and native disabled button now pass pending, completion, rejection, and synchronous-call tests. Existing device-selection tests verify menu closes, `setDevice` receives the chosen audio input, and the header label updates without remounting; a repeated-activation test verifies one menu.

Phase 4 verification: `./node_modules/.bin/jest test/voice-broadcast/components/molecules/VoiceBroadcastPreRecordingPip-test.tsx test/voice-broadcast/components/atoms/VoiceBroadcastHeader-test.tsx test/voice-broadcast/models/VoiceBroadcastPreRecording-test.ts --runInBand --updateSnapshot --silent` passed (3 suites, 18 tests, 5 snapshots). Targeted ESLint, Prettier check, and `git diff --check` passed.

Type check limitation: `./node_modules/.bin/tsc --noEmit --jsx react` exited 2 with five errors outside changed files: `src/components/structures/MatrixChat.tsx:371` missing `MatrixClient.userHasCrossSigningKeys`; `src/utils/device/clientInformation.ts:80` missing `MatrixClient.deleteAccountData`; `test/DeviceListener-test.ts:99,192,201` uses the same missing `deleteAccountData` member. Thus full project type check remains failing on local SDK typings, with no errors reported in edited files. No dependencies were downloaded.
