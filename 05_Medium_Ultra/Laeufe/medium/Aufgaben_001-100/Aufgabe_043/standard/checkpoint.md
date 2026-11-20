Task: Extract tracing provider and exporter construction from gRPC startup into internal/tracing.
Status: Complete.
Changes: Added newResource, NewProvider, and GetExporter in internal/tracing; moved exporter tests there and added resource, sampling, independent-call, endpoint-error, and HTTP header/path coverage. Updated gRPC startup to use the new package and register exporter shutdown.
Verification: go test ./internal/tracing ./internal/cmd; git diff --check (passed).
Constraints observed: Local code/tests only; git history, index, and harness configuration unchanged.
