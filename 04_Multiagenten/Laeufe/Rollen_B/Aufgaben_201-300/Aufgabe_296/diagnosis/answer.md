I traced the failure but did not edit project source or tests: my assigned role for this checkout is fault localization only. I recorded the findings in [checkpoint.md](/app/.codex-role-output/checkpoint.md).

The likely fix spans three files:

- [src/user/invite.js](/app/src/user/invite.js:57) requires an email to verify a token, stores invitation data by email, and has no `confirmIfInviteEmailIsUsed`.
- [public/src/client/register.js](/app/public/src/client/register.js:20) has the URL token population code commented out, although the form already has a hidden `token` input.
- [src/controllers/authentication.js](/app/src/controllers/authentication.js:62) has the post-registration invitation actions commented out.

The fix should verify by token alone; store inviter, email, and groups under `invitation:token:<token>`; confirm email only when the entered address matches the invited address; join the token’s groups; and clean up linked tokens and inviter references for either a token or registration email. Existing invitation tests use the old email-keyed storage, so their expectations will need updating. I did not run tests because no implementation was changed.