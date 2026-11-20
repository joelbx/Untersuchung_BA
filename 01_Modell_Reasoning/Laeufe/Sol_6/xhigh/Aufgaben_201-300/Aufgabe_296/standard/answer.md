Implemented token-only invitation registration. The form now copies the URL token into its hidden field; registration and approval apply invitation groups, confirm email only when it matches the invite, and clean up linked token, email, and inviter records.

Verification passed: 33 invitation tests, 6 approval queue tests, 2 register page tests, ESLint, and syntax checks.