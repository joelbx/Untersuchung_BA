Updated `useShouldMoveOut` to call `onBack` only after mailbox elements finish loading and the active ID is absent from the valid ID list. Both views now receive that list and loading state; conversation views select the message or conversation ID using `isAlwaysMessageLabels`.

Verification: 16 focused tests passed, ESLint passed on changed files, and `git diff --check` passed.