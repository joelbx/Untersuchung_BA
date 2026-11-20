# Checkpoint

Task: Support essential WPScan Enterprise fields in WordPress vulnerability ingestion.

Status: Investigating repository implementation and tests before editing code.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

Investigation: `detector/wordpress.go` decodes WPScan payloads into `WpCveInfo`, then `extractToVulnInfos` builds `models.CveContent`. Enterprise fields are absent from the input struct and therefore lost. The converter loops over all `references.cve`, producing multiple records rather than using the first canonical CVE. Existing mappings for references, classification, and fix status are present; timestamps need explicit UTC normalization.

Hypothesis: extending the WPScan input model and mapping its optional fields to `CveContent` will preserve Enterprise data. Selecting the first CVE will yield one canonical record per vulnerability.

Regression before fix: `GOPROXY=off go test ./detector -run TestConvertToVinfosEnterpriseAndBasic -count=1` failed as expected: both variants returned 2 records instead of 1, confirming the canonical ID defect. The Enterprise case also asserts summary, metadata, CVSS, timestamps, and references after record count is corrected.

Implementation: WPScan decoding now accepts description, poc, introduced_in, and cvss. Conversion uses the first CVE reference as canonical ID, maps summary and CVSS fields into `CveContent`, stores present optional metadata in a non-nil map, and normalizes timestamps to UTC. Existing URL order, vulnerability type, and fix version mappings remain in place.

Verification: Regression test failed before the fix as expected. After the fix, `GOPROXY=off go test ./detector -run 'TestConvertToVinfosEnterpriseAndBasic|TestRemoveInactive' -count=1` passed. Final `GOPROXY=off go test ./detector -count=1 && git diff --check` passed (exit 0). Cases cover enriched, explicit null, and omitted fields.
