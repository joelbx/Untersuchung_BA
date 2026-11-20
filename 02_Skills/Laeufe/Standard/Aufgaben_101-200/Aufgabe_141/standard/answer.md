Added `-wp-ignore-inactive` to `report` and the `wpIgnoreInactive` config setting. When enabled, WordPress vulnerability lookups skip inactive plugins and themes, and report filtering honors the setting. `removeInactives` returns `nil` when nothing remains.

The relevant tests passed with network access disabled: `GOPROXY=off GOSUMDB=off go test ./wordpress ./commands ./config ./models ./report`.