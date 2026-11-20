# Checkpoint

Implemented the current-session kebab context menu in the checked-out repository.

- Added a reusable, accessible KebabContextMenu with a localized label, menu state, focus return, and supplied action nodes.
- Added current-session sign-out and bulk sign-out actions, with the latter targeting only other device IDs.
- Added destructive styling, context-menu click dismissal, translations, tests, and updated snapshots.

Verification: 58 focused Jest tests and 9 snapshots pass; ESLint and stylelint pass; `git diff --check` passes. Full TypeScript checking reports pre-existing matrix-js-sdk API mismatches in unrelated files, with no errors in changed files.
