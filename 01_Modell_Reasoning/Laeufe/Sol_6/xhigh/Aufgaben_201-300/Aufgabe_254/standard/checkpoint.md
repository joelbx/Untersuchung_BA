# EC2 metadata availability fix

- Added variadic `InstanceMetadataClientOption` support and `WithIMDSClient` injection.
- `IsAvailable` now retrieves `instance-id` through IMDS with a 250 ms context deadline and accepts only 8 or 17 lowercase hexadecimal digits after `i-`.
- Added coverage for valid IDs, captive portal HTML, malformed IDs, timeout, and option errors.
- Verified with `GOPROXY=off GOSUMDB=off go test ./lib/utils ./lib/labels/ec2 -count=1` (both packages pass).
