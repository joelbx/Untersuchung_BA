# Checkpoint

Implemented database server name deduplication, host-aware string/sort behavior, candidate selection and shuffled retry dialing, a deterministic shuffle hook, and fake per-server offline tunnel simulation. `tsh db ls` now deduplicates before display.

Validation: `go test ./types` in `/app/api` passed. Root module tests for `./lib/reversetunnel ./lib/srv/db ./tool/tsh` are still running.
