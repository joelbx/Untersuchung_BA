# Checkpoint

Implemented JSON-lines `WriterEmitter` and switched `stdout://` to use it. `NewMultiLog` now rejects loggers that do not implement `Emitter`, embeds a fan-out `MultiEmitter`, and the service propagates constructor errors. `MultiLog.Close` continues to aggregate close errors from all underlying loggers.

Verification: `go test ./lib/events ./lib/service` passed; `git diff --check` passed.
