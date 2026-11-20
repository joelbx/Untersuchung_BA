Task: Replace move-out heuristics with active element ID membership and loading guard.
Status: Implemented. MailboxContainer passes elementIDs and loadingElements to ConversationView and MessageOnlyView; both call the simplified hook. ConversationView selects messageID for isAlwaysMessageLabels labels and conversationID otherwise. Added hook tests and updated ConversationView test props.
Verification: Jest focused suites passed (16 tests); mail TypeScript noEmit passed; git diff --check passed.
Constraints observed: Used local code/tests only; did not alter git history, index, or harness configuration.
