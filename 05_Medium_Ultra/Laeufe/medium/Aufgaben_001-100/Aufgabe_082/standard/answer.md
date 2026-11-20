Fixed the auth startup failure for multiple audit event backends. `MultiLog` now validates its loggers and fans out audit events; `stdout://` now uses `WriterEmitter` to write newline-delimited JSON.

Added tests for writer behavior, fanout, invalid loggers, and a two-URI configuration. The relevant event and service tests passed, as did `git diff --check`.