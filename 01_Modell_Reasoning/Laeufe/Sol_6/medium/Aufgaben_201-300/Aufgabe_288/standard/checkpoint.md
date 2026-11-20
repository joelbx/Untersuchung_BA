Task: Move useShouldMoveOut to active element ID membership with loading guard.
Status: Complete. Hook checks active ID against mailbox elementIDs only after loadingElements is false. MailboxContainer passes both values to ConversationView and MessageOnlyView. ConversationView selects messageID for isAlwaysMessageLabels and conversationID otherwise. Added focused hook cases and conversation message-label test.
Verification: Focused Jest suites passed (16 tests); added conversation case passed separately (1 test); mail TypeScript check passed; git diff --check passed.
Constraints: Used local repository and existing tests; preserved git history/index/harness.
