# Checkpoint

Implemented the EC2 availability fix in `lib/utils/ec2.go`:

- Added `InstanceMetadataClientOption` functional options and `WithIMDSClient` injection.
- Made `NewInstanceMetadataClient` accept and apply optional configuration functions.
- Replaced direct HTTP probing with an IMDS `instance-id` lookup under a 250 ms timeout.
- Availability now requires an exact EC2 instance ID (`i-` plus 8 or 17 lowercase hexadecimal characters).

Validation: `go test ./lib/utils` passed; `git diff --check` passed.
