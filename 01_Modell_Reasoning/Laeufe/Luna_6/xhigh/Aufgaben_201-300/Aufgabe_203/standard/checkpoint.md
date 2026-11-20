# Checkpoint

Task: Resolve accessible link naming and external-link cues in the repository.

Completed:
- Added `ExternalLink` with native anchor prop forwarding, composable custom classes, secure new-tab defaults, a hidden “Opens in a new tab” cue, and an aria-hidden decorative icon.
- Added and globally imported the `_ExternalLink.scss` partial using the requested size and spacing tokens and external-link SVG mask.
- Updated Profile Settings to use `ExternalLink` and removed its duplicate icon-only link.
- Added a localized room-share accessible label and the external-navigation cue string.

Validation:
- Targeted ESLint and Stylelint passed.
- `yarn lint:types` reports existing `ThreadEvent` API errors in `ThreadView.tsx` and `ThreadNotificationState.ts`.
- Full Jest: 69 suites passed, 2 suites failed, 2 skipped; 48 tests failed, 23 skipped, 701 passed; 2 snapshots failed. Failures are in existing test/runtime behavior (including SpaceStore fake timers and snapshot mismatches), not the changed link code.
- The generated `src/component-index.js` created for the Jest run was removed afterward.
