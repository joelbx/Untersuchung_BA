Task: Fix EC2 availability detection in lib/utils/ec2.go.
Status: Complete. Added functional options and WithIMDSClient injection. IsAvailable retrieves instance-id via IMDS with a 250ms context timeout and validates 8 or 17 lowercase hex digits. Added tests for options, valid and invalid IDs, captive portal HTML, and timeout.
Verification: go test ./lib/utils ./lib/labels/ec2 -count=1 passed; git diff --check passed.
