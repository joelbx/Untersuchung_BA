# Checkpoint

Task: Fix EC2 availability detection and add functional client options.

Implemented in `lib/utils/ec2.go`:
- Added `InstanceMetadataClientOption` and `WithIMDSClient` and applied options in `NewInstanceMetadataClient`.
- Replaced the raw HTTP availability probe with IMDS `instance-id` retrieval under a 250 ms context timeout.
- Require an exact EC2 instance ID with 8 or 17 lowercase hexadecimal digits.

Added tests in `lib/utils/ec2_test.go` for valid and invalid IDs, captive portal HTML, timeout, and option errors.

Verification: `GOPROXY=off GOSUMDB=off go test ./lib/utils -count=1` passed. `git diff --check` passed. `rg` was unavailable; used local `find`/`grep` for inspection.
