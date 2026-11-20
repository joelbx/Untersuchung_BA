# Checkpoint

- Task: support essential WPScan Enterprise fields in WordPress vulnerability ingestion.
- Updated `detector/wordpress.go`: first CVE reference is canonical; summary, proof of concept, introduced version, and CVSS 3 fields are mapped; timestamps are normalized to UTC; optional metadata is always an initialized map.
- Added `detector/wordpress_test.go` cases for Enterprise, basic absent, and basic null payloads. The test checks the full record, URL order, canonical ID, fix version, classification, and timestamps.
- Verified: `go test ./detector -count=1` passed; `git diff --check` passed.
- Constraints observed: local code and tests only; no git history, index baseline, or harness configuration changes.
