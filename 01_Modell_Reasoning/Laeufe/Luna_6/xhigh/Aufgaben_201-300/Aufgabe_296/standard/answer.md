Implemented token based invitation registration. The registration form reads the URL token into its hidden field, and registration now confirms a matching invited email, joins groups by token, and cleans up invitation records. Invitation metadata and references are stored under token and inviter keys; email is optional when verifying a token.

ESLint, syntax checks, and `git diff --check` pass. The invitation suite reports 14 passing tests and one failure: `should error if email exists` returned HTTP 200 instead of 400.

Changed [invite.js](/app/src/user/invite.js:63), [authentication.js](/app/src/controllers/authentication.js:56), and [register.js](/app/public/src/client/register.js:21).