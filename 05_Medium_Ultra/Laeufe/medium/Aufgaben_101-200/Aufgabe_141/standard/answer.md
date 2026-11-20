Added `-wp-ignore-inactive` to the scan, report, and TUI commands, plus the `WpIgnoreInactive` config setting. WordPress vulnerability lookups now filter inactive plugins and themes before making API calls; the filter returns `nil` when no packages remain.

The relevant existing package tests, new filtering and TOML loading tests, and `git diff --check` passed.