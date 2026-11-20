Implemented `-wp-ignore-inactive` for scan and report, with config-file support. When enabled, inactive WordPress plugins and themes are excluded before vulnerability lookups; `removeInactives` returns `nil` when none remain.

The relevant Go package tests passed: `config`, `wordpress`, `scan`, `commands`, and `report`.