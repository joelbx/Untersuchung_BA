# Checkpoint

Task: implement `-wp-ignore-inactive` for WordPress plugins and themes.

Progress: added the `-wp-ignore-inactive` flag to scan, report, and TUI commands; added top-level `WpIgnoreInactive` TOML/JSON configuration loading; and filtered inactive packages in `FillWordPress`. Filtering honors the current config, the saved scan config, and the existing per-server setting. Existing relevant tests pass: `GOPROXY=off go test ./config ./wordpress ./commands ./report ./models`. Final diff review is underway.
