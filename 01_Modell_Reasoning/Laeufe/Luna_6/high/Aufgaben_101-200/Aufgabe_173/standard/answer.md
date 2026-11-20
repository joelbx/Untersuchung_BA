Implemented HA database service failover, display deduplication, and deterministic shuffle injection. Database server strings now include `HostID`, and sorting uses service name then host ID.

Verification passed:

- `go test ./types` from `/app/api`
- `go test ./lib/reversetunnel ./lib/srv/db ./tool/tsh`
- `git diff --check`

The checkpoint is in `.codex-role-output/checkpoint.md`.