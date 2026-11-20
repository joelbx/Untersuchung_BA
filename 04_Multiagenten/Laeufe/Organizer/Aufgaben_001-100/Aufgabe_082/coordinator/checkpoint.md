Issue: auth startup fails because MultiLog does not implement Emitter when multiple event backends are configured.
Plan: inspect existing emitter/log/initialization code; implement WriterEmitter and MultiLog emitter fanout with correct close behavior; update stdout wiring; run relevant existing tests.
Status: investigation started. No delegation planned.
Implementation: WriterEmitter added with JSON-lines EmitAuditEvent and aggregate Close; MultiLog now validates Emitter implementations and embeds MultiEmitter; stdout uses WriterEmitter; service propagates NewMultiLog errors.
Verification: go test ./lib/events -run 'TestWriterEmitter|TestProtoStreamer' -count=1 passed; go test ./lib/service -run TestConfig -check.f 'InitExternalLog' -count=1 passed; git diff --check passed. An earlier broader events run failed in existing TestAuditLog.TestBasicLogging because a timestamp crossed a one-second boundary. No delegation used.
Follow-up: go test ./lib/events -count=1 passed on rerun, confirming the earlier timestamp failure was transient.
