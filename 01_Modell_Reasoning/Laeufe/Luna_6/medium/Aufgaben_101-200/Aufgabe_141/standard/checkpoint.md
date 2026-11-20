# Checkpoint

Implemented `-wp-ignore-inactive`, the `WpIgnoreInactive` configuration field, and WordPress package filtering before vulnerability API requests. Explicit CLI use is reapplied after config loading so it takes precedence over a config file.

Validation: `go test ./wordpress ./commands ./config` passed. `git diff --check` passed. The compiler emitted an existing `go-sqlite3` C warning.
