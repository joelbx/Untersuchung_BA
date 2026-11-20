# Invitation token registration checkpoint

Completed: registration form reads token from URL into hidden input; registration accepts a token without email, confirms matching invited email, joins token groups, and cleans invitation metadata. Invitation records now use token metadata, inviter/email references, and per-email token sets. Updated invite tests for token-only registration, confirmation behavior, and cleanup across inviters.

Verification: ESLint passed for changed JS files; `mocha test/user.js --grep 'invites'` passed (31 tests); `git diff --check` passed. Full `mocha test/user.js` reached 176 passing tests but failed later in the unrelated `User email confirm / should confirm email of user` test (`NaN !== 1`).
