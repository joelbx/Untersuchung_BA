# Checkpoint

Task: Repair ACP email validation actions and status display for missing or expired confirmation data.

Completed: paired `confirm:byUid:<uid>` and `confirm:<code>` records with explicit expiry; pending, fallback, and cleanup utilities; safe confirmation and resend flow; cleanup on user deletion and password reset; ACP status labels and missing-address errors. Added focused user, ACP, and socket tests.

Verification: ESLint and `git diff --check` pass. Combined focused Mocha run: 13 passing. Broader suites were attempted: user suite stopped at an invitation group membership test, admin controller suite stopped at an unrelated edit/email 404 assertion, and socket suite stopped at plugin install's blocked external request.
