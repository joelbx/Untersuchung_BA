Implemented Best Book Awards backend support: nomination storage with read-status and uniqueness checks, add/update/remove and count JSON APIs, Work nomination methods, and award updates during work redirects and account anonymization.

Added schema DDL and [migration SQL](/app/scripts/migrate-bestbook.sql) for existing databases. The migration must be applied during deployment.

Verification: 49 relevant tests passed; Ruff and `git diff --check` passed.