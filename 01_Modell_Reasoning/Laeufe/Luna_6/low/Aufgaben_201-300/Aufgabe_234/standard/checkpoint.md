# Checkpoint

Task: simplify SQLite access to one unified `*sql.DB` connection, as stated in the issue title, problem description, expected behavior, and core requirements. The interface section conflicts with those requirements by describing a read/write split; implementation will follow the unified-connection goal.

Next: inspect database initialization, persistence transaction flow, and consumers; update wiring; run relevant existing tests.
