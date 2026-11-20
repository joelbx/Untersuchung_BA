# Checkpoint

Issue: add Ubuntu 20.04 extended support through 2030-04-01 and Ubuntu 22.04 lifecycle metadata (standard support through 2027-04-01; extended support through 2032-04-01).

Findings: Ubuntu releases are detected from the system release string and scanned by the Ubuntu family path. `config.GetEOL` is the release lookup whose missing 22.04 record caused lifecycle detection to report it unknown.

Changes: updated `config/os.go` with Ubuntu 20.04's extended support date and the standard and extended dates for 22.04.

Validation: `go test ./config` passed. `git diff --check` passed.
