# Checkpoint

Task: Fix EC2 instance availability detection in `/app`.

Completed:
- Added `InstanceMetadataClientOption` and `WithIMDSClient` to inject an IMDS client at construction.
- Updated `NewInstanceMetadataClient` to accept and apply functional options; default AWS configuration is loaded only when no client was injected.
- Replaced the direct HTTP probe with a 250 ms `instance-id` metadata lookup and validation for EC2 instance IDs (`i-` followed by 8 or 17 lowercase hex digits).
- Ran `go test ./lib/utils` successfully.
