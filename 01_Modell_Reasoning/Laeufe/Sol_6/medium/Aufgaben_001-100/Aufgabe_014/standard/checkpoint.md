Task: Fix NodeBB v4.4.3 notification dropdown, category selector, quick search, data normalization, routes, and template issues described by the user.
Status: Complete. Implemented all requested changes. ESLint and git diff checks pass; standalone Mocha tests pass (11). Database-backed Mocha files cannot run because Redis at 127.0.0.1:6379 refuses connections (0 tests executed).
Constraints: Local code and existing tests only; preserve git history and index.
