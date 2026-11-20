# Progress
Inspected WordPress API enrichment, configuration loading, CLI flags, and report filtering. No project source or tests changed.

# Findings
- `wordpress.FillWordPress` requests core, then every theme and plugin; a TODO calls out this flag. There is no `removeInactives` helper.
- `config.Config` has no `WpIgnoreInactive`. `config.WordPressConf.IgnoreInactive` exists per server and is loaded from TOML, but only affects late report CVE filtering.
- `commands.ReportCmd.SetFlags` controls the phase that calls `FillWordPress`; `ScanCmd.SetFlags` controls inventory collection. Neither registers `-wp-ignore-inactive`.
- `report.WordPressOption.apply` calls `FillWordPress` before the late `FilterInactiveWordPressLibs` pass, so existing filtering cannot save API calls.
- No existing WordPress-focused tests found.
