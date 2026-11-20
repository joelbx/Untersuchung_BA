Task: Support essential WPScan Enterprise fields in WordPress vulnerability ingestion.
Status: Complete. Updated detector/wordpress.go to map Enterprise fields, normalize timestamps to UTC, and use the first CVE. Added converter tests for enriched, omitted, null, and no-CVE payloads. GOPROXY=off GOSUMDB=off go test ./detector passed.
Constraints: Use local code and existing tests only; preserve git history, index baseline, and harness configuration.
