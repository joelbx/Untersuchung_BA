Added `-wp-ignore-inactive` to the `report` command and a matching `WpIgnoreInactive` config option. When enabled, WordPress vulnerability lookup skips inactive plugins and themes; `removeInactives` returns `nil` if none remain.

The focused tests and `GOPROXY=off GOSUMDB=off go test ./...` passed. The full run emitted an existing go-sqlite3 compiler warning.