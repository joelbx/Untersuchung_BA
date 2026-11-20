VERDICT: ACCEPT

The patch registers `-wp-ignore-inactive`, loads the setting from TOML, and filters inactive plugins and themes before their vulnerability API requests. `removeInactives` returns `nil` when no packages remain. I found no code defect.

`GOPROXY=off GOSUMDB=off go test ./wordpress ./config ./commands ./report` passed (exit 0); `commands` has no test files. `git diff --check` passed. The build emitted a non-failing SQLite C warning.