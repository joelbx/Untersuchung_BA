# Checkpoint

Task: prevent duplicate Kick, Ban, and Mute actions in the user info panel.
Status: complete. A member-scoped synchronous lock disables all three buttons through confirmation and request, and clears on cancel, success, or failure.
Verification: UserInfo Jest suite passes (71 tests); ESLint and git diff --check pass. Full tsc has unrelated existing errors and no errors in changed files.
