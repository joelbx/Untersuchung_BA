Implemented `-wp-ignore-inactive` for `scan`, `report`, and `tui`, with a `wpIgnoreInactive` TOML setting. Inactive plugins and themes are excluded from scan results and filtered before WordPress vulnerability API requests. The existing per-server setting also now avoids those requests.

Relevant offline Go tests passed, including the new filtering and API request tests.