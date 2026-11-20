Implemented token-based invitation registration.

- The registration client copies `token` from the URL into the hidden form field.
- Registration with a token skips the email collection interstitial, confirms the email only when it matches the invitation, joins the invited groups, and cleans up invitation records.
- Invitation lookup and metadata now use token keys, with per-email token sets and inviter references. Verification accepts a token without an email; cleanup accepts either a token or email.

ESLint and `git diff --check` passed. The invitation tests could not start because Redis was unavailable at `127.0.0.1:6379`.