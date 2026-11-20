# Checkpoint

- Task: replace move-out heuristics with active element ID membership, and propagate valid IDs/loading to both views.
- Repository: `/app`; initial status clean.
- Discovery: `rg` is unavailable (`/bin/bash: rg: command not found`); using `find`/`grep`.
- Replaced cache and label checks in `useShouldMoveOut` with an effect that checks active ID membership after `loadingElements` becomes false.
- Passed mailbox `elementIDs` and `loading` to both content views. Conversation view selects `messageID` for `isAlwaysMessageLabels(labelID)`, otherwise the route conversation ID; message-only view uses its message ID.
- Added hook coverage for valid/missing/empty IDs and loading transitions, plus a conversation view test for a message-level label.
- Validation: `../../node_modules/.bin/jest --runInBand --coverage=false src/app/hooks/useShouldMoveOut.test.ts src/app/components/conversation/ConversationView.test.tsx` passed (2 suites, 16 tests).
- Validation: `../../node_modules/.bin/tsc --noEmit --pretty false` passed.
- Initial attempts used `../../../node_modules/.bin/{jest,tsc}` and failed with `No such file or directory`; corrected to `../../node_modules/.bin`.
