# Checkpoint

Task: Replace label/cache heuristics in `useShouldMoveOut` with validity checks against the current mailbox slice's element IDs, suspended while those elements are loading.

Completed:
- Replaced cache, entity-state, and label-membership heuristics with a loading-gated ID membership check.
- Passed mailbox `elementIDs` and loading state through both view types.
- In conversation content, use the message ID for always-message labels and the conversation ID otherwise; message-only content checks its active message ID.
- Updated the existing conversation view test fixture for the new props.

Validation:
- `ConversationView.test.tsx`: 10 tests passed.
- Mail package TypeScript check passed.
- `git diff --check` passed.
