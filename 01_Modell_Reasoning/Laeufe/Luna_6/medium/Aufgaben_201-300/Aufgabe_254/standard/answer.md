Updated [ec2.go](/app/lib/utils/ec2.go) to support functional client options, including `WithIMDSClient`, and to determine availability by retrieving `instance-id` with a 250 ms timeout and validating its format.

Validation passed: `go test ./lib/utils` and `git diff --check`.