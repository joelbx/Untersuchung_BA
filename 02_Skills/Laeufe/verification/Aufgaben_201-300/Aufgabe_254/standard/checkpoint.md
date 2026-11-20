# Checkpoint

Task: Harden EC2 availability detection using validated instance IDs and injectable IMDS client.

Changes:
- Added `InstanceMetadataClientOption` and `WithIMDSClient` to configure the constructor.
- `IsAvailable` retrieves `instance-id` with a 250 ms context deadline and requires `i-` followed by exactly 8 or 17 lowercase hexadecimal digits.
- Removed the direct HTTP probe.
- Added local IMDS tests for valid IDs, captive portal HTML, malformed IDs, metadata errors, option errors, and timeout.

Verification:
- `rg` unavailable: `/bin/sh: rg: not found`; used `grep`/`find` fallback.
- `GOPROXY=off GOSUMDB=off go test ./lib/utils -run 'Test(InstanceMetadataClient|IsEC2NodeID)' -count=1` — exit 0, `ok github.com/gravitational/teleport/lib/utils 0.354s`.
- `GOPROXY=off GOSUMDB=off go test ./lib/utils -count=1` — exit 0, `ok github.com/gravitational/teleport/lib/utils 1.909s`.
- `git diff --check` — exit 0.
