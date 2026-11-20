# Checkpoint

Completed HA database proxy selection and display deduplication. Proxy authorization retains all matching servers, uses a clock-seeded default shuffle, and retries tunnel connection problems. Fake remote sites can mark individual server tunnels offline. Added API display helper coverage and an integration test for fallback and all-offline error.

Tests passed: `GOPROXY=off go test ./types` (from `/app/api`); `GOPROXY=off go test ./lib/reversetunnel ./lib/srv/db ./tool/tsh`; focused proxy fallback test after final edits. `git diff --check` passed.
