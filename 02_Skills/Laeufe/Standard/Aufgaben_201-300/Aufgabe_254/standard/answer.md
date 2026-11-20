Updated EC2 availability detection to retrieve `instance-id` through the IMDS client with a 250 ms timeout and accept only valid EC2 instance IDs. Added functional client options, including `WithIMDSClient`, and tests covering captive portal HTML, invalid IDs, and timeout behavior.

Verification: `go test ./lib/utils -count=1` and `git diff --check` passed.