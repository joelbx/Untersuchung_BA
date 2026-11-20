# Checkpoint

Task: Improve message composer room replacement notice semantics and related cancel/reply/profile consistency.
Status: Implemented and verified.

Changes: Tombstone status and link use paragraphs; reusable accessible CancelButton added and used by reply preview and search bar; reply preview names the sender; profile components support span rendering; relevant styles and English string updated.
Verification: MessageComposer and SearchBar tests passed (7 tests); ESLint, Stylelint, and git diff --check passed. TypeScript reports only pre-existing matrix-js-sdk and room alias API errors outside changed files.
