Added a first class `KEVs` field to each vulnerability, with source types and CISA/VulnCheck detail structs. CISA KEV ingestion now populates the field, including catalog metadata and notes, while preserving the legacy alert. Added KEV sorting and `FormatKEVCveSummary()`.

The VulnCheck types are defined, but ingestion of VulnCheck records is not wired up: the repository’s current detector path only fetches CISA KEV data.

Verification: `go test ./models ./detector` passed, and `git diff --check` passed.