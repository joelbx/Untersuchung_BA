Implemented `-wp-ignore-inactive`, added the `WpIgnoreInactive` config field, and filtered inactive plugins and themes in `FillWordPress`. Added tests for filtering and the nil-on-empty behavior.

Verification passed: `go test ./wordpress ./commands ./config` and `git diff --check`.