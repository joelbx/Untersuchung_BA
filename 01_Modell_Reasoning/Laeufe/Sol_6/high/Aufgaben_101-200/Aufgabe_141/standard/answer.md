Added `-wp-ignore-inactive` to the report command and `WpIgnoreInactive` to the config schema. When enabled, [FillWordPress](/app/wordpress/wordpress.go:50) removes inactive plugins and themes from the result before WPVulnDB lookups. The filter returns `nil` if no packages remain.

Offline tests passed for `wordpress`, `config`, `commands`, `report`, and `models`.