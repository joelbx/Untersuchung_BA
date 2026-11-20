Implemented first-class KEV data on each vulnerability, including CISA and VulnCheck details, date normalization, deterministic sorting, and the `%d KEVs` report summary. `FillWithKEVuln` now maps CISA records into `KEVs` and retains the legacy CISA alert; its decoder also maps VulnCheck entries and their details when present in a payload.

The repository has no separate VulnCheck fetch or configuration path, so this change does not add one.

Validation passed: `go test ./models ./detector` and `git diff --check`.