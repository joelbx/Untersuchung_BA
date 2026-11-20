# Checkpoint

Task: restrict SocketPosts.getUpvoters by category read privilege, preserve ordered deduplicated usernames, and update frontend cutoff/tooltip.

Status: completed.

Changes: bulk category read validation before vote lookup; admin bypass; cutoff=6 returned per post; visible UIDs deduplicated for one username lookup while preserving per-post order; frontend consumes cutoff and enables HTML tooltips; integration coverage added.

Verification: ESLint and git diff --check passed; voting test group passed (12 tests). Local temporary Redis used for tests and stopped.
