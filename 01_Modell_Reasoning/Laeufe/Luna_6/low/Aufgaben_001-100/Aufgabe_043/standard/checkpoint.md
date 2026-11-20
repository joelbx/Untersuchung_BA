# Checkpoint

Task: decouple tracing setup from gRPC startup by adding isolated tracing resource/provider/exporter APIs and wiring provider/exporter shutdown into server lifecycle.

Initial status: repository is clean. Next: inspect current gRPC startup, tracing config, dependencies, and existing tests; implement and run relevant existing tests.
