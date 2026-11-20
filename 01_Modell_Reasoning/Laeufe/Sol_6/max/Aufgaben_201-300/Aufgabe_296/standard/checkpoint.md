# Checkpoint

Task: allow registration using an invitation token without requiring the invited email.
Status: implementation complete.
Changes: URL token fills the registration hidden field; valid token bypasses the email collection interstitial; direct and administrator-approved registration confirm only matching email, join token groups, and remove invitation records. Invite metadata and indexes now use token, inviter, and invited email keys.
Verification: invitation suite 33 passing; authentication suite 30 passing; ESLint and git diff --check passing.
Known unrelated test failure: full test/user.js suite has 206 passing and 1 failing in existing User.email.confirmByCode email confirmation by code.
