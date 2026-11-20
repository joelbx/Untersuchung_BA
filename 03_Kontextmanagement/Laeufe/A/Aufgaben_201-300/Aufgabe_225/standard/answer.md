Added a dedicated `KEVs` field to the vulnerability model, with CISA and VulnCheck types and source specific details. The KEV loader now populates that field from both sources and normalizes empty due dates to `nil`. I also added KEV CVE counting and deterministic JSON ordering.

The existing `AlertDict.CISA` field remains for older JSON compatibility. The `go-kev` dependency was updated to a version already in the local cache that supports VulnCheck.

Verification passed: `go test ./models ./detector` with network access disabled, plus `git diff --check`.