# Fault-localization checkpoint

Inspected `detector/wordpress.go`, `models/cvecontents.go`, `models/wordpress.go`, and existing WordPress tests. No project source or tests changed.

Primary cause: `WpCveInfo` has no `description`, `poc`, `introduced_in`, or `cvss` fields, so `json.Unmarshal` discards Enterprise data. `extractToVulnInfos` only sets title, references, timestamps, type, CVE ID, and fixed version; it never sets summary, CVSS fields, or `CveContent.Optional`. The latter remains nil, while the requirement calls for an empty map when no optional metadata exists.

Additional edge cases: extraction emits one record per value in `references.cve`, whereas requirement selects first; timestamps are passed through without `.UTC()` normalization; `convertToVinfos` iterates every top-level version key through a Go map, so a multi-version body could yield mixed/nondeterministic output. Existing `detector/wordpress_test.go` only tests inactive-package filtering. Exact Enterprise `cvss` JSON shape is not evidenced by repository fixtures.
