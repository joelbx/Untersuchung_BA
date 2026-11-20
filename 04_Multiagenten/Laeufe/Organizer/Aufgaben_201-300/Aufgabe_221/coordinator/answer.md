Implemented Best Book Awards in the repository. Nominations now have durable storage, read-status and uniqueness validation, add/update/remove and count JSON APIs, and `Work` lookup methods. Work redirects update award references and counts; account anonymization updates award usernames.

For existing databases, apply [create-bestbook-awards.sql](/app/scripts/create-bestbook-awards.sql) before enabling the endpoints. New databases receive the table through the schema.

Verification: 50 relevant tests passed, Ruff passed, and `git diff --check` passed. No delegation was used.