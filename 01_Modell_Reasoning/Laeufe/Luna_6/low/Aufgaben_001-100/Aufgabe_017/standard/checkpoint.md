# Checkpoint

Task: Add SQL Server support to the database connection diagnostic flow, including ping and error categorization.

Initial inspection: `lib/client/conntest/database` contains MySQL and PostgreSQL pingers, and `lib/client/conntest` contains protocol selection. Next: follow these implementations, update protocol dispatch as needed, and run the relevant existing Go tests.
