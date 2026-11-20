Resolved invitation registration in `/app`. The form now submits the URL token, and registration can complete with a valid token and no email. Invitations use token keyed metadata; registration confirms a matching email, joins the token’s groups, and cleans up linked invitation records.

Verification passed: 31 invite tests, 30 authentication tests, ESLint, and `git diff --check`.