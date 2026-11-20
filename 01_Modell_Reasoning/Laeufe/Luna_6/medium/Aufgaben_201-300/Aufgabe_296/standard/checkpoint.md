# Checkpoint

Implemented token-centric invitations in `src/user/invite.js`: token validation, group lookup, email confirmation, metadata keyed by token, email-to-token tracking, inviter references, and cleanup by either token or email. Registration now carries the URL token into its hidden field, permits token-only creation, applies invitation post-registration actions, and cleans up invitation records.

Validation: targeted ESLint and `git diff --check` pass. Existing invitation test selection could not start because Redis at 127.0.0.1:6379 is unavailable (Mocha `before all` hook failed before tests ran).
