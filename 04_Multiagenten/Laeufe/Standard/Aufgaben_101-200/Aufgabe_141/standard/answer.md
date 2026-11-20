Added `-wp-ignore-inactive` to the scan and report commands and a `wpIgnoreInactive` config option. When enabled, `FillWordPress` removes inactive plugins and themes before making vulnerability API requests. The package filter returns `nil` when nothing remains.

The relevant existing tests passed: `go test ./wordpress ./config ./commands ./models`.