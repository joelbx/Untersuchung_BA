# Checkpoint

Task: accessible room-share link and consistent external links in settings.

Implemented: `ExternalLink` forwards anchor props and classes, defaults to a new tab with `noreferrer noopener`, provides a CSS-mask icon hidden from assistive technology, and includes a spoken new-tab cue. Settings links now use it; the Profile Settings icon-only anchor is gone. Share dialog links have localized titles matching the target; social link titles describe the sharing action and new-tab behavior, with decorative image alt text emptied. Added the SCSS import and English strings.

Verification:
- `node_modules/.bin/jest test/components/views/elements/ExternalLink-test.tsx test/components/views/settings --runInBand --silent`: PASS, 4/4 tests, 2/2 snapshots. Red-green check: removing the spoken cue made the focused test fail on the missing text; restoring it made the test pass.
- `node_modules/.bin/eslint --max-warnings 0 src/components/views/elements/ExternalLink.tsx src/components/views/dialogs/ShareDialog.tsx src/components/views/settings/BridgeTile.tsx src/components/views/settings/ChangePassword.tsx src/components/views/settings/EventIndexPanel.tsx src/components/views/settings/ProfileSettings.tsx src/components/views/settings/tabs/room/BridgeSettingsTab.tsx src/components/views/settings/tabs/room/SecurityRoomSettingsTab.tsx src/components/views/settings/tabs/user/HelpUserSettingsTab.tsx src/components/views/settings/tabs/user/LabsUserSettingsTab.tsx test/components/views/elements/ExternalLink-test.tsx`: PASS.
- `node_modules/.bin/stylelint res/css/views/elements/_ExternalLink.scss res/css/views/settings/_ProfileSettings.scss`: PASS.
- `git diff --check`: PASS.
- `node_modules/.bin/tsc --noEmit --jsx react`: exit 2, six errors in unchanged files:
  - `src/components/structures/ThreadView.tsx(174,37): error TS2339: Property 'ViewThread' does not exist on type 'typeof ThreadEvent'.`
  - `src/stores/notifications/ThreadNotificationState.ts(32,36): error TS2339: Property 'NewReply' does not exist on type 'typeof ThreadEvent'.`
  - `src/stores/notifications/ThreadNotificationState.ts(33,36): error TS2339: Property 'ViewThread' does not exist on type 'typeof ThreadEvent'.`
  - `src/stores/notifications/ThreadNotificationState.ts(38,37): error TS2339: Property 'NewReply' does not exist on type 'typeof ThreadEvent'.`
  - `src/stores/notifications/ThreadNotificationState.ts(39,37): error TS2339: Property 'ViewThread' does not exist on type 'typeof ThreadEvent'.`
  - `src/stores/notifications/ThreadNotificationState.ts(47,66): error TS2554: Expected 1 arguments, but got 2.`
  Type-check status remains uncertain for the repository as a whole; no errors were reported in changed files.

Local tooling: `rg` is unavailable (`/bin/bash: rg: command not found`), so searches used `grep` and `find`. The first focused Jest attempt failed because `src/component-index` was absent (`Cannot find module './component-index' from 'src/Skinner.ts'`); `node scripts/reskindex.js -h header` generated the ignored local index and subsequent Jest runs passed. No dependencies were downloaded.
