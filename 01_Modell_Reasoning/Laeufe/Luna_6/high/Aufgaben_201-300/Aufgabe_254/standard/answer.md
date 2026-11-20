Updated [ec2.go](/app/lib/utils/ec2.go) with functional client options and `WithIMDSClient` for injecting an IMDS client. `IsAvailable` now retrieves `instance-id` with a 250 ms timeout and validates its EC2 ID format, removing the direct HTTP probe.

Verified with `go test ./lib/utils` (passed).