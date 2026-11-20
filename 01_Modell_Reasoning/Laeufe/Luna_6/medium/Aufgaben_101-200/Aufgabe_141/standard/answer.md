Implemented `-wp-ignore-inactive` and the `WpIgnoreInactive` config field. When enabled, WordPress scanning filters inactive packages before requesting plugin and theme vulnerability data; an explicitly supplied CLI flag takes precedence over the config file.

`go test ./wordpress ./commands ./config` passed. `git diff --check` passed. The build emitted an existing `go-sqlite3` C warning.