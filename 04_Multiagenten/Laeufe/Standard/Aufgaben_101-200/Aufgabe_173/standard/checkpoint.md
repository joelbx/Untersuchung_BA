# Checkpoint

Task: improve HA database service selection, display deduplication, and test tunnel outage support.
Status: implemented and verified.
Changes: database server HostID logging and sorting; display deduplication; fake tunnel outage control; clock-seeded candidate shuffle and dial retry; candidate list in authorization context; proxy integration and API tests.
Verification: `go test ./types -count=1` in api; `go test ./lib/reversetunnel ./lib/srv/db ./tool/tsh` in root; focused new proxy tests; focused tsh test. All passed.
