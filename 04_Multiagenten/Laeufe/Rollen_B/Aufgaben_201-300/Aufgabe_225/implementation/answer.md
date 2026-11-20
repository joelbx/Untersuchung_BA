Added a dedicated `VulnInfo.KEVs` field with CISA and VulnCheck details. Both HTTP and database ingestion now populate it, including XDB and reported exploitation records. I also added the KEV CVE summary and consistent JSON ordering while retaining the legacy CISA alert field for older JSON.

The `models` and `detector` test suites, the focused new tests, and `git diff --check` passed locally.