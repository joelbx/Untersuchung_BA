# Checkpoint

Task: Fix EC2 availability detection in `lib/utils/ec2.go` by validating the instance ID retrieved through IMDS, add functional client options including IMDS injection, and run relevant existing tests.

Status: Complete. `NewInstanceMetadataClient` accepts functional options, including `WithIMDSClient`; `IsAvailable` reads and validates `instance-id` through IMDS under a 250 ms context deadline. Added captive portal, ID format, option error, and timeout tests.

Verification: `GOPROXY=off GOSUMDB=off go test ./lib/utils -count=1` and `GOPROXY=off GOSUMDB=off go test ./lib/labels/ec2 -count=1` passed. No delegation used.
