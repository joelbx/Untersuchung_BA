Implemented the EC2 availability fix in [ec2.go](/app/lib/utils/ec2.go:109). `NewInstanceMetadataClient` now accepts functional options, including `WithIMDSClient` for injecting an IMDS client. `IsAvailable` looks up `instance-id` with a 250 ms timeout and returns true only for a valid EC2 instance ID.

Validation passed: `go test ./lib/utils` and `git diff --check`.