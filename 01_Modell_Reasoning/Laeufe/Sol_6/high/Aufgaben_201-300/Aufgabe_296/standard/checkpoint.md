Issue resolved in checked-out files: token-only invitation registration, token-keyed invitation metadata, email confirmation on matching invite email, group join, and cleanup by email/token.
Verification: ESLint and git diff --check pass; focused user invite suite 32 passing; authentication suite 30 passing.
Full test/user.js run: 179 passing, 1 unrelated existing failure in email confirm/confirmByCode (src/user/email.js calls user.setUserField without UID). The focused invite suite passes.
No git history, index baseline, or harness configuration changes. Local disposable Redis used for tests.
