Implemented token-based invitation registration.

- Registration now copies `?token=` into the form’s hidden `token` field. Token registrations can proceed without an email; matching invited emails are confirmed, associated groups are joined, and invitation records are cleaned up.
- Invitation metadata and lookup are token based, with email token sets and inviter references maintained. Approval queued registrations retain and process the token when accepted.
- Verification, group joining, and cleanup now support token-based lookup while keeping legacy invitation views compatible.

ESLint, syntax checks, and `git diff --check` pass. `test/authentication.js` passed (30 tests). The invitation-filtered `test/user.js` run had 14 passing tests and one failure: “should error if email exists” expected 400 but received 200. That assertion uses the unchanged email lookup path. The local Redis instance used for testing has been stopped.