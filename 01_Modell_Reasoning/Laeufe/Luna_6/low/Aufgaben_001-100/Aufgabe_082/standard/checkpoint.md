# Checkpoint

Issue: auth service initialization fails when multiple audit event backends include stdout, because the configured stdout backend is a WriterLog and does not implement Emitter.

Plan: inspect the event abstractions, MultiLog construction, and external backend configuration; implement WriterEmitter and validated MultiLog fanout; run relevant existing event tests.
