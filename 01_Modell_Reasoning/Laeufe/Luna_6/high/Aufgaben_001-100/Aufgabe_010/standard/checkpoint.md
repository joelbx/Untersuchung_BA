# Checkpoint

Implemented the composer visibility changes and related requirements:

- Tombstone status and continuation link now use paragraph markup; the replacement icon is decorative.
- Added `CancelButton` with a default 16px size, configurable CSS custom property sizing, a cancel icon, and an accessible Cancel label. Reply preview uses it and identifies the reply target in its heading.
- Sender profile rendering now accepts an optional semantic wrapper element.
- Updated the composer test to assert the semantic notice and its text.

Verification:
- `yarn test --runInBand test/components/views/rooms/MessageComposer-test.tsx` passes (3 tests).
- ESLint on modified TypeScript files passes.
- Stylelint on modified SCSS passes.
- `git diff --check` passes.
- `yarn tsc --noEmit --jsx react` remains blocked by five existing errors in installed Matrix SDK types and unrelated room settings files; no errors were reported in modified files.
