# Checkpoint

Task: resolve inaccessible room-share and external links in Element Web.

Completed: added the reusable `ExternalLink` component with secure new-tab defaults, a decorative masked icon, and an announced new-tab cue; migrated the Profile Settings hosting link; added a localized room-share name; created/imported the external-link SCSS partial.

Validation:
- ESLint on the changed TypeScript files passed.
- Stylelint on the changed SCSS files passed.
- Relevant existing settings and GroupView Jest suites passed (4 suites, 13 tests, 2 snapshots) after generating the repository's ignored component index for test setup.
- `yarn lint:types` remains blocked by existing `ThreadEvent.ViewThread`/`NewReply` API errors in `ThreadView.tsx` and `ThreadNotificationState.ts`.
