# Checkpoint

Completed EC2 availability fix in `lib/utils/ec2.go`: functional constructor options, `WithIMDSClient` injection, and a 250 ms IMDS `instance-id` lookup with strict EC2 ID validation. Added regression tests in `lib/utils/ec2_test.go` for valid IDs, captive portal HTML, malformed IDs, metadata errors, timeout, and option errors.

Verification: `GOPROXY=off go test ./lib/utils -count=1` and `GOPROXY=off go test ./lib/labels/ec2 -count=1` passed.
