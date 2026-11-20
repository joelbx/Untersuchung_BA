# Checkpoint

Task: Resolve WordPress cache lookup and inactive package filtering.

Changes:
- Pass the WordPress cache map by value through report and scanner code. Cache values are pointers so a present nil value can be distinguished from a present empty string; nil is treated as a cache miss.
- Read IgnoreInactive from the scanned server's WordPress configuration and filter theme/plugin packages by Status.
- Extend cache lookup tests for nil and empty values; add a scanner test covering active and inactive themes/plugins with opposite global and per-server settings.

Verification:
- `GOPROXY=off GOSUMDB=off go test -count=1 ./wordpress ./report ./models` exited 0; all three packages passed. The local sqlite3 dependency emitted a compiler warning.
- `rg` is unavailable (`/bin/bash: rg: command not found`); local `grep` and `find` were used instead.
