Task: Prevent repeat Kick, Ban, and Mute actions in user info panel.
Status: Implemented member-scoped synchronous lock shared by all three buttons, with disabled/aria-disabled while confirmation or request is pending. Cancel, success, and failure release the lock; failures show one error dialog.
Verification: UserInfo Jest suite passed (69 tests); ESLint passed for edited files; git diff --check passed. Repository-wide tsc reports pre-existing SDK/unrelated type errors, none in edited files.
