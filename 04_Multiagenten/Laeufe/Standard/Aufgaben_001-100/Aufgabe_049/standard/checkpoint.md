Task: Fix ACP email validation for expired or missing confirmation data.
Status: Implemented and verified focused behavior.
Changes: Added confirm:byUid mapping and timestamped confirm objects, pending/expiry checks, email fallback, key cleanup during confirmation/deletion, ACP four-state status, and admin missing-email reporting. Updated creation/profile paths and tests.
Verification: email confirmation tests 6 passing; admin socket validation tests 4 passing; ACP status test 1 passing; template precompile, ESLint, and git diff --check passed. Full test/user.js reached 173 passing and one invitation group membership failure. Full controllers-admin.js reached 11 passing and one unrelated edit/email 404 failure.
