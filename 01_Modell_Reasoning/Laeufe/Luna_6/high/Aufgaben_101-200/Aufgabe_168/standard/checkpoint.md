# Checkpoint

Implemented a member-scoped lock in `UserInfo.tsx` for kick, ban/unban, and mute/unmute. It sets pending synchronously before confirmation, disables all rendered admin action buttons with `disabled` and `aria-disabled`, prevents concurrent action callbacks via a ref, and releases after cancellation or operation settlement. Request failures retain the existing single error dialog and release the lock.

Verification: the existing `UserInfo-test.tsx` suite passes (68 tests). ESLint and `git diff --check` are being checked. Full TypeScript checking is blocked by existing repository/dependency errors in the Matrix SDK and unrelated files; no diagnostics referenced the edited file.
