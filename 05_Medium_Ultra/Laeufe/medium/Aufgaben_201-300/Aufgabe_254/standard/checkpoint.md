Task: Fix EC2 availability false positives in lib/utils/ec2.go.
Status: Complete. Added functional client options and WithIMDSClient injection. IsAvailable now checks the IMDS instance-id within 250ms and accepts only 8- or 17-digit lowercase hexadecimal EC2 IDs. Added regression tests for valid IDs, captive portal HTML, malformed IDs, option errors, and timeout.
Verification: go test ./lib/utils -count=1 passed; git diff --check passed.
Constraints: local repository and tests only; git history, index baseline, and harness configuration untouched.
