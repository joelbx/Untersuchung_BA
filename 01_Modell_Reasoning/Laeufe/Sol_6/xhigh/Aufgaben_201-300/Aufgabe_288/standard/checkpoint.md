# Checkpoint

Task: update mailbox move-out behavior to use active element IDs and loading state in both conversation and message views.

Status: implemented and verified. Replaced cache/label checks with a loading-gated ID membership check; passed mailbox element IDs and loading state into both views; selected message ID for message-level labels in conversation view. Added hook and conversation-view coverage. Focused Jest run passed (2 suites, 16 tests); mail TypeScript check passed. Existing formatting in view render blocks is outside this change.
