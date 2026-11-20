Task: Fix getUpvoters access checks, cutoff/ordering, and frontend tooltip handling.
Status: implementation and focused regression test added.
Validation: ESLint and git diff --check passed. Targeted Mocha test could not start because Redis at 127.0.0.1:6379 refused connections.
