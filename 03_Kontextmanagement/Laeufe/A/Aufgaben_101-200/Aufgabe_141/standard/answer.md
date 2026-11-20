Added `-wp-ignore-inactive` and the `wpIgnoreInactive` config option. When enabled, inactive WordPress plugins and themes are removed before vulnerability API requests and excluded from report results. The package filter returns `nil` when nothing remains.

The relevant Go package tests passed offline, and `git diff --check` passed.