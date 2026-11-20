Task: Prevent duplicate Kick, Ban, and Mute actions in UserInfo.
Status: Implemented member-scoped synchronous action lock spanning confirmation and network request. Buttons set disabled and aria-disabled while pending. Cancellation and failure release lock; failures show one error dialog. Added integration tests for cancel, duplicate requests, shared disabled state, and mute failure.
Verification: UserInfo Jest suite passed (73 tests, 6 snapshots); targeted ESLint passed. Repository-wide tsc has pre-existing errors in SDK typings and unrelated files, none in edited files.
