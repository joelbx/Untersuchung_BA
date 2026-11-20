# Checkpoint

Task: improve message composer replacement notice semantics and related cancel/profile/reply UI.

Implemented:
- Tombstone status and continuation link use paragraphs; decorative icon has empty alt text.
- Reusable CancelButton with configurable icon size, native button defaults, accessible label, and shared styling.
- Reply, search, and link preview cancel controls use CancelButton.
- DisambiguatedProfile supports an inline element; reply preview names the sender.
- Tests cover tombstone semantics, search cancel label, reply sender and cancel dispatch.

Verification: targeted Jest suite passed (3 suites, 8 tests); ESLint and Stylelint passed. Full TypeScript check has only pre-existing SDK/room settings errors.
