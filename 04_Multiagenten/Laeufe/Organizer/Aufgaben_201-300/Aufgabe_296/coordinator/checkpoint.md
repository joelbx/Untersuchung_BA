# Checkpoint

Issue resolved: token-only invitation registration is supported.
Changes: URL token populates form input; registration bypasses optional email interstitial for token registrations, confirms matching invited email, joins token groups, and cleans up invite records. Invitations now store metadata by token with email and inviter indexes. Email cleanup handles every associated token.
Verification: `./node_modules/.bin/mocha test/user.js --grep 'User invites' --reporter dot` (31 passing); ESLint on changed JS files (passing); `git diff --check` (passing).
Delegation: none.
