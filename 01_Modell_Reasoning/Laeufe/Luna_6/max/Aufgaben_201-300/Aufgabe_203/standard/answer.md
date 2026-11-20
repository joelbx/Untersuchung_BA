Implemented the accessible link updates.

- Added [ExternalLink.tsx](/app/src/components/views/elements/ExternalLink.tsx), with secure new tab defaults, a decorative icon, and an announced “Opens in a new tab” cue.
- Updated [ProfileSettings.tsx](/app/src/components/views/settings/ProfileSettings.tsx:164) and [ShareDialog.tsx](/app/src/components/views/dialogs/ShareDialog.tsx:242).
- Added the [external-link styles](/app/res/css/views/elements/_ExternalLink.scss), imported them globally, and added the localization strings.

ESLint and Stylelint passed. The relevant Jest suites passed: 4 suites, 13 tests, 2 snapshots. `yarn lint:types` reports existing errors in `ThreadView.tsx` and `ThreadNotificationState.ts` involving `ThreadEvent` APIs.