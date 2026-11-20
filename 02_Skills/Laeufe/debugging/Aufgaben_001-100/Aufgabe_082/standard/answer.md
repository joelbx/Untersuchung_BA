Fixed the auth service crash when multiple audit event URIs are configured. `MultiLog` now validates its backends and emits events through a `MultiEmitter`; `stdout://` now uses the new `WriterEmitter`, which writes JSON events as newline-delimited records.

The event tests and the service test for a `file://` plus `stdout://` URI list pass. `git diff --check` also passes.