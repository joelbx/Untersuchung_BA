# Checkpoint

Issue: Add first-class KEV entries to vulnerability data, populate them from CISA and VulnCheck, summarize and sort them.

Completed: Added `VulnInfo.KEVs` and source-specific KEV types. `FillWithKEVuln` converts CISA and VulnCheck DB/HTTP responses, including nested VulnCheck records and nil for missing or placeholder due dates. Updated go-kev to the cached version with VulnCheck support. Added KEV summaries to text and one-line reporting and sorted KEVs for JSON output. Added focused tests.

Verification: `GOPROXY=off GOSUMDB=off go test ./models ./detector ./reporter` passed; `git diff --check` passed.
