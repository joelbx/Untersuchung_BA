# Checkpoint: token-based invitation registration

- Task completed: registration accepts a valid invitation token without requiring an email in the request; matching invited emails are confirmed, token groups are joined, and invitation records/references are cleaned.
- Storage is token-first at `invitation:token:<token>`, with inviter UID, email, and groups. Email-to-token sets use normalized email keys, and inviter/email references use `invitation:uid:<uid>:invited:<email>`. Legacy email metadata and inviter email sets are maintained for current admin views.
- Token registration bypasses the email collection interstitial. Approval queued registrations retain the token and run the same invite actions when accepted.
- Registration client populates its existing hidden `token` input from the URL query string and prefills the optional invited email when present.
- Verification: ESLint, JavaScript syntax checks, and `git diff --check` pass. `test/authentication.js`: 30 passing. Invitation-filtered `test/user.js`: 14 passing, 1 failing on the existing “should error if email exists” assertion (expected 400, received 200); that assertion exercises the unchanged user email lookup path. Redis was started locally for testing and has been stopped.
