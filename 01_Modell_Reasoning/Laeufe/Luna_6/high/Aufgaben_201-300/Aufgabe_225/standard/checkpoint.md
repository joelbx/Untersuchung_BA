# Checkpoint

Task: Add first-class CISA and VulnCheck KEV data to the vulnerability model, populate it from source data, and provide JSON sorting and CVE summary behavior.

Implementation: Added the first-class `VulnInfo.KEVs` model and CISA/VulnCheck detail types, normalized go-kev records into that field while retaining the legacy CISA alert, added KEV CVE summary formatting, and sorted KEVs by source and vulnerability name for JSON output.

Verification: `go test ./models ./detector` passed; `git diff --check` passed.
