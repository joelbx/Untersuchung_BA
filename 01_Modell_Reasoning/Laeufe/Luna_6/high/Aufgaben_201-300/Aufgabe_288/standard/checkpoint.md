# Checkpoint

Issue: replace label/cache heuristics for move-out decisions with a loading-aware check that the active element ID exists in the supplied valid element IDs.

Implemented the ID membership check in `useShouldMoveOut`, propagated mailbox `elementIDs` and loading state to both views, and selected the conversation-view active ID by `isAlwaysMessageLabels`.

Verification: the existing `ConversationView` Jest suite passed (10 tests), the mail workspace TypeScript check passed, and `git diff --check` passed.
