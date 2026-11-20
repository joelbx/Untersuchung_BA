Added `-wp-ignore-inactive` to the scan and report commands, with a `WpIgnoreInactive` configuration field. When enabled, WordPress reporting skips API lookups for inactive plugins and themes. `removeInactives` returns `nil` when filtering leaves no packages.

The new filtering test passed. Existing tests passed with `go test ./wordpress ./commands ./config`.