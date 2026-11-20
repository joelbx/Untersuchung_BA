Implemented the Red Hat OVAL advisory filtering and package fix-state propagation. Red Hat-family CVE detection now routes through OVAL instead of Gost; Red Hat API enrichment remains available.

`go test ./...` and `git diff --check` pass. The pinned goval-dictionary model omits `AffectedResolution`, so the compatibility extraction records a state when it is present in definition JSON and otherwise leaves `FixState` empty.

Updated [checkpoint.md](/app/.codex-role-output/checkpoint.md).