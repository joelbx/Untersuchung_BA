# Checkpoint

Task: allow registration with an invitation token and no email, and key invitation data by token.
Status: complete.
Changes: registration form reads query token; backend applies invite email confirmation, group joining, and cleanup; invite metadata and references use token-based keys; cleanup supports email or token.
Verification: invite tests passed (31); ESLint and git diff --check passed.
