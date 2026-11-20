# Work checkpoint

## EC2 availability fix

- Updated `lib/utils/ec2.go` with variadic `InstanceMetadataClientOption` constructor options.
- Added `WithIMDSClient` injection with nil validation.
- Replaced the raw HTTP availability check with a 250ms `instance-id` metadata lookup and EC2 ID format validation.
- `gofmt` and `git diff --check` passed.
- Existing focused tests passed: `go test ./lib/utils`.
