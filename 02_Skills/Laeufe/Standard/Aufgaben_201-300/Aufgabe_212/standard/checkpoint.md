# Checkpoint

Task: support essential WPScan Enterprise fields in WordPress vulnerability ingestion.
Status: implemented and verified.

Changes:
- WordPress WPScan ingestion uses the first CVE reference as the canonical record ID, with the existing WPVDB fallback.
- Maps description, proof of concept, introduced version, and CVSS score/vector/severity; preserves source, references, UTC timestamps, classification, and fix version.
- Initializes optional metadata as an empty map when neither optional key exists.
- Added regression coverage for enriched, null, and absent fields.

Checks:
- `GOPROXY=off GOSUMDB=off go test ./detector -count=1` passed.
- `git diff --check` passed.
