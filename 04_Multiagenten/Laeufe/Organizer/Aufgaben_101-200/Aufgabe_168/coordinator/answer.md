Kick, Ban, and Mute now share a member-scoped lock in the [user info panel](/app/src/components/views/right_panel/UserInfo.tsx:620). The lock starts on the first activation, disables all three buttons with `disabled` and `aria-disabled="true"`, and stays active through confirmation and the request. Cancellation sends no operation; failure shows one error dialog and re-enables the controls.

The [UserInfo tests](/app/test/components/views/right_panel/UserInfo-test.tsx:1206) cover rapid activation, shared locking, cancellation, and failure. All 72 tests pass; ESLint and `git diff --check` pass. The full TypeScript check still reports 47 errors outside the changed files and none in the changed files.

No delegation was used.