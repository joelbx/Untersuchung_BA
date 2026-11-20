# WPScan Enterprise ingestion

- Task: map essential WPScan vulnerability fields into a consistent record for a WordPress version.
- Status: implemented WPScan Enterprise field mapping and a single canonical CVE record per vulnerability. Added regression coverage for enriched, null, and omitted optional fields.
- Verification: `GOPROXY=off go test ./detector -run 'TestConvertToVinfosWPScanFields|TestRemoveInactive' -count=1` passed; `git diff --check` passed.
