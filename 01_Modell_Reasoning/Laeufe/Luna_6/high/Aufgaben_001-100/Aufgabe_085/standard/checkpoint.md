# Checkpoint

Implemented status-aware vulnerability diffs:
- Added `DiffStatus` (`+` / `-`), CVE ID formatting, and plus/minus counting helpers.
- Diff selection now accepts plus/minus booleans, excludes unchanged CVEs, and carries package records from the matching scan side.
- Enabled both statuses in standard diff reports and applied status-prefixed IDs to list, CSV, full text, and TUI displays.
- Added coverage for status selection, scan-side package data, counting, and ID formatting.

Verification underway with the existing `models` and `report` test packages.
