# Checkpoint

Implemented `-wp-ignore-inactive` in the scan command and added `WpIgnoreInactive` to the serializable config schema. `FillWordPress` now filters inactive packages before API lookups, and the helper returns nil when filtering removes every package.

Verification: `go test ./wordpress ./commands ./config` passed. `git diff --check` passed.
