# Checkpoint

Task: move-out logic uses active ID membership in mailbox element IDs, with evaluation suspended while the mailbox list loads.
Status: implemented and verified.
Changes: simplified useShouldMoveOut; passed elementIDs/loadingElements through MailboxContainer to both views; ConversationView selects message ID for always-message labels and conversation ID otherwise; added hook tests and updated ConversationView fixture.
Verification: Jest 2 suites, 15 tests passed; TypeScript noEmit check passed; git diff --check passed.
Delegation: none used.
