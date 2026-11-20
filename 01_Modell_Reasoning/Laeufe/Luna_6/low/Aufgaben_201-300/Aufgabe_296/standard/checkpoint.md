# Checkpoint

Task: allow registration via invitation token without requiring an email, with token-keyed invitation metadata and cleanup.

Implemented token-keyed invitation metadata, token-based validation and group lookup, email/token cleanup, conditional email confirmation, post-registration actions, and registration form token query handling.

Validation: ESLint and `git diff --check` pass. Existing invitation test subset could not start because Redis at 127.0.0.1:6379 is unavailable (before hook fails with ECONNREFUSED).
