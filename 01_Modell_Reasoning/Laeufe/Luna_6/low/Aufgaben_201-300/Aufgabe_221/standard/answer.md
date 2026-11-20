Implemented Best Book Awards persistence and API support.

- Added the `Bestbook` service and `bestbook_awards` table with uniqueness constraints, read validation, filtering, counts, and leaderboard queries.
- Added nomination and count endpoints, plus work award accessors.
- Integrated work redirects and account anonymization with award records.
- Recorded the implementation and verification in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).

Verification: Python compilation and `git diff --check` passed. The existing core database and model tests passed: **42 passed**.