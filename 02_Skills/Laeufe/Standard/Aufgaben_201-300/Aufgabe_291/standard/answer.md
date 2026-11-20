NVD CVSS v4.0 metrics now carry their source through conversion, persist in the existing `CveContent` fields, and appear in `Cvss40Scores()` after MITRE entries. I updated the locally cached `go-cve-dictionary` dependency because the previously pinned version lacked `Nvd.Cvss40`.

The full `models` test suite and `git diff --check` pass.