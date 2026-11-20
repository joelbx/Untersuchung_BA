Added `-wp-ignore-inactive` to the report command and `wpIgnoreInactive` to TOML configuration. When enabled, WordPress scanning removes inactive plugins and themes from the results before making their vulnerability API requests. The filter returns `nil` if no packages remain.

The affected package tests passed: `go test ./wordpress ./config ./models ./commands ./report`.