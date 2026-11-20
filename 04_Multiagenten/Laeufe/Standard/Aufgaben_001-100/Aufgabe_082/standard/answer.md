Fixed the auth service crash when multiple audit event backends are configured. `MultiLog` now validates its backends and fans out audit events; `stdout://` now uses the new `WriterEmitter`, which writes newline-delimited JSON.

Added regression tests for emitter output, fanout, and a file plus stdout configuration. The targeted event and service tests pass.