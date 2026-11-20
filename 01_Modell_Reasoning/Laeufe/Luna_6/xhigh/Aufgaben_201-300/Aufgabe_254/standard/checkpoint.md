# Checkpoint

Task: Fix EC2 availability detection by adding functional configuration options to `InstanceMetadataClient`, supporting injected IMDS clients, and validating a retrieved EC2 instance ID under a short timeout.

Progress: Implemented `InstanceMetadataClientOption`, `WithIMDSClient`, and variadic options on `NewInstanceMetadataClient`. Injected clients bypass default AWS config loading. `IsAvailable` now retrieves `instance-id` through IMDS with a 250 ms context timeout and requires the standard 8 or 17 lowercase hexadecimal suffix format. Removed the direct HTTP endpoint request.

Verification:
- `go test ./lib/utils` passed.
- `go test ./lib/labels/ec2` passed as part of the combined package run.
- `go test ./lib/service` could not build in this environment because the host lacks `linux/hidraw.h` and its C toolchain's SQLite build reports unavailable `pread64`/`off64_t`.
