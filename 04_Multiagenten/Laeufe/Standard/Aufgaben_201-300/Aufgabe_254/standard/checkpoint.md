Task: Fix EC2 availability detection in lib/utils/ec2.go.
Status: Complete.
Changes: NewInstanceMetadataClient accepts functional options; WithIMDSClient injects an IMDS client. IsAvailable reads instance-id through getMetadata with a 250ms context deadline and accepts only i- followed by 8 or 17 lowercase hex digits. Added tests for valid IDs, captive portal HTML, malformed IDs, errors, timeout, and constructor options.
Verification: go test ./lib/utils -count=1 passed; git diff --check passed.
Constraints observed: Local repository and existing dependencies only; git history, index baseline, and harness configuration unchanged.
