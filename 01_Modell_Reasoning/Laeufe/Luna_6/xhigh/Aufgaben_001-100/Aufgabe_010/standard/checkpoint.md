# Checkpoint

Issue: improve message composer visibility and semantic room replacement notices, with reusable accessible cancel controls and consistent reply/profile rendering.

Progress: implemented semantic tombstone paragraph markup; added the reusable, size configurable `CancelButton` with an accessible label; updated reply preview copy and cancellation; and added configurable profile elements with keyboard accessible behavior for clickable profiles. Reply tile sender profiles use inline markup.

Verification: the existing MessageComposer Jest suite passed (3 tests), and ESLint and Stylelint passed for changed files. `yarn lint:types` is blocked by existing errors in `node_modules/matrix-js-sdk/src/http-api.ts` (`IRequest.abort`) and `AliasSettings.tsx` / `SecurityRoomSettingsTab.tsx` (`MatrixClient.getLocalAliases`); it reported no errors in the changed files.
