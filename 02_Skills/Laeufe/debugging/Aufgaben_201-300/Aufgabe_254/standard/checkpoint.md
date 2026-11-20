# Checkpoint

Investigated EC2 availability detection and the metadata client construction path.

`rg` is unavailable (`/bin/sh: rg: not found`); using local `grep` and `find` for repository search.

## Root cause and hypothesis

`lib/utils/ec2.go:IsAvailable` issues a direct HTTP GET to the IMDS URL and accepts any HTTP 200. `lib/service/service.go` then reads the `TeleportHostname` tag and assigns its unvalidated body to `cfg.Hostname`. A captive portal can satisfy both reads with HTML. The existing SDK `getMetadata` path is already used for tags, but availability bypasses it. The proposed fix uses `getMetadata("instance-id")` with a 250 ms context deadline and a full EC2 ID format check; construction options permit a local IMDS endpoint in tests.

Regression test executed before implementation: `GOPROXY=off GOSUMDB=off go test ./lib/utils -run 'TestInstanceMetadataClient' -count=1` failed as expected because `WithIMDSClient` and variadic constructor options do not yet exist (compiler errors in `ec2_test.go`).

## Result

Added functional constructor options and IMDS client injection. `IsAvailable` now reads `instance-id` through the SDK metadata path under a 250 ms timeout and validates the complete `i-` plus 8 or 17 lowercase hex digit format. Removed the direct HTTP probe. Regression tests cover valid IDs, captive portal HTML, malformed IDs, option error propagation, and deadline behavior.

Verification passed with exit code 0:

- `GOPROXY=off GOSUMDB=off go test ./lib/utils -run 'TestInstanceMetadataClient|TestIsEC2NodeID' -count=1`
- `GOPROXY=off GOSUMDB=off go test ./lib/utils -count=1`
- `GOPROXY=off GOSUMDB=off go test ./lib/labels/ec2 -count=1`
- `git diff --check`
