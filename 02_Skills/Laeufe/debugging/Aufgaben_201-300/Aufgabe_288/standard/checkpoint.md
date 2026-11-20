# Checkpoint

Task: replace label/cache move-out heuristics with active element ID membership, gated by mailbox elements loading, for both conversation and message views.

Investigation: `useShouldMoveOut` selected conversation/message cache entries and checked label membership; it never received the mailbox list. `MailboxContainer` already obtains `elementIDs` and `loading` from `useElements`. `isAlwaysMessageLabels` identifies labels whose list IDs are message IDs. A focused pre-fix hook test failed on undefined, empty, absent, and empty-list cases (five expected callback assertions failed). A route-transition test then showed the internal `useConversation` ID lags the current route and caused a premature `onBack`; using the route prop resolved it. `rg` is unavailable (`/bin/bash: rg: command not found`); local searches used `find` and `grep`.

Patch: hook checks `elementID` membership in `elementIDs` only after `loadingElements` is false. Both views receive these values from `MailboxContainer`; conversation view chooses `messageID` for always-message labels and the route `conversationID` otherwise. Removed hook cache selectors and content-loading gates.

Verification:
- `../../node_modules/.bin/jest src/app/hooks/useShouldMoveOut.test.ts src/app/components/conversation/ConversationView.test.tsx --runInBand --coverage=false --silent`: passed, 2 suites and 18 tests.
- `../../node_modules/.bin/tsc --noEmit --incremental false -p tsconfig.json`: passed after fixing the test fixture's optional `messageID` type. The first run failed with TS2345 for that fixture.
- `../../node_modules/.bin/eslint src/app/hooks/useShouldMoveOut.ts src/app/hooks/useShouldMoveOut.test.ts src/app/components/conversation/ConversationView.tsx src/app/components/conversation/ConversationView.test.tsx src/app/components/message/MessageOnlyView.tsx src/app/containers/mailbox/MailboxContainer.tsx --quiet`: passed.
- `git diff --check`: passed.
- `../../node_modules/.bin/prettier --check src/app/hooks/useShouldMoveOut.ts src/app/hooks/useShouldMoveOut.test.ts src/app/components/conversation/ConversationView.tsx src/app/components/conversation/ConversationView.test.tsx src/app/components/message/MessageOnlyView.tsx src/app/containers/mailbox/MailboxContainer.tsx`: failed; ConversationView.tsx and MessageOnlyView.tsx have preexisting formatting differences in untouched sections (JSX indentation, import order). No broad reformat was applied.
