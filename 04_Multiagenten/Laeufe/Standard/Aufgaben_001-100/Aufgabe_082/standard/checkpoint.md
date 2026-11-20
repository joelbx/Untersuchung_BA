Task: fix auth service multi-backend audit event initialization.
Completed: Added WriterEmitter with JSON newline emission and aggregate close; NewMultiLog now validates Emitter loggers and embeds MultiEmitter; stdout backend uses WriterEmitter; added regression tests for fanout and multi-URI service configuration.
Verification: GOPROXY=off go test ./lib/events -run 'TestWriterEmitter|TestMultiLogEmitter|TestProtoStreamer' -count=1 passed; GOPROXY=off go test ./lib/service -run '^TestConfig$' -check.f TestInitExternalLog -count=1 passed; git diff --check passed.
