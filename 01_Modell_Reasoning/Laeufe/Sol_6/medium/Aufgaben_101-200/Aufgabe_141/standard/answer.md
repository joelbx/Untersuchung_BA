Added `-wp-ignore-inactive` to the report, server, and TUI commands, plus `wpIgnoreInactive` in the config schema. When enabled, WordPress vulnerability lookups skip inactive plugins and themes. The new `removeInactives` helper returns `nil` when every package is inactive.

Focused tests were added, and `go test -p 1 ./config ./wordpress ./commands ./report` passed with network access disabled.