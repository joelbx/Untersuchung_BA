Token-only invitation registration is implemented. The form copies the URL token into its hidden input, and the backend verifies invitations, joins groups, and cleans up records using token metadata. It confirms the user’s email only when the entered address matches the invited address.

Verification passed: 31 invitation tests, 30 authentication tests, ESLint, and `git diff --check`.