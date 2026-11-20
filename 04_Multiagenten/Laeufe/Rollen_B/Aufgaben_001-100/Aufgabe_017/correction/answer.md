Fixed the SQL Server diagnostic classification issue. The agent now preserves upstream SQL Server error codes when forwarding failures, so invalid users and database names can be categorized correctly. Agent-generated errors still use `28353`.

The protocol test and both test packages flagged by the reviewer pass. There are no remaining test failures.