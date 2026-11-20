Implemented the accessible link updates.

- Added [ExternalLink.tsx](/app/src/components/views/elements/ExternalLink.tsx:20), with native anchor props, composable custom classes, secure new-tab defaults, a screen-reader cue, and an aria-hidden icon.
- Added and globally imported [_ExternalLink.scss](/app/res/css/views/elements/_ExternalLink.scss:17), using the requested size and spacing tokens and SVG mask.
- Updated [ProfileSettings.tsx](/app/src/components/views/settings/ProfileSettings.tsx:169) to use the component and remove the duplicate icon-only link.
- Added the “Link to room” accessible label to [ShareDialog.tsx](/app/src/components/views/dialogs/ShareDialog.tsx:203) and added the localization strings.

Targeted ESLint and Stylelint passed. Full Jest and TypeScript checks did not pass: Jest reported existing fake-timer and snapshot/runtime failures; TypeScript reported `ThreadEvent` errors in untouched files. The generated component index used to run Jest was removed.