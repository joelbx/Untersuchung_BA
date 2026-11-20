# Accessibility links checkpoint

- Inspected the repository location and identified `ShareDialog.tsx`, `ProfileSettings.tsx`, and the existing external-link SVG.
- Implemented a reusable external anchor with native props, merged classes, secure new-tab defaults, a masked decorative icon, and a translated screen reader description.
- Migrated external links throughout settings and removed the separate icon-only hosting link. Added contextual accessible names for the room permalink and generic settings links, with English localization entries.
- Existing settings tests: 3 suites and 3 tests passed after generating the ignored `component-index.js` file. The generated file was removed afterward.
- ESLint and Stylelint passed. TypeScript reports six existing errors in untouched thread files (`ThreadView.tsx` and `ThreadNotificationState.ts`).
